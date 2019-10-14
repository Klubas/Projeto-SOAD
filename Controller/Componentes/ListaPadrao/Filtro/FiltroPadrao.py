from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem
from View.Componentes import Ui_FiltroPadrao

class FiltroPadrao(QDialog, Ui_FiltroPadrao):
    def __init__(self, parent=None):
        super(FiltroPadrao, self).__init__(parent)

