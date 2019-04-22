from PySide2.QtWidgets import QMainWindow
from View.MainWindow import Ui_MainWindow
from Controller.WindowCreator import WindowCreator
from Controller.CadastroPessoa_Controller import CadastroPessoa
from Controller.CadastroProduto_Controller import CadastroProduto
from Controller.CadastroInsumo_Controller import CadastroInsumo
from Controller.CadastroToner_Controller import CadastroToner
from Controller.About import About


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.setWindowIcon()
        self.setWindowTitle("SOAD - Vip Cartuchos")
        self.connect_menu_actions()

    def connect_menu_actions(self):
        # Arquivo
        self.actionSair.triggered.connect(self.close_clicked)

        # Cadastros
        self.actionPessoa.triggered.connect(lambda: self.new_window_clicked(window_cls=CadastroPessoa, modal=False))
        self.actionProduto.triggered.connect(lambda: self.new_window_clicked(window_cls=CadastroProduto, modal=False))
        self.actionInsumo.triggered.connect(lambda: self.new_window_clicked(window_cls=CadastroInsumo, modal=False))
        self.actionToners.triggered.connect(lambda: self.new_window_clicked(window_cls=CadastroToner, modal=False))

        # Vendas

        # Estoque

        # Ajuda
        self.actionSobre.triggered.connect(lambda: self.new_window_clicked(window_cls=About, modal=True))

    def new_window_clicked(self, window_cls, modal):
        w = WindowCreator(0, window_cls, self)
        w.run()
        return 0

    def close_clicked(self):
        self.close()
