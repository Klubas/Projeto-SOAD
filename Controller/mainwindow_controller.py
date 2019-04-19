import sys
sys.path.append('..')

from PySide2.QtWidgets import QMainWindow
from View.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow ,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.showMaximized()