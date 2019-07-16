import logging
import os
import sys

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

from Controller.LoginDialog import LoginDialog

QCoreApplication.addLibraryPath(os.path.join(".", "Resources", "lib"))
logging.debug(QCoreApplication.libraryPaths())

AMBIENTE = None

# todo: precisa melhorar esse tratamento de parametros
if len(sys.argv) > 1:
    if sys.argv[1] == 'dsv' or sys.argv[1] == 'prod':
        AMBIENTE = sys.argv[1]
    else:
        AMBIENTE = 'prod'
else:
    AMBIENTE = 'prod'

if AMBIENTE == 'dsv':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
else:
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)


print(AMBIENTE)


def update_ui():    # Atualiza os arquivos da pasta View
    from Resources.Scripts.Builder import Builder

    b = Builder(
        pyuic_path="pyside2-uic",
        ui_folder=os.path.join(".", "View"),
        py_folder=os.path.join(".", "Resources", "UI"))
    b.build_files_from_folder(os.path.join(".", "Resources", "UI"))


def main():

    # update_ui()

    app = QApplication(sys.argv)

    w = LoginDialog()
    w.exec()

    sys.exit(app.exec_())


if __name__ == '__main__':

    main()

else:
    print("Sorry Dave, you can't do that!")
