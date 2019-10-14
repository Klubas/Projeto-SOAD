from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_FiltroPadrao import Ui_FiltroPadrao


class FiltroPadrao(QDialog, Ui_FiltroPadrao):

    def __init__(self, child=None, parent=None):
        super(FiltroPadrao, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.child = child(self.widget)
        self.child.setupUi(self.child)
        self.child.setWindowFlags(Qt.Widget)
        self.child.move(0, 0)

        self.setMinimumSize(self.child.minimumSize())
        self.setMaximumSize(self.child.maximumSize())
        self.setBaseSize(self.child.size())

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)

        self.show()

    def show(self):
        self.child.show()
        super(FiltroPadrao, self).show()

    def confirma(self):
        self.parent.show()
        self.hide()

    def cancela(self):
        self.parent.show()
        self.hide()




