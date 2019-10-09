import logging

from PySide2.QtCore import QRegExp
from PySide2.QtGui import QDoubleValidator, QRegExpValidator
from PySide2.QtWidgets import QDialogButtonBox

from Controller.Componentes.CadastroPadrao import CadastroPadrao
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog
from Model.Mercadoria import Mercadoria
from View.Ui_CadastroMercadoria import Ui_CadastroMercadoria


class CadastroMercadoria(CadastroPadrao, Ui_CadastroMercadoria):

    def __init__(self, db=None, window_list=None, parent=None, **kwargs):
        super(CadastroMercadoria, self).__init__(parent, **kwargs)
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
            ('Código', self.lineEdit_codigo)
            , ('Descrição', self.lineEdit_descricao)
            , ('Fabricante', self.comboBox_fabricante)
            , ('Valor de Venda', self.lineEdit_valor_venda)
        ])

        self.filtro_adicional = None
        self.view_busca = 'vw_mercadoria'

        self.checkBox_ativo.setChecked(True)

        self.tipo = 'MERCADORIA' if kwargs.get('tipo') \
                                    is None else kwargs.get('tipo')

        if self.tipo == 'MERCADORIA':

            self.tipo = 'MERCADORIA'
            self.stackedWidget.setVisible(False)
            self.checkBox_permite_venda.setChecked(True)
            self.setMinimumHeight(300)
            self.setMaximumHeight(300)

        elif self.tipo == 'CASCO':

            self.label_valor_venda.setText('Valor da remanufatura (R$)')
            self.campos_obrigatorios['Insumo'] = self.lineEdit_insumo_id
            self.campos_obrigatorios['Quantidade'] = self.lineEdit_quantidade_insumo
            self.campos_obrigatorios['Un. Medida (Insumo)'] = self.comboBox_unidade_medida_insumo
            self.stackedWidget.setVisible(True)
            self.page_insumo.setVisible(False)
            self.stackedWidget.setCurrentWidget(self.page_casco)
            self.setMinimumHeight(360)
            self.setMaximumHeight(360)

        elif self.tipo == 'INSUMO':

            self.campos_obrigatorios['Quantidade Embalagem'] = self.lineEdit_quantidade_embalagem
            self.campos_obrigatorios['Un. Medida (Embalagem)'] = self.comboBox_unidade_medida_embalagem
            self.stackedWidget.setVisible(True)
            self.page_casco.setVisible(False)
            self.stackedWidget.setCurrentWidget(self.page_insumo)
            self.setMinimumHeight(360)
            self.setMaximumHeight(360)

        else:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='TIPO DE MERCADORIA INVÁLIDO'
                , parent=self.parent_window)
            dialog.exec()

        self.label_tipo.setText(self.tipo)
        self.setWindowTitle('SOAD - Cadastrar ' + self.tipo.capitalize())

        # Define se ativa o botão editar e excluir
        self.pushButton_editar.setDisabled(True)
        self.pushButton_excluir.setDisabled(True)
        self.lineEdit_id.textChanged[str].connect(
            self.define_permite_editar)

        # Validadores de tipos de dados
        validador_double = QDoubleValidator(bottom=0.000001, top=1000000.00, decimals=6)
        validador_regex_id = QRegExpValidator(QRegExp("[0-9]{1,9}"))
        validador_regex_codigo = QRegExpValidator(QRegExp("([A-z][0-9])*\w+"))

        self.lineEdit_insumo_id.setValidator(validador_regex_id)
        self.lineEdit_quantidade_insumo.setValidator(validador_double)
        self.lineEdit_quantidade_embalagem.setValidator(validador_double)
        self.lineEdit_valor_venda.setValidator(validador_double)
        self.lineEdit_codigo.setValidator(validador_regex_codigo)

        self.lineEdit_descricao.editingFinished.connect(
            lambda: self.lineEdit_descricao.setText(
                self.lineEdit_descricao.text().upper()
            )
        )

        self.lineEdit_codigo.editingFinished.connect(
            lambda: self.lineEdit_codigo.setText(
                self.lineEdit_codigo.text().upper()
            )
        )

        self.checkBox_permite_venda.toggled.connect(
            self.permite_venda_toggled
        )

        # Busca registros
        self.lineEdit_insumo_id.editingFinished.connect(
            self.busca_insumo
        )

        self.unidades_medida = dict()

        # Cadastro de fabricante
        self.fabricantes = set()
        self.lineEdit_fabricante.setVisible(False)
        self.toolButton_addFabricante.clicked.connect(
            self.cadastrar_fabricante)

        self.lineEdit_fabricante.textChanged[str].connect(
            lambda: self.toolButton_addFabricante.setText('Cancelar')
            if self.lineEdit_fabricante.text() == ''
            else self.toolButton_addFabricante.setText('Salvar')
        )
        self.toolButton_addFabricante.setText('+')

        self.dialog_localizar = LocalizarDialog(db=self.db)

        self.define_icones()

        self.popular_dados_padrao()
        self.show()

    def cadastrar(self):
        super(CadastroMercadoria, self).cadastrar()
        self.limpar_dados()
        self.checkBox_permite_venda.setChecked(self.tipo == 'MERCADORIA')
        self.checkBox_ativo.setChecked(True)
        self.lineEdit_valor_venda.setText('0,00')

    def excluir(self):

        self.dados = {
            "metodo": "prc_delete_mercadoria",
            "schema": "soad",
            "params": {
                "mercadoria_id": self.lineEdit_id.text()
            }
        }

        retorno = super(CadastroMercadoria, self).excluir()

        if retorno[0]:
            dialog = StatusDialog(status='OK'
                                  , mensagem='Mercadoria excluída com sucesso.'
                                  , parent=self.parent_window)
            self.limpar_dados()
        else:
            dialog = StatusDialog(status='ALERTA'
                                  , mensagem='Não foi possível excluir a mercadoria.'
                                  , exception=retorno
                                  , parent=self.parent_window)
        dialog.exec()

    def limpar_dados(self):
        super(CadastroMercadoria, self).limpar_dados()
        # mercadoria
        self.lineEdit_codigo.clear()
        self.lineEdit_descricao.clear()
        self.checkBox_permite_venda.setChecked(False)
        self.checkBox_ativo.setChecked(False)
        self.comboBox_fabricante.setCurrentIndex(0)
        self.lineEdit_valor_venda.clear()

        # insumo
        self.lineEdit_quantidade_embalagem.clear()
        self.comboBox_unidade_medida_embalagem.setCurrentIndex(0)

        # casco
        self.lineEdit_insumo_fabricante.clear()
        self.lineEdit_insumo_id.clear()
        self.lineEdit_insumo.clear()
        self.lineEdit_insumo_fabricante.clear()
        self.lineEdit_quantidade_insumo.clear()
        self.comboBox_unidade_medida_insumo.setCurrentIndex(0)

    def localizar(self, parent=None):

        self.localizar_campos = {
            'id_mercadoria': 'ID'
            , "codigo": 'Código'
            , "descricao": self.tipo.capitalize()
            , "marca": "Fabricante"
        }

        self.colunas_busca = {
            'id_mercadoria': 'ID'
            , "codigo": 'Código'
            , "descricao": self.tipo.capitalize()
            , "marca": "Fabricante"
        }

        self.filtro_adicional = "tipo_mercadoria=$$" + self.tipo.capitalize() + "$$"

        retorno = super(CadastroMercadoria, self).localizar(parent=self)

        if retorno is not None:
            self.atualizar_interface(retorno)

    def confirma(self):

        if self.valida_obrigatorios() != 'OK':
            return

        unidade_medida = self.comboBox_unidade_medida_insumo.currentText() \
                         if self.tipo == 'CASCO' \
                         else self.comboBox_unidade_medida_embalagem.currentText()

        mercadoria = Mercadoria(
            mercadoria_id=self.lineEdit_id.text()
            , codigo=self.lineEdit_codigo.text()
            , descricao=self.lineEdit_descricao.text()
            , fabricante=self.comboBox_fabricante.currentText()
            , valor_venda=self.lineEdit_valor_venda.text().replace(',', '.')
            , ativo=self.checkBox_ativo.isChecked()
            , permite_venda=self.checkBox_permite_venda.isChecked()
            , tipo_mercadoria=self.tipo
            , unidade_medida_id=self.unidades_medida.get(unidade_medida)

            # Insumo
            , quantidade_embalagem=self.lineEdit_quantidade_embalagem.text().replace(',', '.')
            , colorido=self.radioButton_cor.isChecked()
            # Casco
            , insumo_id=self.lineEdit_insumo_id.text()
            , quantidade_insumo=self.lineEdit_quantidade_insumo.text().replace(',', '.')
        )

        self.dados = {
            "metodo": "fnc_insert_update_mercadoria",
            "schema": "soad",
            "params": mercadoria.to_dict()
        }

        retorno = super(CadastroMercadoria, self).confirma()

        if retorno[0]:
            mercadoria_id = retorno[1]['p_retorno_json']['mercadoria_id']
            self.atualizar_interface(mercadoria_id)

        else:
            return

    def cancela(self):
        if super(CadastroMercadoria, self).cancela():
            self.limpar_dados()

    def atualizar_interface(self, mercadoria_id):

        self.limpar_dados()

        dados = self.db.get_registro(
            "fnc_get_mercadoria"
            , "mercadoria_id"
            , mercadoria_id
        )

        if dados[0]:
            dados = dados[1][0]['json_mercadoria']
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

        mercadoria = dados

        tipo = str(mercadoria['tipo']).upper()

        if tipo == 'MERCADORIA':
            mercadoria = Mercadoria(
                mercadoria_id=mercadoria['id_mercadoria']
                , codigo=mercadoria['codigo']
                , descricao=mercadoria['descricao']
                , fabricante=mercadoria['marca']
                , valor_venda=mercadoria['valor_venda']
                , ativo=mercadoria['ativo']
                , permite_venda=mercadoria['permite_venda']
                , tipo_mercadoria=tipo
            )

        elif tipo == 'INSUMO':
            mercadoria = Mercadoria(
                mercadoria_id=mercadoria['id_mercadoria']
                , codigo=mercadoria['codigo']
                , descricao=mercadoria['descricao']
                , fabricante=mercadoria['marca']
                , valor_venda=mercadoria['valor_venda']
                , ativo=mercadoria['ativo']
                , permite_venda=mercadoria['permite_venda']
                , tipo_mercadoria=tipo
                , unidade_medida_id=mercadoria['unidade_medida_id']
                , quantidade_embalagem=mercadoria['quantidade_embalagem']
                , colorido=mercadoria['colorido']
            )

            if mercadoria.colorido:
                self.radioButton_cor.setChecked(True)
            else:
                self.radioButton_pb.setChecked(True)

            self.lineEdit_quantidade_embalagem.setText(
                str(mercadoria.quantidade_embalagem).replace('', '')
            )

            for key in self.unidades_medida:
                if self.unidades_medida[key] == mercadoria.unidade_medida_id:
                    self.comboBox_unidade_medida_embalagem.setCurrentText(key)
                    break

        elif tipo == 'CASCO':
            mercadoria = Mercadoria(
                mercadoria_id=mercadoria['id_mercadoria']
                , codigo=mercadoria['codigo']
                , descricao=mercadoria['descricao']
                , fabricante=mercadoria['marca']
                , valor_venda=mercadoria['valor_venda']
                , ativo=mercadoria['ativo']
                , permite_venda=mercadoria['permite_venda']
                , tipo_mercadoria=tipo
                , unidade_medida_id=mercadoria['unidade_medida_id']
                , quantidade_insumo=mercadoria['quantidade_insumo']
                , insumo_id=mercadoria['insumo_id']
            )

            self.lineEdit_quantidade_insumo.setText(
                str(mercadoria.quantidade_insumo).replace('', '')
            )

            for key in self.unidades_medida:
                if self.unidades_medida[key] == mercadoria.unidade_medida_id:
                    self.comboBox_unidade_medida_insumo.setCurrentText(key)
                    break

            self.lineEdit_insumo_id.setText(
                str(mercadoria.insumo_id)
            )

            self.busca_insumo()

        else:
            logging.debug('[CadastroMercadoria] Tipo desconhecido: ' + self.tipo)
            return

        self.lineEdit_id.setText(
            str(mercadoria.mercadoria_id)
        )

        self.label_tipo.setText(mercadoria.tipo)
        self.lineEdit_codigo.setText(mercadoria.codigo)
        self.checkBox_ativo.setChecked(mercadoria.ativo)
        self.checkBox_permite_venda.setChecked(mercadoria.permite_venda)
        self.lineEdit_descricao.setText(mercadoria.descricao)
        self.comboBox_fabricante.setCurrentText(mercadoria.fabricante)

        self.lineEdit_valor_venda.setText(
            str(mercadoria.valor_venda).replace('.', ',')
        )

    def popular_dados_padrao(self):
        self.permite_venda_toggled()

        ### Fabricantes
        self.comboBox_fabricante.clear()
        items = self.db.busca_registro("vw_fabricante", "fabricante")

        if items[0]:
            items = items[1][0]['fnc_buscar_registro']

            if items:
                for item in items:
                    self.fabricantes.add(item['fabricante'])

                self.comboBox_fabricante.addItems(list(self.fabricantes))

        else:
            dialog = StatusDialog(status='ALERTA'
                                  , mensagem="Não foi possível buscar os fabricantes"
                                  , exception=items[1]
                                  , parent=self.parent_window)
            dialog.exec()

        ### Unidades de medida
        self.comboBox_unidade_medida_insumo.clear()
        self.comboBox_unidade_medida_embalagem.clear()

        items = self.db.busca_registro("unidade_medida", "id_unidade_medida")

        if items[0]:
            items = items[1][0]['fnc_buscar_registro']

            for item in items:
                self.unidades_medida[item['abreviacao']] = item['id_unidade_medida']

            self.comboBox_unidade_medida_embalagem.addItems(
                list(self.unidades_medida.keys())
            )
            self.comboBox_unidade_medida_insumo.addItems(
                list(self.unidades_medida.keys())
            )

    def busca_insumo(self):

        insumo = None
        tabela = 'vw_insumo'
        campo = 'id_insumo'
        lineEdit_id = self.lineEdit_insumo_id
        lineEdit_descricao = self.lineEdit_insumo
        lineEdit_marca = self.lineEdit_insumo_fabricante

        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':

            insumo = self.db.busca_registro(tabela, campo, valor, '=')[1][0]['fnc_buscar_registro']

            logging.debug('[CadastroMercadoria] ' + str(insumo))
            if insumo is not None:
                insumo = insumo[0]

        if insumo is None:

            localizar_campos = {
                campo: 'ID'
                , "codigo": 'Código'
                , "descricao": 'Insumo'
                , "marca": "Fabricante"
            }

            colunas_busca = {
                campo: 'ID'
                , "codigo": 'Código'
                , "descricao": 'Insumo'
                , "marca": "Fabricante"
            }

            self.dialog_localizar.define_tabela(tabela)
            self.dialog_localizar.define_campos(localizar_campos)
            self.dialog_localizar.define_colunas(colunas_busca)

            self.dialog_localizar.define_valor_padrao(localizar_campos[campo], lineEdit_id.text())

            mercadoria_id = self.dialog_localizar.exec()
            insumo = self.db.busca_registro(tabela, campo, str(mercadoria_id), '=')[1][0]['fnc_buscar_registro']

            if insumo is not None:
                insumo = insumo[0]

        if insumo:
            lineEdit_id.setText(str(insumo['id_insumo']))
            lineEdit_descricao.setText(insumo['descricao'])
            lineEdit_marca.setText(insumo['marca'])
            return True

        else:
            lineEdit_id.clear()
            lineEdit_descricao.clear()
            lineEdit_marca.clear()
            return False

    def cadastrar_fabricante(self):

        pressed = self.toolButton_addFabricante.isChecked()

        self.comboBox_fabricante.setVisible(not pressed)
        self.lineEdit_fabricante.setVisible(pressed)

        if pressed:
            self.toolButton_addFabricante.setText('Cancelar')
            self.lineEdit_fabricante.setFocus()
            self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(True)

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
            self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(False)
            self.toolButton_addFabricante.setText('+')

    def permite_venda_toggled(self):
        if self.checkBox_permite_venda.isChecked():
            self.lineEdit_valor_venda.setDisabled(False)
        else:
            self.lineEdit_valor_venda.setDisabled(True)
            self.lineEdit_valor_venda.setText('0,00')
