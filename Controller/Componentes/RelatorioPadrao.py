import os
from datetime import datetime

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QTableWidgetItem

from Controller.Componentes.ConfigRelatorio import ConfigRelatorio
from Controller.Componentes.StatusDialog import StatusDialog
from View.Componentes.Ui_RelatorioPadrao import Ui_RelatorioPadrao


class RelatorioPadrao(QWidget, ConfigRelatorio, Ui_RelatorioPadrao):
    """

    Classe para criar dinamicamente um relatório com base em uma tabela/view e as colunas desejadas

    Parametros:
    tipo = Localiza um tipo em ConfigRelatorio
    titulo = titulo da janela precedido por "SOAD - "
    data = dados a serem carregados na tabela

    """

    def __init__(self, db, window_list, tipo , **kwargs):
        super(ConfigRelatorio, self).__init__()
        super(RelatorioPadrao, self).__init__()
        self.parent_window = self
        self.setupUi(self)
        self.window_list = window_list
        self.db = db
        self.define_icones()

        relatorio = super(RelatorioPadrao, self).get_tipo_relatorio(tipo)

        titulo = kwargs.get('titulo')
        if titulo:
            titulo = "SOAD - " + str(titulo)
        else:
            titulo = "SOAD - Relatório"

        self.setWindowTitle(titulo)

        self.tabela = relatorio["tabela"]
        self.colunas = relatorio["colunas"]

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
        """
        if not data:
            data = self.get_data()
            if data != 0:
                self.set_data(data)
        """
        self.pushButton_atualizar.clicked.connect(self.refresh)
        self.checkBox_data.toggled.connect(
            lambda: self.horizontalWidget_data.setDisabled(not self.checkBox_data.isChecked())
        )
        self.pushButton_filtro.clicked.connect(self.filter)

        self.show()

    def refresh(self):

        self.tableWidget_tabela.setRowCount(0)

        data = self.get_data()
        if data != 0:
            self.set_data(data)

    def get_column_by_key(self, key):
        return self.colunas_chave.index(key)

    def select_all_rows(self):
        pass

    def set_columns(self):
        i = 0
        for coluna in self.colunas:
            self.colunas[coluna] = self.colunas[coluna][0], self.colunas[coluna][1], i
            i = i + 1

        for tupla in self.colunas.values():
            self.colunas_descricao.append(tupla[0])

        self.tableWidget_tabela.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_tabela.setHorizontalHeaderLabels(self.colunas_descricao)
        self.tableWidget_tabela.resizeColumnsToContents()

    def get_data(self):

        retorno = self.db.busca_registro(
            self.tabela
            , ''
            , ''
            , '='
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

        if valor == 'None':
            valor = None

        if tipo == datetime:
            alinhamento = Qt.AlignRight
            if valor:
                valor = valor.split('T')[0]
                data = datetime.strptime(valor, '%Y-%m-%d')
                valor = data.strftime('%d/%m/%Y')
            else:
                valor = ''

        elif tipo == str:
            valor = str(valor) if valor else ''

        elif tipo == float:
            alinhamento = Qt.AlignRight
            if valor is None:
                valor = ''
            else:
                valor = "{0:.2f}".format(valor).replace('.', ',') if valor else '0,00'

        elif tipo == int:
            alinhamento = Qt.AlignHCenter
            valor = str(valor) if valor else ''

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

    def filter(self):
        # Montar string de filtro
        # REFRESH
        self.refresh()

    def define_icones(self):
        self.pushButton_atualizar.setIcon(QIcon(os.path.join('Resources', 'icons', 'refresh.png')))
        self.pushButton_filtro.setIcon(QIcon(os.path.join('Resources', 'icons', 'filter.png')))

    def show(self):
        self.showMaximized()