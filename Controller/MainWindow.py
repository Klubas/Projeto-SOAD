import logging
import os
import sys

from PySide2.QtGui import QCloseEvent, QImage, QPixmap
from PySide2.QtWidgets import QMainWindow

from Controller.About import About
from Controller.CadastroMercadoria import CadastroMercadoria
from Controller.CadastroPedido import CadastroPedido
from Controller.CadastroPessoa import CadastroPessoa
from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.RelatorioPadrao import RelatorioPadrao
from Controller.Componentes.StatusDialog import StatusDialog
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

        icone_venda=QImage(os.path.join('Resources', 'icons', 'vendas.png')).smoothScaled(85, 85)
        icone_compra = QImage(os.path.join('Resources', 'icons', 'compras.png')).smoothScaled(85, 85)
        icone_mercadoria = QImage(os.path.join('Resources', 'icons', 'mercadorias.png')).smoothScaled(85, 85)
        icone_pessoa = QImage(os.path.join('Resources', 'icons', 'pessoa_fisica.png')).smoothScaled(85, 85)
        icone_logo = QImage(os.path.join('Resources', 'Imagens', 'soad.png')).smoothScaled(150, 150)
        icone_empresa = QImage(os.path.join('Resources', 'Imagens', 'logo.png')).smoothScaled(90, 70)

        self.label_icone_venda.setPixmap(QPixmap.fromImage(icone_venda))
        self.label_icone_compra.setPixmap(QPixmap.fromImage(icone_compra))
        self.label_icone_mercadoria.setPixmap(QPixmap.fromImage(icone_mercadoria))
        self.label_icone_pessoa.setPixmap(QPixmap.fromImage(icone_pessoa))
        self.label_logo.setPixmap(QPixmap.fromImage(icone_logo))
        self.label_logo_empresa.setPixmap(QPixmap.fromImage(icone_empresa))

        self.label_logo.setWindowOpacity(0)


        # Menus
        self.actionSair.triggered.connect(
            lambda: self.closeEvent(event=QCloseEvent())
        )

        self.actionReconectar.triggered.connect(self.login)

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

        self.actionNova_Venda.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPedido, tipo="VENDA")
        )

        self.actionDevolucao.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=EstornoPedido
            )
        )

        self.actionRegistrar_compra.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPedido, tipo="COMPRA")
        )

        self.actionRegistrar_Remanufaturas.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RegistroRemanufatura, tipo='NORMAL')
        )

        # Relatórios

        self.actionProdutos_em_Estoque.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Relatório de itens em estoque'
                , tipo='ESTOQUE'
            )
        )

        self.actionVendas.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Relatório de vendas'
                , tipo='VENDA'
            )
        )

        self.actionCompras.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Relatório de compras'
                , tipo='COMPRA'
            )
        )

        self.actionMercadorias.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Lista de mercadorias'
                , tipo='MERCADORIA'
            )
        )

        # self.actionDescartes.triggered.connect()

        self.actionRelacao_de_clientes.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Lista de clientes'
                , tipo='CLIENTE'
            )
        )

        self.actionRelacao_de_fornecedores.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Lista de fornecedores'
                , tipo='FORNECEDOR'
            )
        )

        self.actionLista_de_remanufaturas.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Lista de remanufaturas'
                , tipo='REMANUFATURA'
            )
        )

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
                , titulo='Relatório de vendas'
                , tipo='VENDA'
            )
        )

        self.pushButton_lista_compras.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Relatório de compras'
                , tipo='COMPRA'
            )
        )

        self.pushButton_lista_estoque.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Relatório de itens em estoque'
                , tipo='ESTOQUE'
            )
        )

        self.pushButton_lista_clientes.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Lista de clientes'
                , tipo='CLIENTE'
            )
        )

        self.pushButton_lista_fornecedores.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Lista de fornecedores'
                , tipo='FORNECEDOR'
            )
        )

        self.pushButton_lista_mercadoria.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Lista de mercadorias'
                , tipo='MERCADORIA'
            )
        )

        self.pushButton_lista_remanufatura.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=RelatorioPadrao
                , titulo='Lista de remanufaturas'
                , tipo='REMANUFATURA'
            )
        )

    def abrir_interface(self, window_cls, **kwargs):
        try:

            tela = window_cls(
                self.db
                , self.window_list
                , parent=None
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
        print(self.window_list)
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
