import logging

from PySide2.QtCore import QDate
from PySide2.QtWidgets import QDialog

from Controller.Componentes.LocalizarDialog import LocalizarDialog
from View.Componentes.Ui_FiltroPedido import Ui_FiltroPedido

class FiltroPedido(QDialog, Ui_FiltroPedido):

    def __init__(self, db=None, parent=None):
        super(FiltroPedido, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        self.metodos = tuple()

        self.dados = None

        ## Conectar botões/campos

        self.limpar_filtro()

    def limpar_filtro(self):
        pass
