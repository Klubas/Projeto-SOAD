from PySide2.QtWidgets import QWidget

from Controller.CadastroPadrao import CadastroPadrao
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog
from View.Ui_CadastroMercadoria import Ui_CadastroMercadoria


class CadastroMercadoria(QWidget, CadastroPadrao, Ui_CadastroMercadoria):

    def __init__(self, db=None, window_list=None, **kwargs):
        super(CadastroPadrao, self).__init__()
        super(CadastroMercadoria, self).__init__()
        self.setupUi(self)

        self.db = db
        self.window_list = window_list
        self.modo_edicao = False
        self.parent_window = self
        self.tipo_pedido = kwargs.get('tipo')

        if self.tipo_pedido is None:
            self.tipo_pedido = 'MERCADORIA'

        elif self.tipo_pedido == 'MERCADORIA':
            pass

        elif self.tipo_pedido == 'CASCO':
            pass

        elif self.tipo_pedido == 'INSUMO':
            pass

        else:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='TIPO DE MERCADORIA INVÁLIDO'
                , parent=self.parent_window)
            dialog.exec()

        self.setWindowTitle('SOAD - Cadastrar ' + self.tipo_pedido.capitalize())

        self.campos_obrigatorios = dict([

        ])

        # Define se ativa o botão editar e excluir
        self.pushButton_editar.setDisabled(True)
        self.pushButton_excluir.setDisabled(True)
        self.lineEdit_id.textChanged[str].connect(self.define_permite_editar)

        self.dialog_localizar = LocalizarDialog(db=self.db)

        self.show()

    def cadastrar(self):
        super(CadastroMercadoria, self).cadastrar()

    def editar(self):
        super(CadastroMercadoria, self).editar()

    def excluir(self):
        retorno = super(CadastroMercadoria, self).excluir()

    def limpar_dados(self):
        super(CadastroMercadoria, self).limpar_dados()

    def localizar(self, parent=None):
        super(CadastroMercadoria, self).localizar(parent=self)

    def valida_obrigatorios(self):
        super(CadastroMercadoria, self).valida_obrigatorios()

    def confirma(self):
        super(CadastroMercadoria, self).confirma()

    def cancela(self):
        super(CadastroMercadoria, self).cancela()

    def atualizar_interface(self):
        pass

    def popular_interface(self):
        pass

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()

