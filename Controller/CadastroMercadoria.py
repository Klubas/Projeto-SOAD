import logging

from PySide2.QtCore import QRegExp
from PySide2.QtGui import QDoubleValidator, QRegExpValidator
from PySide2.QtWidgets import QWidget, QDialogButtonBox

from Controller.CadastroPadrao import CadastroPadrao
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog
from View.Ui_CadastroMercadoria import Ui_CadastroMercadoria


class CadastroMercadoria(QWidget, CadastroPadrao, Ui_CadastroMercadoria):

    def __init__(self, db=None, window_list=None, **kwargs):
        super(CadastroPadrao, self).__init__()
        super(CadastroMercadoria, self).__init__()
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
            ('Descrição', self.lineEdit_descricao)
            , ('Fabricante', self.comboBox_fabricante)
            , ('Valor de Venda', self.lineEdit_valor_venda)
        ])

        self.tipo = 'MERCADORIA' if kwargs.get('tipo') \
                                    is None else kwargs.get('tipo')

        if self.tipo == 'MERCADORIA':

            self.tipo = 'MERCADORIA'
            self.stackedWidget.setVisible(False)

        elif self.tipo == 'CASCO':

            self.campos_obrigatorios['Insumo'] = self.lineEdit_insumo_id
            self.campos_obrigatorios['Quantidade'] = self.lineEdit_quantidade_insumo
            self.campos_obrigatorios['Un. Medida (Insumo)'] = self.comboBox_unidade_medida_insumo

            self.stackedWidget.setVisible(True)
            self.page_insumo.setVisible(False)
            self.stackedWidget.setCurrentWidget(self.page_casco)

        elif self.tipo == 'INSUMO':

            self.campos_obrigatorios['Quantidade Embalagem'] = self.lineEdit_quantidade_embalagem
            self.campos_obrigatorios['Un. Medida (Embalagem)'] = self.comboBox_unidade_medida_embalagem

            self.stackedWidget.setVisible(True)
            self.page_casco.setVisible(False)
            self.stackedWidget.setCurrentWidget(self.page_insumo)

        else:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='TIPO DE MERCADORIA INVÁLIDO'
                , parent=self.parent_window)
            dialog.exec()

        self.setWindowTitle('SOAD - Cadastrar ' + self.tipo.capitalize())

        # Define se ativa o botão editar e excluir
        self.pushButton_editar.setDisabled(True)
        self.pushButton_excluir.setDisabled(True)
        self.lineEdit_id.textChanged[str].connect(self.define_permite_editar)

        # Validadores de tipos de dados
        validador_double = QDoubleValidator(bottom=0.000001, top=1000000.00, decimals=6)
        validador_regex_id = QRegExpValidator(QRegExp("[0-9]{1,9}"))

        self.lineEdit_insumo_id.setValidator(validador_regex_id)
        self.lineEdit_quantidade_insumo.setValidator(validador_double)
        self.lineEdit_quantidade_embalagem.setValidator(validador_double)

        # Busca registros
        self.lineEdit_insumo_id.editingFinished.connect(
            lambda: self.busca_insumo(
                insumo_id=self.lineEdit_insumo_id.text()
            )
        )

        # Cadastro de fabricante
        self.fabricantes = set()
        self.lineEdit_fabricante.setVisible(False)
        self.toolButton_addFabricante.clicked.connect(self.cadastrar_fabricante)

        self.lineEdit_fabricante.textChanged[str].connect(
            lambda: self.toolButton_addFabricante.setText('Cancelar')
            if self.lineEdit_fabricante.text() == '' #and self.lineEdit_fabricante.isVisible()
            else self.toolButton_addFabricante.setText('Salvar')
        )
        self.toolButton_addFabricante.setText('+')

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

    def busca_insumo(self, id_insumo):
        pass

    def cadastrar_fabricante(self):

        pressed = self.toolButton_addFabricante.isChecked()

        self.comboBox_fabricante.setVisible(not pressed)
        self.lineEdit_fabricante.setVisible(pressed)

        if pressed:
            self.toolButton_addFabricante.setText('Cancelar')
            self.lineEdit_fabricante.setFocus()

        else:
            texto = self.lineEdit_fabricante.text().upper()
            if texto != '':
                self.fabricantes.add(texto)
                self.comboBox_fabricante.clear()
                self.comboBox_fabricante.addItems(list(self.fabricantes))
                self.comboBox_fabricante.setCurrentText(texto)
                logging.info('[CadastroMercadoria] Adicionado fornecedor: ' + texto)

            self.lineEdit_fabricante.clear()
            self.comboBox_fabricante.setFocus()
            self.toolButton_addFabricante.setText('+')

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()

