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

    def __init__(self
                 , dados_relatorio
                 , title=''
                 , landscape=True
                 , page_size='A4'
                 , cabecalho=''
                 , rodape=''
                 , file=False
                 , stylesheet=None
                 , sort_column=None
                 , override_style=False
    ):
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
        self.html_string = '''
<!DOCTYPE html>
<html lang="pt-br">
    <meta charset="utf-8">
    <head><title>{title}</title></head>
    <body>
        <h1 class="titulo">{title}</h1>
        <div class="cabecalho">{cabecalho}</div> 
        <div class="tabela">{table}</div>
        <div class="rodape">{rodape}</div>
    </body>
</html>
'''

        self.html_style = '''
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
}}'''

        self.sort_column = sort_column
        self.dados = dados_relatorio
        self.title = title

        self.remover = list()

        if not file:
            self.cabecalho = cabecalho
            self.rodape = rodape

        else:
            try:

                with open(cabecalho, 'r') as f:
                    self.cabecalho = f.read()

                with open(rodape, 'r') as f:
                    self.rodape = f.read()

            except Exception as e:
                self.cabecalho = ''
                self.rodape = ''
                logging.debug('[RelatorioPadrao] Não foi possível abrir o arquivo de cabecalho/rodape.\n>' + str(e))

        if landscape:
            orientation = 'landscape'
        else:
            orientation = 'portrait'

        self.html_style = self.criar_stylesheet_dinamica(
            size=page_size + ' ' + orientation
            , title=self.title
            , nome='VIP Cartuchos'
        )

        self.default_stylesheet = os.path.join('Resources', 'styles', 'relatorio_padrao.css')
        self.tabela_stylesheet = os.path.join('Resources', 'styles', 'tabela.css')

        self.stylesheets = list()
        self.stylesheets.append(self.html_style)
        self.stylesheets.append(self.tabela_stylesheet)

        if not override_style:
            self.stylesheets.append(self.default_stylesheet)

        if stylesheet:
            self.stylesheets.append(stylesheet)

    def gerar_relatorio(self):
        logging.info('[RelatorioPadrao] Gerando relatorio...')
        html = self.__dict2html__(self.dados)
        pdf = self.__html2pdf__(html)
        path_relatorio = self.salvar_relatorio(pdf)
        self.cleanup(self.remover)
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

        html_style = self.html_style.format(
            page_size=size
            , title=title
            , date=str(datetime.datetime.now())[:-7]
            , nome_empresa=nome
        )

        path = self.gravar_stylesheet_temp(html_style)

        return path

    def gravar_stylesheet_temp(self, style):

        path = os.path.join(
            tempfile.gettempdir(), 'style-' + str(datetime.datetime.now().timestamp()).replace('.', '') + '.css'
        )

        try:
            with open(path, 'w') as f:
                f.write(style)
        except Exception as e:
            logging.debug('[RelatorioPadrao] Erro ao salvar style dinamico.\n> ' + str(e))
            return None

        self.remover.append(path)
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

        def align_fields(val):
            try:
                print(val)
                val = val.replace(',', '.')
                val = float(val)

            except Exception as e:
                logging.debug(str(e))

            if isinstance(val, float):

                try:
                    val = int(val)
                    align = 'center'
                except Exception as e:
                    logging.debug(str(e))
                    align = 'right'
            else:
                align = 'left'

            return 'text-align: %s !important' % align

        logging.info('[RelatorioPadrao] Gerando html...')

        for dicionario in dicts:
            for key, value in dicionario.items():
                if value is None:
                    value = ''

        df = pd.DataFrame(dicts)

        if self.sort_column:
            df = df.sort_values(by=self.sort_column, ascending=True)

        """
        html_table = df.to_html(
            index=False
            , classes='dados'
            , na_rep=" "
            , show_dimensions=False
            , bold_rows=False
            , border=0
        )
        """

        html_table = df.style\
            .applymap(align_fields)\
            .render()

        html_table = html_table.replace("<table id=", "<table border=\"0\" class=\"dataframe dados\" id=")
        html_table = html_table.replace("<th class=\"blank level0\" ></th>", "<!--<th class=\"blank level0\" ></th>-->")
        html_table = html_table.replace("<th id=", "<!-- <th id=")
        html_table = html_table.replace("</th>\n", "</th> -->\n")

        print(html_table)

        html_string = self.html_string.format(
            style=self.html_style
            , table=html_table
            , title=self.title
            , cabecalho=self.cabecalho
            , rodape=self.rodape
        )

        html_string = html_string.replace('&gt;', '>')
        html_string = html_string.replace('&lt;', '<')
        html_string = html_string.replace('\\n', ' ')

        return html_string

    def __html2pdf__(self, html):

        logging.info('[RelatorioPadrao] Gerando PDF...')

        html = HTML(string=html, base_url=os.getcwd())

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
