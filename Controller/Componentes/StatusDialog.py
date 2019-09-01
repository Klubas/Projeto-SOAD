import logging

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_StatusDialog import Ui_StatusDialog


class StatusDialog(QDialog, Ui_StatusDialog):

    def __init__(self, status='ERRO', mensagem='', exception=''):
        super().__init__()
        self.setupUi(self)

        # todo: definir características de cada tipo de alerta
        if status == 'ERRO':
            self.setWindowTitle("Mensagem de Erro")
            self.groupBox_mensagem.setVisible(True)

        elif status == 'ALERTA':
            self.setWindowTitle("Mensagem de Alerta")
            self.label_mensagem.setAlignment(Qt.AlignCenter)
            self.setMinimumHeight(200)
            self.setMaximumHeight(200)
            self.groupBox_mensagem.setVisible(False)

        elif status == 'OK':
            self.setWindowTitle("Mensagem de Confirmação")
            self.label_mensagem.setAlignment(Qt.AlignCenter)
            self.setMinimumHeight(200)
            self.setMaximumHeight(200)
            self.groupBox_mensagem.setVisible(False)

        else:
            self.definir_mensagem("O valor " + status + " não é um status válido para StatusDialog\n")
            logging.debug("O valor " + status + " não é um status válido para StatusDialog\n")
            self.exec()

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_clicked)

        self.definir_mensagem(mensagem, exception)

    def definir_mensagem(self, mensagem='', json_exception=''):
        # todo: configurar mensagem para aparecer no dialogo
        # Tratar esse formato de json '{"erro": "Não foi possível executar a operacao.","metodo": "%","retorno": "%","parametros": "%","requisicao_id": "%"}'

        #json_mensagem = '{"erro": "Não foi possível executar a operacao.","metodo": "%","retorno": "%","parametros": "%","requisicao_id": "%"}'

        logging.info(mensagem)
        logging.debug(json_exception)

        self.label_mensagem.setText(mensagem)

        self.textBrowser_exception.setText(
            str(mensagem) + '\n\n' + str(json_exception)
        )

        #self.textEdit_exception.setText('\n' + exception["erro"] + '\n' + exception["metodo"] + '\n' + exception["parametros"] + '\n' + exception["retorno"] + '\n' + str(exception))

    def close_clicked(self):
        self.close()
