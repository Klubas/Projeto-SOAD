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

        self.comboBox_uf.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.ufs = list()

        self.busca_ufs()
        self.define_icones()
        self.show()

    def confirma(self):
        # criar procedure que cadastre apenas municipio pela sigla_uf
        super(CadastroMunicipio, self).confirma()

    def cancela(self):
        self.limpar_dados()
        super(CadastroMunicipio, self).cancela()

    def excluir(self, validar=True):
        # criar procedure
        super(CadastroMunicipio, self).excluir()

    def localizar(self, parent=None):
        super(CadastroMunicipio, self).localizar(parent=self)

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



