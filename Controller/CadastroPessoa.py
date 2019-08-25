from PySide2.QtWidgets import QDialogButtonBox
from PySide2.QtWidgets import QWidget

from Controller.CadastroPadrao import CadastroPadrao
from Model.Pessoa import Pessoa
from View.Ui_CadastroPessoa import Ui_CadastroPessoa


class CadastroPessoa(QWidget, CadastroPadrao, Ui_CadastroPessoa):

    def __init__(self, db, window_list, **kwargs):
        super(CadastroPessoa, self).__init__()
        super(CadastroPadrao, self).__init__()

        self.setupUi(self)

        self.db = db
        self.window_list = window_list
        self.modo_edicao = False

        self.frame_menu.setDisabled(False)
        self.widget.setDisabled(True)
        self.frame_buttons.setDisabled(True)

        self.pushButton_cadastrar.clicked.connect(self.cadastrar)
        self.pushButton_editar.clicked.connect(self.editar)
        self.pushButton_excluir.clicked.connect(self.excluir)
        self.pushButton_localizar.clicked.connect(self.localizar)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)

        # Marca como isento o lineEdit
        self.checkBox_isento.clicked.connect(
            lambda: self.checkBox_isento.setDisabled(not self.checkBox_isento.isEnabled())
        )

        # Ativar e desativar campos de acordo com o tipo
        self.radioButton_pf.clicked.connect(self.define_tipo)

        self.show()

    def cadastrar(self):
        super(CadastroPessoa, self).cadastrar()
        self.widget_tipo_pessoa.setDisabled(False)

    def editar(self):
        super(CadastroPessoa, self).editar()
        self.widget_tipo_pessoa.setDisabled(True)

    def excluir(self):
        super(CadastroPessoa, self).excluir()

    def limpar_dados(self):
        # limpa todos os campos
        super(CadastroPessoa, self).limpar_dados()
        self.lineEdit_nome.clear()
        self.lineEdit_email.clear()
        self.lineEdit_telefone.clear()
        self.lineEdit_IE.clear()
        self.lineEdit_documento.clear()
        self.lineEdit_fantasia.clear()

    def localizar(self):
        self.localizar_campos = {
            "id_pessoa": 'ID',
            "nome": 'Nome',
            'documento': "Documento"
        }

        self.colunas_busca = {
            "id_pessoa": 'ID',
            "nome": 'Nome',
            'documento': "Documento"
        }

        self.view_busca = 'vw_pessoa'

        super(CadastroPessoa, self).localizar()

        self.popular_interface(self.dados[0])

    def confirma(self):

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
        self.dados = {
            "metodo": "prc_insert_pessoa",
            "schema": "soad",
            "params": pessoa.to_dict()
        }

        #todo: tratar existencia de ID para verificar se cadastra ou edita
        if super(CadastroPessoa, self).confirma():
            print('Sucesso')
            self.limpar_dados()
            self.carrega_dados()

        else:
            print('Erro ao salvar')

    def popular_interface(self, dados):

        pessoa = Pessoa(
            nome=dados['nome']
            , email=dados['email']
            , telefone=dados['telefone']
            , inscricao_estadual=dados['inscricao_estadual']
            , documento=dados['documento']
            , fantasia=dados['fantasia']
        )

        self.lineEdit_nome.setText(pessoa.nome)
        self.lineEdit_email.setText(pessoa.email)
        self.lineEdit_telefone.setText(pessoa.telefone)
        if pessoa.inscricao_estadual == 'ISENTO':
            self.checkBox_isento.setChecked(True)
        else:
            self.checkBox_isento.setChecked(False)
        self.lineEdit_IE.setText(pessoa.inscricao_estadual)
        self.lineEdit_documento.setText(pessoa.documento)
        self.lineEdit_fantasia.setText(pessoa.fantasia)

        if len(pessoa.documento) == 11:
            self.radioButton_pf.setChecked(True)
        elif len(pessoa.documento) == 14:
            self.radioButton_pj.setChecked(True)



    def define_tipo(self):
        print('Tipo')

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()
