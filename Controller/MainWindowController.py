import sys

from PySide2.QtCore import SIGNAL
from PySide2.QtWidgets import QMainWindow, QWidget
from View.MainWindow import Ui_MainWindow

from CadastroProdutoController import CadastroProduto


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.setWindowIcon()
        self.setWindowTitle("SOAD - Vip Cartuchos")
        self.dialogs = list()
        self.create_menus()

    def create_menus(self):
        self.actionPessoa.setStatusTip("Cadastrar pessoas")

        self.actionProduto.setStatusTip("Cadastrar produtos")
        #self.actionProduto.triggered.connect(self.cadastro_produto_clicked)
        self.connect(self.actionProduto, SIGNAL('clicked()'), self.cadastro_produto_clicked)

        self.actionInsumo.setStatusTip("Cadastrar insumos")

        self.actionToners.setStatusTip("Cadastrar toners")

        self.actionSobre.setStatusTip("Sobre o sistema SOAD")

        self.actionSair.setStatusTip("Sair do sistema")
        self.actionSair.triggered.connect(self.close_clicked)

    def cadastro_produto_clicked(self):
        form = CadastroProduto(self)
        self.dialogs.append(form)
        form.show()

    def close_clicked(self):
        self.close()
