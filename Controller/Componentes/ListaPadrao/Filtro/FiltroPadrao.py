import logging
import os

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_FiltroPadrao import Ui_FiltroPadrao


class FiltroPadrao(QDialog, Ui_FiltroPadrao):

    string_filtro = Signal(tuple)

    def __init__(self, db, child=None, parent=None, **kwargs):
        super(FiltroPadrao, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.parent = parent

        self.setWindowIcon(QIcon(os.path.join('Resources', 'icons', 'filter.png')))

        self.child = child(db=self.db, parent=self.widget, **kwargs)
        self.child.setWindowFlags(Qt.Widget)
        self.child.move(0, 0)
        self.child.show()

        self.setMinimumHeight(self.child.height() + 60)
        self.setMinimumWidth(self.child.width() + 20)
        self.setMaximumHeight(self.child.height() + 60)
        self.setMaximumWidth(self.child.width() + 20)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)

        self.translate_ui()

        self.show()

    def montar_filtro(self) -> tuple:
        i = 0
        filtro = ''
        cabecalho = '<div class=filtros>'
        descricao = ''
        for metodo in self.child.metodos:
            valor = metodo()
            if isinstance(valor, tuple):
                valor_filtro = valor[0]
                if valor[2] != '':
                    cabecalho = \
                        cabecalho + \
                        '<span class=filtroLinha>' + \
                        '   <strong>' + valor[1] + ': </strong>' + valor[2] + \
                        '</span>'

            elif isinstance(valor, str):
                valor_filtro = valor

            else:
                break

            if valor_filtro != '':
                i = i + 1
                if i > 1:
                    filtro = filtro + " and "
                filtro = filtro + valor_filtro

        cabecalho = cabecalho + '</div>'
        logging.info('[FiltroPadrao] Filtro: ' + str(filtro))
        return filtro, cabecalho

    def confirma(self):
        filtro = self.montar_filtro()
        string_filtro = filtro[0]
        filtro_cabecalho = filtro[1]
        self.string_filtro.emit((string_filtro, filtro_cabecalho))
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

    def translate_ui(self):
        self.buttonBox.button(QDialogButtonBox.Ok).setIcon(QIcon(os.path.join('Resources', 'icons', 'filter.png')))
        self.buttonBox.button(QDialogButtonBox.Ok).setText('Filtrar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')





