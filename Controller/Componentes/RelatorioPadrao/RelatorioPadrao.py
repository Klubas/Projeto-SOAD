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

    def __init__(self, dados_relatorio, title='', footer='', landscape=True, page_size='A4', stylesheet=None):

        # Converter dicionário para HTML (pandas)
        # Transformar HTML em PDF (WeasyPrint)
        # Usar FileDialog para salvar o arquivo geradoz
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

        self.dados = dados_relatorio
        self.title = title
        self.footer = footer

        if landscape:
            orientation = 'landscape'
        else:
            orientation = 'portrait'

        html_style = \
            '<style>' + \
            '   @page {' \
            '       size: ' + page_size + ' ' + orientation + ';' \
            '       @top-left { content: "' + self.title + '";}' \
            '       @bottom-left { content: "' + str(datetime.datetime.now())[:-7] + '";}' \
            '       @top-right { content: "VIP Cartuchos"; }' \
            '   }' + \
            '</style>'

        html = \
            '<h1>' + self.title + '</h1>'

        self.html = html_style + html

        self.default_stylesheet = os.path.join('Controller', 'Componentes', 'RelatorioPadrao', 'styles', 'style.css')

        self.stylesheets = list()

        if stylesheet:
            self.stylesheets.append(stylesheet)

        self.stylesheets.append(self.default_stylesheet)


    def gerar_relatorio(self):
        logging.info('[RelatorioPadrao] Gerando relatorio...')
        html = self.__dict2html__(self.dados)
        pdf = self.__html2pdf__(html)
        path_relatorio = self.salvar_relatorio(pdf)
        self.exibir_relatorio(path_relatorio)

    def salvar_relatorio(self, pdf, path=None):
        if path is None:

            path = os.path.join(
                tempfile.gettempdir(), 'relatorio-' + str(datetime.datetime.now().timestamp()).replace('.', '') + '.pdf'
            )

        open(path, 'wb').write(pdf)
        logging.info('[RelatorioPadrao] Relatorio salvo em ' + path)
        return path

    def exibir_relatorio(self, filepath):
        if platform.system() == 'Darwin':
            subprocess.call(('open', filepath))

        elif platform.system() == 'Windows':
            try:
                os.startfile(filepath)
            except Exception as e:
                print(e)
                subprocess.run(['open', filepath], check=True)
        else:
            subprocess.call(('xdg-open', filepath))
        #os.remove(filepath)

    def __dict2html__(self, dicts):
        """
        :param dicts: lista de dicionários
        :return: html -> str
        """
        df = pd.DataFrame(dicts)
        html = df.to_html(
            index=False
            , na_rep=" "
            , show_dimensions=False
            , bold_rows=False
            , border=5
        )

        html =  self.html + html

        return html

    def __html2pdf__(self, html):
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
