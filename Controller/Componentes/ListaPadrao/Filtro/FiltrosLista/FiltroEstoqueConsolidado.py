import logging
import os

from PySide2.QtCore import QDate
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from Controller.Componentes.LocalizarDialog import LocalizarDialog
from View.Componentes.Ui_FiltroEstoqueConsolidado import Ui_FiltroEstoqueConsolidado


class FiltroEstoqueConsolidado(QDialog, Ui_FiltroEstoqueConsolidado):
    """
    Fazer mapeamento dos campos
    nome_campo - nome_coluna - sinal
    "nome_coluna": (campo, sinal)
    """

    def __init__(self, db=None, parent=None, **kwargs):
        super(FiltroEstoqueConsolidado, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        filtro_padrao = kwargs.get('filtro_padrao')

        self.metodos = (
            self.get_mercadoria
            , self.get_fornecedor
            , self.get_classificacao
            , self.get_estoque
            , self.get_data_base
        )

        find_icon = QIcon(os.path.join('Resources', 'icons', 'search.png'))
        self.toolButton_fornecedor.setIcon(find_icon)
        self.toolButton_mercadoria.setIcon(find_icon)

        help = '''Escolha uma data para ver como estava o estoque'''
        self.adiciona_help(help)

        self.dados = None

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

    def adiciona_help(self, texto="Teste ToolButton", layout=None):
        from PySide2.QtWidgets import QToolButton
        self.toolButton_help = QToolButton(self.horizontalLayout_data_base.widget())
        self.toolButton_help.setToolTipDuration(5000)
        self.toolButton_help.setText("?")
        self.toolButton_help.setToolTip(texto)
        self.toolButton_help.setStyleSheet("background: rgb(38, 183, 212);\n"
                                      "color: white;\n"
                                      "border: 10px;\n"
                                      "border-radius: 5px;")
        self.toolButton_help.setObjectName("toolButton_help")
        self.horizontalLayout_data_base.addWidget(self.toolButton_help)

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

    def get_data_base(self):
        if not self.groupBox_data_base.isChecked():
            self.dateEdit_data_base.setDate(QDate().currentDate())
        data_base = self.dateEdit_data_base.date().toString("dd.MM.yyyy").replace('.', '/')

        filtro = str('''
            data_cadastro::date <= $${data_base}$$::date
            AND(data_retirada::date > $${data_base}$$::date or data_retirada is null)
            '''.format(data_base=data_base))

        return filtro, "Data base", data_base

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
        if not self.checkBox_inativos.isChecked():
            filtro = filtro + " and " if filtro != '' else filtro
            filtro = filtro + "ativo = true::boolean"
        else:
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + "Itens inativos"
        return filtro, 'Estoque', cabecalho



