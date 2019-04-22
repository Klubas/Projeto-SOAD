from PySide2.QtWidgets import QDialog
from View.CadastroProduto import Ui_CadastroProduto


class CadastroProduto(QDialog, Ui_CadastroProduto):

    def __init__(self, parent=None):
        super(CadastroProduto, self).__init__(parent)
        self.setupUi(self)

    def close_clicked(self):
        self.close()
