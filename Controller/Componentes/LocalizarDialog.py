from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem

from Controller.Componentes.StatusDialog import StatusDialog
from View.Componentes.Ui_LocalizarDialog import Ui_LocalizarDialog


class LocalizarDialog(QDialog, Ui_LocalizarDialog):

    """
    Modal de busca de registros
    Retornar ID do registro selecionado e emite um json com o registro selecionado em retorno_dados

    db = conexao com o banco
    campos dict() = campos a serem exibidos no comboBox
    tabela str = tabela onde os dados serão buscados
    colunas dict() = colunas a serem exibidas no tableWidget

    """

    retorno_dados = Signal(list)

    def __init__(self, db, campos=None, tabela=None, colunas=None, filtro=None, parent=None):
        super(LocalizarDialog, self).__init__(parent)

        self.db = db
        self.operador = '='
        self.setupUi(self)

        self.linhas = None
        self.campos = campos
        self.tabela = tabela

        self.filtro = filtro

        self.define_tabela(tabela)

        if colunas is not None:
            self.define_colunas(colunas)

        if campos is not None:
            self.define_campos(campos)

        self.tableWidget_linhas.horizontalHeader().setVisible(True)

        self.pushButton_buscar.clicked.connect(self.buscar)
        self.tableWidget_linhas.doubleClicked.connect(self.retornar_selecionado)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.retornar_selecionado)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close)

        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(True)

    def define_colunas(self, colunas):
        # dicionário nome_coluna : descricao
        self.colunas = colunas # colunas do tablewidget
        self.colunas_descricao = list(colunas.values())
        self.colunas_chave = list(colunas.keys())

        # coluna do QTableWidget (dicionário nome_coluna : descricao
        # primeira coluna do widget sempre deve ser o ID
        self.tableWidget_linhas.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_linhas.setHorizontalHeaderLabels(self.colunas_descricao)

    def define_campos(self, campos):
        self.comboBox_campo.clear()
        self.campos = campos
        for campo in campos:
            self.comboBox_campo.addItem(campos[campo])

    def define_tabela(self, tabela):
        if self.tabela != tabela:
            self.tableWidget_linhas.setRowCount(0)
            self.tabela = tabela

    def define_valor_padrao(self, campo, valor):
        self.comboBox_campo.setCurrentText(campo)
        self.lineEdit_valor.setText(str(valor))
        self.lineEdit_valor.setFocus()

    def buscar(self):

        valor = self.lineEdit_valor.text()
        operador = '='
        campo = None

        for c in self.campos:
            if self.campos[c] == self.comboBox_campo.currentText():
                campo = c
                try:
                    valor = int(valor)
                    operador = '='
                except:

                    try:
                        valor = float(valor)
                        operador = '='

                    except:
                        valor = str(valor)
                        operador = 'like'

                break

        valor = str(valor)
        if operador == '=':
            valor.replace('%', '')

        # retorna uma lista de dicionários
        retorno = self.db.busca_registro(
            self.tabela
            , campo
            , valor
            , operador
            , self.filtro
        )

        if not retorno[0]:

            dialog = StatusDialog(status='ALERTA'
                                  , exception=retorno
                                  , mensagem="Não foi possível buscar os dados desse registro."
                                  , parent=self)

            retorno = retorno[0]

            dialog.exec()

        else:
            retorno = retorno[1][0]['fnc_buscar_registro']

        self.preencher_tabela(retorno)

    def preencher_tabela(self, linhas):

        if not linhas:
            self.tableWidget_linhas.setRowCount(0)
            self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(True)
            return

        self.tableWidget_linhas.setRowCount(len(linhas))
        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(False)

        row = 0
        for linha in linhas:
            col = 0
            for coluna in self.colunas:
                valor = '' if linha[coluna] is None else linha[coluna]
                item = QTableWidgetItem(str(valor))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tableWidget_linhas.setItem(row, col, item)
                col = col + 1
            row = row + 1

        #self.tableWidget_linhas.resizeColumnsToContents()

    def retornar_selecionado(self):
        row = self.tableWidget_linhas.currentRow()
        item = self.db.busca_registro(
            self.tabela
            , self.colunas_chave[0]
            , self.tableWidget_linhas.item(row, 0).text()
            , '=')

        if item[0]:
            self.retorno_dados.emit(item)
            self.done(int(self.tableWidget_linhas.item(row, 0).text())) # retorna o ID
        else:
            dialog = StatusDialog(status='ALERTA'
                                  , exception=item[1]
                                  , mensagem="Não foi possível buscar os dados desse registro."
                                  , parent=self)
            dialog.exec()




