import logging

from PySide2.QtWidgets import QDialog

from Controller.Componentes.LocalizarDialog import LocalizarDialog
from View.Componentes.Ui_FiltroEstoque import Ui_FiltroEstoque


class FiltroEstoque(QDialog, Ui_FiltroEstoque):
    """
    Fazer mapeamento dos campos
    nome_campo - nome_coluna - sinal
    "nome_coluna": (campo, sinal)
    """

    def __init__(self, db=None, parent=None):
        super(FiltroEstoque, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        self.metodos = (
            self.get_mercadoria
            , self.get_fornecedor
            , self.get_entrada
            , self.get_saida
            , self.get_classificacao
            , self.get_estoque
        )

        self.dados = None

        self.campos_filtro = {
            "codigo_mercadoria": (self.lineEdit_mercadoria_id,  '=')
        }

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

    def limpar_filtro(self):
        pass

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
            #registro = self.dados[1][0]['fnc_buscar_registro']
            print(registro)

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

    def get_fornecedor(self):
        pessoa_documento = self.lineEdit_fornecedor_documento.text()
        if pessoa_documento is not None and pessoa_documento != '':
            return str("id_pessoa_entrada = $$" + str(pessoa_documento) + "$$")
        else:
            return ''

    def get_periodo(self, groupBox, dateEdit_fim, dateEdit_inicio, campo) -> str:
        if groupBox.isChecked():
            data_inicio = dateEdit_inicio.date().toString("dd.MM.yyyy").replace('.', '/')
            data_fim = dateEdit_fim.date().toString("dd.MM.yyyy").replace('.', '/')
            print(data_inicio)
            return str(campo + " >= $$" + str(data_inicio) + "$$" + " and " + campo + " <= $$" + str(data_fim) + "$$")
        else:
            return ''

    def get_entrada(self) -> str:
        return self.get_periodo(
                groupBox=self.groupBox_entrada
                , dateEdit_inicio=self.dateEdit_data_entrada1
                , dateEdit_fim=self.dateEdit_data_entrada2
                , campo="data_cadastro"
        )

    def get_saida(self) -> str:
        return self.get_periodo(
                groupBox=self.groupBox_saida
                , dateEdit_inicio=self.dateEdit_data_saida1
                , dateEdit_fim=self.dateEdit_data_saida2
                , campo="data_retirada"
        )

    def get_classificacao(self) -> str:
        return ''

    def get_estoque(self) -> str:
        return ''

    def get_dados_localizar(self, dados):
        self.dados = dados


