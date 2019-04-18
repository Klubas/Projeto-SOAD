import sys

sys.path.append('..')

from Controller.AppWindow import AppWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    sys.exit(app.exec_())
