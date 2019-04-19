import sys

sys.path.append('..')

from Controller.AppWindow import AppWindow
from PySide2.QtWidgets import QApplication

from Interface.Builder import Builder
builder = Builder()
builder.build_files_from_folder("./Interface")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    sys.exit(app.exec_())
