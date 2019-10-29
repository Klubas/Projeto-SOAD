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

    def __init__(self, dados_relatorio):

        # Converter dicionário para HTML (pandas)
        # Transformar HTML em PDF (WeasyPrint)
        # Usar FileDialog para salvar o arquivo geradoz

        self.dados = dados_relatorio
        self.stylesheet = os.path.join('Controller', 'Componentes', 'RelatorioPadrao', 'styles', 'style.css')

    def gerar_relatorio(self):
        logging.info('[RelatorioPadrao] Gerando relatorio...')
        html = self.__dict2html__(self.dados)
        pdf = self.__html2pdf__(html)
        path_relatorio = self.salvar_relatorio(pdf)
        self.exibir_relatorio(path_relatorio)

    def salvar_relatorio(self, pdf, path=None):
        if path is None:
            path = os.path.join(tempfile.gettempdir(), 'relatorio.pdf')
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

    def __dict2html__(self, dicts):
        """
        :param dicts: lista de dicionários
        :return: html -> str
        """
        """        
        colunas = list()
        dict_relatorio = dict()
        index = str()

        if isinstance(dicts, list):
            colunas = dicts[0].keys()
            for coluna in colunas:
                dict_relatorio[coluna] = list()
                for linha in dicts:
                    for key, value in linha.items():
                        if key == coluna:
                            dict_relatorio[coluna].append(value)

        elif isinstance(dicts, dict):
            colunas = dicts.keys()
            dict_relatorio = dicts"""

        df = pd.DataFrame(dicts)
        html = df.to_html(index=False)
        return html

    def __html2pdf__(self, html):
        html = HTML(string=html)

        content = BytesIO(
            html.write_pdf(
                stylesheets=[self.stylesheet]
            )
        )

        pdf_file = PDFFile(content)
        params = pdf_format('/OpenAction [0 /FitV null]')
        pdf_file.extend_dict(pdf_file.catalog, params)
        pdf_file.finish()
        pdf = pdf_file.fileobj.getvalue()
        return pdf