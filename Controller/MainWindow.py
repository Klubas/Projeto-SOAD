import logging
import sys
from _datetime import datetime

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QMainWindow

from Controller.About import About
from Controller.CadastroMercadoria import CadastroMercadoria
from Controller.CadastroPedido import CadastroPedido
from Controller.CadastroPessoa import CadastroPessoa
from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.RelatorioPadrao import RelatorioPadrao
from Controller.Componentes.StatusDialog import StatusDialog
from Controller.EstornoPedido import EstornoPedido
from Controller.RegistroRemanufatura import RegistroRemanufatura
from View.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, db, login_dialog, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = login_dialog
        self.db = db
        self.window_list = list()
        # todo: self.setWindowIcon()
        self.setWindowTitle("SOAD - VIP Cartuchos")

        # Menus
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
        # todo: Arquivo
        self.actionSair.triggered.connect(
            lambda: self.closeEvent(event=QCloseEvent())
        )

        self.actionReconectar.triggered.connect(self.login)

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

        self.actionRegistrar_Remanufaturas.triggered.connect(
            lambda: self.abrir_interface(window_cls=RegistroRemanufatura, tipo='NORMAL')
        )

        #self.actionDescarte_de_Material.triggered.connect(
        #    lambda: self.abrir_cadastro(DescarteMercadoria)
        #)

        # Relatórios

        self.actionSobre.triggered.connect(self.abrir_sobre)

        # Botões

        self.pushButton_venda.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPedido, tipo="VENDA"
            )
        )

        self.pushButton_compra.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPedido, tipo="COMPRA"
            )
        )

        self.pushButton_pessoa.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPessoa
            )
        )

        self.pushButton_mercadoria.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroMercadoria
            )
        )

        self.pushButton_remanufatura.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RegistroRemanufatura
            )
        )

        # Relatórios

        self.pushButton_lista_vendas.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , tabela='vw_pedido_venda'
                , colunas={
                    "id_pedido":
                        ("Número", int),
                    "situacao":
                        ("Situação", str),
                    "data_cadastro":
                        ("Data do Pedido", datetime),
                    "data_entrega":
                        ("Data para Entrega", datetime),
                    "valor_total":
                        ("Valor Total", float),
                    "pessoa":
                        ("Cliente", str),
                    "documento":
                        ("Documento", str),
                    "inscricao_estadual":
                        ("Inscrição Estadual", str),
                    "fantasia":
                        ("Nome Fantasia", str),
                    "email":
                        ("Email", str),
                    "telefone":
                        ("Telefone", str),
                    "observacao":
                        ("Observações", str),
                }
            )
        )

        self.pushButton_lista_compras.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , tabela='vw_pedido_compra'
                , colunas={
                    "id_pedido":
                        ("Número", int),
                    "situacao":
                        ("Situação", str),
                    "data_cadastro":
                        ("Data do Pedido", datetime),
                    "data_entrega":
                        ("Data para Entrega", datetime),
                    "valor_total":
                        ("Valor Total", float),
                    "pessoa":
                        ("Cliente", str),
                    "documento":
                        ("Documento", str),
                    "inscricao_estadual":
                        ("Inscrição Estadual", str),
                    "fantasia":
                        ("Nome Fantasia", str),
                    "email":
                        ("Email", str),
                    "telefone":
                        ("Telefone", str),
                    "observacao":
                        ("Observações", str),
                }
            )
        )

    def abrir_interface(self, window_cls, **kwargs):
        try:

            tela = window_cls(
                self.db
                , self.window_list
                , parent=self
                , **kwargs
            )
            tela.setWindowIcon(self.windowIcon())
            self.window_list.append(tela)

        except Exception as e:
            logging.exception('[MainWindow] ' + str(e))
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='Não foi possível abrir a interface'
                , exception=e
                , parent=self
            )
            dialog.exec()

    def abrir_sobre(self):
        s = About()
        s.exec()

    def fechar(self):
        self.closeEvent(event=QCloseEvent())

    #Override QWidget closeEvent
    def closeEvent(self, event):
        if len(self.window_list) > 0:
            sair = ConfirmDialog()
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
    def login(self):
        self.hide()
        self.parent.exec()
