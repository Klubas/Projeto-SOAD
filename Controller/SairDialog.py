from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Ui_SairDialog import Ui_SairDialog


class SairDialog(QDialog, Ui_SairDialog):

    def __init__(self, parent=None):
        super(SairDialog, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Yes).clicked.connect(self.sim_clicked)
        self.buttonBox.button(QDialogButtonBox.No).clicked.connect(self.nao_clicked)

    def definir_mensagem(self, mensagem):
        self.label.setText(mensagem)

    def sim_clicked(self):
        self.accept()

    def nao_clicked(self):
        self.reject()
