from PySide2.QtWidgets import QDialog, QDialogButtonBox
from View.Ui_About import Ui_about


class About(QDialog, Ui_about):

    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_clicked)

    def close_clicked(self):
        self.close()
