from PySide2.QtWidgets import QDialogButtonBox
from PySide2.QtWidgets import QWidget

from Controller.CadastroPadrao import CadastroPadrao
from Model.Pessoa import Pessoa
from View.Ui_CadastroPessoa import Ui_CadastroPessoa


class CadastroPessoa(QWidget, CadastroPadrao, Ui_CadastroPessoa):

    def __init__(self, db, window_list, parent=None, **kwargs):
        super(CadastroPessoa, self).__init__()
        super(CadastroPadrao, self).__init__()
        self.setupUi(self)

        self.db = db
        self.window_list = window_list

        self.frame_menu.setDisabled(False)
        self.widget.setDisabled(True)
        self.frame_buttons.setDisabled(True)

        self.pushButton_cadastrar.clicked.connect(self.cadastrar)
        self.pushButton_editar.clicked.connect(self.editar)
        self.pushButton_excluir.clicked.connect(self.excluir)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.formata_dados_e_salva)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.limpar_dados)

        # Marca como isento o lineEdit
        self.checkBox_isento.clicked.connect(
            lambda: self.checkBox_isento.setDisabled(not self.checkBox_isento.isEnabled())
        )

        # Ativar e desativar campos de acordo com o tipo
        self.radioButton_pf.clicked.connect(self.define_tipo)

        self.show()

    def cadastrar(self):
        self.widget_tipo_pessoa.setDisabled(False)
        self.frame_menu.setDisabled(True)
        self.frame_buttons.setDisabled(False)
        self.widget.setDisabled(False)

    def editar(self):
        self.widget_tipo_pessoa.setDisabled(True)
        self.frame_menu.setDisabled(True)
        self.frame_buttons.setDisabled(False)
        self.widget.setDisabled(False)

    def excluir(self):
        #excluir
        self.limpar_dados()

    def limpar_dados(self):
        # limpa todos os campos
        self.lineEdit_nome.clear()
        self.lineEdit_email.clear()
        self.lineEdit_telefone.clear()
        self.lineEdit_IE.clear()
        self.lineEdit_documento.clear()
        self.lineEdit_fantasia.clear()

        self.frame_menu.setDisabled(False)
        self.widget.setDisabled(True)
        self.frame_buttons.setDisabled(True)

    def carrega_dados(self):
        # pega os dados dos banco e popula a interface
        pass

    def define_tipo(self):
        print('Tipo')
        pass

    def formata_dados_e_salva(self):

        if self.checkBox_isento.isChecked():
            IE_pessoa = 'ISENTO'
        else:
            IE_pessoa = self.lineEdit_IE.text()

        pessoa = Pessoa(
            nome=self.lineEdit_nome.text()
            , email=self.lineEdit_email.text()
            , telefone=self.lineEdit_telefone.text()
            , inscricao_estadual=IE_pessoa
            , documento=self.lineEdit_documento.text()
            , fantasia=self.lineEdit_fantasia.text()
        )

        # pega os dados da tela e popula um dicionario de dados
        dados = {
            "metodo": "fnc_insert_pessoa",
            "params": {
                "nome": pessoa.nome,
                "email": pessoa.email,
                "telefone": pessoa.telefone,
                "documento": pessoa.documento,
                "inscricao_estadual": pessoa.inscricao_estadual,
                "fantasia": pessoa.fantasia
            }
        }

        #todo: tratar existencia de ID para verificar se cadastra ou edita
        if self.confirma(dados):
            print('Sucesso')
            self.limpar_dados()
            self.carrega_dados()

        else:
            print('Erro ao salvar')


    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()
