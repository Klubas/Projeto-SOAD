from PySide2.QtWidgets import QDialog

from View.Componentes.Ui_FiltroRemanufatura import Ui_FiltroRemanufatura


class FiltroRemanufatura(QDialog, Ui_FiltroRemanufatura):

    def __init__(self, db=None, parent=None):
        super(FiltroRemanufatura, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        self.metodos = tuple()

        self.dados = None

        ## Conectar botões/campos

        self.limpar_filtro()

    def limpar_filtro(self):
        pass
