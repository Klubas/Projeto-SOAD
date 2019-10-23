import json
import logging
import os

from PySide2.QtCore import Qt, QRegExp, QDate
from PySide2.QtGui import QRegExpValidator, QImage, QPixmap, QIcon
from PySide2.QtWidgets import QDialogButtonBox, QTableWidgetItem

from Controller.Componentes.CadastroPadrao import CadastroPadrao
from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog
from Model.Remanufatura import Remanufatura
from View.Ui_RegistroRemanufatura import Ui_RegistroRemanufatura


class RegistroRemanufatura(CadastroPadrao, Ui_RegistroRemanufatura):

    def __init__(self, db=None, window_list=None, parent=None, **kwargs):
        super(RegistroRemanufatura, self).__init__(parent, **kwargs)
        ### Padrão
        self.parent_window = self
        self.setupUi(self)

        self.db = db
        self.window_list = window_list
        self.modo_edicao = True

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
            , "log": "Log"
        }

        self.col_remanufatura_id = 0
        self.col_codigo = 1
        self.col_casco_id = 2
        self.col_insumo_id = 3
        self.col_situacao = 4
        self.col_log = 5

        self.colunas_descricao = list(self.colunas_remanufaturas.values())
        self.colunas_chave = list(self.colunas_remanufaturas.keys())

        self.label_situacao.setVisible(False)

        self.tableWidget_remanufaturas.setRowCount(len(self.remanufaturas))
        self.tableWidget_remanufaturas.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_remanufaturas.setHorizontalHeaderLabels(self.colunas_descricao)
        self.tableWidget_remanufaturas.verticalHeader().setVisible(False)
        self.tableWidget_remanufaturas.horizontalHeader().setVisible(True)

        ### Fim monta tableWidget

        # Imagens
        self.color_ink = QImage(os.path.join("Resources", "icons", "color_ink.png")).smoothScaled(90, 90)
        self.bw_ink = QImage(os.path.join("Resources", "icons", "bw_ink.png")).smoothScaled(90, 90)
        self.open_box = QImage(os.path.join("Resources", "icons", "open_box.png")).smoothScaled(120, 120)
        self.closed_box = QImage(os.path.join("Resources", "icons", "closed_box.png")).smoothScaled(120, 120)
        self.vazio = QImage(os.path.join("Resources", "icons", "vazio.png")).smoothScaled(120, 120)
        self.icone_esvaziar = QIcon(os.path.join("Resources", "icons", "delete.png"))
        self.icone_realizar = QIcon(os.path.join("Resources", "icons", "ok.png"))
        self.icone_limpar = QIcon(os.path.join("Resources", "icons", "clean.png"))
        self.pushButton_esvaziar.setIcon(self.icone_esvaziar)
        self.pushButton_realizar.setIcon(self.icone_realizar)
        self.pushButton_limpar.setIcon(self.icone_limpar)

        self.label_icone_item_lote.setPixmap(
            QPixmap.fromImage(self.closed_box)
        )

        self.label_tinta.setText('')

        self.formFrame_item_lote.setVisible(False)

        # Validadores
        validador_regex_id = QRegExpValidator(QRegExp("[0-9]{1,9}"))
        self.lineEdit_casco_id.setValidator(validador_regex_id)
        self.lineEdit_insumo_id.setValidator(validador_regex_id)

        # Conectar botões

        self.pushButton_limpar.setDisabled(True)
        self.pushButton_realizar.setDisabled(True)

        self.tableWidget_remanufaturas.itemPressed.connect(self.ativar_botoes)

        self.buttonBox_remanufatura.button(
            QDialogButtonBox.Ok).clicked.connect(self.gerar_remanufaturas)

        self.buttonBox_remanufatura.button(
            QDialogButtonBox.Reset).clicked.connect(self.limpar_formulario)

        self.pushButton_realizar.clicked.connect(
            lambda: self.realizar_remanufaturas(apenas_selecionados=True)
        )

        self.pushButton_limpar.clicked.connect(
            lambda: self.limpar_tabela(apenas_selecionados=True)
        )

        self.pushButton_esvaziar.clicked.connect(
            lambda: self.esvaziar_embalagem(
                int(self.label_item_lote_id.text() if self.label_item_lote_id.text() != '' else None)
            )
        )

        self.checkBox_selecionar_tudo.toggled.connect(self.selecionar_todas)

        self.lineEdit_insumo_id.editingFinished.connect(
            lambda: self.busca_mercadoria(tipo='INSUMO')
        )

        self.lineEdit_casco_id.editingFinished.connect(
            lambda: self.busca_mercadoria(tipo='CASCO')
        )

        self.tableWidget_remanufaturas.setColumnHidden(0, True)
        self.dialog_localizar = LocalizarDialog(db=self.db, parent=self)

        self.id_registro = kwargs.get('id_registro')
        if self.id_registro:
            self.visualizar_remanufatura(self.id_registro)
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

            if self.localiza_item_lote(remanufaturas_ids[0]):
                self.popular_tabela(remanufaturas)

        else:
            dialog = StatusDialog(
                status='ERRO'
                , exception=retorno
                , mensagem='Erro ao buscar dados.'
                , parent=self
            )
            dialog.exec()

    def popular_tabela(self, itens=None):

        self.tableWidget_remanufaturas.setRowCount(0)
        self.checkBox_selecionar_tudo.setChecked(False)

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

                    if remanufatura.situacao != 'CADASTRADA':
                        item.setSelected(False)
                        item.setFlags(Qt.NoItemFlags)

                    col = col + 1
                row = row + 1

        self.tableWidget_remanufaturas.setColumnHidden(0, True)

        self.ativar_botoes()

    def limpar_formulario(self):
        # limpa os campos de cadastro da remanufatura
        self.lineEdit_insumo_id.clear()
        self.lineEdit_insumo.clear()
        self.lineEdit_marca_insumo.clear()
        self.lineEdit_casco_id.clear()
        self.lineEdit_casco.clear()
        self.lineEdit_marca_casco.clear()
        self.spinBox_quantidade.setValue(1)
        self.lineEdit_insumo_id.setDisabled(False)
        self.lineEdit_casco_id.setDisabled(False)

    def limpar_tabela(self, apenas_selecionados=False):
        # remove todas as remanufaturas selecionadas da lista (excluir do banco)

        if self.id_registro:
            dialog = ConfirmDialog(parent=self)
            dialog.definir_mensagem("Tem certeza que deseja excluir essa remanufatura? Essa ação não pode ser desfeita.")
            if not dialog.exec():
                return

        if not apenas_selecionados:
            self.selecionar_todas(nao_valida_checkbox=True)

        items = self.tableWidget_remanufaturas.selectedItems()
        remover = list()

        if not len(items) > 0:
            return

        linhas = list()
        for item in items:
            linhas.append(item.row())
        linhas = list(dict.fromkeys(linhas))

        for linha in linhas:

            id_remanufatura = self.get_id_by_row(linha)

            for remanufatura in self.remanufaturas:
                if remanufatura.remanufatura_id == int(id_remanufatura) \
                        and remanufatura.situacao == 'CADASTRADA':
                    remover.append(remanufatura)

        remover_ids = list()

        for rem in remover:
            remover_ids.append(rem.remanufatura_id)

        dados = {
            "metodo": "prc_delete_remanufatura"
            , "schema": "soad"
            , "params": {
                "remanufatura_id": json.dumps(remover_ids)
            }
        }

        retorno = self.db.call_procedure(self.db.schema, dados)

        if retorno[0]:

            manter = list()
            for remanufatura in self.remanufaturas:
                if remanufatura not in remover:
                    manter.append(remanufatura)
            self.remanufaturas = manter

        else:
            dialog = StatusDialog(
                status='ALERTA'
                , mensagem='Não foi possível remover todas as remanufaturas.'
                , exception=retorno
                , parent=self
            )
            dialog.exec()
        self.popular_tabela()

        if self.id_registro:
            dialog = StatusDialog(
                status='OK'
                , mensagem='Remanufatura removida com sucesso.'
                , parent=self
            )
            dialog.exec()
            self.parent().refresh()
            self.close()

    def realizar_remanufaturas(self, apenas_selecionados=True):
        # chama o procedimento de realizar remanufatura para
        # todas as remanufaturas selecionadas na lista

        if self.label_situacao.text() == 'CADASTRADA' and self.id_registro:
            if not self.localiza_item_lote(remanufatura_id=self.id_registro, novo=True):
                return

        if not apenas_selecionados:
            self.selecionar_todas(nao_valida_checkbox=True)
            logging.debug('[RegistroRemanufatura] Realizando todas remanufaturas.')
        else:
            logging.debug('[RegistroRemanufatura] Realizando remanufaturas selecionadas.')

        items = self.tableWidget_remanufaturas.selectedItems()

        linhas = list()
        for item in items:
            linhas.append(item.row())
        linhas = list(dict.fromkeys(linhas))

        for linha in linhas:

            id_remanufatura = self.get_id_by_row(linha)

            logging.debug('[RegistroRemanufatura] Selecionados: ' + str(id_remanufatura))

            dados = {
                "metodo": "fnc_realizar_remanufatura"
                , "schema": "soad"
                , "params": {
                    "remanufatura_id": int(id_remanufatura)
                }
            }

            retorno = self.db.call_procedure(self.db.schema, dados)
            logging.info('[RegistroRemanufatura] Executado procedimento para realizar remanufatura.')

            if retorno[0]:

                atualiza = self.db.busca_registro(
                    'vw_remanufatura'
                    , 'id_remanufatura'
                    , id_remanufatura
                    , '='
                )

                logging.info('[RegistroRemanufatura] Executado procedimento para buscar remanufatura.')

                if atualiza[0]:

                    registro = atualiza[1][0]['fnc_buscar_registro'][0]

                    self.localiza_item_lote(remanufatura_id=id_remanufatura)

                    for remanufatura in self.remanufaturas:
                        if remanufatura.remanufatura_id == int(id_remanufatura):
                            remanufatura.situacao = registro['situacao_remanufatura']
                            remanufatura.codigo = registro['codigo']

                            self.tableWidget_remanufaturas.item(
                                linha, self.col_situacao).setText(remanufatura.situacao)

                            self.tableWidget_remanufaturas.item(
                                linha, self.col_codigo).setText(remanufatura.codigo)

                            self.tableWidget_remanufaturas.item(
                                linha, self.col_log).setText('')

                else:
                    self.tableWidget_remanufaturas.item(str(linha), self.col_log).setText(str(atualiza[1][0]))
                    logging.debug('[RegistroRemanufatura] Não foi possível atualizar os dados da remanufatura:')
                    logging.debug('exception> ' + str(atualiza[1]) + '\nsql> ' + str(atualiza[2]))

            else:
                self.tableWidget_remanufaturas.item(str(linha), self.col_log).setText(str(retorno[1][0]))
                logging.debug('[RegistroRemanufatura] Não foi possível realizar a remanufatura:')
                logging.debug('exception> ' + str(retorno[1]) + '\nsql> ' + str(retorno[2]))

        self.popular_tabela()

    def get_id_by_row(self, row_id):
        return self.tableWidget_remanufaturas.item(int(row_id), int(self.col_remanufatura_id)).text()

    def selecionar_todas(self, nao_valida_checkbox=False):
        # seleciona todas as remanufaturas com situacao == 'CADASTRADA'
        if self.checkBox_selecionar_tudo.isChecked() or nao_valida_checkbox:
            self.tableWidget_remanufaturas.selectAll()
            self.ativar_botoes()
            logging.debug('[RegistroRemanufatura] Selecionado todas as remanufaturas.')

        else:
            for item in self.tableWidget_remanufaturas.selectedItems():
                item.setSelected(False)
            logging.debug('[RegistroRemanufatura] Deselecionado todas as remanufaturas.')

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

            logging.debug('[RegistroRemanufatura] ' + str(mercadoria))
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

            if tipo == 'CASCO':
                self.lineEdit_insumo_id.setText(str(mercadoria['id_insumo']))
                self.lineEdit_insumo_id.editingFinished.emit()
                self.buttonBox_remanufatura.setFocus()

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

    def localiza_item_lote(self, remanufatura_id, novo=True):

        if novo:
            dados = {
                "metodo": "fnc_realizar_remanufatura"
                , "schema": "soad"
                , "params": {
                    "remanufatura_id": remanufatura_id
                    , "simular": True
                }
            }

            retorno = self.db.call_procedure(self.db.schema, dados)

        else:
            dados = {
                "metodo": "fnc_get_item_lote_remanufatura"
                , "schema": "soad"
                , "params": {
                    "remanufatura_id": remanufatura_id
                }
            }

            retorno = self.db.call_procedure(self.db.schema, dados)

        if retorno[0]:
            id_item_lote = retorno[1][0]['p_retorno_json']['p_item_lote_id']

            registro = self.db.busca_registro(
                'vw_item_lote'
                , 'id_item_lote'
                , str(id_item_lote)
                , '='
            )

            logging.info('[RegistroRemanufatura] Localizando item lote.')

            if registro[0]:

                registro = registro[1][0]['fnc_buscar_registro'][0]

                self.posiciona_item_lote(registro)
                return True

        else:
            dialog = StatusDialog(
                status='ALERTA'
                , exception=retorno
                , mensagem=' Não foi possível inserir remanufatura.'
                , parent=self
            )
            dialog.exec()
            logging.info('[RegistroRemanufatura] Não foi possível identificar insumo em estoque.')
            self.lineEdit_insumo_id.setDisabled(False)
            self.lineEdit_casco_id.setDisabled(False)
            return False

    def posiciona_item_lote(self, dados):

        self.formFrame_item_lote.setVisible(True)

        item_lote = dados

        self.label_item_lote_descricao.setText(
            item_lote['codigo_mercadoria'] + ' - ' + item_lote['descricao']
        )

        self.label_item_lote_fabricante.setText(item_lote['marca'])

        ### datas
        data = str(item_lote['data_cadastro']).split('T')[0]
        data = data if data != 'None' else None
        if data is None:
            self.dateEdit_entrada.setDisabled(True)
        else:
            self.dateEdit_entrada.setDisabled(False)
            self.dateEdit_entrada.setDate(
                QDate.fromString(
                    data, 'yyyy-MM-dd')

            )

        data = str(item_lote['data_abertura']).split('T')[0]
        data = data if data != 'None' else None
        if data is None:
            self.dateEdit_abertura.setDisabled(True)
        else:
            self.dateEdit_abertura.setDisabled(False)
            self.dateEdit_abertura.setDate(
                QDate.fromString(
                    data, 'yyyy-MM-dd')
            )

        data = str(item_lote['data_validade']).split('T')[0]
        data = data if data != 'None' else None
        if data is None:
            self.dateEdit_validade.setDisabled(True)
        else:
            self.dateEdit_validade.setDisabled(False)
            self.dateEdit_validade.setDate(
                QDate.fromString(
                    data, 'yyyy-MM-dd')
            )

        self.label_item_lote_lote_id.setText(str(item_lote['id_lote']))

        self.label_item_lote_id.setText(str(item_lote['id_item_lote']))

        quantidade_remanufatura = item_lote['quantidade_remanufaturas']
        quantidade_remanufatura = '0' if quantidade_remanufatura is None else str(quantidade_remanufatura)
        self.label_item_lote_quantidade_remanufaturas.setText(quantidade_remanufatura)

        aberto = item_lote['aberto']
        self.label_item_lote_aberto.setText(
            'Sim' if aberto else 'Não'
        )

        self.label_icone_item_lote.setPixmap(
            QPixmap.fromImage(self.open_box if aberto else self.closed_box)
        )

        vazio = True if int(item_lote['quantidade_item']) == 0 else False
        self.label_item_lote_vazio.setText('Sim' if vazio else 'Não')

        if vazio:
            self.label_icone_item_lote.setPixmap(
                QPixmap.fromImage(self.vazio))
            self.pushButton_esvaziar.setDisabled(True)
        else:
            self.pushButton_esvaziar.setDisabled(False)
        self.ativar_botoes()

    def esvaziar_embalagem(self, item_lote_id):
        # Marca lote sendo utilizado para recargas como vazio
        if item_lote_id is None:
            return

        dialog = ConfirmDialog(parent=self)
        dialog.definir_mensagem(
            "Tem certeza que deseja marcar essa embalagem como 'Vazia'?\nEssa ação não pode ser desfeita.")

        if dialog.exec():

            dados = {
                "metodo": "prc_esvaziar_item_lote"
                , "schema": "soad"
                , "params": {
                    "item_lote_id": str(item_lote_id)
                }
            }

            retorno = self.db.call_procedure(self.db.schema, dados)
            logging.info('[RegistroRemanufatura] Executado procedimento para esvaziar lote.')

            if retorno[0]:
                if retorno[1][0]['p_retorno'] == 100:
                    self.label_icone_item_lote.setPixmap(QPixmap.fromImage(self.vazio))
                    self.pushButton_esvaziar.setDisabled(True)
                    self.label_item_lote_vazio.setText('Sim')
                self.ativar_botoes()
            else:
                dialog = StatusDialog(
                    status='ALERTA'
                    , exception=retorno
                    , mensagem='Não foi possível esvaziar o insumo.'
                    , parent=self
                )
                dialog.exec()

    def ativar_botoes(self):
        disabled = True
        disabled = disabled and len(self.tableWidget_remanufaturas.selectedIndexes()) <= 0
        self.pushButton_limpar.setDisabled(disabled)

        disabled = disabled or self.label_item_lote_vazio.text() == 'Sim'
        self.pushButton_realizar.setDisabled(disabled)

    def fechar(self):
        if self.modo_edicao:

            if self.id_registro:
                return True

            if self.tableWidget_remanufaturas.rowCount() > 0:
                dialog = ConfirmDialog(parent=self)
                dialog.definir_mensagem("Tem certeza que deseja fechar? As remanufaturas CADASTRADAS serão perdidas.")
                fechar = dialog.exec()
            else:
                fechar = True
        else:
            fechar = True

        if fechar:
            self.limpar_tabela(apenas_selecionados=False)

        return fechar

    def visualizar_remanufatura(self, id_remanufatura):
        self.lineEdit_casco_id.setDisabled(True)
        self.lineEdit_insumo_id.setDisabled(True)
        #self.groupBox_remanufaturas.setVisible(False)
        self.buttonBox_remanufatura.setVisible(False)
        self.spinBox_quantidade.setVisible(False)
        self.label_situacao.setVisible(True)
        self.buscar_remanufatura(remanufatura_id=id_remanufatura)
        # Manipular botões

        self.pushButton_limpar.setText('Remover remanufatura')
        self.pushButton_realizar.setText('Realizar remanufatura')

        situacao = self.label_situacao.text()

        if situacao == 'CADASTRADA':
            self.pushButton_realizar.setDisabled(False)
            self.pushButton_limpar.setDisabled(False)

        else:
            self.pushButton_esvaziar.setVisible(False)
            self.pushButton_realizar.setVisible(False)
            self.pushButton_limpar.setVisible(False)

    def buscar_remanufatura(self, remanufatura_id):

        remanufatura = None

        tabela = 'vw_remanufatura'
        campo = 'id_remanufatura'

        if remanufatura_id != '':

            remanufatura = self.db.busca_registro(tabela, campo, str(remanufatura_id), '=')[1][0]['fnc_buscar_registro']

            logging.debug('[RegistroRemanufatura] ' + str(remanufatura))
            if remanufatura is not None:
                remanufatura = remanufatura[0]

                remanufaturas = list(dict())

                remanufaturas.append(
                    Remanufatura(
                        remanufatura_id=remanufatura_id
                        , casco_id=int(remanufatura['id_casco'])
                        , insumo_id=int(remanufatura['id_insumo'])
                        , situacao=remanufatura['situacao_remanufatura']
                    )
                )

                self.popular_tabela(remanufaturas)
                self.localiza_item_lote(remanufatura_id=remanufatura_id, novo=False)
                self.selecionar_todas(nao_valida_checkbox=True)

        if remanufatura:
            self.lineEdit_codigo.setText(str(remanufatura['codigo']))
            self.lineEdit_casco_id.setText(str(remanufatura['id_casco']))
            self.lineEdit_casco_id.editingFinished.emit()

            self.lineEdit_insumo_id.setText(str(remanufatura['id_insumo']))
            self.lineEdit_insumo_id.editingFinished.emit()

            self.label_situacao.setText(str(remanufatura['situacao_remanufatura']))
            return True

        else:
            return False


