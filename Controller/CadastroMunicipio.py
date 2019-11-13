from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QDialogButtonBox

from Controller.Componentes.CadastroPadrao import CadastroPadrao
from Controller.Componentes.StatusDialog import StatusDialog
from View.Ui_CadastroMunicipio import Ui_CadastroMunicipio


class CadastroMunicipio(CadastroPadrao, Ui_CadastroMunicipio):

    def __init__(self, db=None, window_list=None, parent=None, **kwargs):
        super(CadastroMunicipio, self).__init__(parent, **kwargs)
        ### Padrão
        self.parent_window = self
        self.setupUi(self)

        self.db = db
        self.window_list = window_list
        self.modo_edicao = False

        self.frame_menu.setDisabled(False)
        self.frame_contents.setDisabled(True)
        self.frame_buttons.setDisabled(True)

        self.pushButton_cadastrar.clicked.connect(self.cadastrar)
        self.pushButton_editar.clicked.connect(self.editar)
        self.pushButton_editar.setVisible(False)
        self.pushButton_excluir.clicked.connect(self.excluir)
        self.pushButton_localizar.clicked.connect(self.localizar)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)
        ### Fim padrão

        self.campos_obrigatorios = dict([
            ('Cód IBGE', self.lineEdit_ibge)
            , ('UF', self.comboBox_uf)
            , ('Município', self.lineEdit_municipio)
        ])

        self.view_busca = 'vw_municipio'

        self.lineEdit_id.textChanged[str].connect(
            self.define_permite_editar)

        self.comboBox_uf.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        validador_regex_ibge = QRegExpValidator(QRegExp("[0-9]{7}"))
        self.lineEdit_ibge.setValidator(validador_regex_ibge)

        self.ufs = list()
        self.define_permite_editar()
        self.busca_ufs()
        self.define_icones()
        self.show()

    def cadastrar(self):
        super(CadastroMunicipio, self).cadastrar()
        self.limpar_dados()

    def confirma(self):
        # criar procedure que cadastre apenas municipio pela sigla_uf

        municipio = {
            "municipio": self.lineEdit_municipio.text()
            , "uf": self.comboBox_uf.currentText()
            , "ibge": self.lineEdit_ibge.text()
        }

        self.dados = {
            "metodo": "fnc_cadastro_municipio",
            "schema": "soad",
            "params": municipio
        }

        retorno = super(CadastroMunicipio, self).confirma()

        if retorno[0]:
            mercadoria_id = retorno[1]['p_retorno_json']['municipio_id']
            self.atualizar_interface(mercadoria_id)

        else:
            return

    def cancela(self):
        self.limpar_dados()
        super(CadastroMunicipio, self).cancela()

    def excluir(self, validar=True):
        self.dados = {
            "metodo": "prc_delete_municipio"
            , "schema": "soad"
            , "params": {
                "municipio_id": self.lineEdit_id.text()
            }
        }

        retorno = super(CadastroMunicipio, self).excluir()

        if retorno[0]:
            dialog = StatusDialog(status='OK'
                                  , mensagem='Município excluído com sucesso.'
                                  , parent=self.parent_window)
            self.limpar_dados()
        else:
            dialog = StatusDialog(status='ALERTA'
                                  , mensagem='Não foi possível excluir o município.'
                                  , exception=retorno
                                  , parent=self.parent_window)
        dialog.exec()

    def localizar(self, parent=None):

        self.localizar_campos = {
            'id_municipio': 'ID'
            , "ibge": 'Cód. IBGE'
            , "municipio": "Municipio"
            , "sigla_uf": "UF"
        }

        self.colunas_busca = {
            "id_municipio": 'ID'
            , "ibge": 'Cód. IBGE'
            , "municipio": "Municipio"
            , "sigla_uf": "UF"
        }

        self.filtro_adicional = '1=1'


        retorno = super(CadastroMunicipio, self).localizar(parent=self)

        if retorno is not None:
            self.atualizar_interface(retorno)

    def busca_ufs(self):
        # preenche estados

        items = self.db.busca_registro("vw_estado", "pais", "brasil")

        if items[0]:
            self.ufs = items[1][0]['fnc_buscar_registro']
            self.comboBox_uf.clear()
            if self.ufs:
                for uf in self.ufs:
                    self.comboBox_uf.addItem(uf["sigla_uf"])

            self.comboBox_uf.setCurrentIndex(0)

        else:
            dialog = StatusDialog(status='ALERTA'
                                  , exception=items[1]
                                  , mensagem="Não foi possível localizar as UFs"
                                  , parent=self.parent_window)
            dialog.exec()

    def limpar_dados(self):
        super(CadastroMunicipio, self).limpar_dados()
        self.lineEdit_ibge.clear()
        self.lineEdit_municipio.clear()
        self.comboBox_uf.setCurrentIndex(0)

    def atualizar_interface(self, municipio_id=None):
        self.limpar_dados()

        if not municipio_id or municipio_id == '':
            return

        dados = self.db.busca_registro(
            "vw_municipio"
            , "id_municipio"
            , str(municipio_id)
        )

        if dados[0]:
            dados = dados[1][0]['fnc_buscar_registro'][0]
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

        municipio = dados

        municipio = {
            "id_municipio": municipio['id_municipio']
            , "municipio": municipio['municipio']
            , "uf": municipio['sigla_uf']
            , "ibge": municipio['ibge']
        }

        self.lineEdit_id.setText(str(municipio['id_municipio']))
        self.lineEdit_municipio.setText(municipio['municipio'])
        self.lineEdit_ibge.setText(str(municipio['ibge']))
        self.comboBox_uf.setCurrentText(municipio['uf'])