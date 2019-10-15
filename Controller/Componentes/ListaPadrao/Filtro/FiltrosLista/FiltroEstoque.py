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

        self.campos_filtro = {
            "codigo_mercadoria": (self.lineEdit_mercadoria_id,  '=')
        }

        self.dialog_localizar = LocalizarDialog(db=self.db, parent=self)
        self.lineEdit_mercadoria_id.editingFinished.connect(self.busca_mercadoria)

    def montar_filtro(self) -> str:
        filtro = ''
        filtro = filtro + self.get_mercadoria()
        self.get_entrada()
        self.get_saida()
        self.get_classificacao()
        self.get_estoque()
        return filtro

    def limpar_filtro(self):
        pass

    def busca_mercadoria(self):

        mercadoria = None
        tabela = 'vw_mercadoria'
        campo = 'id_mercadoria'
        lineEdit_id = self.lineEdit_mercadoria_id
        lineEdit_descricao = self.lineEdit_mercadoria

        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':

            mercadoria = self.db.busca_registro(tabela, campo, valor, '=')[1][0]['fnc_buscar_registro']

            logging.debug('[CadastroPedido] ' + str(mercadoria))
            if mercadoria is not None:
                mercadoria = mercadoria[0]
        else:
            lineEdit_descricao.clear()

        if mercadoria is None:

            localizar_campos = {
                campo: 'ID',
                "codigo": 'Código',
                "descricao": "Mercadoria",
                'marca': "Marca"
            }

            colunas_busca = {
                campo: 'ID',
                "codigo": 'Código',
                "descricao": "Mercadoria",
                'marca': "Marca"
            }

            self.dialog_localizar.define_tabela(tabela)
            self.dialog_localizar.define_campos(localizar_campos)
            self.dialog_localizar.define_colunas(colunas_busca)
            self.dialog_localizar.define_valor_padrao(localizar_campos[campo], lineEdit_id.text())

            mercadoria_id = self.dialog_localizar.exec()
            mercadoria = self.db.busca_registro(tabela, campo, str(mercadoria_id), '=')[1][0]['fnc_buscar_registro']

            if mercadoria is not None:
                mercadoria = mercadoria[0]

        if mercadoria:
            lineEdit_id.setText(str(mercadoria[campo]))
            lineEdit_descricao.setText(mercadoria['descricao'])
            return True

        else:
            lineEdit_id.clear()
            lineEdit_descricao.clear()
            lineEdit_marca.clear()
            return False

    def get_mercadoria(self) -> str:
        mercadoria_id = self.lineEdit_mercadoria_id.text()
        if mercadoria_id is not None and mercadoria_id != '':
            return str("id_mercadoria=$$" + str(mercadoria_id) + "$$")
        else:
            return ''

    def get_entrada(self):
        pass

    def get_saida(self):
        pass

    def get_classificacao(self):
        pass

    def get_estoque(self):
        pass



