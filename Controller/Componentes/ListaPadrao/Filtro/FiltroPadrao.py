import os

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_FiltroPadrao import Ui_FiltroPadrao


class FiltroPadrao(QDialog, Ui_FiltroPadrao):

    string_filtro = Signal(list)

    def __init__(self, db, child=None, parent=None):
        super(FiltroPadrao, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.parent = parent

        self.setWindowIcon(QIcon(os.path.join('Resources', 'icons', 'filter.png')))

        self.child = child(db=self.db, parent=self.widget)
        self.child.setWindowFlags(Qt.Widget)
        self.child.move(0, 0)
        self.child.show()

        self.setMinimumHeight(self.child.height() + 60)
        self.setMinimumWidth(self.child.width() + 20)
        self.setMaximumHeight(self.child.height() + 60)
        self.setMaximumWidth(self.child.width() + 20)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)
        self.show()

    def montar_filtro(self) -> str:
        i = 0
        filtro = ''
        for metodo in self.child.metodos:
            valor = metodo()
            if valor != '':
                i = i + 1
                if i > 1:
                    filtro = filtro + " and "
                filtro = filtro + valor

        if i > 0:
            filtro = filtro + ";"

        print(filtro)
        return filtro

    def confirma(self):
        string_filtro = self.montar_filtro()
        print(string_filtro)
        self.string_filtro.emit(string_filtro)
        self.parent.show()
        self.hide()
        self.done(0)

    def cancela(self):
        if self.parent.isVisible():
            self.hide()
        else:
            self.parent.close()
            self.close()

    def limpar_filtro(self):
        self.child.limpar_filtro()





