import logging

from PySide2.QtWidgets import QListWidgetItem, QDialogButtonBox

from Controller.Componentes.CadastroPadrao import CadastroPadrao
from Controller.Componentes.StatusDialog import StatusDialog
from View.Ui_CadastroUsuario import Ui_CadastroUsuario


class CadastroUsuario(CadastroPadrao, Ui_CadastroUsuario):

    def __init__(self, db, window_list, parent=None, **kwargs):
        super(CadastroUsuario, self).__init__(parent, **kwargs)
        self.setupUi(self)
        self.show()
