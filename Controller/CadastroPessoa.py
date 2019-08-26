from PySide2.QtWidgets import QDialogButtonBox
from PySide2.QtWidgets import QWidget

from Controller.CadastroPadrao import CadastroPadrao
from Controller.Componentes.StatusDialog import StatusDialog
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
        self.frame_contents.setDisabled(True)
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

        # campos obrigatorios
        self.campos_obrigatorios = dict([
                ('Documento', self.lineEdit_documento)
                , ('Nome', self.lineEdit_nome)
                , ('CEP', self.lineEdit_cep)
                , ('UF', self.comboBox_uf)
                , ('Município', self.comboBox_municipio)
                , ('Logradouro', self.lineEdit_logradouro)
                , ('Número', self.lineEdit_numero)
                , ('Bairro', self.lineEdit_bairro)
        ])

        # Ativar e desativar campos de acordo com o tipo
        self.radioButton_pf.toggled.connect(self.define_tipo)
        self.define_tipo()

        # Atualiza combobox de municipios
        self.comboBox_uf.currentTextChanged[str].connect(self.altera_uf)

        self.modalidades = dict()
        self.ufs = dict()
        self.ufs_municipios = dict()

        self.popular_dados_padrao()

        self.show()

    def cadastrar(self):
        super(CadastroPessoa, self).cadastrar()
        self.limpar_dados()
        self.widget_tipo_pessoa.setDisabled(False)

    def editar(self):
        super(CadastroPessoa, self).editar()
        self.widget_tipo_pessoa.setDisabled(True)

    def excluir(self):
        super(CadastroPessoa, self).excluir()

    def limpar_dados(self):
        # limpa todos os campos
        super(CadastroPessoa, self).limpar_dados()

        # identificacao
        self.lineEdit_nome.clear()
        self.lineEdit_email.clear()
        self.lineEdit_telefone.clear()
        self.lineEdit_IE.clear()
        self.lineEdit_documento.clear()
        self.lineEdit_fantasia.clear()

        # endereco
        self.lineEdit_cep.clear()
        self.lineEdit_logradouro.clear()
        self.lineEdit_numero.clear()
        self.lineEdit_bairro.clear()
        self.lineEdit_complemento.clear()

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

        dados = super(CadastroPessoa, self).localizar()

        dados = self.db.get_registro("fnc_get_pessoa", "pessoa_id", dados)
        # todo: banco
        print("precisa implementar no banco essa funcao")

        if dados[0] != 0:
            self.popular_interface(dados[0])

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

        #endereco = Endereco()

        # pega os dados da tela e popula um dicionario de dados
        self.dados = {
            "metodo": "fnc_insert_pessoa",
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
            , id_pessoa=dados['id_pessoa']
        )

        #endereco = Endereco()

        self.label_id.setText(pessoa.id_pessoa)
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

        # buscar endereco

        # buscar modalidade

    def popular_dados_padrao(self):
        # preenche modalidades
        items = self.db.busca_registro("modalidade", "id_modalidade")

        if items[0]:
            self.modalidades = items[1][0]['fnc_buscar_registro']

            for mod in self.modalidades:
                self.listWidget_modalidade.addItem(mod["descricao"])

        else:
            dialog = StatusDialog(status='AVISO', exception=items[1])
            dialog.definir_mensagem("Não foi possível localizar as Modalidades")
            dialog.exec()

        # preenche estados

        items = self.db.busca_registro("vw_estado", "pais", "brasil")

        if items[0]:
            self.ufs = items[1][0]['fnc_buscar_registro']

            for uf in self.ufs:
                self.comboBox_uf.addItem(uf["sigla_uf"])

            self.comboBox_uf.setCurrentIndex(0)

        else:
            dialog = StatusDialog(status='AVISO', exception=items[1])
            dialog.definir_mensagem("Não foi possível localizar as UFs")
            dialog.exec()

        # preenche municipios

        self.altera_uf()

    def define_tipo(self):
        if self.radioButton_pj.isChecked():
            self.lineEdit_fantasia.setVisible(True)
            self.label_fantasia.setVisible(True)
            self.label_documento.setText('CNPJ:')
            self.lineEdit_documento.setInputMask('99.999.999/9990-99')

        elif self.radioButton_pf.isChecked():
            self.lineEdit_fantasia.setVisible(False)
            self.label_fantasia.setVisible(False)
            self.label_documento.setText('CPF:')
            self.lineEdit_documento.setInputMask('999.999.999-99')


    def altera_uf(self):
        items = self.db.busca_registro("vw_municipio", "sigla_uf", self.comboBox_uf.currentText())
        print(items)
        if items[0]:
            self.ufs_municipios = items[1][0]['fnc_buscar_registro']
            if self.ufs_municipios is not None :
                print(self.ufs_municipios)
                self.comboBox_municipio.clear()
                for mun in self.ufs_municipios:
                    self.comboBox_municipio.addItem(mun["municipio"])

        else:
            dialog = StatusDialog(status='AVISO', exception=items[1])
            dialog.definir_mensagem("Não foi possível localizar os municipios.")
            dialog.exec()

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()
