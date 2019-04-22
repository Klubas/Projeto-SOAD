from PySide2.QtWidgets import QDialog
from View.CadastroToner import Ui_CadastroToner


class CadastroToner(QDialog, Ui_CadastroToner):

    def __init__(self, parent=None):
        super(CadastroToner, self).__init__(parent)
        self.setupUi(self)

    def close_clicked(self):
        self.close()
