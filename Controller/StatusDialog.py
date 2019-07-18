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

    def definir_mensagem(self, mensagem, exception):
        # todo: configurar mensagem para aparecer no dialogo
        logging.info(mensagem)
        logging.debug(exception)
        self.label_mensagem.setText(mensagem)
        self.textBrowser_exception.setText(str(exception))

    def close_clicked(self):
        self.close()
