from PySide2.QtWidgets import QDialog

from View.Componentes.Ui_FiltroEstoque import Ui_FiltroEstoque


class FiltroEstoque(QDialog, Ui_FiltroEstoque):
    """
    Fazer mapeamento dos campos
    nome_campo - nome_coluna - sinal
    "nome_coluna": (campo, sinal)
    """

    def __init__(self, parent=None):
        super(FiltroEstoque, self).__init__(parent)

        self.campos_filtro = {
            "codigo_mercadoria": (self.lineEdit_mercadoria_id,  '=')
        }

    def montar_filtro(self) -> str:
        self.get_mercadoria()
        self.get_entrada()
        self.get_saida()
        self.get_classificacao()
        self.get_estoque()
        return "$$"

    def limpar_filtro(self):
        pass

    def busca_mercadoria(self):
        pass

    def get_mercadoria(self):
        pass

    def get_entrada(self):
        pass

    def get_saida(self):
        pass

    def get_classificacao(self):
        pass

    def get_estoque(self):
        pass



