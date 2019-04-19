import sys
sys.path.append('..')

from PySide2.QtWidgets import (QDialog)
from Interface.mainwindow import Ui_MainWindow

class AppWindow(QDialog, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
