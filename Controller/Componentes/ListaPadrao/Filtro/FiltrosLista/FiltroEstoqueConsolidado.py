import logging

from PySide2.QtCore import QDate
from PySide2.QtWidgets import QDialog

from Controller.Componentes.LocalizarDialog import LocalizarDialog
from View.Componentes.Ui_FiltroEstoqueConsolidado import Ui_FiltroEstoqueConsolidado


class FiltroEstoqueConsolidado(QDialog, Ui_FiltroEstoqueConsolidado):
    """
    Fazer mapeamento dos campos
    nome_campo - nome_coluna - sinal
    "nome_coluna": (campo, sinal)
    """

    def __init__(self, db=None, parent=None):
        super(FiltroEstoqueConsolidado, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        self.metodos = (
            self.get_mercadoria
            , self.get_fornecedor
            , self.get_classificacao
            , self.get_estoque
            , self.get_data_base
        )

        self.dados = None

        self.lineEdit_fornecedor_documento.editingFinished.connect(
            lambda: self.busca_registro(
                "vw_pessoa_fornecedor"
                , "id_pessoa"
                , self.lineEdit_fornecedor_documento
                , "nome"
                , self.lineEdit_fornecedor
                , {
                    "id_pessoa": 'ID',
                    "nome": 'Nome',
                    'documento': "Documento"
                }
            )
        )

        self.lineEdit_mercadoria_id.editingFinished.connect(
            lambda: self.busca_registro(
                "vw_mercadoria"
                , "id_mercadoria"
                , self.lineEdit_mercadoria_id
                , "descricao"
                , self.lineEdit_mercadoria
                , {
                    "id_mercadoria": 'ID',
                    "codigo": 'Código',
                    "descricao": "Mercadoria",
                    'marca': "Marca"
                }
            )
        )

        self.limpar_filtro()

    def limpar_filtro(self):
        self.lineEdit_fornecedor.clear()
        self.lineEdit_fornecedor_documento.clear()
        self.lineEdit_mercadoria_id.clear()
        self.lineEdit_mercadoria.clear()

        self.checkBox_mercadoria.setChecked(False)
        self.checkBox_insumo.setChecked(False)
        self.checkBox_casco.setChecked(False)

        self.dateEdit_data_base.setDate(QDate().currentDate())

    def busca_registro(self, tabela, campo, lineEdit_id, campo_descricao, lineEdit_descricao, colunas_dict):

        dialog_localizar = LocalizarDialog(db=self.db, parent=self)

        registro = None
        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':

            registro = self.db.busca_registro(tabela, campo, valor, '=')[1][0]['fnc_buscar_registro']

            logging.debug('[FiltroEstoqueConsolidado] ' + str(registro))
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
            #registro = self.dados[1][0]['fnc_buscar_registro']

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

    def get_mercadoria(self) -> str:
        mercadoria_id = self.lineEdit_mercadoria_id.text()
        if mercadoria_id is not None and mercadoria_id != '':
            return str("id_mercadoria = $$" + str(mercadoria_id) + "$$")
        else:
            return ''

    def get_fornecedor(self) -> str:
        pessoa_documento = self.lineEdit_fornecedor_documento.text()
        if pessoa_documento is not None and pessoa_documento != '':
            return str("id_pessoa_entrada = $$" + str(pessoa_documento) + "$$")
        else:
            return ''

    def get_periodo(self, groupBox, dateEdit_fim, dateEdit_inicio, campo) -> str:
        if groupBox.isChecked():
            data_inicio = dateEdit_inicio.date().toString("dd.MM.yyyy").replace('.', '/')
            data_fim = dateEdit_fim.date().toString("dd.MM.yyyy").replace('.', '/')
            return str(campo + " >= $$" + str(data_inicio) + "$$" + " and " + campo + " <= $$" + str(data_fim) + "$$")
        else:
            return ''

    def get_data_base(self):
        if not self.groupBox_data_base.isChecked():
            self.dateEdit_data_base.setDate(QDate().currentDate())
        data_base = self.dateEdit_data_base.date().toString("dd.MM.yyyy").replace('.', '/')

        return str('''
            data_cadastro::date <= $${data_base}$$::date
            AND(data_retirada::date > $${data_base}$$::date or data_retirada is null)
            '''.format(data_base=data_base))

    def get_classificacao(self) -> str:
        filtro = ''
        if self.checkBox_mercadoria.isChecked():
            filtro = filtro + "UPPER(tipo_mercadoria) = $$MERCADORIA$$"

        if self.checkBox_insumo.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + "UPPER(tipo_mercadoria) = $$INSUMO$$"

        if self.checkBox_casco.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + "UPPER(tipo_mercadoria) = $$CASCO$$"

        return "(" + filtro + ")" if filtro != '' else filtro

    def get_estoque(self) -> str:
        filtro = ''

        if not self.checkBox_inativos.isChecked():
            filtro = filtro + " and " if filtro != '' else filtro
            filtro = filtro + "ativo = true::boolean"

        return filtro

    def get_dados_localizar(self, dados):
        self.dados = dados


