import sys
import os
from Model.DataBase import DataBase

import os
from PySide2.QtCore import QCoreApplication
QCoreApplication.addLibraryPath(os.path.join(".", "Resources", "lib"))
print(QCoreApplication.libraryPaths())


def update_ui():    # Atualiza os arquivos da pasta View
    from Resources.Scripts.Builder import Builder

    b = Builder(
        pyuic_path="pyside2-uic",
        ui_folder=os.path.join(".", "View"),
        py_folder=os.path.join(".", "Resources", "UI"))
    b.build_files_from_folder(os.path.join(".", "Resources", "UI"))


def setup_db_connection():
    try:
        return DataBase('soadmin', 'soad2019', 'localhost', port=5432)
    except Exception as e:
        print("Não foi possível se conectar ao banco de dados.")
        print(e)


def main(db):
    from Controller.MainWindow import MainWindow
    from PySide2.QtWidgets import QApplication

    # update_ui()

    app = QApplication(sys.argv)

    w = MainWindow(db)
    w.showMaximized()

    sys.exit(app.exec_())


if __name__ == '__main__':
    db = setup_db_connection()
    main(db)
else:
    print("Sorry Dave, you can't do that!")
