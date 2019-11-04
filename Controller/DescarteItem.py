import logging

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QDialogButtonBox

from Controller.Componentes.StatusDialog import StatusDialog
from View.Ui_DescarteItems import Ui_DescarteItems


class DescarteItem(QWidget, Ui_DescarteItems):
    def __init__(self, db=None, window_list=None, parent=None, **kwargs):
        super(DescarteItem, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = db
        self.window_list = window_list
        self.setWindowFlags(Qt.Dialog)

        ids = kwargs.get('ids') \
            if "ids" in kwargs else None

        self.buttonBox_descartar.button(QDialogButtonBox.Ok).clicked.connect(self.confirma_descarte)
        self.buttonBox_descartar.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelar)

        self.buttonBox_descartar.button(QDialogButtonBox.Ok).setText("Confirmar Descarte")
        self.buttonBox_descartar.button(QDialogButtonBox.Cancel).setText("Cancelar Descarte")

        self.lista_ids = list()

        self.buscar_items(ids)
        self.show()

    def buscar_items(self, ids):
        items = list()
        print(ids)
        for item_id in ids:
            item = dict()
            try:
                retorno = self.db.busca_registro(
                    'vw_item_lote'
                    , 'id_item_lote'
                    , str(item_id)
                    , '=')
            except Exception as e:
                logging.debug('[DescarteItem] Exceção ao buscar items:\n> ' + str(e))
                return

            if retorno[0]:
                retorno = retorno[1][0]['fnc_buscar_registro'][0]
                print(retorno)
                item['id'] = retorno['id_item_lote']
                item['descricao'] = retorno['codigo_mercadoria'] + ' - ' + retorno['descricao']
                print(item)
                items.append(item)
                print(items)
                self.lista_ids.append(item["id"])
        print(items)
        self.posicionar_items(items)

    def posicionar_items(self, items):
        texto = ''
        for item in items:
            texto = texto + '''({item_id}) {descricao}\n'''.format(item_id=item['id'], descricao=item['descricao'])
        self.label_items.setText(texto)

    def realizar_descarte(self) -> tuple:

        sucesso = True
        msg_retorno = ''

        for item_id in self.lista_ids:

            dados = {
                "metodo": "fnc_descarte_item"
                , "schema": "soad"
                , "params": {
                    "item_lote_id": str(item_id)
                }
            }

            retorno = self.db.call_procedure(params=dados)

            if retorno[0]:
                retorno = retorno[1][0]['p_retorno_json']['status']
            sucesso = sucesso and retorno == 'OK'
            msg_retorno = msg_retorno + str(item_id) + ' - ' + str(retorno) + '\n'
        return sucesso, msg_retorno

    def confirma_descarte(self):
        if self.textEdit_motivo.text() == '':
            dialog = StatusDialog(
                status='ALERTA'
                , mensagem='É necessário informar um motivo.'
                , parent=self
            )
            dialog.exec()
            return
        else:

            status = self.realizar_descarte()

            if status[0]:
                dialog = StatusDialog(
                    status='OK'
                    , mensagem='Descarte realizado com sucesso!'
                    , parent=self
                )

            else:
                dialog = StatusDialog(
                    status='ALERTA'
                    , mensagem='Não foi possível descartar todas as mercadorias selecionadas!\n'
                    , exception=status[1]
                    , parent=self
                )
        if dialog.exec():
            self.close()

    def cancelar(self):
        self.close()

    def closeEvent(self, event):
        self.window_list.remove(self)
        try:
            self.parent().refresh(atualiza_filtro=False)
        except Exception as e:
            logging.debug('[DescarteItem] Exceção ao recarregar lista (parent)\n> ' + str(e))
        event.accept()
