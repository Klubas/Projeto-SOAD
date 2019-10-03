import logging

from PySide2.QtWidgets import QWidget, QListWidgetItem, QDialogButtonBox

from Controller.Componentes.CadastroPadrao import CadastroPadrao
from Controller.Componentes.StatusDialog import StatusDialog
from Model.Endereco import Endereco
from Model.Pessoa import Pessoa
from View.Ui_CadastroPessoa import Ui_CadastroPessoa


class CadastroPessoa(QWidget, CadastroPadrao, Ui_CadastroPessoa):

    def __init__(self, db, window_list, **kwargs):
        super(CadastroPessoa, self).__init__()
        super(CadastroPadrao, self).__init__()
        self.parent_window = self
        self.setupUi(self)

        self.setWindowTitle('SOAD - Cadastro de Pessoa')

        self.db = db
        self.window_list = window_list
        self.modo_edicao = False

        self.filtro_adicional = None

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
        self.checkBox_isento.toggled.connect(self.altera_ie)
        self.checkBox_isento.setChecked(False)

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
        self.widget_tipo_pessoa.setVisible(False)
        self.radioButton_pf.toggled.connect(self.define_tipo)
        self.define_tipo()

        # Atualiza combobox de municipios
        self.comboBox_uf.currentTextChanged[str].connect(self.altera_uf)

        self.ufs = list(dict())
        self.ufs_municipios = list(dict())
        self.modalidades = list(dict())

        self.popular_dados_padrao()

        # Define se ativa o botão editar
        self.pushButton_editar.setDisabled(True)
        self.lineEdit_id.textChanged[str].connect(self.define_permite_editar)

        self.define_icones()

        self.show()

    def cadastrar(self):
        super(CadastroPessoa, self).cadastrar()
        self.limpar_dados()
        self.widget_tipo_pessoa.setDisabled(False)
        self.widget_tipo_pessoa.setVisible(True)

    def editar(self):
        super(CadastroPessoa, self).editar()
        self.widget_tipo_pessoa.setDisabled(True)
        self.widget_tipo_pessoa.setVisible(False)

    def excluir(self):

        self.dados = {
            "metodo": "prc_delete_pessoa",
            "schema": "soad",
            "params": {
                "pessoa_id": self.lineEdit_id.text()
            }
        }

        retorno = super(CadastroPessoa, self).excluir()

        if retorno[0]:
            dialog = StatusDialog(status='OK'
                                  , mensagem='Pessoa excluída com sucesso.'
                                  , parent=self.parent_window)
            self.limpar_dados()
        else:
            dialog = StatusDialog(status='ALERTA'
                                  , mensagem='Não foi possível excluir a pessoa.'
                                  , exception=retorno
                                  , parent=self.parent_window)
        dialog.exec()

    def cancela(self):
        if super(CadastroPessoa, self).cancela():
            self.limpar_dados()

    def limpar_dados(self):
        # limpa todos os campos
        super(CadastroPessoa, self).limpar_dados()

        self.popular_dados_padrao()

        # identificacao
        self.lineEdit_nome.clear()
        self.lineEdit_email.clear()
        self.lineEdit_telefone.clear()
        self.lineEdit_IE.clear()
        self.lineEdit_documento.clear()
        self.lineEdit_fantasia.clear()

        # endereco
        self.label_endereco_id.setText('')
        self.lineEdit_cep.clear()
        self.lineEdit_logradouro.clear()
        self.lineEdit_numero.clear()
        self.lineEdit_bairro.clear()
        self.lineEdit_complemento.clear()
        self.comboBox_uf.setCurrentIndex(-1)
        self.comboBox_municipio.setCurrentIndex(-1)

    def localizar(self, parent=None):
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

        retorno = super(CadastroPessoa, self).localizar(parent=self)

        if retorno is not None:
            self.atualizar_interface(retorno)

        return

    def confirma(self):

        if self.valida_obrigatorios() != 'OK':
            return

        if self.checkBox_isento.isChecked():
            IE_pessoa = 'ISENTO'
        else:
            IE_pessoa = self.lineEdit_IE.text()

        pessoa = Pessoa(
            nome=self.lineEdit_nome.text()
            , email=self.lineEdit_email.text()
            , telefone=self.lineEdit_telefone.text()
                    .replace(' ', '')
                    .replace('+', '')
                    .replace('(', '')
                    .replace(')', '')
                    .replace('-', '')
            , inscricao_estadual=IE_pessoa
            , documento=self.lineEdit_documento.text()
                    .replace('.', '')
                    .replace('-', '')
                    .replace('/', '')
            , fantasia=self.lineEdit_fantasia.text()
        )

        if self.novo_cadastro:
            pessoa.id_pessoa = ''
        else:
            pessoa.id_pessoa = self.lineEdit_id.text()

        endereco = Endereco(
            id_pessoa=pessoa.id_pessoa
            , id_municipio=self.get_municipio_selecionado()['id_municipio']
            , logradouro=self.lineEdit_logradouro.text()
            , numero=self.lineEdit_numero.text()
            , bairro=self.lineEdit_bairro.text()
            , cep=self.lineEdit_cep.text().replace('-', '')
            , complemento=self.lineEdit_complemento.text()
        )

        if self.label_endereco_id.text() == '':
            endereco.id_endereco = ''
        else:
            endereco.id_endereco = self.label_endereco_id.text()

        # tratar em loop quando for dar suporte a vários endereços
        pessoa.endereco.append(endereco)

        pessoa.modalidade = (self.get_modalidades_selecionadas())

        # pega os dados da tela e popula um dicionario de dados
        self.dados = {
            "metodo": "fnc_cadastro_pessoa",
            "schema": "soad",
            "params": pessoa.to_dict()
        }

        retorno = super(CadastroPessoa, self).confirma()

        if retorno[0]:
            pessoa_id = retorno[1]['p_retorno_json']['pessoa_id']
            self.atualizar_interface(pessoa_id)

        else:
            return

    def atualizar_interface(self, pessoa_id):

        self.limpar_dados()

        dados = self.db.get_registro(
            "fnc_get_pessoa"
            , "pessoa_id"
            , pessoa_id
        )

        if dados[0]:
            dados = dados[1][0]['json_pessoa']
            self.popular_interface(dados)

        else:
            dialog = StatusDialog(
                status='ERRO'
                , exception=dados
                , mensagem='Erro ao buscar dados.'
                , parent=self
            )
            dialog.exec()

    def popular_interface(self, dados):

        self.limpar_dados()

        pessoa = dados[0]

        pessoa = Pessoa(
            nome=pessoa['nome']
            , email=pessoa['email']
            , telefone=pessoa['telefone']
            , inscricao_estadual=pessoa['inscricao_estadual']
            , documento=pessoa['documento']
            , fantasia=pessoa['fantasia']
            , id_pessoa=pessoa['id_pessoa']
        )

        self.lineEdit_id.setText(str(pessoa.id_pessoa))
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
        self.widget_tipo_pessoa.setVisible(False)

        try:
            endereco = dados[1][0] # pode retornar vários endereços, pego apenas o primeiro

            endereco = Endereco(
                id_pessoa=endereco['id_pessoa']
                , id_municipio=endereco['id_municipio']
                , id_estado=endereco['id_estado']
                , id_pais=endereco['id_pais']
                , logradouro=endereco['logradouro']
                , numero=endereco['numero']
                , bairro=endereco['bairro']
                , cep=endereco['cep']
                , complemento=endereco['complemento']
                , tipo=endereco['tipo']
                , id_endereco=endereco['id_endereco']
            )

            for uf in self.ufs:
                if uf['id_estado'] == endereco.id_estado:
                    self.comboBox_uf.setCurrentText(uf['sigla_uf'])
                    self.altera_uf()
                    for mun in self.ufs_municipios:
                        if mun['id_municipio'] == endereco.id_municipio:
                            self.comboBox_municipio.setCurrentText(mun['municipio'])
                            break
                    break

            self.label_endereco_id.setText(str(endereco.id_endereco))
            self.lineEdit_cep.setText(endereco.cep)
            self.lineEdit_logradouro.setText(endereco.logradouro)
            self.lineEdit_numero.setText(endereco.numero)
            self.lineEdit_bairro.setText(endereco.bairro)
            self.lineEdit_complemento.setText(endereco.complemento)

        except TypeError as te:
            logging.debug('[CadastroPessoa] ' + str(te))
            logging.info('[CadastroPessoa] Não foi possível buscar endereço.')

        for mod in self.modalidades:
            self.listWidget_modalidade.setItemSelected(mod['item'], False)

        try:

            modalidade = dados[2]

            for mod_pessoa in modalidade:
                for mod in self.modalidades:
                    if mod_pessoa['id_modalidade'] == mod['id_modalidade']:
                        self.listWidget_modalidade.setItemSelected(mod['item'], True)

        except TypeError as te:
            logging.debug('[CadastroPessoa] ' + str(te))
            logging.info('[CadastroPessoa] Não foi possível buscar modalidades.')

    def popular_dados_padrao(self):
        # preenche modalidades

        self.listWidget_modalidade.clear()

        items = self.db.busca_registro("modalidade", "id_modalidade")

        if items[0]:

            self.modalidades = items[1][0]['fnc_buscar_registro']

            for mod in self.modalidades:
                mod['item'] = QListWidgetItem(mod["descricao"], self.listWidget_modalidade)

        else:
            dialog = StatusDialog(status='ALERTA'
                                  , mensagem="Não foi possível localizar as Modalidades"
                                  , exception=items[1]
                                  , parent=self.parent_window)
            dialog.exec()

        # preenche estados

        items = self.db.busca_registro("vw_estado", "pais", "brasil")

        if items[0]:
            self.ufs = items[1][0]['fnc_buscar_registro']

            for uf in self.ufs:
                self.comboBox_uf.addItem(uf["sigla_uf"])

            self.comboBox_uf.setCurrentIndex(0)

        else:
            dialog = StatusDialog(status='ALERTA'
                                  , exception=items[1]
                                  , mensagem="Não foi possível localizar as UFs"
                                  , parent=self.parent_window)
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

        if items[0]:
            self.ufs_municipios = items[1][0]['fnc_buscar_registro']
            self.comboBox_municipio.clear()
            if self.ufs_municipios is not None:
                for mun in self.ufs_municipios:
                    self.comboBox_municipio.addItem(mun["municipio"])

        else:
            dialog = StatusDialog(status='ALERTA'
                                  , mensagem="Não foi possível localizar os municipios."
                                  , exception=items[1]
                                  , parent=self.parent_window)
            dialog.exec()

    def altera_ie(self):

        self.lineEdit_IE.setDisabled(self.checkBox_isento.isChecked())

        if self.checkBox_isento.isChecked():
            self.lineEdit_IE.setText('ISENTO')
        else:
            self.lineEdit_IE.setText('')

    def get_municipio_selecionado(self):
        for mun in self.ufs_municipios:
            if self.comboBox_municipio.currentText() == mun['municipio']:
                return mun

    def get_modalidades_selecionadas(self):
        modalidades = list()
        for mod in self.modalidades:
            if mod['item'].isSelected():
                modalidades.append(mod['id_modalidade'])
        return modalidades

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()
