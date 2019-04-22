from PySide2.QtWidgets import QDialog
from View.CadastroInsumo import Ui_CadastroInsumo


class CadastroInsumo(QDialog, Ui_CadastroInsumo):

    def __init__(self, parent=None):
        super(CadastroInsumo, self).__init__(parent)
        self.setupUi(self)

    def close_clicked(self):
        self.close()
