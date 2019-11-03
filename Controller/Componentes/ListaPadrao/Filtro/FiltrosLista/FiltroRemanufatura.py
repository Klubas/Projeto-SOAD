import logging

from PySide2.QtWidgets import QDialog

from Controller.Componentes.LocalizarDialog import LocalizarDialog
from View.Componentes.Ui_FiltroRemanufatura import Ui_FiltroRemanufatura


class FiltroRemanufatura(QDialog, Ui_FiltroRemanufatura):

    def __init__(self, db=None, parent=None):
        super(FiltroRemanufatura, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        self.metodos = (
            self.get_cadastro
            , self.get_realizacao
            , self.get_casco
            , self.get_cliente
            , self.get_situacao
            , self.get_cor
        )

        self.dados = None

        self.lineEdit_cliente_documento.editingFinished.connect(
            lambda: self.busca_registro(
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
            lambda: self.busca_registro(
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

    def get_periodo(self, groupBox, dateEdit_inicio, dateEdit_fim, campo) -> str:
        if groupBox.isChecked():
            data_inicio = dateEdit_inicio.date().toString("dd.MM.yyyy").replace('.', '/')
            data_fim = dateEdit_fim.date().toString("dd.MM.yyyy").replace('.', '/')
            return str("(" + campo + " >= $$" + str(data_inicio) + "$$" + " and " + campo + " <= $$" + str(data_fim) + "$$) or " + campo + " is null")
        else:
            return ''

    def get_cadastro(self):
        return self.get_periodo(
            groupBox=self.groupBox_cadastro
            , dateEdit_fim=self.dateEdit_data_entrada1
            , dateEdit_inicio=self.dateEdit_data_entrada2
            , campo="data_cadastro"
        )

    def get_realizacao(self):
        return self.get_periodo(
            groupBox=self.groupBox_realizada
            , dateEdit_fim=self.dateEdit_data_saida1
            , dateEdit_inicio=self.dateEdit_data_saida2
            , campo="data_realizada"
        )

    def get_casco(self):
        casco_id = self.lineEdit_mercadoria_id.text()
        if casco_id is not None and casco_id != '':
            return str("id_casco = $$" + str(casco_id) + "$$")
        else:
            return ''

    def get_cliente(self):
        pessoa_documento = self.lineEdit_cliente_documento.text()
        if pessoa_documento is not None and pessoa_documento != '':
            return str("id_pessoa = $$" + str(pessoa_documento) + "$$")
        else:
            return ''

    def get_situacao(self):
        filtro = ''

        if self.checkBox_cadastrada.isChecked() \
                and self.checkBox_realizada.isChecked() \
                and self.checkBox_encerrada.isChecked():
            return filtro

        if self.checkBox_cadastrada.isChecked():
            filtro = 'UPPER(situacao_remanufatura) = UPPER($$CADASTRADA$$)'

        if self.checkBox_realizada.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'UPPER(situacao_remanufatura) = UPPER($$REALIZADA$$)'

        if self.checkBox_encerrada.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'UPPER(situacao_remanufatura) = UPPER($$ENCERRADA$$)'

        return filtro

    def get_cor(self):
        filtro = ''
        if self.checkBox_colorido.isChecked() \
                and self.checkBox_PB.isChecked():
            return filtro

        if self.checkBox_PB.isChecked():
            filtro = 'colorido = false::boolean'

        if self.checkBox_colorido.isChecked():
            filtro = filtro + " or " if filtro != '' else filtro
            filtro = filtro + 'colorido = true::boolean'

        return filtro

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
