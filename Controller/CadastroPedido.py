import logging
from datetime import date

from PySide2.QtCore import QRegExp, QDate
from PySide2.QtGui import QDoubleValidator, QIntValidator, QRegExpValidator
from PySide2.QtWidgets import QWidget, QDialogButtonBox, QTableWidgetItem

from Controller.CadastroPadrao import CadastroPadrao
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog
from Model.ItemPedido import ItemPedido
from Model.Pedido import Pedido
from View.Ui_CadastroPedido import Ui_CadastroPedido


class CadastroPedido(QWidget, CadastroPadrao, Ui_CadastroPedido):

    def __init__(self, db=None, window_list=None, **kwargs):
        super(CadastroPadrao, self).__init__()
        super(CadastroPedido, self).__init__()
        self.setupUi(self)

        self.db = db
        self.window_list = window_list
        self.modo_edicao = False
        self.parent = self

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
            self.tipo_pessoa = 'Cliente'
            self.formGroupBox_pessoa.setTitle(self.tipo_pessoa)
            self.horizontalFrame_tipo_item.setVisible(True)
            self.label_data.setText('Data entrega')

        elif self.tipo_pedido == 'COMPRA':
            self.tipo_pessoa = 'Fornecedor'
            self.formGroupBox_pessoa.setTitle(self.tipo_pessoa)
            self.radioButton_mercadoria.setChecked(True)
            self.horizontalFrame_tipo_item.setVisible(False)
            self.label_data.setText('Data compra')

        else:
            dialog = StatusDialog(status='ERRO', mensagem='TIPO DE PEDIDO INVÁLIDO')
            dialog.exec()

        # buttonBox items
        self.buttonBox_item.button(QDialogButtonBox.Save).clicked.connect(self.salva_item)
        self.buttonBox_item.button(QDialogButtonBox.Discard).clicked.connect(self.apagar_item)
        self.buttonBox_item.button(QDialogButtonBox.Reset).clicked.connect(self.limpar_item)

        # campos obrigatorios:
        self.campos_obrigatorios = dict([
            ('Documento', self.lineEdit_documento)
            , ('Quantidade', self.lineEdit_quantidade)
            , ('Valor Unitário', self.lineEdit_valor_unitario)
            , ('Valor Total Item', self.lineEdit_valor_total_item)
            , ('Casco', self.lineEdit_casco_id)
            , ('Mercadoria', self.lineEdit_mercadoria_id)
            , ('Insumo', self.lineEdit_insumo_id)
        ])

        # Radio Button item
        self.radioButton_remanufatura.toggled.connect(self.define_tipo)

        # Define se ativa o botão editar e excluir
        self.pushButton_editar.setDisabled(True)
        self.pushButton_excluir.setDisabled(True)
        self.lineEdit_id.textChanged[str].connect(self.define_permite_editar)

        self.pushButton_excluir.setText('Cancelar Pedido')

        # Validadores de tipos de dados
        validador_double = QDoubleValidator(bottom=0.000001, top=1000000.00, decimals=6)
        validador_integer = QIntValidator(bottom=1, top=1000000)
        validador_regex_doc = QRegExpValidator(QRegExp("[0-9]{1,14}"))
        validador_regex_id = QRegExpValidator(QRegExp("[0-9]{1,9}"))

        self.lineEdit_quantidade.setValidator(validador_integer)
        self.lineEdit_valor_unitario.setValidator(validador_double)

        self.lineEdit_mercadoria_id.setValidator(validador_regex_id)
        self.lineEdit_casco_id.setValidator(validador_regex_id)
        self.lineEdit_insumo_id.setValidator(validador_regex_id)
        self.lineEdit_documento.setValidator(validador_regex_doc)

        hoje = str(date.today()).split('-')

        self.hoje = QDate(
            int(hoje[0])
            , int(hoje[1])
            , int(hoje[2])
        )

        self.dateEdit_entrega.setDate(self.hoje)

        # Atualiza valores
        self.lineEdit_valor_total_pedido.setText('0,00')
        self.lineEdit_quantidade.editingFinished.connect(self.calcula_totais_item)
        self.lineEdit_valor_unitario.editingFinished.connect(self.calcula_totais_item)

        # Buscar registros
        self.lineEdit_documento.editingFinished.connect(self.busca_pessoa)
        self.lineEdit_casco_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='CASCO'))
        self.lineEdit_insumo_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='INSUMO'))
        self.lineEdit_mercadoria_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='MERCADORIA'))

        #self.lineEdit_documento.inputRejected.connect(self.busca_pessoa)
        #self.lineEdit_casco_id.inputRejected.connect(lambda: self.busca_mercadoria(tipo='CASCO'))
        #self.lineEdit_insumo_id.inputRejected.connect(lambda: self.busca_mercadoria(tipo='INSUMO'))
        #self.lineEdit_mercadoria_id.inputRejected.connect(lambda: self.busca_mercadoria(tipo='MERCADORIA'))

        # Variaveis para gravar o pedido
        self.pedido = Pedido(pessoa_id=None, tipo_pedido=self.tipo_pedido)

        ## Monta QTableWidget
        self.colunas_item = {
            "item_pedido_id": 'ID'
            , "tipo": 'Tipo'
            , "descricao": 'Descrição'
            , "quantidade": "Documento"
            , "valor_unitario": "Valor Unitário"
            , "valor_total": "Valor_total"
        }

        self.colunas_descricao = list(self.colunas_item.values())
        self.colunas_chave = list(self.colunas_item.keys())

        self.tableWidget_items.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_items.setHorizontalHeaderLabels(self.colunas_descricao)
        self.tableWidget_items.horizontalHeader().setVisible(True)
        ### Fim monta tableWidget

        self.radioButton_mercadoria.setChecked(True)
        self.define_tipo()

        self.dialog_localizar = LocalizarDialog(db=self.db)

        self.show()

    def cadastrar(self):
        super(CadastroPedido, self).cadastrar()
        self.lineEdit_documento.setDisabled(False)
        self.limpar_dados()

    def editar(self):
        super(CadastroPedido, self).editar()
        self.lineEdit_documento.setDisabled(True)

    def excluir(self):
        self.dados = {
            "metodo": "prc_cancelar_pedido",
            "schema": "soad",
            "params": {
                "pedido_id": self.lineEdit_id.text()
            }
        }

        if super(CadastroPedido, self).excluir():
            dialog = StatusDialog(status='OK', mensagem='Pedido Cancelado com Sucesso.')
            dialog.exec()
            self.limpar_dados()

    def define_tipo(self):

        self.campos_obrigatorios = dict([
            ('Documento', self.lineEdit_documento)
            , ('Quantidade', self.lineEdit_quantidade)
            , ('Valor Unitário', self.lineEdit_valor_unitario)
            , ('Valor Total Item', self.lineEdit_valor_total_item)
            , ('Casco', self.lineEdit_casco_id)
            , ('Mercadoria', self.lineEdit_mercadoria_id)
            , ('Insumo', self.lineEdit_insumo_id)
        ])

        if self.radioButton_mercadoria.isChecked():
            self.stackedWidget_item.setCurrentWidget(self.page_mercadoria)
            self.campos_obrigatorios.pop('Casco')
            self.campos_obrigatorios.pop('Insumo')
            self.campos_obrigatorios['Mercadoria'] = self.lineEdit_mercadoria_id

        elif self.radioButton_remanufatura.isChecked():
            self.stackedWidget_item.setCurrentWidget(self.page_remanufatura)
            self.campos_obrigatorios.pop('Mercadoria')
            self.campos_obrigatorios['Casco'] = self.lineEdit_casco_id
            self.campos_obrigatorios['Insumo'] = self.lineEdit_insumo_id

        self.limpar_item()

    def limpar_dados(self):
        super(CadastroPedido, self).limpar_dados()
        self.limpar_item()
        self.lineEdit_documento.clear()
        self.lineEdit_nome_pessoa.clear()
        self.dateEdit_entrega.setDate(self.hoje)

    def localizar(self, parent=None):

        self.localizar_campos = {
            "id_pedido": 'ID',
            "pessoa": self.tipo_pessoa,
            "documento": 'Documento',
            "data_entrega": self.label_data.text()
        }

        self.colunas_busca = {
            "id_pedido": 'ID',
            "pessoa": self.tipo_pessoa,
            "documento": 'Documento',
            "data_entrega": self.label_data.text()
        }

        self.view_busca = 'vw_pedido'

        dados = super(CadastroPedido, self).localizar(parent=self)
        dados = self.db.get_registro("fnc_get_pedido", "pedido_id", dados)

        if dados[0]:
            dados = dados[1][0]['json_pedido']
            self.popular_interface(dados)

    def valida_obrigatorios(self):
        if self.tableWidget_items.rowCount() == 0:
            dialog = StatusDialog(
                status='ALERTA'
                , mensagem='Não é possível realizar uma '
                           + self.tipo_pedido +  ' sem itens.')
            return dialog.exec()
        return super(CadastroPedido, self).valida_obrigatorios()

    def confirma(self):
        # Remove obrigatoriedade dos itens
        self.campos_obrigatorios = dict([
            ('Documento', self.lineEdit_documento)
        ])

        if self.valida_obrigatorios() != 'OK':
            return False

        self.pedido.data_entrega = self.dateEdit_entrega.text()

        if self.novo_cadastro:
            self.pedido.pedido_id = ''
        else:
            self.pedido.pedido_id = self.lineEdit_id.text()

        self.dados = {
            "metodo": "prc_cadastro_pedido",
            "shcema": "soad",
            "params": self.pedido.to_dict()
        }

        # super...
        # Volta os obrigatorios para a forma inicial
        self.define_tipo()

    def popular_iterface(self, dados):
        # Preenche identificação
        # Preenche tabela
        # Posiciona o primeiro item da tabela no stack
        pass

    def salva_item(self):

        if super(CadastroPedido, self).valida_obrigatorios() != 'OK':
            return

        tipo_item = 'MERCADORIA' if self.radioButton_mercadoria.isChecked() else 'REMANUFATURA'

        if tipo_item == 'REMANUFATURA':
            descricao = 'Casco: ' + self.lineEdit_casco.text() \
                        + ' Insumo: ' + self.lineEdit_insumo.text()
        else:
            descricao = self.lineEdit_mercadoria.text()

        item = ItemPedido(
            item_pedido_id=(len(self.pedido.itens)+1)*-1
            , tipo=tipo_item
            , descricao=descricao
            , quantidade=self.lineEdit_quantidade.text().replace(',', '.')
            , valor_unitario=self.lineEdit_valor_unitario.text()
            , valor_total=self.lineEdit_valor_total_item.text()
            , unidade_medida_id=self.db.busca_registro( # todo: Fazer dinâmico
                'unidade_medida'
                , 'abreviacao'
                , 'UN'
                , 'like'
            )[1][0]['fnc_buscar_registro'][0]['id_unidade_medida']
            , mercadoria_id = self.lineEdit_mercadoria_id.text()
            , casco_id=self.lineEdit_casco_id.text()
            , insumo_id=self.lineEdit_insumo_id.text()
            , nova_remanufatura=(not self.checkBox_reutilizar_casco.isChecked())
        )

        self.pedido.itens.append(item)

        self.preencher_tabela()
        self.calcula_totais_pedido()

    def preencher_tabela(self):

        self.tableWidget_items.setRowCount(len(self.pedido.itens))

        row = 0
        for item_pedido in self.pedido.itens:
            col = 0
            for coluna in self.colunas_item:
                valor = item_pedido.to_item_dict()[coluna]
                item = QTableWidgetItem(str(valor))
                self.tableWidget_items.setItem(row, col, item)
                col = col + 1
            row = row + 1

        self.limpar_item()

    def apagar_item(self):
        # Remove da tabela
        # Remove do objeto pedido
        # Limpa campos
        pass

    def limpar_item(self):

        if self.radioButton_mercadoria.isChecked():
            self.lineEdit_mercadoria_id.clear()
            self.lineEdit_mercadoria.clear()
        elif self.radioButton_remanufatura.isChecked():
            self.lineEdit_casco_id.clear()
            self.lineEdit_casco.clear()
            self.lineEdit_insumo_id.clear()
            self.lineEdit_insumo.clear()
            self.checkBox_reutilizar_casco.setChecked(False)

        self.lineEdit_quantidade.clear()
        self.lineEdit_valor_unitario.clear()
        self.lineEdit_valor_total_item.clear()

    def carrega_dados(self):
        # pega os dados dos banco e popula a interface
        pass

    def calcula_totais_item(self):

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

    def calcula_totais_pedido(self):
        valor = 0
        for row in range(0, self.tableWidget_items.rowCount()):
            self.tableWidget_items.item(row, 5)
            v = 0 if self.tableWidget_items.item(row, 5).text() is None \
                else self.tableWidget_items.item(row, 5).text().replace(',', '.')
            valor = valor + float(v)
            print(valor)

        print(self.lineEdit_valor_total_item.text()) #.replace(',', '.'))

        valor = valor + float(1)
        self.lineEdit_valor_total_pedido.setText(str(valor).replace('.', ','))

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

            self.dialog_localizar.define_tabela(tabela)
            self.dialog_localizar.define_campos(localizar_campos)
            self.dialog_localizar.define_colunas(colunas_busca)

            self.dialog_localizar.define_valor_padrao(localizar_campos['documento'], self.lineEdit_documento.text())

            pessoa_id = self.dialog_localizar.exec()
            pessoa = self.db.busca_registro(tabela, 'id_pessoa', str(pessoa_id), '=')[1][0]['fnc_buscar_registro']

            if pessoa is not None:
                pessoa = pessoa[0]

        if pessoa:
            self.lineEdit_documento.setText(pessoa['documento'])
            self.lineEdit_nome_pessoa.setText(pessoa['nome'])
            self.pedido.pessoa_id = pessoa['id_pessoa']
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

            logging.debug(str(mercadoria))
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

            self.dialog_localizar.define_tabela(tabela)
            self.dialog_localizar.define_campos(localizar_campos)
            self.dialog_localizar.define_colunas(colunas_busca)

            self.dialog_localizar.define_valor_padrao(localizar_campos[campo], lineEdit_id.text())

            mercadoria_id = self.dialog_localizar.exec()
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