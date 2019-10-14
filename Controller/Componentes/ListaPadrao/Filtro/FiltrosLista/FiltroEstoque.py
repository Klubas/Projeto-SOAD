from PySide2.QtWidgets import QDialog

from View.Componentes.Ui_FiltroEstoque import Ui_FiltroEstoque


class FiltroEstoque(QDialog, Ui_FiltroEstoque):

    def __init__(self, parent=None):
        super(FiltroEstoque, self).__init__(parent)



