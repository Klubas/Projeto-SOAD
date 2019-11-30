import logging
import os

from PySide2.QtCore import QDate
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from View.Componentes.Ui_FiltroPedido import Ui_FiltroPedido


class FiltroPedido(QDialog, Ui_FiltroPedido):

    def __init__(self, db=None, parent=None, **kwargs):
        super(FiltroPedido, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        filtro_padrao = kwargs.get('filtro_padrao')

        self.tipo = kwargs.get('tipo') if 'tipo' in kwargs else None

        if self.tipo == 'COMPRA':
            self.pessoa = 'fornecedor'
        elif self.tipo == 'VENDA':
            self.pessoa = 'cliente'
        else:
            logging.info('[FiltroPedido] Tipo de pedido não suportado.')
            return

        self.groupBox_pessoa.setTitle(self.pessoa.capitalize())

        self.metodos = (
            self.get_pessoa
            , self.get_cadastro
            , self.get_entrega
            , self.get_situacao
        )

        find_icon = QIcon(os.path.join('Resources', 'icons', 'search.png'))
        self.toolButton_pessoa.setIcon(find_icon)

        self.dados = None

        self.toolButton_pessoa.clicked.connect(
            lambda: filtro_padrao.busca_registro(
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
                , force=True
            )
        )

        self.lineEdit_pessoa_documento.editingFinished.connect(
            lambda: filtro_padrao.busca_registro(
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
            filtro = str("id_pessoa = $$" + str(pessoa_documento) + "$$")
            return filtro, self.pessoa.capitalize(), pessoa_documento + ' - ' + self.lineEdit_pessoa.text()
        else:
            return '1=1', 'Pessoa', 'Todas'

    def get_periodo(self, groupBox, dateEdit_fim, dateEdit_inicio, campo, descricao=''):
        descricao = 'Período (' + descricao + ')'
        if groupBox.isChecked():
            data_inicio = dateEdit_inicio.date().toString("dd.MM.yyyy").replace('.', '/')
            data_fim = dateEdit_fim.date().toString("dd.MM.yyyy").replace('.', '/')
            return (str("(" + campo + " >= $$" + str(data_inicio) + "$$" + " and " + campo + " <= $$" + str(data_fim)
                        + "$$) or " + campo + " is null")
                    , descricao
                    , str(data_inicio + ' até ' + data_fim))
        else:
            return '1=1', descricao, 'Desde o início'

    def get_cadastro(self):
        return self.get_periodo(
                groupBox=self.groupBox_entrada
                , dateEdit_inicio=self.dateEdit_data_entrada1
                , dateEdit_fim=self.dateEdit_data_entrada2
                , campo="data_cadastro"
                , descricao="Cadastro"
        )

    def get_entrega(self):
        return self.get_periodo(
                groupBox=self.groupBox_saida
                , dateEdit_inicio=self.dateEdit_data_saida1
                , dateEdit_fim=self.dateEdit_data_saida2
                , campo="data_entrega"
                , descricao="Entrega"
        )

    def get_situacao(self):
        filtro = ''
        cabecalho = ''
        if self.checkBox_cadastrado.isChecked() \
                and self.checkBox_cancelado.isChecked() \
                and self.checkBox_estornado.isChecked() \
                and self.checkBox_encerrado.isChecked():
            return filtro, "Situação", "Todas"

        if self.checkBox_cadastrado.isChecked():
            filtro = 'UPPER(situacao) = UPPER($$CADASTRADO$$)'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = 'Cadastrados'

        if self.checkBox_encerrado.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'UPPER(situacao) = UPPER($$ENCERRADO$$)'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + 'Encerrados'

        if self.checkBox_estornado.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'UPPER(situacao) = UPPER($$ESTORNADO$$)'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + 'Estornados'

        if self.checkBox_cancelado.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'UPPER(situacao) = UPPER($$CANCELADO$$)'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + 'Cancelados'

        return filtro, "Situação", cabecalho