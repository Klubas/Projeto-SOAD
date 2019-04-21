import sys
from PySide2.QtWidgets import QMainWindow, QWidget
from View.CadastroProduto import Ui_CadastroPessoa


class CadastroProduto(QWidget, Ui_CadastroPessoa):

    def __init__(self, parent=None):
        super(CadastroProduto, self).__init__(parent)
        print("Cadastro Produto")
        self.setupUi(self)

    def close_clicked(self):
        self.close()
