import os

from PySide2.QtGui import QImage, QPixmap, QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_ConfirmDialog import Ui_ConfirmDialog


class ConfirmDialog(QDialog, Ui_ConfirmDialog):

    def __init__(self, parent=None):
        super(ConfirmDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Diálogo de confirmação")
        self.buttonBox.button(QDialogButtonBox.Yes).clicked.connect(self.sim_clicked)
        self.buttonBox.button(QDialogButtonBox.No).clicked.connect(self.nao_clicked)
        self.buttonBox.button(QDialogButtonBox.No).setDefault(True)

        icon_path = os.path.join("Resources", "icons", "question.png")
        icone = QImage(icon_path).smoothScaled(60, 60)
        self.setWindowIcon(QIcon(icon_path))
        self.label_imagem.setPixmap(QPixmap.fromImage(icone))

    def definir_mensagem(self, mensagem):
        self.label.setText(mensagem)

    def sim_clicked(self):
        self.accept()

    def nao_clicked(self):
        self.reject()
