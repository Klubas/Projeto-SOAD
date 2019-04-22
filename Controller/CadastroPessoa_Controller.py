from PySide2.QtWidgets import QDialog
from View.CadastroPessoa import Ui_CadastroPessoa


class CadastroPessoa(QDialog, Ui_CadastroPessoa):

    def __init__(self, parent=None):
        super(CadastroPessoa, self).__init__(parent)
        self.setupUi(self)

    def close_clicked(self):
        self.close()
