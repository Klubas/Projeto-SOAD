import logging
import os
import sys

__LOG_LEVEL__ = logging.DEBUG
__LOG_STREAM__ = sys.stderr

logging.basicConfig(stream=__LOG_STREAM__, level=__LOG_LEVEL__)


def update_ui():    # Atualiza os arquivos da pasta View
    import os
    from Resources.Scripts.Builder import Builder

    UI = "UI"
    # Pasta raiz
    b = Builder(
        pyuic_path="pyside2-uic",
        py_folder=os.path.join(".", "View"),
        ui_folder=os.path.join(".", "Resources", UI))

    b.build_files_from_folder(os.path.join(".", "Resources", UI))

    # Pasta componentes
    b = Builder(
        pyuic_path="pyside2-uic",
        py_folder=os.path.join(".", "View", "Componentes"),
        ui_folder=os.path.join(".", "Resources", UI, "Componentes"))

    b.build_files_from_folder(os.path.join(".", "Resources", UI, "Componentes"))


def main():

    os.environ['PATH'] = \
         os.path.join(os.getcwd(), 'Resources', 'mingw32', 'bin') \
         + os.pathsep \
         + os.environ['PATH']

    from PySide2.QtWidgets import QApplication
    from Controller.LoginDialog import LoginDialog

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    w = LoginDialog()
    login = w.exec()

    app.exec_()


if __name__ == '__main__':

    #update_ui()
    main()
    sys.exit()

else:
    print(__name__)
    print("Sorry Dave, you can't do that!")
