from PySide2.QtWidgets import QWidget

from View.Componentes.Ui_MenuCadastro import Ui_MenuCadastro


class MenuCadastro(QWidget, Ui_MenuCadastro):

    def __init__(self, parent, **kwargs):
        super(MenuCadastro, self).__init__(parent)
        self.setupUi(self)
