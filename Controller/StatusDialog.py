import logging

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Ui_StatusDialog import Ui_StatusDialog


class StatusDialog(QDialog, Ui_StatusDialog):

    def __init__(self, status='ERRO'):
        super().__init__()
        self.setupUi(self)

        # todo: definir características de cada tipo de alerta
        if status == 'ERRO':
            pass

        elif status == 'AVISO':
            self.label_mensagem.setAlignment(Qt.AlignCenter)
            self.textBrowser_exception.setVisible(False)
            pass

        elif status == 'OK':
            self.label_mensagem.setAlignment(Qt.AlignCenter)
            self.textBrowser_exception.setVisible(False)

        else:
            logging.debug("O valor <" + status + "> não é um status válido para StatusDialog\n")

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_clicked)

    def definir_mensagem(self, mensagem, json_exception):
        # todo: configurar mensagem para aparecer no dialogo
        # Tratar esse formato de json '{"erro": "Não foi possível executar a operacao.","metodo": "%","retorno": "%","parametros": "%","requisicao_id": "%"}'

        #json_mensagem = '{"erro": "Não foi possível executar a operacao.","metodo": "%","retorno": "%","parametros": "%","requisicao_id": "%"}'

        logging.info(mensagem)
        logging.debug(json_exception)

        #self.label_mensagem.setText(mensagem)
        #self.textEdit_exception.setText('\n' + exception["erro"] + '\n' + exception["metodo"] + '\n' + exception["parametros"] + '\n' + exception["retorno"] + '\n' + str(exception))

    def close_clicked(self):
        self.close()
