import datetime
import logging
import os
import platform
import subprocess
import tempfile
from io import BytesIO

import pandas as pd
from weasyprint import HTML
from weasyprint.pdf import PDFFile, pdf_format


class RelatorioPadrao:

    def __init__(self, dados_relatorio, title='', footer='', landscape=True, page_size='A4', stylesheet=None, sanitize_html=True):
        """
        Cabeçalho com filtros
        Paginação com numero total de paginas
        Mudar a cor para impressão
        Ordernar campos de maior importancia

        :param dados_relatorio:
        :param header:
        :param footer:
        :param landscape:
        :param page_size:
        :param stylesheet:
        """
        self.sanitize_html = sanitize_html
        self.dados = dados_relatorio
        self.title = title
        self.footer = footer

        if landscape:
            orientation = 'landscape'
        else:
            orientation = 'portrait'

        self.html_style = self.criar_stylesheet_dinamica(
            size=page_size + ' ' + orientation
            , title=self.title
            , nome='VIP Cartuchos'
        )

        self.html_cab = '''
            <h1 class="cabecalho"> {title} </h1>
        '''.format(title=self.title)

        self.default_stylesheet = os.path.join('Resources', 'styles', 'relatorio_padrao.css')
        self.stylesheets = list()
        self.stylesheets.append(self.html_style)
        if stylesheet:
            self.stylesheets.append(stylesheet)
        self.stylesheets.append(self.default_stylesheet)

    def gerar_relatorio(self):
        logging.info('[RelatorioPadrao] Gerando relatorio...')
        html = self.__dict2html__(self.dados)
        pdf = self.__html2pdf__(html)
        path_relatorio = self.salvar_relatorio(pdf)
        self.cleanup(self.html_style)
        return path_relatorio

    def salvar_relatorio(self, pdf, path=None):

        logging.info('[RelatorioPadrao] Salvando PDF...')

        if path is None:

            path = os.path.join(
                tempfile.gettempdir(), 'relatorio-' + str(datetime.datetime.now().timestamp()).replace('.', '') + '.pdf'
            )

        open(path, 'wb').write(pdf)
        logging.info('[RelatorioPadrao] Relatorio salvo em ' + path)
        return path

    def criar_stylesheet_dinamica(self, size, title, nome):
        html_style = \
            '''
                @page {{
                    size: {page_size};
                
                    @top-left {{
                        content: "{title}";
                    }}
                
                    @bottom-left {{
                        content: "{date}";
                    }}
                
                    @top-right {{ 
                        content: "{nome_empresa}";
                    }}
                }}
            '''

        html_style = html_style.format(
            page_size=size
            , title=title
            , date=str(datetime.datetime.now())[:-7]
            , nome_empresa=nome
        )

        path = os.path.join(
            tempfile.gettempdir(), 'style-' + str(datetime.datetime.now().timestamp()).replace('.', '') + '.css'
        )

        try:
            with open(path, 'w') as f:
                f.write(html_style)
        except Exception as e:
            logging.debug('[RelatorioPadrao] Erro ao salvar style dinamico.\n> ' + str(e))
            return None

        return path

    def exibir_relatorio(self, filepath):

        logging.info('[RelatorioPadrao] Exibindo pdf...')

        if platform.system() == 'Darwin':
            subprocess.call(('open', filepath))

        elif platform.system() == 'Windows':
            try:
                os.startfile(filepath)
            except Exception as e:
                logging.debug('[RelatorioPadrao] Tentando método alternativo de abertura de arquivo devido a exceção: \n>' + str(e))
                subprocess.run(['open', filepath], check=True)
        else:
            subprocess.call(('xdg-open', filepath))

    def __dict2html__(self, dicts):
        """
        :param dicts: lista de dicionários
        :return: html -> str
        """
        logging.info('[RelatorioPadrao] Gerando html...')

        df = pd.DataFrame(dicts)
        html_table = df.to_html(
            index=False
            , classes='tabela'
            , na_rep=" "
            , show_dimensions=False
            , bold_rows=False
            , border=5
        )

        html_string = '''
        <html>
          <head><title>{title}</title></head>
          <body>
            {table_cab}
            {table}
          </body>
        </html>.
        '''.format(style=self.html_style, table_cab=self.html_cab, table=html_table, title=self.title)

        return html_string

    def __html2pdf__(self, html):

        logging.info('[RelatorioPadrao] Gerando PDF...')

        html = HTML(string=html)

        content = BytesIO(
            html.write_pdf(
                stylesheets=self.stylesheets
            )
        )

        pdf_file = PDFFile(content)
        params = pdf_format('/OpenAction [0 /FitV null]')
        pdf_file.extend_dict(pdf_file.catalog, params)
        pdf_file.finish()
        pdf = pdf_file.fileobj.getvalue()
        return pdf

    def sanitize(self, s):
        import re
        s = re.sub(r"\s+", "", s)
        return s

    def cleanup(self, path_list):
        """
        :param paths: Lista de arquivos a resem removidos
        :return: success

        """
        paths = list()
        if isinstance(path_list, list):
            paths = path_list
        elif isinstance(path_list, str):
            paths.append(path_list)
        else:
            logging.debug('[RelatorioPadrao] Parâmetro <path_list> inválido.')

        for path in paths:
            try:
                os.remove(path)
            except Exception as e:
                logging.debug('[RelatorioPadrao] Não foi possível remover arquivo temporário: ' + str(path) + '\n> ' + str(e))
