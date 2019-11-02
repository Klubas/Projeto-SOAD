from PySide2.QtCore import QDate
from PySide2.QtWidgets import QDialog

from View.Componentes.Ui_FiltroPedido import Ui_FiltroPedido


class FiltroPedido(QDialog, Ui_FiltroPedido):

    def __init__(self, db=None, parent=None, tipo='COMPRA'):
        super(FiltroPedido, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        self.tipo = tipo

        if self.tipo == 'COMPRA':
            self.pessoa = 'fornecedor'
        else:
            self.pessoa = 'cliente'

        self.metodos = (
            self.get_pessoa
            , self.get_cadastro
            , self.get_entrega
        )

        self.dados = None

        self.lineEdit_pessoa_documento.editingFinished.connect(
            lambda: self.busca_registro(
                "vw_pessoa_" + self.pessoa
                , "id_pessoa"
                , self.lineEdit_pessoa_documento
                , "nome"
                , self.lineEdit_pessoa
                , {
                    "id_pessoa": 'ID',
                    "nome": 'Nome',
                    'documento': "Documento"
                }
            )
        )

        self.limpar_filtro()

    def limpar_filtro(self):
        self.lineEdit_pessoa_documento.clear()
        self.lineEdit_pessoa.clear()

        self.groupBox_entrada.setChecked(False)
        self.groupBox_saida.setChecked(False)

        self.dateEdit_data_entrada1.setDate(QDate().currentDate())
        self.dateEdit_data_entrada2.setDate(QDate().currentDate())
        self.dateEdit_data_saida1.setDate(QDate().currentDate())
        self.dateEdit_data_saida2.setDate(QDate().currentDate())

    def get_pessoa(self):
        pessoa_documento = self.lineEdit_pessoa_documento.text()
        if pessoa_documento is not None and pessoa_documento != '':
            pessoa = "id_pessoa_entrada" if self.tipo == 'COMPRA' else "id_pessoa_saida"
            return str(pessoa + " = $$" + str(pessoa_documento) + "$$")
        else:
            return ''

    def get_periodo(self, groupBox, dateEdit_fim, dateEdit_inicio, campo) -> str:
        if groupBox.isChecked():
            data_inicio = dateEdit_inicio.date().toString("dd.MM.yyyy").replace('.', '/')
            data_fim = dateEdit_fim.date().toString("dd.MM.yyyy").replace('.', '/')
            return str("(" + campo + " >= $$" + str(data_inicio) + "$$" + " and " + campo + " <= $$" + str(data_fim) + "$$) or " + campo + " is null")
        else:
            return ''

    def get_cadastro(self) -> str:
        return self.get_periodo(
                groupBox=self.groupBox_entrada
                , dateEdit_inicio=self.dateEdit_data_entrada1
                , dateEdit_fim=self.dateEdit_data_entrada2
                , campo="data_cadastro"
        )

    def get_entrega(self) -> str:
        return self.get_periodo(
                groupBox=self.groupBox_saida
                , dateEdit_inicio=self.dateEdit_data_saida1
                , dateEdit_fim=self.dateEdit_data_saida2
                , campo="data_entrega"
        )
