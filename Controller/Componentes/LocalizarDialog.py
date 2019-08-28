from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem

from Controller.Componentes.StatusDialog import StatusDialog
from View.Componentes.Ui_LocalizarDialog import Ui_LocalizarDialog


class LocalizarDialog(QDialog, Ui_LocalizarDialog):

    retorno_dados = Signal(list)

    def __init__(self, db, campos, tabela, colunas, parent=None):
        super(LocalizarDialog, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.tabela = tabela

        self.campos = campos # items do combobox

        self.operador = '='

        self.linhas = None

        self.colunas = colunas # colunas do tablewidget
        self.colunas_descricao = list(colunas.values())
        self.colunas_chave = list(colunas.keys())

        # coluna do QTableWidget (dicionário nome_coluna : descricao
        # primeira coluna do widget sempre deve ser o ID
        self.tableWidget_linhas.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_linhas.setHorizontalHeaderLabels(self.colunas_descricao)


        # dicionário nome_coluna : descricao

        for campo in campos:
            self.comboBox_campo.addItem(campos[campo])

        self.pushButton_buscar.clicked.connect(self.buscar)

        self.tableWidget_linhas.doubleClicked.connect(self.retornar_selecionado)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.retornar_selecionado)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close)

        self.show()

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
        # retorna uma lista de dicionários
        retorno = self.db.busca_registro(self.tabela, campo, valor, operador)

        if not retorno[0]:
            retorno = retorno[0]
        else:
            retorno = retorno[1][0]['fnc_buscar_registro']

        self.preencher_tabela(retorno)

    def preencher_tabela(self, linhas):

        if not linhas:
            self.tableWidget_linhas.setRowCount(0)
            return

        self.tableWidget_linhas.setRowCount(len(linhas))

        row = 0
        for linha in linhas:
            col = 0
            for coluna in self.colunas:
                valor = linha[coluna]
                item = QTableWidgetItem(str(valor))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tableWidget_linhas.setItem(row, col, item)
                col = col + 1
            row = row + 1

        self.tableWidget_linhas.resizeColumnsToContents()

    def retornar_selecionado(self):
        row = self.tableWidget_linhas.currentRow()
        item = self.db.busca_registro(self.tabela, self.colunas_chave[0], self.tableWidget_linhas.item(row, 0).text(), '=')
        print(str(int(self.tableWidget_linhas.item(row, 0).text())))
        if item[0]:
           # item = item[1][0]['fnc_buscar_registro']
           # self.retorno_dados.emit(item)
            self.done(int(self.tableWidget_linhas.item(row, 0).text())) # retorna o ID
        else:
            dialog = StatusDialog(status='AVISO', exception=item[1])
            dialog.definir_mensagem("Não foi possível buscar os dados desse registro.")
            dialog.exec()




