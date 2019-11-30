import os

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from View.Componentes.Ui_FiltroRemanufatura import Ui_FiltroRemanufatura


class FiltroRemanufatura(QDialog, Ui_FiltroRemanufatura):

    def __init__(self, db=None, parent=None, **kwargs):
        super(FiltroRemanufatura, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        filtro_padrao = kwargs.get('filtro_padrao')

        self.metodos = (
            self.get_cadastro
            , self.get_realizacao
            , self.get_casco
            , self.get_cliente
            , self.get_situacao
            , self.get_cor
        )

        find_icon = QIcon(os.path.join('Resources', 'icons', 'search.png'))
        self.toolButton_mercadoria.setIcon(find_icon)
        self.toolButton_cliente.setIcon(find_icon)

        self.dados = None

        self.toolButton_cliente.clicked.connect(
            lambda: filtro_padrao.busca_registro(
                "vw_pessoa_fornecedor"
                , "id_pessoa"
                , self.lineEdit_cliente_documento
                , "nome"
                , self.lineEdit_cliente
                , {
                    "id_pessoa": 'ID',
                    "nome": 'Nome',
                    'documento': "Documento"
                }
                , force=True
            )
        )

        self.toolButton_mercadoria.clicked.connect(
            lambda: filtro_padrao.busca_registro(
                "vw_casco"
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

        self.lineEdit_cliente_documento.editingFinished.connect(
            lambda: filtro_padrao.busca_registro(
                "vw_pessoa_fornecedor"
                , "id_pessoa"
                , self.lineEdit_cliente_documento
                , "nome"
                , self.lineEdit_cliente
                , {
                    "id_pessoa": 'ID',
                    "nome": 'Nome',
                    'documento': "Documento"
                }

            )
        )

        self.lineEdit_mercadoria_id.editingFinished.connect(
            lambda: filtro_padrao.busca_registro(
                "vw_casco"
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
        self.lineEdit_mercadoria_id.clear()
        self.lineEdit_mercadoria.clear()
        self.lineEdit_cliente.clear()
        self.lineEdit_cliente_documento.clear()

        self.checkBox_cadastrada.setChecked(False)
        self.checkBox_realizada.setChecked(False)
        self.checkBox_encerrada.setChecked(False)

        self.checkBox_colorido.setChecked(False)
        self.checkBox_PB.setChecked(False)

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
            groupBox=self.groupBox_cadastro
            , dateEdit_fim=self.dateEdit_data_entrada1
            , dateEdit_inicio=self.dateEdit_data_entrada2
            , campo="data_cadastro"
            , descricao="Cadastro"
        )

    def get_realizacao(self):
        return self.get_periodo(
            groupBox=self.groupBox_realizada
            , dateEdit_fim=self.dateEdit_data_saida1
            , dateEdit_inicio=self.dateEdit_data_saida2
            , campo="data_realizada"
            , descricao="Realizada"
        )

    def get_casco(self):
        casco_id = self.lineEdit_mercadoria_id.text()
        if casco_id is not None and casco_id != '':
            return str("id_mercadoria_casco = $$" + str(casco_id) + "$$")
        else:
            return '1=1', 'Casco', 'Todos'

    def get_cliente(self):
        pessoa_documento = self.lineEdit_cliente_documento.text()
        if pessoa_documento is not None and pessoa_documento != '':
            filtro = str("id_pessoa = $$" + str(pessoa_documento) + "$$")
            return filtro, "Cliente", str(pessoa_documento) + ' - ' + self.lineEdit_cliente.text()
        else:
            return '1=1', 'Cliente', 'Todos'

    def get_situacao(self):
        filtro = ''
        cabecalho = ''
        if self.checkBox_cadastrada.isChecked() \
                and self.checkBox_realizada.isChecked() \
                and self.checkBox_encerrada.isChecked():
            return filtro, "Situação", "Todas"

        if self.checkBox_cadastrada.isChecked():
            filtro = 'UPPER(situacao_remanufatura) = UPPER($$CADASTRADA$$)'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = 'Cadastradas'

        if self.checkBox_realizada.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'UPPER(situacao_remanufatura) = UPPER($$REALIZADA$$)'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + 'Realizadas'

        if self.checkBox_encerrada.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'UPPER(situacao_remanufatura) = UPPER($$ENCERRADA$$)'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + 'Encerradas'

        return filtro, "Situação", cabecalho

    def get_cor(self):
        filtro = ''
        cabecalho = ''
        if self.checkBox_colorido.isChecked() \
                and self.checkBox_PB.isChecked():
            return filtro, "Cor", "Colorido, Preto"

        if self.checkBox_PB.isChecked():
            filtro = 'colorido = false::boolean'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + "Preto"

        if self.checkBox_colorido.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'colorido = true::boolean'
            cabecalho = cabecalho + ",  " if cabecalho != '' else cabecalho
            cabecalho = cabecalho + "Colorido"

        return filtro, "Cor", cabecalho

