import os

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_FiltroPadrao import Ui_FiltroPadrao


class FiltroPadrao(QDialog, Ui_FiltroPadrao):

    string_filtro = Signal(list)

    def __init__(self, child=None, parent=None):
        super(FiltroPadrao, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.setWindowIcon(QIcon(os.path.join('Resources', 'icons', 'filter.png')))

        self.child = child(self.widget)
        self.child.setupUi(self.child)
        self.child.setWindowFlags(Qt.Widget)
        self.child.move(0, 0)

        self.setMinimumHeight(self.child.height() + 60)
        self.setMinimumWidth(self.child.width() + 20)
        self.setMaximumHeight(self.child.height() + 60)
        self.setMaximumWidth(self.child.width() + 20)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)

    def show(self):
        self.child.show()
        super(FiltroPadrao, self).show()

    def confirma(self):
        string_filtro = self.child.montar_filtro()
        self.string_filtro.emit(string_filtro)
        self.parent.show()
        self.hide()
        self.done(0)

    def cancela(self):
        self.parent.show()
        self.hide()

    def limpar_filtro(self):
        pass




