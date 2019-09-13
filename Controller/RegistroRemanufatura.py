import json
import logging
import os

from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator, QImage, QPixmap
from PySide2.QtWidgets import QWidget, QDialogButtonBox, QTableWidgetItem

from Controller.Componentes.CadastroPadrao import CadastroPadrao
from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog
from Model.Remanufatura import Remanufatura
from View.Ui_RegistroRemanufatura import Ui_RegistroRemanufatura


class RegistroRemanufatura(QWidget, CadastroPadrao, Ui_RegistroRemanufatura):

    def __init__(self, db=None, window_list=None, **kwargs):
        super(CadastroPadrao, self).__init__()
        super(RegistroRemanufatura, self).__init__()
        ### Padrão
        self.parent_window = self
        self.setupUi(self)

        self.db = db
        self.window_list = window_list
        self.modo_edicao = True

        self.define_lote()

        # Configurações

        self.campos_obrigatorios = dict([
            ('Casco', self.lineEdit_casco_id)
            , ('Insumo', self.lineEdit_insumo_id)
            , ('Quantidade', self.spinBox_quantidade)
        ])

        ## Monta QTableWidget

        self.remanufaturas = list()

        self.colunas_remanufaturas = {
            "remanufatura_id": "ID"
            , "codigo": "Código"
            , "casco_id": "Casco"
            , "insumo_id": "Insumo"
            , "situacao": "Situação"
            , "log": "Ultimo erro"
        }

        self.colunas_descricao = list(self.colunas_remanufaturas.values())
        self.colunas_chave = list(self.colunas_remanufaturas.keys())

        self.tableWidget_remanufaturas.setRowCount(len(self.remanufaturas))
        self.tableWidget_remanufaturas.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_remanufaturas.setHorizontalHeaderLabels(self.colunas_descricao)
        self.tableWidget_remanufaturas.verticalHeader().setVisible(False)
        self.tableWidget_remanufaturas.horizontalHeader().setVisible(True)

        ### Fim monta tableWidget

        # Validadores
        validador_regex_id = QRegExpValidator(QRegExp("[0-9]{1,9}"))
        self.lineEdit_casco_id.setValidator(validador_regex_id)
        self.lineEdit_insumo_id.setValidator(validador_regex_id)

        # Conectar botões

        self.pushButton_limpar.setDisabled(True)
        self.pushButton_realizar.setDisabled(True)

        self.tableWidget_remanufaturas.itemClicked.connect(
            lambda: self.pushButton_realizar.setDisabled(
                len(self.tableWidget_remanufaturas.selectedIndexes()) <= 0
            )
        )

        self.tableWidget_remanufaturas.itemClicked.connect(
            lambda: self.pushButton_limpar.setDisabled(
                len(self.tableWidget_remanufaturas.selectedIndexes()) <= 0
            )
        )

        self.buttonBox_remanufatura.button(
            QDialogButtonBox.Ok).clicked.connect(self.gerar_remanufaturas)

        self.buttonBox_remanufatura.button(
            QDialogButtonBox.Discard).clicked.connect(self.limpar_formulario)

        self.pushButton_realizar.clicked.connect(self.realizar_remanufaturas)

        self.pushButton_limpar.clicked.connect(
            lambda: self.limpar_tabela(apenas_selecionados=True)
        )

        self.pushButton_esvaziar.clicked.connect(self.esvaziar_embalagem)

        self.checkBox_selecionar_tudo.toggled.connect(self.selecionar_todas)

        self.lineEdit_insumo_id.editingFinished.connect(
            lambda: self.busca_mercadoria(tipo='INSUMO')
        )

        self.lineEdit_casco_id.editingFinished.connect(
            lambda: self.busca_mercadoria(tipo='CASCO')
        )

        self.dialog_localizar = LocalizarDialog(db=self.db, parent=self)
        self.show()

    def gerar_remanufaturas(self):

        if self.valida_obrigatorios() != 'OK':
            return

        self.lineEdit_insumo_id.setDisabled(True)
        self.lineEdit_casco_id.setDisabled(True)

        casco_id = self.lineEdit_casco_id.text()
        insumo_id = self.lineEdit_insumo_id.text()
        quantidade = self.spinBox_quantidade.text()
        realizar = False

        dados = {
            "metodo": "fnc_gerar_remanufatura",
            "schema": "soad",
            "params": {
                "casco_id": casco_id,
                "insumo_id": insumo_id,
                "quantidade": quantidade,
                "realizar": realizar
            }
        }

        # pega ids das remanufturas geradas
        retorno = self.db.call_procedure(self.db.schema, dados)

        remanufaturas = list(dict())

        if retorno[0]:

            remanufaturas_ids = retorno[1][0]['p_retorno_json']
            remanufaturas_ids = remanufaturas_ids['remanufaturas_ids']

            for remanufatura_id in remanufaturas_ids:
                remanufaturas.append(
                    Remanufatura(
                        remanufatura_id=remanufatura_id
                        , casco_id=casco_id
                        , insumo_id=insumo_id
                        , situacao='CADASTRADA' if not realizar
                        else 'REALIZADA'
                    )
                )

        else:
            dialog = StatusDialog(
                status='ERRO'
                , exception=retorno
                , mensagem='Erro ao buscar dados.'
                , parent=self
            )
            dialog.exec()

        # posiciona na tabela
        self.popular_tabela(remanufaturas)

    def popular_tabela(self, itens=None):

        self.tableWidget_remanufaturas.setRowCount(0)

        if itens is not None:
            self.remanufaturas = self.remanufaturas + itens

        self.tableWidget_remanufaturas.setRowCount(len(self.remanufaturas))

        if len(self.remanufaturas) > 0:
            row = 0
            for remanufatura in self.remanufaturas:
                col = 0
                for coluna in self.colunas_remanufaturas:
                    valor = remanufatura.to_dict()[coluna]
                    item = QTableWidgetItem(str(valor))
                    self.tableWidget_remanufaturas.setItem(row, col, item)
                    col = col + 1
                row = row + 1

        self.pushButton_realizar.setDisabled(True)
        self.pushButton_limpar.setDisabled(True)

    def limpar_formulario(self):
        # limpa os campos de cadastro da remanufatura
        self.lineEdit_insumo_id.clear()
        self.lineEdit_insumo.clear()
        self.lineEdit_marca_insumo.clear()
        self.lineEdit_casco_id.clear()
        self.lineEdit_casco.clear()
        self.lineEdit_marca_casco.clear()
        self.spinBox_quantidade.setValue(1)

    def limpar_tabela(self, apenas_selecionados=False):
        # remove todas as remanufaturas selecionadas da lista (excluir do banco)

        if not apenas_selecionados:
            self.selecionar_todas(True)

        ids = list()

        # identifica quais serão removidos
        for row in range(0, self.tableWidget_remanufaturas.rowCount()):

            situacao = self.tableWidget_remanufaturas.item(row, 4)
            if situacao.text() == 'CADASTRADA' and situacao.isSelected():

                id_item = self.tableWidget_remanufaturas.item(row, 0).text()
                ids.append(int(id_item))

        # remove da lista

        remanufaturas = list()
        for rem in self.remanufaturas:
            if rem.remanufatura_id not in ids:
                remanufaturas.append(rem)
        self.remanufaturas = remanufaturas

        # remove do banco
        if len(ids) > 0:
            dados = {
                "metodo": "prc_delete_remanufatura"
                , "schema": "soad"
                , "params": {
                    "remanufatura_id": json.dumps(ids)
                }
            }

            retorno = self.db.call_procedure(self.db.schema, dados)

            if retorno[0]:
                pass
            else:
                dialog = StatusDialog(
                    status='ALERTA'
                    , mensagem='Não foi possível remover todas as remanufaturas.'
                    , exception=retorno
                    , parent=self
                )
                dialog.exec()

        # Repopular tabela
        self.popular_tabela()

    def realizar_remanufaturas(self, apenas_selecionados=True):
        # chama o procedimento de realizar remanufatura para
        # todas as remanufaturas selecionadas na lista

        if apenas_selecionados == False:
            self.selecionar_todas(True)
            #self.tableWidget_remanufaturas.selectAll()

        for row in range(0, self.tableWidget_remanufaturas.rowCount()):
            id = self.tableWidget_remanufaturas.item(row, 0)
            if id.isSelected():

                dados = {
                    "metodo": "prc_realizar_remanufatura"
                    , "schema": "soad"
                    , "params": {
                        "remanufatura_id": int(id.text())
                    }
                }

                retorno = self.db.call_procedure(self.db.schema, dados)

                logging.info('[RegistroRemanufatura] Executado procedimento para realizar remanufatura.')

                if retorno[0]:

                    atualiza = self.db.busca_registro(
                        'vw_remanufatura'
                        , 'id_remanufatura'
                        , id.text()
                        , '='
                    )

                    if atualiza[0]:
                        print(atualiza)

                        registro = atualiza[1][0]['fnc_buscar_registro'][0]

                        logging.info('[RegistroRemanufatura] Executado procedimento para buscar remanufatura.')

                        for remanufatura in self.remanufaturas:
                            if remanufatura.remanufatura_id == int(id.text()):

                                remanufatura.situacao = registro['id_remanufatura']

                                self.tableWidget_remanufaturas.item(row, 4)\
                                    .setText(registro['situacao_remanufatura'])

                    else:
                        self.tableWidget_remanufaturas.item(row, 5).setText(str(atualiza[1]))
                        logging.debug('[RegistroRemanufatura] Não foi possível atualizar os dados da remanufatura:')
                        logging.debug('exception> ' + str(atualiza[1]) + '\nsql> ' + str(atualiza[2]))

                else:
                    self.tableWidget_remanufaturas.item(row, 5).setText(str(retorno[1]))
                    logging.debug('[RegistroRemanufatura] Não foi possível realizar a remanufatura:')
                    logging.debug('exception> ' + str(retorno[1]) + '\nsql> ' + str(retorno[2]))

    def selecionar_todas(self, nao_valida_checkbox=False):
        # seleciona todas as remanufaturas com situacao == 'CADASTRADA'

        if self.checkBox_selecionar_tudo.isChecked() or nao_valida_checkbox:
            self.tableWidget_remanufaturas.selectAll()

            for row in range(0, self.tableWidget_remanufaturas.rowCount()-1):
                situacao = self.tableWidget_remanufaturas.item(row, 4)
                if situacao.text() != 'CADASTRADA':
                    for col in range(0, self.tableWidget_remanufaturas.columnCount()):
                        self.tableWidget_remanufaturas.item(row, col).setSelected(False)

            self.pushButton_limpar.setDisabled(False)
            self.pushButton_realizar.setDisabled(False)

        else:
            for item in self.tableWidget_remanufaturas.selectedItems():
                item.setSelected(False)

    def esvaziar_embalagem(self):
        # Marca lote sendo utilizado para recargas como vazio e busca o próximo
        icone_lote = QImage(
            os.path.join("Resources", "icons", "closed_box.png")).smoothScaled(185, 185)
        self.label_embalagem.setPixmap(QPixmap.fromImage(icone_lote))
        self.pushButton_esvaziar.setDisabled(True)

    def busca_mercadoria(self, tipo):
        # Busca insumo e casco e preenche os campos

        mercadoria = None

        if tipo == 'CASCO':
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
            logging.debug("[RegistroRemanufatura] Tipo inválido: " + tipo)
            return False

        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':

            mercadoria = self.db.busca_registro(tabela, campo, valor, '=')[1][0]['fnc_buscar_registro']

            logging.debug('[CadastroPedido] ' + str(mercadoria))
            if mercadoria is not None:
                mercadoria = mercadoria[0]

        if mercadoria is None:

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

            self.dialog_localizar.define_valor_padrao(localizar_campos[campo], lineEdit_id.text())

            mercadoria_id = self.dialog_localizar.exec()

            mercadoria = self.db.busca_registro(
                tabela
                , campo
                , str(mercadoria_id)
                , '='
            )[1][0]['fnc_buscar_registro']

            if mercadoria is not None:
                mercadoria = mercadoria[0]

        if mercadoria:
            lineEdit_id.setText(str(mercadoria[campo]))
            lineEdit_descricao.setText(mercadoria['descricao'])
            lineEdit_marca.setText(mercadoria['marca'])
            return True

        else:
            lineEdit_id.clear()
            lineEdit_descricao.clear()
            lineEdit_marca.clear()
            return False

    def define_lote(self):
        icone_lote = QImage(
            os.path.join("Resources", "icons", "open_box.png")).smoothScaled(185, 185)
        self.label_embalagem.setPixmap(QPixmap.fromImage(icone_lote))

        icone_tinta = QImage(
            os.path.join("Resources", "icons", "ink_wheel.png")).smoothScaled(90, 90)
        self.label_tinta.setPixmap(QPixmap.fromImage(icone_tinta))

    def fechar(self):
        if self.modo_edicao:
            dialog = ConfirmDialog()
            dialog.definir_mensagem("Tem certeza que deseja fechar? As remanufaturas CADASTRADAS serão perdidas.")
            fechar = dialog.exec()
        else:
            fechar = True

        return fechar

    def closeEvent(self, event):
        if self.fechar():
            self.limpar_tabela(apenas_selecionados=False)
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()
