import sys
sys.path.append('..')

from View.MainWindow import MainWindow

from PyQt5.QtWidgets import (QDialog)

class AppWindow(QDialog, MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pass