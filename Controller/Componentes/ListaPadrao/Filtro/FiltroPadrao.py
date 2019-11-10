import logging
import os

from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from Controller.Componentes.LocalizarDialog import LocalizarDialog
from View.Componentes.Ui_FiltroPadrao import Ui_FiltroPadrao


class FiltroPadrao(QDialog, Ui_FiltroPadrao):

    string_filtro = Signal(tuple)

    def __init__(self, db, child=None, parent=None, **kwargs):
        super(FiltroPadrao, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.parent = parent

        self.setWindowIcon(QIcon(os.path.join('Resources', 'icons', 'filter.png')))

        self.child = child(db=self.db, parent=self.widget, filtro_padrao=self, **kwargs)
        self.child.setWindowFlags(Qt.Widget)
        self.child.move(0, 0)
        self.child.show()

        self.setMinimumHeight(self.child.height() + 60)
        self.setMinimumWidth(self.child.width() + 20)
        self.setMaximumHeight(self.child.height() + 60)
        self.setMaximumWidth(self.child.width() + 20)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirma)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancela)

        self.dialog_localizar = LocalizarDialog(db=self.db, parent=self)

        self.translate_ui()

        self.show()

    def montar_filtro(self) -> tuple:
        i = 0
        filtro = ''
        cabecalho = '<div class=filtros>'
        descricao = ''
        for metodo in self.child.metodos:
            valor = metodo()
            if isinstance(valor, tuple):
                valor_filtro = valor[0]
                if valor[2] != '':
                    cabecalho = \
                        cabecalho + \
                        '<span class=filtroLinha>' + \
                        '   <strong>' + valor[1] + ': </strong>' + valor[2] + \
                        '</span>'

            elif isinstance(valor, str):
                valor_filtro = valor

            else:
                break

            if valor_filtro != '':
                i = i + 1
                if i > 1:
                    filtro = filtro + " and "
                filtro = filtro + valor_filtro

        cabecalho = cabecalho + '</div>'
        logging.info('[FiltroPadrao] Filtro: ' + str(filtro))
        return filtro, cabecalho

    def confirma(self):
        filtro = self.montar_filtro()
        string_filtro = filtro[0]
        filtro_cabecalho = filtro[1]
        self.string_filtro.emit((string_filtro, filtro_cabecalho))
        self.parent.showMaximized()
        self.hide()
        self.done(0)

    def cancela(self):
        if self.parent.isVisible():
            self.hide()
        else:
            self.parent.close()
            self.close()

    def limpar_filtro(self):
        self.child.limpar_filtro()

    def translate_ui(self):
        self.buttonBox.button(QDialogButtonBox.Ok).setIcon(QIcon(os.path.join('Resources', 'icons', 'filter.png')))
        self.buttonBox.button(QDialogButtonBox.Ok).setText('Filtrar')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')

    def busca_registro(
            self, tabela, campo, lineEdit_id, campo_descricao, lineEdit_descricao, colunas_dict, force=False
    ):

        dialog_localizar = self.dialog_localizar

        registro = None
        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':

            registro = self.db.busca_registro(tabela, campo, valor, '=')[1][0]['fnc_buscar_registro']

            logging.debug('[FiltroEstoque] ' + str(registro))
            if registro is not None:
                registro = registro[0]

        else:
            if not force:
                return False

        if registro is None or force:

            localizar_campos = colunas_dict
            colunas_busca = colunas_dict

            dialog_localizar.define_tabela(tabela)
            dialog_localizar.define_campos(localizar_campos)
            dialog_localizar.define_colunas(colunas_busca)
            dialog_localizar.define_valor_padrao(localizar_campos[campo], lineEdit_id.text())

            valor = dialog_localizar.exec()

            if valor == 0:
                return False

            registro = self.db.busca_registro(tabela, campo, str(valor), '=')

            registro = registro[1][0]['fnc_buscar_registro']

            #dialog_localizar.retorno_dados.connect(self.get_dados_localizar)

            if registro is not None:
                registro = registro[0]

        if registro is not None:
            lineEdit_id.setText(str(registro[campo]))
            lineEdit_descricao.setText(registro[campo_descricao])
            return True

        else:
            lineEdit_id.clear()
            lineEdit_descricao.clear()
            return False

    def get_dados_localizar(self, dados):
        self.child.dados = dados