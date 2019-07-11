from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QCloseEvent
from View.Ui_MainWindow import Ui_MainWindow
from Controller.About import About
from Controller.CadastroPessoa import CadastroPessoa

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, db, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        # self.setWindowIcon()
        self.setWindowTitle("SOAD - VIP Cartuchos")
        self.connect_menu_actions()
        self.window_list = list()

    def connect_menu_actions(self):
        # Arquivo
        self.actionSair.triggered.connect(lambda: self.closeEvent(event=QCloseEvent()))

        # Cadastros
        self.actionPessoa.triggered.connect(lambda: self.abrir_cadastro(window_cls=CadastroPessoa))

        # Vendas

        # Estoque

        # Ajuda
        self.actionSobre.triggered.connect(self.abrir_sobre)

    def abrir_cadastro(self, window_cls):
        cad = window_cls(self.db, self.window_list)
        self.window_list.append(cad)
        cad.show()

    def abrir_sobre(self):
        s = About()
        s.exec()

    def __fechar(self):
        if len(self.window_list) > 0:
            sair = input("Deseja fechar? (s/n)").upper()
            if sair == 'S':
                return True
            else:
                return False
        elif len(self.window_list) == 0:
            return True

    def closeEvent(self, event):
        if self.__fechar():
            for window in self.window_list:
                window.close()
            event.accept() # let the window close
        else:
            event.ignore()
