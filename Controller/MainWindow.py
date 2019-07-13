from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QCloseEvent
from View.Ui_MainWindow import Ui_MainWindow

from Controller.About import About
from Controller.SairDialog import SairDialog
from Controller.StatusDialog import StatusDialog

from Controller.CadastroPessoa import CadastroPessoa


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, db, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.window_list = list()
        # self.setWindowIcon()
        self.setWindowTitle("SOAD - VIP Cartuchos")
        self.connect_menu_actions()

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
        #try:
        cad = window_cls(self.db, self.window_list)
        self.window_list.append(cad)
        cad.show()
        cad.confirma()
        #except Exception as e:
         #   dialog = StatusDialog(status='ERRO')
          #  dialog.definir_mensagem(str(e))
           # dialog.exec()

    def abrir_sobre(self):
        s = About()
        s.exec()

    def fechar(self):
        self.closeEvent(event=QCloseEvent())

    #Override QWidget closeEvent
    def closeEvent(self, event):
        if len(self.window_list) > 0:
            sair = SairDialog()
            if sair.exec():
                for window in self.window_list:
                    window.close() # fecha todas as janelas
                self.db.fechar_conexao()
                event.accept()     # fecha a MainWindow
            else:
                print(self.window_list)
                event.ignore()
        else:
            event.accept()

