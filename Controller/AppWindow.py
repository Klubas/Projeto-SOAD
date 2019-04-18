import sys
sys.path.append('..')

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QDialog,
                             QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QWidget)

class AppWindow(QDialog, MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pass