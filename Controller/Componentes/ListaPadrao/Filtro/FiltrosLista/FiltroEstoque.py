import os

from PySide2.QtCore import QDate
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from View.Componentes.Ui_FiltroEstoque import Ui_FiltroEstoque


class FiltroEstoque(QDialog, Ui_FiltroEstoque):
    """
    Fazer mapeamento dos campos
    nome_campo - nome_coluna - sinal
    "nome_coluna": (campo, sinal)
    """

    def __init__(self, db=None, parent=None, **kwargs):
        super(FiltroEstoque, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        filtro_padrao = kwargs.get('filtro_padrao')

        self.metodos = (
            self.get_mercadoria
            , self.get_fornecedor
            , self.get_entrada
            , self.get_saida
            , self.get_classificacao
            , self.get_estoque
        )

        find_icon = QIcon(os.path.join('Resources', 'icons', 'search.png'))
        self.toolButton_mercadoria.setIcon(find_icon)
        self.toolButton_fornecedor.setIcon(find_icon)

        self.toolButton_mercadoria.clicked.connect(
            lambda: filtro_padrao.busca_registro(
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
                , force=True
            )
        )

        self.toolButton_fornecedor.clicked.connect(
            lambda: filtro_padrao.busca_registro(
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
                , force=True
            )
        )

        self.lineEdit_fornecedor_documento.editingFinished.connect(
            lambda: filtro_padrao.busca_registro(
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
            lambda: filtro_padrao.busca_registro(
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

        self.checkBox_abertos.setChecked(False)
        self.checkBox_vazios.setChecked(False)

        self.groupBox_entrada.setChecked(False)
        self.groupBox_saida.setChecked(False)

        self.dateEdit_data_entrada1.setDate(QDate().currentDate())
        self.dateEdit_data_entrada2.setDate(QDate().currentDate())
        self.dateEdit_data_saida1.setDate(QDate().currentDate())
        self.dateEdit_data_saida2.setDate(QDate().currentDate())

    def get_mercadoria(self):
        mercadoria_id = self.lineEdit_mercadoria_id.text()
        if mercadoria_id is not None and mercadoria_id != '':
            filtro = str("id_mercadoria = $$" + str(mercadoria_id) + "$$"), \
                    "Mercadoria", str(self.lineEdit_mercadoria_id.text() + '-' + self.lineEdit_mercadoria.text())
            return filtro
        else:
            return '1=1', 'Mercadoria', 'Todos'

    def get_fornecedor(self):
        pessoa_documento = self.lineEdit_fornecedor_documento.text()
        if pessoa_documento is not None and pessoa_documento != '':
            return str("id_pessoa_entrada = $$" + str(pessoa_documento) + "$$"), \
                   "Fornecedor", str(self.lineEdit_fornecedor_documento.text() + ' - ' + self.lineEdit_fornecedor.text())
        else:
            return '1=1', 'Fornecedor', 'Todos'

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

    def get_entrada(self) :
        return self.get_periodo(
                groupBox=self.groupBox_entrada
                , dateEdit_inicio=self.dateEdit_data_entrada1
                , dateEdit_fim=self.dateEdit_data_entrada2
                , campo="data_cadastro"
                , descricao='Entrada'
        )

    def get_saida(self) :
        return self.get_periodo(
                groupBox=self.groupBox_saida
                , dateEdit_inicio=self.dateEdit_data_saida1
                , dateEdit_fim=self.dateEdit_data_saida2
                , campo="data_retirada"
                , descricao="Saída"
        )

    def get_classificacao(self):
        filtro = ''
        cabecalho = ''

        if self.checkBox_mercadoria.isChecked():
            filtro = filtro + "UPPER(tipo_mercadoria) = $$MERCADORIA$$"
            cabecalho = cabecalho + "Mercadoria, "

        if self.checkBox_insumo.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + "UPPER(tipo_mercadoria) = $$INSUMO$$"
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + "Insumo"

        if self.checkBox_casco.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + "UPPER(tipo_mercadoria) = $$CASCO$$"
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + "Casco"

        if ((self.checkBox_insumo.isChecked()
                and self.checkBox_mercadoria.isChecked()
                and self.checkBox_casco.isChecked())
                or (not self.checkBox_mercadoria.isChecked()
                    and not self.checkBox_casco.isChecked()
                    and not self.checkBox_insumo.isChecked())):
            cabecalho = "Mercadoria, Insumo, Casco"

        filtro = "(" + filtro + ")" if filtro != '' else filtro
        return filtro, "Classificação", cabecalho

    def get_estoque(self):
        filtro = ''
        cabecalho = ''

        if self.checkBox_abertos.isChecked():
            filtro = filtro + "aberto = true::boolean"
            cabecalho = cabecalho + "Itens abertos"

        if not self.checkBox_vazios.isChecked():
            filtro = filtro + " and " if filtro != '' else filtro
            filtro = filtro + "quantidade_item > 0::integer"

        else:
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + "Itens vazios"

        if not self.checkBox_inativos.isChecked():
            filtro = filtro + " and " if filtro != '' else filtro
            filtro = filtro + "ativo = true::boolean"
        else:
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + "Itens inativos"
        return filtro, 'Estoque', cabecalho


