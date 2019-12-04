import logging, os

from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QRegExpValidator, QIcon
from PySide2.QtWidgets import QWidget, QDialogButtonBox

from Controller.Componentes.StatusDialog import StatusDialog
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.ListaPadrao.ListaPadrao import ListaPadrao
from Controller.Componentes.CadastroPadrao import CadastroPadrao
from View.Ui_AjusteEstoque import Ui_AjusteEstoque


class AjusteEstoque(CadastroPadrao, Ui_AjusteEstoque):
    def __init__(self, db=None, window_list=None, parent=None, **kwargs):
        super(AjusteEstoque, self).__init__(parent=parent, **kwargs)
        self.setupUi(self)
        self.db = db
        self.window_list = window_list
        self.setWindowFlags(Qt.Dialog)

        self.buttonBox_confirmar.button(QDialogButtonBox.Ok).clicked.connect(self.confirmar_ajuste)
        self.buttonBox_confirmar.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelar)

        self.buttonBox_confirmar.button(QDialogButtonBox.Ok).setText("Confirmar")
        self.buttonBox_confirmar.button(QDialogButtonBox.Cancel).setText("Cancelar")

        self.pushButton_historico.clicked.connect(self.abrir_historico)

        validador_regex_id = QRegExpValidator(QRegExp("[0-9]{1,9}"))
        self.lineEdit_mercadoria_id.setValidator(validador_regex_id)

        self.lineEdit_mercadoria_id.editingFinished.connect(self.busca_mercadoria)
        self.toolButton_mercadoria.clicked.connect(lambda: self.busca_mercadoria(force=True))

        self.dialog_localizar = LocalizarDialog(db=self.db, parent=self)

        self.lineEdit_mercadoria_id.setStyleSheet("\nborder: 0.5px solid red")

        find_icon = QIcon(os.path.join('Resources', 'icons', 'search.png'))
        self.toolButton_mercadoria.setIcon(find_icon)
        clock_icon = QIcon(os.path.join('Resources', 'icons', 'clock.png'))
        self.pushButton_historico.setIcon(clock_icon)

        self.spinBox_quantidade.setRange(1, 999)

        help=\
'''Aqui é possível realizar lançamentos de entrada/saída, de forma manual,
para operações que ocorrem sem um pedido.

ENTRADA: Serão adicionados itens sem vínculo com pedido de entrada.
SAÍDA: Apenas itens fechados podem ser retirados do estoque.'''

        self.adiciona_help(texto=help)

        self.show()

    def confirmar_ajuste(self):

        close = False

        if self.textEdit_motivo.text() != '' \
                and self.spinBox_quantidade.text() != '0' \
                and self.lineEdit_mercadoria_id.text() != '':

            dialog = ConfirmDialog(parent=self)
            dialog.definir_mensagem('Tem certeza que deseja realizar esse ajuste?')

            if not dialog.exec():
                return

            oper = self.comboBox_operacao.currentText().replace('í', 'i')

            dados = {
                "metodo": "fnc_ajuste_estoque"
                , "schema": "soad"
                , "params": {
                    "mercadoria_id": str(self.lineEdit_mercadoria_id.text())
                    , "tipo": oper
                    , "quantidade": self.spinBox_quantidade.text()
                    , "motivo": self.textEdit_motivo.text()
                }
            }

            retorno = self.db.call_procedure(params=dados)
            status = 'ERRO'
            mensagem = ''

            if retorno[0]:
                status = retorno[1][0]['p_retorno_json']['status']

                if status:
                    status = 'OK'
                    mensagem = '[{oper}] Operação realizada com sucesso.'\
                        .format(oper=oper.upper())
                    close = True

                else:
                    status = 'ALERTA'
                    mensagem = '[{oper}] Não foi possível realizar a operação.'\
                        .format(oper=oper.upper())

        else:

            status = 'ALERTA'
            mensagem = 'Erro não tratado.'

            if self.lineEdit_mercadoria_id.text() == '':
                mensagem = 'É necessário informar uma mercadoria.'

            elif self.spinBox_quantidade.text() == '0':
                mensagem = "A quantidade não pode ser 0 (zero)."

            elif self.textEdit_motivo.text() == '':
                mensagem = "É necessário informar um motivo."

            retorno = mensagem

        dialog = StatusDialog(
            status=status
            , mensagem=mensagem
            , exception=retorno
            , parent=self
        )

        dialog.exec()

        self.limpar_campos() if close else None

    def cancelar(self):
        self.close()

    def limpar_campos(self):
        self.lineEdit_mercadoria_id.clear()
        self.lineEdit_mercadoria.clear()
        self.textEdit_motivo.clear()
        self.spinBox_quantidade.setValue(
            self.spinBox_quantidade.minimum()
        )

    def busca_mercadoria(self, force=False):
        mercadoria = None
        filtro_adicional = ''

        tipo = 'MERCADORIA'
        tabela = 'vw_mercadoria'
        campo = 'id_mercadoria'
        lineEdit_id = self.lineEdit_mercadoria_id
        lineEdit_descricao = self.lineEdit_mercadoria

        valor = lineEdit_id.text().replace(' ', '')

        if valor != '':

            mercadoria = self.db.busca_registro(
                tabela, campo, valor, '=', filtro=filtro_adicional)[1][0]['fnc_buscar_registro']

            logging.debug('[CadastroPedido] ' + str(mercadoria))
            if mercadoria is not None:
                mercadoria = mercadoria[0]
        else:
            lineEdit_descricao.clear()

        if mercadoria is None or force:

            localizar_campos = {
                campo: 'ID',
                "codigo": 'Código',
                "descricao": tipo.capitalize(),
                'marca': "Marca"
            }

            colunas_busca = {
                campo: 'ID',
                "codigo": 'Código',
                "descricao": tipo.capitalize(),
                'marca': "Marca"
            }

            self.dialog_localizar.define_tabela(tabela)
            self.dialog_localizar.define_campos(localizar_campos)
            self.dialog_localizar.define_colunas(colunas_busca)
            self.dialog_localizar.filtro = filtro_adicional

            self.dialog_localizar.define_valor_padrao(localizar_campos["descricao"], '') if force \
                else self.dialog_localizar.define_valor_padrao(localizar_campos[campo], lineEdit_id.text())

            mercadoria_id = self.dialog_localizar.exec()
            mercadoria = self.db.busca_registro(
                tabela, campo, str(mercadoria_id), '=')[1][0]['fnc_buscar_registro']

            if mercadoria_id == 0:
                return

            if mercadoria is not None:
                mercadoria = mercadoria[0]

        if mercadoria is not None:
            lineEdit_id.setText(str(mercadoria[campo]))
            lineEdit_descricao.setText(mercadoria['descricao'])
            return True

        else:
            lineEdit_id.clear()
            lineEdit_descricao.clear()
            return False

    def abrir_historico(self):

        lista = ListaPadrao(
            db=self.db
            , window_list=self.window_list
            , tipo='INVENTARIO'
            , parent=self
        )

        self.hide()

    def closeEvent(self, event):
        self.window_list.remove(self)
        event.accept()
