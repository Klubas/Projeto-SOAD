import logging

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow

from Controller.About import About
from Controller.CadastroPedido import CadastroPedido
from Controller.CadastroPessoa import CadastroPessoa
from Controller.SairDialog import SairDialog
from Controller.StatusDialog import StatusDialog
from View.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, db, parent):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.db = db
        self.window_list = list()
        # todo: self.setWindowIcon()
        self.setWindowTitle("SOAD - VIP Cartuchos")

        # Menus
        # todo: Arquivo
        self.actionSair.triggered.connect(
            lambda: self.closeEvent(event=QCloseEvent())
        )

        self.actionReconectar.triggered.connect(
            lambda: self.login(parent)
        )

        # todo: Cadastros
        self.actionPessoa.triggered.connect(
            lambda: self.abrir_cadastro(window_cls=CadastroPessoa)
        )

        # todo: Vendas
        self.actionNova_Venda.triggered.connect(
            lambda: self.abrir_cadastro(CadastroPedido, tipo_pedido="VENDA")
        )

        # todo: Estoque

        # todo: Ajuda
        self.actionSobre.triggered.connect(self.abrir_sobre)

    def abrir_cadastro(self, window_cls, **kwargs):
        try:

            cad = window_cls(
                self.db, self.window_list
                ,  tipo_pedido=kwargs.get('tipo_pedido')
            )

            self.window_list.append(cad)
            cad.show()
            cad.confirma()

        except Exception as e:
            logging.exception(e)
            dialog = StatusDialog(status='ERRO')
            dialog.definir_mensagem('Não foi possível abrir a interface', e)
            dialog.exec()

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

    # metodo para reconectar ao banco
    def login(self, parent):
        parent.show()