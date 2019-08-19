from PySide2.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem

from View.Componentes.Ui_LocalizarDialog import Ui_LocalizarDialog


class LocalizarDialog(QDialog, Ui_LocalizarDialog):

    def __init__(self, db, campos, tabela, colunas, parent=None):
        super(LocalizarDialog, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.tabela = tabela

        self.campos = campos

        self.operador = '='

        self.linhas = None

        self.colunas = colunas
        self.colunas_descricao = list(colunas.values())
        self.colunas_chave = list(colunas.keys())

        # coluna do QTableWidget (dicionário nome_coluna : descricao
        self.tableWidget_linhas.setColumnCount(len(self.colunas_descricao))
        self.tableWidget_linhas.setHorizontalHeaderLabels(self.colunas_descricao)

        # dicionário nome_coluna : descricao

        for campo in campos:
            self.comboBox_campo.addItem(campos[campo])

        self.pushButton_buscar.clicked.connect(self.buscar)

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
            print(linha)
            col = 0
            for coluna in self.colunas:
                valor = linha[coluna]
                print(valor)
                self.tableWidget_linhas.setItem(row, col, QTableWidgetItem(str(valor)))
                col = col + 1
            row = row + 1

        self.tableWidget_linhas.resizeColumnsToContents()

    def retornar_selecionado(self):
        pass