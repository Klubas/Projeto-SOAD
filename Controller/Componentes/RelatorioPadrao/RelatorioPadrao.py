import pandas as pd

from Controller.Componentes.RelatorioPadrao.PdfGenerator import PdfGenerator


class RelatorioPadrao:
    def __init__(self, dados_relatorio):
        self.dados = dados_relatorio
        # Converter dicionário para HTML (pandas)
        # Transformar HTML em PDF (WeasyPrint)
        # Usar FileDialog para salvar o arquivo gerado
        pass

    def gerar_relatorio(self):
        html = self.__dict2html__(self.dados)
        #print(html)
        pdf = self.__html2pdf__(html)
        #print(pdf)

    def salvar_relatorio(self):
        pass

    def exibir_relatorio(self):
        pass

    def __dict2html__(self, dict):

        print(dict)
        """
        dict = {'Job1': {'2017-01-10': [44, 33, 11, 75, 22]},
             'Job2': {'2017-01-05': [25, 25, 0, 100, 25], '2017-01-10': [50, 50, 0, 100, 25]},
             'Job3': {'2017-01-03': [44, 22, 22, 50, 22], '2017-01-04': [66, 36, 30, 54, 22],
                      '2017-01-06': [88, 52, 36, 59, 22], '2017-01-10': [132, 68, 64, 51, 22],
                      '2017-01-02': [22, 9, 13, 40, 22], '2017-01-08': [110, 52, 58, 47, 22]},
             'Job4': {'2017-01-10': [25, 25, 0, 100, 25]}}
        """
        df = pd.DataFrame(data=dict)
        df = df.fillna(' ').T
        html = df.to_html()
        return html

    def __html2pdf__(self, html):
        from io import BytesIO
        from weasyprint import HTML
        from weasyprint.pdf import PDFFile, pdf_format

        #html = HTML(html)
        content = BytesIO(html.write_pdf())
        pdf_file = PDFFile(content)
        params = pdf_format('/OpenAction [0 /FitV null]')
        pdf_file.extend_dict(pdf_file.catalog, params)
        pdf_file.finish()
        pdf = pdf_file.fileobj.getvalue()
        open('/tmp/relatorio.pdf', 'wb').write(pdf)
        return pdf
        #pdf = PdfGenerator(main_html=html)
        #return pdf.render_pdf()
