import logging
import os
from datetime import datetime

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QTableWidgetItem

from Controller.Componentes.ListaPadrao.ConfigLista import ConfigLista
from Controller.Componentes.ListaPadrao.Filtro.FiltroPadrao import FiltroPadrao
from Controller.Componentes.RelatorioPadrao.RelatorioPadrao import RelatorioPadrao
from Controller.Componentes.StatusDialog import StatusDialog
from View.Componentes.Ui_ListaPadrao import Ui_ListaPadrao


class ListaPadrao(QWidget, ConfigLista, Ui_ListaPadrao):
    """

    Classe para criar dinamicamente um relatório com base em uma tabela/view e as colunas desejadas

    Parametros:
    tipo = Localiza um tipo em ConfigRelatorio
    titulo = titulo da janela precedido por "SOAD - "
    data = dados a serem carregados na tabela

    """
    def __init__(self, db, window_list, tipo , **kwargs):
        super(ConfigLista, self).__init__()
        super(ListaPadrao, self).__init__()
        self.parent_window = self
        self.setupUi(self)
        self.window_list = window_list
        self.db = db
        self.define_icones()
        self.dados_lista_relatorio = dict()

        relatorio = super(ListaPadrao, self).get_tipo_relatorio(tipo)

        self.titulo = relatorio["descricao"]

        self.setWindowTitle("SOAD - " + self.titulo)

        self.tabela = relatorio["tabela"]
        self.colunas = relatorio["colunas"]

        if isinstance(relatorio["interface"], tuple):
            self.interface = relatorio["interface"][0]
            self.interface_args = relatorio["interface"][1]
        else:
            self.interface = relatorio["interface"]
            self.interface_args = dict()

        self.filtro = relatorio["filtro"]
        self.relatorio = relatorio["relatorio"]

        if not self.filtro:
            self.pushButton_filtro.setVisible(False)

        if not self.relatorio:
            self.pushButton_relatorio.setVisible(False)
        else:
            self.colunas_relatorio = self.relatorio

        if not self.tabela:
            dialog = StatusDialog(status='ERRO'
                                  , mensagem="Não foi definida a tabela."
                                  , parent=self)
            dialog.exec()

        if not self.colunas:
            dialog = StatusDialog(status='ERRO'
                                  , mensagem="Não foram definidas as colunas."
                                  , parent=self)
            dialog.exec()
        else:
            self.colunas_chave = list(self.colunas.keys())
            self.colunas_descricao = list()
            self.set_columns()

        data = kwargs.get('data')
        if data:
            self.set_data(data)

        self.string_filtro = ''

        self.pushButton_atualizar.clicked.connect(lambda: self.refresh(string_filtro=self.string_filtro))

        self.checkBox_data.toggled.connect(
            lambda: self.horizontalWidget_data.setDisabled(not self.checkBox_data.isChecked())
        )

        self.pushButton_filtro.clicked.connect(self.filter)

        self.pushButton_relatorio.clicked.connect(
            lambda: self.gerar_relatorio(self.dados_lista_relatorio)
        )

        self.tableWidget_tabela.doubleClicked.connect(self.abrir_cadastro)

        if self.filtro is not None:
            self.filter()
        else:
            self.show()
            self.refresh()

    def refresh(self, string_filtro=''):

        self.string_filtro = string_filtro

        self.tableWidget_tabela.setRowCount(0)
        self.tableWidget_tabela.setColumnCount(0)
        self.tableWidget_tabela.clear()
        self.set_columns()

        data = self.get_data(filtro=string_filtro)
        if data != 0:
            self.set_data(data)

    def get_column_by_key(self, key):
        return self.colunas_chave.index(key)

    def select_all_rows(self):
        pass

    def set_columns(self):
        i = 0
        for coluna in self.colunas:
            try:
                if self.colunas[coluna][2] is False:
                    visible = False
                else:
                    visible = True
            except IndexError:
                visible = True

            except Exception as e:
                logging.debug("[ListaPadrao] Exception=" + str(e))
                return -1

            self.colunas[coluna] = self.colunas[coluna][0], self.colunas[coluna][1], visible, i
            i = i + 1

        self.colunas_descricao = list()
        for tupla in self.colunas.values():
            self.colunas_descricao.append(tupla[0])

        self.tableWidget_tabela.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_tabela.setHorizontalHeaderLabels(self.colunas_descricao)
        self.tableWidget_tabela.resizeColumnsToContents()

    def get_data(self, filtro):

        retorno = self.db.busca_registro(
            self.tabela
            , ''
            , ''
            , '='
            , filtro=filtro
        )

        if retorno[0]:
            retorno = retorno[1][0]['fnc_buscar_registro']
            return retorno
        else:
            dialog = StatusDialog(status='ERRO'
                                  , exception=retorno
                                  , mensagem="Não foi possível localizar os registros."
                                  , parent=self)

            dialog.exec()
            return retorno[0]

    def tratar_valor(self, linha, coluna):

        tipo = self.colunas[coluna][1]
        valor = linha[coluna]

        alinhamento = Qt.AlignLeft

        if valor == 'None' or valor == 'NaN':
            valor = None

        if tipo == datetime:
            alinhamento = Qt.AlignRight
            if valor:
                try:
                    valor = valor.split('T')[0]
                    data = datetime.strptime(valor, '%Y-%m-%d')
                    valor = data.strftime('%d/%m/%Y')
                except Exception as e:
                    logging.debug('[ListaPadrao] Exception:\n> ' + str(e))
            else:
                valor = ''

        elif tipo == str:
            valor = str(valor) if valor else ''

        elif tipo == float:
            alinhamento = Qt.AlignRight
            if valor is None:
                valor = ''
            else:
                valor = "{0:.2f}".format(float(valor)).replace('.', ',') if valor else '0,00'

        elif tipo == int:
            alinhamento = Qt.AlignHCenter
            valor = str(int(valor)) if valor else ''

        elif tipo == bool:
            alinhamento = Qt.AlignHCenter
            if valor is None:
                valor = ''
            else:
                valor = 'Sim' if valor else 'Não'

        else:
            valor = str(valor) if valor else ''

        return valor, alinhamento

    def set_data(self, linhas):

        if not linhas:
            self.tableWidget_tabela.setRowCount(0)
            return

        self.tableWidget_tabela.setRowCount(len(linhas))

        row = 0
        for linha in linhas:
            col = 0
            for coluna in self.colunas:
                valor, alinhamento = self.tratar_valor(linha, coluna)
                item = QTableWidgetItem(str(valor))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setTextAlignment(alinhamento)
                self.tableWidget_tabela.setItem(row, col, item)
                col = col + 1
            row = row + 1

        self.tableWidget_tabela.resizeColumnsToContents()

        # Oculta colunas marcadas como not visible
        for coluna in self.colunas.values():
            self.tableWidget_tabela.setColumnHidden(coluna[3], not coluna[2])

        self.dados_lista_relatorio = linhas

    def filter(self):
        if not isinstance(self.filtro, FiltroPadrao):
            self.filtro = FiltroPadrao(db=self.db, child=self.filtro, parent=self)
            self.filtro.setWindowTitle("Filtro - " + self.titulo)
            self.filtro.string_filtro.connect(self.refresh)

        self.filtro.show()

    def abrir_cadastro(self):
        try:
            row = self.tableWidget_tabela.currentRow()
            id = int(self.tableWidget_tabela.item(row, 0).text())
            self.interface_args['id_registro'] = id
            self.interface_args['dialog'] = True
            tela = self.interface(
                self.db
                , self.window_list
                , parent=self
                , **self.interface_args
            )
            """
            self.tableWidget_tabela.setDisabled(True)
            import time
            try:
                while True:
                    if not tela.isVisible():
                        time.sleep(1)
            except:
                self.tableWidget_tabela.setDisabled(False)

            #tela.atualizar_interface(id)
            """
        except Exception as e:
            logging.error("[ListaPadrao] Erro ao abrir tela de cadastro:\n> " + str(e))

    def gerar_relatorio(self, dados):

        if not dados:
            logging.info("[ListaPadrao] Nenhum dado informado para gerar o relatório.")
            return

        dados_relatorio = list()

        row = 0
        for linha in dados:
            col = 0
            linha_relatorio = dict()
            for coluna in self.colunas_relatorio:
                coluna_relatorio = self.colunas_relatorio[coluna]
                linha_relatorio[coluna] = linha[coluna]
                valor = str(self.tratar_valor(linha_relatorio, coluna)[0])
                linha_relatorio.pop(coluna)
                linha_relatorio[coluna_relatorio] = valor
            dados_relatorio.append(linha_relatorio)

        try:

            relatorio = RelatorioPadrao(
                dados_relatorio=dados_relatorio
                , header=self.titulo.replace('Lista', 'Relatório')
                , page_size='A4'
                , landscape=True
            )

            relatorio.gerar_relatorio()

        except Exception as e:
            dialog = StatusDialog(
                status='ERRO'
                , exception=e
                , mensagem="Não foi possível gerar o relatório."
                , parent=self
            )

            dialog.exec()

    def define_icones(self):
        self.pushButton_atualizar.setIcon(QIcon(os.path.join('Resources', 'icons', 'refresh.png')))
        self.pushButton_filtro.setIcon(QIcon(os.path.join('Resources', 'icons', 'filter.png')))
        self.pushButton_relatorio.setIcon(QIcon(os.path.join('Resources', 'icons', 'printer.png')))

    def show(self):
        self.showMaximized()

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        self.window_list.remove(self)
        event.accept()
