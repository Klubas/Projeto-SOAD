import logging
import sys

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow

from Controller.About import About
from Controller.CadastroMercadoria import CadastroMercadoria
from Controller.CadastroPedido import CadastroPedido
from Controller.CadastroPessoa import CadastroPessoa
from Controller.Componentes.SairDialog import SairDialog
from Controller.Componentes.StatusDialog import StatusDialog
from Controller.EstornoPedido import EstornoPedido
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

        #self.window_list.append(self)

        # Menus
        # todo: Arquivo
        self.actionSair.triggered.connect(
            lambda: self.closeEvent(event=QCloseEvent())
        )

        self.actionReconectar.triggered.connect(
            lambda: self.reconectar()
        )

        # todo: Cadastros
        self.actionPessoa.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPessoa)
        )

        self.actionMercadoria.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroMercadoria, tipo='MERCADORIA')
        )

        self.actionInsumo.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroMercadoria, tipo='INSUMO')
        )

        self.actionCasco.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroMercadoria, tipo='CASCO')
        )

        # todo: Vendas
        self.actionNova_Venda.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPedido, tipo="VENDA")
        )

        self.actionDevolucao.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=EstornoPedido
            )
        )

        # todo: Estoque
        self.actionRegistrar_compra.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPedido, tipo="COMPRA")
        )

        #self.actionNova_Remanufatura.triggered.connect(
        #    lambda: self.abrir_cadastro(CadastrarRemanufatura)
        #)

        #self.actionDescarte_de_Material.triggered.connect(
        #    lambda: self.abrir_cadastro(DescarteMercadoria)
        #)

        # Relatórios

        # todo: Ajuda
        self.actionSobre.triggered.connect(self.abrir_sobre)

        self.pushButton_venda.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPedido, tipo="VENDA")
        )

        self.pushButton_pessoa.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPessoa)
        )

    def abrir_interface(self, window_cls, **kwargs):
        try:

            cad = window_cls(
                self.db
                , self.window_list
                , parent=self
                , **kwargs
            )

            self.window_list.append(cad)
            print('MAIN: ' + str(self.window_list))

        except Exception as e:
            logging.exception(e)
            dialog = StatusDialog(status='ERRO')
            dialog.definir_mensagem('Não foi possível abrir a interface', e)
            dialog.exec()

    def abrir_sobre(self):
        s = About()
        s.exec()

    def reconectar(self):
        self.parent.exec()

    def fechar(self):
        self.closeEvent(event=QCloseEvent())

    #Override QWidget closeEvent
    def closeEvent(self, event):
        if len(self.window_list) > 0:
            sair = SairDialog()
            if sair.exec():
                for window in self.window_list:
                    window.close() # Fecha todas as janelas
                self.db.fechar_conexao()
                event.accept()     # Finaliza a aplicação
                sys.exit()
        else:
            event.accept() # Finaliza a aplicação
            sys.exit()

        # Não finaliza a aplicação
        event.ignore()

    # metodo para reconectar ao banco
    def login(self, parent):
        parent.show()
