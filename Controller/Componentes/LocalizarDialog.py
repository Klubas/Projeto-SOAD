from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_LocalizarDialog import Ui_LocalizarDialog


class LocalizarDialog(QDialog, Ui_LocalizarDialog):

    def __init__(self, db, campos, tabela, parent=None):
        super(LocalizarDialog, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.tabela = tabela

        self.campos = campos

        self.linhas = None

        # dicionário nome_coluna : descricao amigavel

        for campo in campos:
            self.comboBox_campo.addItem(campos[campo])

        self.pushButton_buscar.clicked.connect(self.buscar)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.retornar_selecionado)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close)

        self.show()

    def buscar(self):

        campo = None
        for c in self.campos:
            if self.campos[c] == self.comboBox_campo.currentText():
                campo = c
                break

        valor = self.lineEdit_valor.text()

        self.linhas = self.db.busca_registro(self.tabela, campo, valor)

        print(self.linhas)
        self.preencher_tabela()

    def preencher_tabela(self):
        pass

    def retornar_selecionado(self):
        pass