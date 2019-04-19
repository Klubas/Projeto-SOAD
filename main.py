import sys, os
from Resources.Builder import Builder

sys.path.append('..')

#from Controller.AppWindow import AppWindow
from PySide2.QtWidgets import QApplication


if __name__ == '__main__':
    # Generate UI files
    builder = Builder(view=os.path.join(".", "View"), resources=os.path.join(".", "View"))
    builder.build_files_from_folder("Resources")
    app = QApplication(sys.argv)
    #w = AppWindow()
    sys.exit(app.exec_())
