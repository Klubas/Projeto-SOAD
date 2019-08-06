from PySide2.QtWidgets import QWidget

from Controller.CadastroPadrao import CadastroPadrao
from View.Ui_CadastroMercadoria import Ui_CadastroMercadoria


class CadastroMercadoria(QWidget, CadastroPadrao, Ui_CadastroMercadoria):

    def __init__(self, db=None, window_list=None, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list
        self.tipo_pedido = kwargs.get('tipo_pedido')
        self.show()
