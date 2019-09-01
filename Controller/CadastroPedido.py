import logging

from PySide2.QtCore import QRegExp
from PySide2.QtGui import QDoubleValidator, QIntValidator, QRegExpValidator
from PySide2.QtWidgets import QWidget, QDialogButtonBox

from Controller.CadastroPadrao import CadastroPadrao
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog
from View.Ui_CadastroPedido import Ui_CadastroPedido


class CadastroPedido(QWidget, CadastroPadrao, Ui_CadastroPedido):

    def __init__(self, db=None, window_list=None, **kwargs):
        super(CadastroPadrao, self).__init__()
        super(CadastroPedido, self).__init__()
        self.setupUi(self)

        self.db = db
        self.window_list = window_list
        self.modo_edicao = False

        self.tipo_pedido = kwargs.get('tipo')
        self.setWindowTitle('SOAD - Registrar ' + self.tipo_pedido.capitalize())

        self.frame_menu.setDisabled(False)
        self.frame_contents.setDisabled(True)
        self.frame_buttons.setDisabled(True)

        self.pushButton_cadastrar.clicked.connect(self.cadastrar)
        self.pushButton_editar.clicked.connect(self.editar)
        self.pushButton_excluir.clicked.connect(self.excluir)
        self.pushButton_localizar.clicked.connect(self.localizar)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)

        # Compra ou venda
        if self.tipo_pedido == 'VENDA':
            self.horizontalFrame_tipo_item.setVisible(True)

        elif self.tipo_pedido == 'COMPRA':
            self.radioButton_mercadoria.setChecked(True)
            self.horizontalFrame_tipo_item.setVisible(False)
        else:
            dialog = StatusDialog(status='ERRO', mensagem='TIPO DE PEDIDO INVÁLIDO')
            dialog.exec()

        # buttonBox items
        self.buttonBox_item.button(QDialogButtonBox.Save).clicked.connect(self.salva_item)
        self.buttonBox_item.button(QDialogButtonBox.Discard).clicked.connect(self.apagar_item)
        self.buttonBox_item.button(QDialogButtonBox.Reset).clicked.connect(self.limpar_item)

        # Radio Button item
        self.define_tipo()
        self.radioButton_remanufatura.toggled.connect(self.define_tipo)

        # campos obrigatorios:
        self.campos_obrigatorios = dict([
            ('Documento', self.lineEdit_documento)
        ])

        # Define se ativa o botão editar
        self.pushButton_editar.setDisabled(True)
        self.lineEdit_id.textChanged[str].connect(self.define_permite_editar)

        # Atualiza valores
        self.lineEdit_quantidade.editingFinished.connect(self.calcula_totais)
        self.lineEdit_valor_unitario.editingFinished.connect(self.calcula_totais)

        # Validadores de tipos de dados
        validador_double = QDoubleValidator(bottom=0.00, top=1000000.00, decimals=6)
        validador_integer = QIntValidator(bottom=1, top=1000000)
        validador_regex = QRegExpValidator()
        validador_regex.setRegExp(QRegExp("[1-9]+[ ]*"))

        self.lineEdit_quantidade.setValidator(validador_integer)
        self.lineEdit_valor_unitario.setValidator(validador_double)

        self.lineEdit_mercadoria_id.setValidator(validador_integer)
        self.lineEdit_casco_id.setValidator(validador_integer)
        self.lineEdit_insumo_id.setValidator(validador_integer)

        # Buscar registros
        self.lineEdit_documento.editingFinished.connect(self.busca_pessoa)
        self.lineEdit_casco_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='CASCO'))
        self.lineEdit_insumo_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='INSUMO'))
        self.lineEdit_mercadoria_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='MERCADORIA'))

        #self.lineEdit_documento.inputRejected.connect(self.busca_pessoa)
        #self.lineEdit_casco_id.inputRejected.connect(lambda: self.busca_mercadoria(tipo='CASCO'))
        #self.lineEdit_insumo_id.inputRejected.connect(lambda: self.busca_mercadoria(tipo='INSUMO'))
        #self.lineEdit_mercadoria_id.inputRejected.connect(lambda: self.busca_mercadoria(tipo='MERCADORIA'))

        self.show()

    def define_tipo(self):
        # todo: Atualiza campos obrigatorios
        if self.radioButton_mercadoria.isChecked():
            self.stackedWidget_item.setCurrentWidget(self.page_mercadoria)

        elif self.radioButton_remanufatura.isChecked():
            self.stackedWidget_item.setCurrentWidget(self.page_remanufatura)


    def salva_item(self):
        pass

    def apagar_item(self):
        pass

    def limpar_item(self):
        pass

    def carrega_dados(self):
        # pega os dados dos banco e popula a interface
        pass

    def formata_dados_e_salva(self):
        # pega os dados da tela e popula um dicionario de dados
        #https://stackoverflow.com/questions/10252010/serializing-class-instance-to-json

        #pedido = Pedido()
        #item1 = Mercadoria()
        #item2 = Mercadoria()
        #item3 = Remanufatura()

        dados = {
            "metodo": "prc_cadastro_pedido",
            "params": {
                "tipo_pedido": self.tipo_pedido,
                "pessoa_id": 134,
                "observacao": 'teste observacao',
                "data_entrega": '',
                "itens ": [
                    {
                        "tipo_item": 'MERCADORIA',
                        "mercadoria_id": 24,
                        "quantidade": 5,
                        "valor_unitario": 25.00,
                        "unidade_medida": 276
                    },
                    {
                        "tipo_item": 'MERCADORIA',
                        "mercadoria_id": 25,
                        "quantidade": 3,
                        "valor_unitario": 30.00,
                        "unidade_medida": 276
                    },
                    {
                        "tipo_item": 'REMANUFATURA',
                        "casco_id": 2,
                        "insumo_id": 7,
                        "quantidade": 3,
                        "valor_unitario": 15.00,
                        "nova_remanufatura": False
                    }
                ]
            }
        }

        self.confirma(dados)

    def calcula_totais(self):

        if self.lineEdit_valor_unitario.text() == '':

            valor_unitario = 0

            self.lineEdit_valor_unitario.setText('0,00')

        else:

            valor_unitario = float(self.lineEdit_valor_unitario.text().replace(',', '.').replace(' ', ''))

            self.lineEdit_valor_unitario.setText(
                str(valor_unitario).replace('.', ',')
            )

        if self.lineEdit_quantidade.text() == '':

            quantidade = 0

            self.lineEdit_quantidade.setText('0,00')

        else:

            quantidade = float(self.lineEdit_quantidade.text().replace(',', '.').replace(' ', ''))

            self.lineEdit_quantidade.setText(
                str(quantidade).replace('.', ',')
            )

        total_item = quantidade * valor_unitario

        self.lineEdit_valor_total_item.setText(str(total_item).replace('.', ','))

        # todo: calcular soma dos itens
        self.lineEdit_valor_total_pedido.setText(str(total_item).replace('.', ','))

    def busca_pessoa(self):

        tabela = 'vw_pessoa'
        documento = self.lineEdit_documento.text().replace(' ', '')
        pessoa = None

        if documento != '':

            documento = documento.replace('-', '').replace('/', '')
            pessoa = self.db.busca_registro(tabela, 'documento', documento, '=')[1][0]['fnc_buscar_registro']

            if pessoa is not None:
                pessoa = pessoa[0]

        if pessoa is None:

            localizar_campos = {
                "id_pessoa": 'ID',
                "nome": 'Nome',
                'documento': "Documento"
            }

            colunas_busca = {
                "id_pessoa": 'ID',
                "nome": 'Nome',
                'documento': "Documento"
            }

            localizar = LocalizarDialog(
                self.db
                , campos=localizar_campos
                , tabela=tabela
                , colunas=colunas_busca
                , parent=self
            )

            pessoa_id = localizar.exec()
            pessoa = self.db.busca_registro(tabela, 'id_pessoa', str(pessoa_id), '=')[1][0]['fnc_buscar_registro']

            if pessoa is not None:
                pessoa = pessoa[0]

        if pessoa:
            self.lineEdit_documento.setText(pessoa['documento'])
            self.lineEdit_nome_pessoa.setText(pessoa['nome'])
            return True

        else:
            self.lineEdit_documento.clear()
            self.lineEdit_nome_pessoa.clear()
            return False

    def busca_mercadoria(self, tipo):

        mercadoria = None

        if tipo == 'MERCADORIA':
            tabela = 'vw_mercadoria'
            campo = 'id_mercadoria'
            lineEdit_id = self.lineEdit_mercadoria_id
            lineEdit_descricao = self.lineEdit_mercadoria

        elif tipo == 'CASCO':
            tabela = 'vw_casco'
            campo = 'id_casco'
            lineEdit_id = self.lineEdit_casco_id
            lineEdit_descricao = self.lineEdit_casco

        elif tipo == 'INSUMO':
            tabela = 'vw_insumo'
            campo = 'id_insumo'
            lineEdit_id = self.lineEdit_insumo_id
            lineEdit_descricao = self.lineEdit_insumo

        else:
            logging.debug("Tipo inválido: " + tipo)
            return False

        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':
            mercadoria = self.db.busca_registro(tabela, campo, valor, '=')[1][0]['fnc_buscar_registro']

            if mercadoria is not None:
                mercadoria = mercadoria[0]

        if mercadoria is None:

            localizar_campos = {
                campo: 'ID',
                "descricao": tipo.capitalize(),
                'marca': "Marca"
            }

            colunas_busca = {
                campo: 'ID',
                "descricao": tipo.capitalize(),
                'marca': "Marca"
            }

            localizar = LocalizarDialog(
                self.db
                , campos=localizar_campos
                , tabela=tabela
                , colunas=colunas_busca
                , parent=self
            )

            mercadoria_id = localizar.exec()
            mercadoria = self.db.busca_registro(tabela, campo, str(mercadoria_id), '=')[1][0]['fnc_buscar_registro']

            if mercadoria is not None:
                mercadoria = mercadoria[0]

        if mercadoria:
            lineEdit_id.setText(str(mercadoria[campo]))
            lineEdit_descricao.setText(mercadoria['descricao'])
            return True

        else:
            lineEdit_id.clear()
            lineEdit_descricao.clear()
            return False

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()