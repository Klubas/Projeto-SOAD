import logging
import os

from PySide2.QtCore import QRegExp, QDate
from PySide2.QtGui import QDoubleValidator, QIntValidator, QRegExpValidator, QIcon, QPixmap, QImage
from PySide2.QtWidgets import QDialogButtonBox, QTableWidgetItem

from Controller.Componentes.CadastroPadrao import CadastroPadrao
from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.RelatorioPadrao.RelatorioPadrao import RelatorioPadrao
from Controller.Componentes.StatusDialog import StatusDialog
from Model.Endereco import Endereco
from Model.ItemPedido import ItemPedido
from Model.Pedido import Pedido
from Model.Pessoa import Pessoa
from View.Ui_CadastroPedido import Ui_CadastroPedido


class CadastroPedido(CadastroPadrao, Ui_CadastroPedido):

    def __init__(self, db=None, window_list=None, parent=None, **kwargs):
        super(CadastroPedido, self).__init__(parent, **kwargs)
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
        self.pushButton_imprimir.clicked.connect(self.imprimir_pedido)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)
        ### Fim padrão

        self.label_tinta.setText('')
        self.color_ink = QImage(os.path.join("Resources", "icons", "color_ink.png")).smoothScaled(45, 45)
        self.bw_ink = QImage(os.path.join("Resources", "icons", "bw_ink.png")).smoothScaled(45, 45)
        self.label_tinta.setPixmap(QPixmap.fromImage(self.bw_ink))

        self.icone_cancelar = QIcon(os.path.join('Resources', 'icons', 'cancel.png'))
        self.icone_estornar = QIcon(os.path.join('Resources', 'icons', 'undo.png'))

        # Compra ou venda
        self.tipo_pedido = kwargs.get('tipo')

        self.configura_tipo()

        self.filtro_adicional = None
        self.setWindowTitle('SOAD - Registrar ' + self.tipo_pedido.capitalize())

        # buttonBox items
        self.buttonBox_item.button(QDialogButtonBox.Save).clicked.connect(self.salva_item)
        self.buttonBox_item.button(QDialogButtonBox.Reset).clicked.connect(self.limpar_item)

        self.lineEdit_valor_total_item.textChanged[str].connect(self.valida_valores)
        self.lineEdit_casco_id.textChanged[str].connect(self.valida_valores)
        self.lineEdit_insumo_id.textChanged[str].connect(self.valida_valores)
        self.lineEdit_mercadoria_id.textChanged[str].connect(self.valida_valores)
        self.lineEdit_quantidade.textChanged[str].connect(self.valida_valores)
        self.lineEdit_valor_unitario.textChanged[str].connect(self.valida_valores)

        self.tableWidget_items.itemDoubleClicked.connect(self.posicionar_item)

        self.pushButton_movimentar.clicked.connect(
            lambda: self.movimentar(self.lineEdit_id.text())
        )

        self.pushButton_remover_item.setDisabled(True)

        self.tableWidget_items.itemClicked.connect(
            lambda: self.pushButton_remover_item.setDisabled(
                len(self.tableWidget_items.selectedIndexes()) <= 0
            )
        )

        self.pushButton_remover_item.clicked.connect(self.apagar_item)

        # campos obrigatorios:
        self.campos_obrigatorios = dict([
            ('Documento', self.lineEdit_documento)
            , ('Casco', self.lineEdit_casco_id)
            , ('Mercadoria', self.lineEdit_mercadoria_id)
            , ('Insumo', self.lineEdit_insumo_id)
            , ('Quantidade', self.lineEdit_quantidade)
            , ('Valor Unitário', self.lineEdit_valor_unitario)
            , ('Valor Total Item', self.lineEdit_valor_total_item)
        ])

        # Radio Button item
        self.radioButton_remanufatura.toggled.connect(self.define_tipo)

        # Define se ativa o botão editar e excluir
        self.pushButton_editar.setDisabled(True)
        self.pushButton_excluir.setDisabled(True)
        self.lineEdit_id.textChanged[str].connect(self.define_permite_editar)

        self.pushButton_excluir.setText('Cancelar Pedido')
        self.pushButton_excluir.setIcon(self.icone_cancelar)

        self.pushButton_movimentar.setDisabled(True)

        # Validadores de tipos de dados
        validador_double = QDoubleValidator(bottom=0.000001, top=1000000.00, decimals=6)
        validador_integer = QIntValidator(bottom=1, top=1000000)
        validador_regex_doc = QRegExpValidator(QRegExp("[0-9]{1,14}"))
        validador_regex_id = QRegExpValidator(QRegExp("[0-9]{1,9}"))

        self.lineEdit_quantidade.setValidator(validador_regex_doc)
        self.lineEdit_valor_unitario.setValidator(validador_double)

        self.lineEdit_mercadoria_id.setValidator(validador_regex_id)
        self.lineEdit_casco_id.setValidator(validador_regex_id)
        self.lineEdit_insumo_id.setValidator(validador_regex_id)
        self.lineEdit_documento.setValidator(validador_regex_doc)

        self.dateEdit_entrega.setDate(QDate().currentDate())
        self.dateEdit_cadastro.setDate(QDate().currentDate())

        self.label_situacao.setText('')

        # Atualiza valores
        self.lineEdit_valor_total_pedido.setText('0,00')
        self.lineEdit_quantidade.editingFinished.connect(self.calcula_totais_item)
        self.lineEdit_valor_unitario.editingFinished.connect(self.calcula_totais_item)

        # Buscar registros
        self.lineEdit_documento.editingFinished.connect(self.busca_pessoa)
        self.lineEdit_casco_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='CASCO'))
        self.lineEdit_insumo_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='INSUMO'))
        self.lineEdit_mercadoria_id.editingFinished.connect(lambda: self.busca_mercadoria(tipo='MERCADORIA'))

        self.toolButton_pessoa.clicked.connect(lambda: self.busca_pessoa(force=True))
        self.toolButton_insumo.clicked.connect(lambda: self.busca_mercadoria(tipo='INSUMO', force=True))
        self.toolButton_casco.clicked.connect(lambda: self.busca_mercadoria(tipo='CASCO', force=True))
        self.toolButton_mercadoria.clicked.connect(lambda: self.busca_mercadoria(tipo='MERCADORIA', force=True))

        # Variaveis para gravar o pedido
        self.pedido = Pedido(tipo_pedido=self.tipo_pedido)
        self.pessoa = None

        ## Monta QTableWidget
        self.colunas_item = {
            "item_pedido_id": 'ID'
            , "codigo": 'Código'
            , "tipo_item": 'Tipo'
            , "descricao": 'Descrição'
            , "quantidade": "Quant."
            , "valor_unitario": "V. Unitário"
            , "valor_total": "V. Total"
        }

        self.colunas_descricao = list(self.colunas_item.values())
        self.colunas_chave = list(self.colunas_item.keys())

        self.tableWidget_items.setRowCount(len(self.pedido.itens))
        self.tableWidget_items.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_items.setHorizontalHeaderLabels(self.colunas_descricao)
        self.tableWidget_items.horizontalHeader().setVisible(True)
        ### Fim monta tableWidget

        self.radioButton_mercadoria.setChecked(True)
        self.define_tipo()

        self.dialog_localizar = LocalizarDialog(db=self.db, parent=self)

        self.define_icones()

        self.adiciona_help(texto=self.help)

        self.tabWidget.setCurrentIndex(0)

        self.id_registro = kwargs.get('id_registro')
        if self.id_registro:
            self.atualizar_interface(self.id_registro)

        self.lineEdit_item_pedido_id.setVisible(False)
        self.visualizar()

        self.limpa_obrigatorios()
        self.define_permite_editar()

        self.translate_ui()

        self.show()

    def cadastrar(self):
        super(CadastroPedido, self).cadastrar()
        self.limpar_dados()
        self.visualizar(False)
        self.pushButton_excluir.setText('Cancelar Pedido')
        self.pushButton_excluir.setIcon(self.icone_cancelar)
        self.label_situacao.setText('')
        self.lineEdit_documento.setDisabled(False)
        self.buttonBox_item.button(QDialogButtonBox.Save).setDisabled(True)

    def editar(self):
        super(CadastroPedido, self).editar()
        self.visualizar(False)
        self.lineEdit_documento.setDisabled(True)

    def excluir(self, validar=True):

        if self.label_situacao.text() == 'CADASTRADO'\
                or self.label_situacao.text() == 'ESTORNADO':
            acao = 'cancelamento'
            prc = 'prc_cancelar_pedido'

        elif self.label_situacao.text() == 'ENCERRADO':
            acao = 'estorno'
            prc = 'prc_estornar_pedido'

        else:
            logging.debug('[CadastroPedido] Situacao invalida=' + self.label_situacao.text())
            return

        pedido_id = self.lineEdit_id.text()

        dialog = ConfirmDialog(self)
        dialog.definir_mensagem('Tem certeza que deseja realizar o ' + acao + ' desse pedido?')

        if dialog.exec():

            self.dados = {
                "metodo": prc,
                "schema": "soad",
                "params": {
                    "pedido_id": pedido_id
                }
            }

            retorno = super(CadastroPedido, self).excluir(validar=False)

            if retorno[0]:
                dialog = StatusDialog(status='OK'
                                      , mensagem=acao.capitalize() + ' realizado com sucesso.'
                                      , parent=self.parent_window)
                self.atualizar_interface(pedido_id)

            else:
                dialog = StatusDialog(status='ALERTA'
                                      , mensagem='Não foi possível realizar o ' + acao + ' do pedido.'
                                      , exception=retorno
                                      , parent=self.parent_window)

            dialog.exec()

    def valida_obrigatorios(self):
        if self.tableWidget_items.rowCount() == 0:
            dialog = StatusDialog(
                status='ALERTA'
                , mensagem='Não é possível realizar uma '
                           + self.tipo_pedido + ' sem itens.'
                , parent=self.parent_window
                , esconder_detalhes=True
            )
            return dialog.exec()
        return super(CadastroPedido, self).valida_obrigatorios()

    def confirma(self):

        if self.buttonBox_item.button(QDialogButtonBox.Save).isEnabled():
            self.salva_item()

        # Remove obrigatoriedade dos itens
        self.campos_obrigatorios = dict([
            ('Documento', self.lineEdit_documento)
        ])

        if self.valida_obrigatorios() != 'OK':
            return False

        if self.novo_cadastro:
            self.pedido.pedido_id = ''

        else:
            self.pedido.pedido_id = self.lineEdit_id.text()

        self.pedido.data_entrega = self.dateEdit_entrega.date().toString("dd.MM.yyyy").replace('.', '/')
        self.pedido.observacao = self.textEdit_observacao.toPlainText()

        pedido_dict = self.pedido.to_dict()
        pedido_dict.pop('data_cadastro')
        pedido_dict.pop('situacao')

        self.dados = {
            "metodo": "fnc_cadastro_pedido",
            "schema": "soad",
            "params": pedido_dict
        }

        retorno = super(CadastroPedido, self).confirma()

        if retorno[0]:
            pedido_id = retorno[1]['p_retorno_json']['pedido_id']
            self.movimentar(pedido_id)

        else:
            logging.debug('[CadastroPedido] Não foi possível confirmar o cadastro.')

    def cancela(self):
        if super(CadastroPedido, self).cancela():
            if self.lineEdit_id.text() == '':
                self.limpar_dados()
            else:
                id = self.lineEdit_id.text()
                self.atualizar_interface(int(id))
            self.define_permite_editar()

    def limpar_dados(self):
        super(CadastroPedido, self).limpar_dados()
        self.pedido = Pedido(tipo_pedido=self.tipo_pedido)
        self.pedido.itens = []
        self.label_tipo_pedido.setText('')
        self.limpar_item()
        self.lineEdit_documento.clear()
        self.lineEdit_nome_pessoa.clear()
        self.label_situacao.setText('')
        self.dateEdit_entrega.setDate(QDate().currentDate())
        self.preencher_tabela()
        self.pushButton_movimentar.setDisabled(True)
        self.textEdit_observacao.clear()

    def localizar(self, parent=None):

        self.localizar_campos = {
            "id_pedido": 'ID',
            "pessoa": self.tipo_pessoa,
            "documento": 'Documento',
            "data_cadastro": 'Data cadastro',
            "situacao": 'Situação',
            "data_entrega": self.label_data.text()
        }

        self.colunas_busca = {
            "id_pedido": 'ID',
            "pessoa": self.tipo_pessoa,
            "documento": 'Documento',
            "data_cadastro": 'Data cadastro',
            "situacao": 'Situação',
            "data_entrega": self.label_data.text()
        }

        retorno = super(CadastroPedido, self).localizar(parent=self)

        if retorno is not None:
            self.atualizar_interface(retorno)

    def visualizar(self, entrar_modo_visualziacao=True):

        if entrar_modo_visualziacao:
            self.entrar_modo_visualizacao()
            self.groupBox_identificacao.setDisabled(True)
            self.groupBox_items.setDisabled(False)
            self.tabWidget.setDisabled(False)
            self.tab_campos.setDisabled(True)
            self.horizontalWidget_botoes_tabela.setVisible(False)
            self.buttonBox_item.setVisible(False)

        else:
            self.groupBox_identificacao.setDisabled(False)
            self.groupBox_items.setDisabled(False)
            self.tabWidget.setDisabled(False)
            self.tab_campos.setDisabled(False)
            self.horizontalWidget_botoes_tabela.setVisible(True)
            self.buttonBox_item.setVisible(True)

    def movimentar(self, pedido_id):
        dialog = ConfirmDialog(self)
        dialog.definir_mensagem(
            'Deseja realizar a movimentação dessa ' + self.tipo_pedido.capitalize()
            + '\n(Pedido: ' + str(pedido_id) + ')?\nO pedido não poderá mais ser editado.')

        if dialog.exec():
            dados = {
                "metodo": "prc_encerrar_pedido",
                "schema": "soad",
                "params": {"pedido_id": str(pedido_id)}
            }

            retorno = self.db.call_procedure(self.db.schema, dados)
            self.atualizar_interface(pedido_id)

            if retorno[0]:
                retorno = retorno[1][0]['p_retorno']

                if int(retorno) == int(100):
                    return True
                else:
                    return False
            else:
                dialog = StatusDialog(
                    mensagem='Não foi possível realizar a movimentação do pedido.',
                    exception=retorno,
                    status='ALERTA'
                )
                dialog.exec()
                return False
        else:
            self.atualizar_interface(pedido_id)

    def define_tipo(self):

        self.campos_obrigatorios = dict([
            ('Documento', self.lineEdit_documento)
            , ('Casco', self.lineEdit_casco_id)
            , ('Mercadoria', self.lineEdit_mercadoria_id)
            , ('Insumo', self.lineEdit_insumo_id)
            , ('Quantidade', self.lineEdit_quantidade)
            , ('Valor Unitário', self.lineEdit_valor_unitario)
            , ('Valor Total Item', self.lineEdit_valor_total_item)
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

        self.limpa_obrigatorios()
        self.marca_obrigatorios()
        self.limpar_item()

    def atualizar_interface(self, id_pedido):

        self.limpar_dados()
        self.pedido.pedido_id = id_pedido

        dados = self.db.get_registro(
            "fnc_get_pedido"
            , "pedido_id"
            , self.pedido.pedido_id
        )

        if dados[0]:
            dados = dados[1][0]['json_pedido']
            self.popular_interface(dados)
            self.tabWidget.setCurrentIndex(1)

        else:
            dialog = StatusDialog(
                status='ERRO'
                , exception=dados
                , mensagem='Erro ao buscar dados.'
                , parent=self
            )
            dialog.exec()

    def popular_interface(self, dados):
        # Preenche identificação

        pedido = dados[0]

        self.lineEdit_documento.setText(pedido['documento'])
        self.lineEdit_nome_pessoa.setText(pedido['pessoa'])

        pedido = Pedido(
            pedido_id=pedido['id_pedido']
            , pessoa_id=pedido['id_pessoa']
            , tipo_pedido=pedido['tipo_pedido']
            , data_entrega=pedido['data_entrega']
            , situacao=pedido['situacao']
            , data_cadastro=pedido['data_cadastro']
            , observacao=pedido['observacao']
        )

        self.label_situacao.setText(
            pedido.situacao if pedido.situacao is not None else ''
        )

        self.label_tipo_pedido.setText(pedido.tipo_pedido)
        self.tipo_pedido = pedido.tipo_pedido
        self.configura_tipo()

        self.textEdit_observacao.setText(pedido.observacao)

        self.dateEdit_cadastro.setDate(
            QDate.fromString(
                pedido.data_cadastro
                , 'yyyy-MM-ddTHH:mm:ss')
        )

        if pedido.situacao == 'CADASTRADO'\
                or pedido.situacao == 'ESTORNADO':
            self.pushButton_excluir.setText('Cancelar Pedido')
            self.pushButton_excluir.setIcon(self.icone_cancelar)

        elif pedido.situacao == 'ENCERRADO':
            self.pushButton_excluir.setText('Estornar Pedido')
            self.pushButton_excluir.setIcon(self.icone_estornar)

        if pedido.data_entrega is not None:

            self.dateEdit_entrega.setDate(
                QDate.fromString(
                    pedido.data_entrega
                    , 'yyyy-MM-ddTHH:mm:ss')
            )

        else:
            self.dateEdit_entrega.clear()

        # ID é o ultimo a alterar para evitar race condition com self.define_permite_editar
        self.lineEdit_id.setText(str(pedido.pedido_id))

        # Montar ItemPedido
        for item in dados[1]:
            if item['tipo'] == 'MERCADORIA':

                item_pedido = ItemPedido(
                    item_pedido_id=item['id_item_pedido']
                    , tipo=item['tipo']
                    , quantidade=item['quantidade']
                    , valor_unitario=item['valor_unitario']
                    , mercadoria_id=item['id_mercadoria']
                    , unidade_medida_id=item['id_unidade_medida']
                    , unidade_medida=item['unidade_medida']
                    , mercadoria=item['descricao']
                    , descricao=item['descricao']
                )

            elif item['tipo'] == 'REMANUFATURA':

                item_pedido = ItemPedido(
                    item_pedido_id=item['id_remanufatura']
                    , tipo=item['tipo']
                    , quantidade=item['quantidade']
                    , valor_unitario=item['valor_unitario']
                    , casco_id=item['casco_id']
                    , insumo_id=item['insumo_id']
                    , nova_remanufatura=None #item['nova_remanufatura']
                    , descricao='Casco: ' + item['casco']
                                + ' Insumo: ' + item['insumo']
                )

            else:
                logging.debug('[CadastroPedido] Não foi possível identificar o tipo do item do pedido')
                logging.debug('[CadastroPedido] Abortando...')
                return

            pedido.itens.append(item_pedido)

        # Preenche tabela
        self.pedido = pedido
        self.preencher_tabela()
        self.calcula_totais_pedido()

        self.pushButton_movimentar.setDisabled(
            self.label_situacao.text() != 'CADASTRADO'
            and self.label_situacao.text() != 'ESTORNADO'
        )

        # Posiciona o primeiro item da tabela no stack
        self.tableWidget_items.selectRow(0)
        self.posicionar_item(None)

        self.visualizar(True)

    def busca_pessoa(self, force=False):

        tabela = 'vw_pessoa_' + self.tipo_pessoa.lower()
        documento = self.lineEdit_documento.text().replace(' ', '')
        pessoa = None
        filtro_adicional = ''

        if documento != '':

            documento = documento.replace('-', '').replace('/', '')
            pessoa = self.db.busca_registro(tabela, 'documento', documento, '=')[1][0]['fnc_buscar_registro']

            if pessoa is not None:
                pessoa = pessoa[0]

        if pessoa is None or force:

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
            self.dialog_localizar.filtro = filtro_adicional

            self.dialog_localizar.define_valor_padrao(localizar_campos['documento'], self.lineEdit_documento.text())

            pessoa_id = self.dialog_localizar.exec()

            if pessoa_id == 0:
                return False

            pessoa = self.db.busca_registro(tabela, 'id_pessoa', str(pessoa_id), '=')[1][0]['fnc_buscar_registro']

            if pessoa is not None:
                pessoa = pessoa[0]

        if pessoa:

            pessoa_pedido = Pessoa(
                nome=pessoa['nome']
                , email=pessoa['email']
                , telefone=pessoa['telefone']
                , documento=pessoa['documento']
                , inscricao_estadual=pessoa['inscricao_estadual']
                , fantasia=pessoa['fantasia']
                , id_pessoa=pessoa['id_pessoa']
            )
            self.lineEdit_documento.setText(pessoa_pedido.documento)
            self.lineEdit_nome_pessoa.setText(pessoa_pedido.nome)
            self.pedido.pessoa_id = pessoa_pedido.id_pessoa

            endereco = Endereco(
                id_pessoa=pessoa['id_pessoa']
                , municipio=pessoa['municipio']
                , estado=pessoa['sigla_uf']
                , pais=pessoa['pais']
                , logradouro=pessoa['logradouro']
                , numero=pessoa['numero']
                , bairro=pessoa['bairro']
                , cep=pessoa['cep']
                , complemento=pessoa['complemento']
                , tipo=pessoa['tipo_endereco']
            )

            pessoa_pedido.endereco.append(endereco)

            self.pessoa = pessoa_pedido

            return True

        else:
            self.lineEdit_documento.clear()
            self.lineEdit_nome_pessoa.clear()
            return False

    def busca_mercadoria(self, tipo, force=False):
        mercadoria = None
        filtro_adicional = ''

        if tipo == 'MERCADORIA':
            tabela = 'vw_mercadoria'
            campo = 'id_mercadoria'
            lineEdit_id = self.lineEdit_mercadoria_id
            lineEdit_descricao = self.lineEdit_mercadoria
            lineEdit_marca = self.lineEdit_marca_mercadoria

            if self.tipo_pedido == 'VENDA':
                filtro_adicional = 'permite_venda=true::boolean'

        elif tipo == 'CASCO':
            tabela = 'vw_casco'
            campo = 'id_casco'
            lineEdit_id = self.lineEdit_casco_id
            lineEdit_descricao = self.lineEdit_casco
            lineEdit_marca = self.lineEdit_marca_casco

        elif tipo == 'INSUMO':
            tabela = 'vw_insumo'
            campo = 'id_insumo'
            lineEdit_id = self.lineEdit_insumo_id
            lineEdit_descricao = self.lineEdit_insumo
            lineEdit_marca = self.lineEdit_marca_insumo

        else:
            logging.debug("[CadastroPedido] Tipo inválido: " + tipo)
            return False

        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':

            mercadoria = self.db.busca_registro(tabela, campo, valor, '=', filtro=filtro_adicional)[1][0]['fnc_buscar_registro']

            logging.debug('[CadastroPedido] ' + str(mercadoria))
            if mercadoria is not None:
                mercadoria = mercadoria[0]
        else:
            lineEdit_descricao.clear()
            lineEdit_marca.clear()
            self.lineEdit_valor_unitario.clear()

        if mercadoria is None or force:

            localizar_campos = {
                campo: 'ID',
                "codigo": 'Código',
                "descricao": tipo.capitalize(),
                'marca': "Marca"
            }

            colunas_busca = {
                campo: 'ID',
                "codigo": 'Código',
                "descricao": tipo.capitalize(),
                'marca': "Marca"
            }

            self.dialog_localizar.define_tabela(tabela)
            self.dialog_localizar.define_campos(localizar_campos)
            self.dialog_localizar.define_colunas(colunas_busca)
            self.dialog_localizar.filtro = filtro_adicional

            self.dialog_localizar.define_valor_padrao(localizar_campos[campo], lineEdit_id.text())

            mercadoria_id = self.dialog_localizar.exec()
            mercadoria = self.db.busca_registro(tabela, campo, str(mercadoria_id), '=')[1][0]['fnc_buscar_registro']

            if mercadoria_id == 0:
                return

            if mercadoria is not None:
                mercadoria = mercadoria[0]

        if mercadoria is not None:
            lineEdit_id.setText(str(mercadoria[campo]))
            lineEdit_descricao.setText(mercadoria['descricao'])
            lineEdit_marca.setText(mercadoria['marca'])

            valor = str(mercadoria['valor_venda']) if tipo != 'INSUMO' else '0,00'
            self.lineEdit_valor_unitario.setText(valor)

            if tipo == 'CASCO':
                self.lineEdit_insumo_id.setText(str(mercadoria['id_insumo']))
                self.lineEdit_insumo_id.editingFinished.emit()
                self.lineEdit_quantidade.setFocus()

                medida = str(mercadoria['quantidade_insumo']) + str(mercadoria['unidade_medida_insumo'])
                self.label_medida.setText(medida)

            if tipo == 'INSUMO':
                if bool(mercadoria['colorido']):
                    self.label_tinta.setPixmap(QPixmap.fromImage(self.color_ink))
                else:
                    self.label_tinta.setPixmap(QPixmap.fromImage(self.bw_ink))

            return True

        else:
            lineEdit_id.clear()
            lineEdit_descricao.clear()
            lineEdit_marca.clear()
            return False

    def posicionar_item(self, item):

        # buscar item em pedido.itens

        item_pedido = ItemPedido

        selecionado = self.tableWidget_items.selectedItems()[0]

        item_pedido.item_pedido_id = int(self.tableWidget_items.item(selecionado.row(), 0).text())

        for it in self.pedido.itens:
            if int(it.item_pedido_id) == int(item_pedido.item_pedido_id):
                item_pedido = it
                break

        if item_pedido.tipo == 'REMANUFATURA':

            self.radioButton_remanufatura.setChecked(True)
            self.define_tipo()
            self.lineEdit_casco_id.setText(str(item_pedido.casco_id))
            self.busca_mercadoria('CASCO')

            self.lineEdit_insumo_id.setText(str(item_pedido.insumo_id))
            self.busca_mercadoria('INSUMO')

        elif item_pedido.tipo == 'MERCADORIA':

            self.radioButton_mercadoria.setChecked(True)

            self.lineEdit_mercadoria_id.setText(str(item_pedido.mercadoria_id))
            self.busca_mercadoria('MERCADORIA')

        self.lineEdit_item_pedido_id.setText(str(item_pedido.item_pedido_id))

        if self.lineEdit_item_pedido_id.text() != '':
            self.buttonBox_item.button(QDialogButtonBox.Save).setText('Editar')
        else:
            self.buttonBox_item.button(QDialogButtonBox.Save).setText('Salvar')

        self.lineEdit_quantidade.setText(
            self.formatar_numero(item_pedido.quantidade))
        self.lineEdit_valor_unitario.setText(
            self.formatar_numero(item_pedido.valor_unitario))

        self.calcula_totais_item()

        self.tabWidget.setCurrentWidget(self.tab_campos)

        return item_pedido

    def salva_item(self):

        #if self.valida_obrigatorios() != 'OK':
        #    return

        tipo_item = 'MERCADORIA' if self.radioButton_mercadoria.isChecked() else 'REMANUFATURA'

        if tipo_item == 'REMANUFATURA':
            descricao = 'Casco: ' + self.lineEdit_casco.text() \
                        + ' Insumo: ' + self.lineEdit_insumo.text()

            item = ItemPedido(
                tipo=tipo_item
                , quantidade=self.formatar_numero(self.lineEdit_quantidade.text())
                , valor_unitario=self.formatar_numero(self.lineEdit_valor_unitario.text())
                , casco_id=self.lineEdit_casco_id.text()
                , insumo_id=self.lineEdit_insumo_id.text()
                , nova_remanufatura=(self.checkBox_reutilizar_casco.isChecked())
                , descricao=descricao
            )

        else:

            descricao = self.lineEdit_mercadoria.text()

            item = ItemPedido(
                tipo=tipo_item
                , quantidade=self.formatar_numero(self.lineEdit_quantidade.text())
                , valor_unitario=self.formatar_numero(self.lineEdit_valor_unitario.text())
                , mercadoria_id=self.lineEdit_mercadoria_id.text()
                , unidade_medida_id=self.db.busca_registro(  # todo: Fazer dinâmico
                    'unidade_medida'
                    , 'abreviacao'
                    , 'UN'
                    , 'like')[1][0]['fnc_buscar_registro'][0]['id_unidade_medida']
                , mercadoria=descricao
                , descricao=descricao
            )

        item_pedido_id = self.lineEdit_item_pedido_id.text()
        novo_item = True if item_pedido_id == '' else False

        if novo_item:
            # Valida itens repetidos
            if len(self.pedido.itens) > 0:
                novo_item_id = self.lineEdit_mercadoria_id.text()
                for item_antigo in self.pedido.itens:
                    if item_antigo.tipo == 'MERCADORIA':
                        if novo_item_id == str(item_antigo.mercadoria_id):
                            print('validando repetidos')
                            dialog = StatusDialog(
                                status='ALERTA'
                                , mensagem='Não é possível inserir o mesmo item duas vezes em um pedido.'
                                , parent=self
                                , esconder_detalhes=True
                            )
                            dialog.exec()
                            return

            item.item_pedido_id = (len(self.pedido.itens) + 1) * -1
        else:
            item.item_pedido_id = int(item_pedido_id)

            for item_antigo in self.pedido.itens:
                if int(item_antigo.item_pedido_id) == int(item_pedido_id):
                    self.pedido.itens.remove(item_antigo)
                    break

        self.pedido.itens.append(item)
        self.preencher_tabela()
        self.calcula_totais_pedido()

    def preencher_tabela(self):

        self.tableWidget_items.setRowCount(len(self.pedido.itens))

        if len(self.pedido.itens) > 0:
            row = 0
            for item_pedido in self.pedido.itens:
                col = 0
                for coluna in self.colunas_item:
                    valor = item_pedido.to_item_dict()[coluna]
                    item = QTableWidgetItem(self.formatar_numero(valor))
                    self.tableWidget_items.setItem(row, col, item)
                    col = col + 1
                row = row + 1

        self.tableWidget_items.setColumnHidden(0, True)

        self.tableWidget_items.resizeColumnsToContents()

        self.limpar_item()

    def apagar_item(self, item):
        # Remove do objeto pedido

        selecionado = self.tableWidget_items.selectedItems()

        if len(selecionado) > 0:
            selecionado = selecionado[0]

        item_pedido_id = int(self.tableWidget_items.item(selecionado.row(), 0).text())

        for it in self.pedido.itens:
            if int(it.item_pedido_id) == int(item_pedido_id):
                self.pedido.itens.remove(it)
                self.preencher_tabela()
                self.pushButton_remover_item.setDisabled(True)
                break

        self.calcula_totais_pedido()

    def limpar_item(self):

        if self.radioButton_mercadoria.isChecked():
            self.lineEdit_mercadoria_id.clear()
            self.lineEdit_mercadoria.clear()
            self.lineEdit_marca_mercadoria.clear()
        elif self.radioButton_remanufatura.isChecked():
            self.lineEdit_casco_id.clear()
            self.lineEdit_casco.clear()
            self.lineEdit_insumo_id.clear()
            self.lineEdit_insumo.clear()
            self.lineEdit_marca_casco.clear()
            self.lineEdit_marca_insumo.clear()
            self.checkBox_reutilizar_casco.setChecked(False)

        self.lineEdit_item_pedido_id.clear()
        self.lineEdit_quantidade.clear()
        self.lineEdit_valor_unitario.clear()
        self.lineEdit_valor_total_item.clear()
        self.lineEdit_valor_total_pedido.clear()

        self.label_medida.setText('0,00g')

        self.buttonBox_item.button(QDialogButtonBox.Save).setText('Salvar')

        self.calcula_totais_pedido()

    def calcula_totais_item(self):

        if self.lineEdit_valor_unitario.text() == '' or self.lineEdit_valor_unitario.text() == '0':
            valor_unitario = 0
            self.lineEdit_valor_unitario.setText('0,00')

        else:
            valor_unitario = float(self.formatar_numero(self.lineEdit_valor_unitario.text()).replace(' ', ''))
            self.lineEdit_valor_unitario.setText(self.formatar_numero(valor_unitario))

        if self.lineEdit_quantidade.text() == '' or self.lineEdit_quantidade.text() == '0':
            quantidade = 0
            self.lineEdit_quantidade.setText('0.00')

        else:
            quantidade = float(self.formatar_numero(self.lineEdit_quantidade.text()).replace(' ', ''))
            self.lineEdit_quantidade.setText(self.formatar_numero(quantidade))

        total_item = quantidade * valor_unitario
        self.lineEdit_valor_total_item.setText(self.formatar_numero(total_item))

    def calcula_totais_pedido(self):
        valor = 0
        for row in range(0, self.tableWidget_items.rowCount()):
            v = 0 if self.tableWidget_items.item(row, 6) is None else self.tableWidget_items.item(row, 6).text()
            v = self.formatar_numero(v)
            valor = valor + float(v)
        self.lineEdit_valor_total_pedido.setText(self.formatar_numero(valor))

    def define_icones(self):
        super(CadastroPedido, self).define_icones()
        self.pushButton_movimentar.setIcon(QIcon(os.path.join('Resources', 'icons', 'confirm.png')))
        self.pushButton_excluir.setIcon(self.icone_cancelar)
        self.pushButton_remover_item.setIcon(self.icone_delete)
        self.pushButton_imprimir.setIcon(QIcon(os.path.join('Resources', 'icons', 'printer.png')))
        find_icon = QIcon(os.path.join('Resources', 'icons', 'search.png'))
        self.toolButton_pessoa.setIcon(find_icon)
        self.toolButton_mercadoria.setIcon(find_icon)
        self.toolButton_insumo.setIcon(find_icon)
        self.toolButton_casco.setIcon(find_icon)

    def define_permite_editar(self):

        super(CadastroPedido, self).define_permite_editar()

        situacao = self.label_situacao.text()

        self.pushButton_editar.setDisabled(
            situacao == 'ENCERRADO' or situacao == 'CANCELADO' or self.lineEdit_id.text() == ''
        )

        self.pushButton_excluir.setDisabled(situacao == 'CANCELADO' or self.lineEdit_id.text() == '')

        self.pushButton_imprimir.setDisabled(situacao == 'CANCELADO' or self.lineEdit_id.text() == '')

    def configura_tipo(self):
        self.tipo_pedido = 'VENDA' if not self.tipo_pedido else self.tipo_pedido
        if self.tipo_pedido == 'VENDA':
            self.tipo_pessoa = 'Cliente'
            self.view_busca = 'vw_pedido_venda'
            self.formGroupBox_pessoa.setTitle(self.tipo_pessoa)
            self.horizontalFrame_tipo_item.setVisible(True)
            self.label_data.setText('Data entrega')
            self.help = \
'''Aqui podem ser realizadas vendas (remanufaturas e mercadorias).
Quando tiver terminado de cadastrar a venda é só encerrar o pedido para confirmar a venda.
Vendas encerradas devem ser estornadas para que possam ser editadas.'''

        elif self.tipo_pedido == 'COMPRA':
            self.tipo_pessoa = 'Fornecedor'
            self.view_busca = 'vw_pedido_compra'
            self.formGroupBox_pessoa.setTitle(self.tipo_pessoa)
            self.radioButton_mercadoria.setChecked(True)
            self.horizontalFrame_tipo_item.setVisible(False)
            self.label_data.setText('Data compra')
            self.help = \
'''Aqui podem ser registradas as suas compras.
Quando tiver terminado de cadastrar é só encerrar o pedido para confirmar a entrada da mercadoria.
Compras encerradas devem ser estornadas para que possam ser editadas.'''

        else:
            dialog = StatusDialog(status='ERRO', mensagem='TIPO DE PEDIDO ' + str(self.tipo_pedido) + ' INVÁLIDO',
                                  parent=self)
            dialog.exec()

    def valida_valores(self):

        ativo = (self.lineEdit_quantidade.text() == '' or self.lineEdit_quantidade.text() == '0') \
                or (self.lineEdit_valor_unitario.text() == '' or self.lineEdit_valor_unitario.text() == '0') \
                or (self.lineEdit_valor_total_item.text() == '' or self.lineEdit_valor_total_item.text() == '0.0')

        if self.radioButton_mercadoria.isChecked():
            ativo = ativo \
                    or self.lineEdit_mercadoria_id.text() == ''

        if self.radioButton_remanufatura.isChecked():
            ativo = ativo \
                    or self.lineEdit_insumo_id.text() == '' \
                    or self.lineEdit_casco_id.text() == ''

        self.buttonBox_item.button(QDialogButtonBox.Save).setDisabled(ativo)

    def imprimir_pedido(self):

        if self.lineEdit_id.text() == '':
            logging.debug("[CadastroPedido] Nenhum pedido selecionado para impressão.")
            return

        if self.pedido.situacao == 'CANCELADO':
            logging.debug("[CadastroPedido] Não é possível imprimir um pedido cancelado.")
            return

        pedido = list()
        pedido_atual = self.pedido.to_dict(generic=True)
        pedido_itens = pedido_atual['itens']
        del pedido_atual['itens']
        pedido.append(pedido_atual)

        items_aux = list()

        for item in pedido_itens:
            aux = dict()
            for coluna, desc in self.colunas_item.items():
                if coluna != 'item_pedido_id' and coluna != 'codigo':
                    if coluna == 'valor_unitario' or coluna == 'valor_total':
                        aux[desc] = "{0:.2f}".format(
                            float(item[coluna])).replace('.', ',')
                    else:
                        aux[desc] = item[coluna]
                    if aux[desc] is None or aux[desc] == 'None':
                        aux[desc] = ''
            items_aux.append(aux)
        pedido_itens = items_aux

        cnpj_emitente = "12.141.655/0001-69"
        IE_emitente = "90524475-23"
        endereco_emitente = 'Rua Dr. Paula Xavier, 1486 - sala 01 - CEP 84010 - Centro - Ponta Grossa - PR'

        html_cabecalho = os.path.join('Resources', 'html', 'RelatorioPadrao', 'cabecalho.html')
        html_rodape = os.path.join('Resources', 'html', 'RelatorioPadrao', 'rodape.html')

        try:
            with open(html_cabecalho, 'r') as f:
                html_cabecalho = f.read()

            with open(html_rodape, 'r') as f:
                html_rodape = f.read()

        except Exception as e:
            logging.debug('[] Exception ao abrir html\n> ' + str(e))
            return

        self.busca_pessoa()
        endereco = self.pessoa.endereco[0]

        html_cabecalho = html_cabecalho.format(
            razao='COMÉRCIO DE EQUIPAMENTOS E SUPRIMENTOS DE INFORMÁTICA'
            , fantasia='JOCIANE F. DA SILVA - INFORMÁTICA'
            , fone='(42) 3224-0660'
            , tipo_pedido=pedido_atual['tipo_pedido']
            , num_pedido=pedido_atual['pedido_id']
            , nome_pessoa=self.pessoa.nome
            , endereco_pessoa=endereco.logradouro + (', ' + endereco.numero if endereco.numero is not None else '')
            , bairro_pessoa=endereco.bairro if endereco.bairro is not None else ''
            , municipio_pessoa=endereco.municipio if endereco.municipio is not None else ''
            , cep_pessoa=endereco.cep if endereco.cep is not None else ''
            , uf_pessoa=endereco.estado if endereco.estado is not None else ''
            , fone_pessoa=self.pessoa.telefone if self.pessoa.telefone is not None else ''
            , situacao=self.pedido.situacao.upper()
            , endereco_emitente=endereco_emitente
            , cnpj_emitente=cnpj_emitente
            , ie_emitente=IE_emitente
            , data_cadastro=self.dateEdit_entrega.date().toString("dd.MM.yyyy").replace('.', '/')
        )

        total = "{0:.2f}".format(
                float(self.lineEdit_valor_total_pedido.text())).replace('.', ',')

        html_rodape = html_rodape.format(
            cnpj_pagador=self.pessoa.get_documento()
            , ie_pagador=self.pessoa.inscricao_estadual
            , total=total
        )

        ficha_pedido = RelatorioPadrao(
            pedido_itens
            , cabecalho=html_cabecalho
            , rodape=html_rodape
            , file=False
            , landscape=False
            , page_size='A4'
            , stylesheet=os.path.join('Resources', 'styles', 'ficha_pedido.css')
            , sort_column='Tipo'
            , override_style=True
        )

        pdf = ficha_pedido.gerar_relatorio()
        ficha_pedido.exibir_relatorio(pdf)

    def translate_ui(self):
        super(CadastroPedido, self).translate_ui()
        self.buttonBox_item.button(QDialogButtonBox.Save).setText('Salvar')
        self.buttonBox_item.button(QDialogButtonBox.Reset).setText('Limpar')
