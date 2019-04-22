import sys
import os


def update_ui():    # Atualiza os arquivos da pasta View
    from Resources.Builder import Builder

    Builder(
        py_uic_path="pyside2-uic",
        ui_folder=os.path.join(".", "View"),
        py_folder=os.path.join(".", "Resources")).build_files_from_folder("Resources")


def main():
    from Controller.MainWindow_Controller import MainWindow
    from PySide2.QtWidgets import QApplication

    # update_ui()

    app = QApplication(sys.argv)

    w = MainWindow()
    w.showMaximized()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
else:
    print("Sorry Dave, you can't do that!")
