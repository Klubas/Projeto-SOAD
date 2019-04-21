import sys
from PySide2.QtWidgets import QWidget
from View.CadastroProduto import Ui_CadastroPessoa


class CadastroProduto(QWidget, Ui_CadastroPessoa):

    def __init__(self, parent=None):
        super(CadastroProduto, self).__init__(parent)
        print("Cadastro Produto")
        self.setupUi(self)

    def close(self):
        sys.exit()
