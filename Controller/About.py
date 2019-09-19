import os

from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Ui_About import Ui_about


class About(QDialog, Ui_about):

    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)
        icone_logo = QImage(os.path.join('Resources', 'Imagens', 'soad.png')).smoothScaled(50, 50)
        self.label_logo.setPixmap(QPixmap.fromImage(icone_logo))

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_clicked)

    def close_clicked(self):
        self.close()
