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
        print(html)

    def salvar_relatorio(self):
        pass

    def exibir_relatorio(self):
        pass

    def __dict2html__(self, dict):
        df = pd.DataFrame(data=dict)
        df = df.fillna(' ').T
        return df

    def __html2pdf__(self):
        pdf = PdfGenerator()
        pass
