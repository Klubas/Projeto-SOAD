import logging

from PySide2.QtCore import QDate
from PySide2.QtWidgets import QDialog

from Controller.Componentes.LocalizarDialog import LocalizarDialog
from View.Componentes.Ui_FiltroPedido import Ui_FiltroPedido


class FiltroPedido(QDialog, Ui_FiltroPedido):

    def __init__(self, db=None, parent=None, **kwargs):
        super(FiltroPedido, self).__init__(parent)
        self.setupUi(self)
        self.db = db

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
            filtro = str("id_pessoa = $$" + str(pessoa_documento) + "$$")
            return filtro, self.pessoa.capitalize(), pessoa_documento + ' - ' + self.lineEdit_pessoa.text()
        else:
            return ''

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
            return ''

    def get_cadastro(self) -> str:
        return self.get_periodo(
                groupBox=self.groupBox_entrada
                , dateEdit_inicio=self.dateEdit_data_entrada1
                , dateEdit_fim=self.dateEdit_data_entrada2
                , campo="data_cadastro"
                , descricao="Cadastro"
        )

    def get_entrega(self) -> str:
        return self.get_periodo(
                groupBox=self.groupBox_saida
                , dateEdit_inicio=self.dateEdit_data_saida1
                , dateEdit_fim=self.dateEdit_data_saida2
                , campo="data_entrega"
                , descricao="Entrega"
        )

    def busca_registro(self, tabela, campo, lineEdit_id, campo_descricao, lineEdit_descricao, colunas_dict):

        dialog_localizar = LocalizarDialog(db=self.db, parent=self)

        registro = None
        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':

            registro = self.db.busca_registro(tabela, campo, valor, '=')[1][0]['fnc_buscar_registro']

            logging.debug('[FiltroEstoque] ' + str(registro))
            if registro is not None:
                registro = registro[0]
        else:
            lineEdit_descricao.clear()

        if registro is None and lineEdit_id.text() != '':

            localizar_campos = colunas_dict
            colunas_busca = colunas_dict

            dialog_localizar.define_tabela(tabela)
            dialog_localizar.define_campos(localizar_campos)
            dialog_localizar.define_colunas(colunas_busca)
            dialog_localizar.define_valor_padrao(localizar_campos[campo], lineEdit_id.text())

            valor = dialog_localizar.exec()
            registro = self.db.busca_registro(tabela, campo, str(valor), '=')[1][0]['fnc_buscar_registro']

            dialog_localizar.retorno_dados.connect(self.get_dados_localizar)
            # registro = self.dados[1][0]['fnc_buscar_registro']

            if registro is not None:
                registro = registro[0]

        if registro:
            lineEdit_id.setText(str(registro[campo]))
            lineEdit_descricao.setText(registro[campo_descricao])
            return True

        else:
            lineEdit_id.clear()
            lineEdit_descricao.clear()
            return False

    def get_dados_localizar(self, dados):
        self.dados = dados

