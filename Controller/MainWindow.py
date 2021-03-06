import logging
import os
import sys

from PySide2.QtGui import QCloseEvent, QImage, QPixmap
from PySide2.QtWidgets import QMainWindow

from Controller.About import About
from Controller.CadastroMercadoria import CadastroMercadoria
from Controller.CadastroMunicipio import CadastroMunicipio
from Controller.CadastroPedido import CadastroPedido
from Controller.CadastroPessoa import CadastroPessoa
from Controller.CadastroUsuario import CadastroUsuario
from Controller.AjusteEstoque import AjusteEstoque
from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.ListaPadrao.ListaPadrao import ListaPadrao
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
        self.setWindowTitle("SOAD - VIP Cartuchos")

        self.label_user.setText('Usuário: {username}\n[{host}:{port}]'
                                .format(username=self.db.username, host=self.db.host, port=str(self.db.port)))

        icone_venda=QImage(os.path.join('Resources', 'icons', 'vendas.png')).smoothScaled(85, 85)
        icone_compra = QImage(os.path.join('Resources', 'icons', 'compras.png')).smoothScaled(85, 85)
        icone_mercadoria = QImage(os.path.join('Resources', 'icons', 'mercadorias.png')).smoothScaled(85, 85)
        icone_pessoa = QImage(os.path.join('Resources', 'icons', 'pessoa_fisica.png')).smoothScaled(85, 85)
        icone_logo = QImage(os.path.join('Resources', 'Imagens', 'soad.png')).smoothScaled(150, 150)
        icone_empresa = QImage(os.path.join('Resources', 'Imagens', 'logo_mono.png')).smoothScaled(174, 122)

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

        self.actionCadastroUsuario.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroUsuario
            )
        )

        self.actionPessoa.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPessoa)
        )

        self.actionMunicipios.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroMunicipio
            )
        )

        self.actionAjusteDeEstoque.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=AjusteEstoque
            )
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

        self.actionRegistrar_compra.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=CadastroPedido, tipo="COMPRA")
        )

        self.actionRegistrar_Remanufaturas.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=RegistroRemanufatura, tipo='NORMAL')
        )

        # Relatórios

        self.actionLista_estoque.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='ESTOQUE'
            )
        )

        self.actionListaDeInventrio.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='INVENTARIO'
            )
        )

        self.actionLista_de_itens_em_estoque.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='ITEM_ESTOQUE'
            )
        )

        self.actionVendas.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='VENDA'
            )
        )

        self.actionCompras.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='COMPRA'
            )
        )

        self.actionMercadorias.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='MERCADORIA'
            )
        )

        # self.actionDescartes.triggered.connect()

        self.actionRelacao_de_clientes.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='CLIENTE'
            )
        )

        self.actionRelacao_de_fornecedores.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='FORNECEDOR'
            )
        )

        self.actionLista_de_remanufaturas.triggered.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='REMANUFATURA'
            )
        )

        self.actionSobre.triggered.connect(self.abrir_sobre)

        self.actionAjuda.triggered.connect(self.abrir_manual)

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
                window_cls=ListaPadrao
                , tipo='VENDA'
            )
        )

        self.pushButton_lista_compras.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='COMPRA'
            )
        )

        self.pushButton_lista_estoque.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='ESTOQUE'
            )
        )

        self.pushButton_lista_itens.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='ITEM_ESTOQUE'
            )
        )

        self.pushButton_lista_clientes.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='CLIENTE'
            )
        )

        self.pushButton_lista_fornecedores.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='FORNECEDOR'
            )
        )

        self.pushButton_lista_mercadoria.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
                , tipo='MERCADORIA'
            )
        )

        self.pushButton_lista_remanufatura.clicked.connect(
            lambda: self.abrir_interface(
                window_cls=ListaPadrao
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
        logging.info("[MainWindow] Janelas abertas: " + str(self.window_list))
        if len(self.window_list) > 0:
            sair = ConfirmDialog(parent=self)
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

    def abrir_manual(self):
        import platform, subprocess

        filepath = os.path.join('Resources', 'misc', 'manual-soad.pdf')

        logging.info('[MainWindow] Abrindo manual...')

        try:
            if platform.system() == 'Darwin':
                subprocess.call(('open', filepath))

            elif platform.system() == 'Windows':
                try:
                    os.startfile(filepath)
                except Exception as e:
                    logging.debug('[MainWindow] Tentando método alternativo de abertura de arquivo devido a exceção: \n>' + str(e))
                    subprocess.run(['open', filepath], check=True)
            else:
                subprocess.call(('xdg-open', filepath))

        except Exception as e:

            dialog = StatusDialog(
                status='ALERTA'
                , mensagem="Arquivo " + filepath + " não encontrado."
                , exception=e
                , parent=self
            )

            logging.debug(
                '[MainWindow] Arquivo não encontrado: \n>' + str(e))

            dialog.exec()

