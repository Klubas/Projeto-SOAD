import logging

from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Ui_StatusDialog import Ui_StatusDialog


class StatusDialog(QDialog, Ui_StatusDialog):

    def __init__(self, status='ERRO'):
        super().__init__()
        self.setupUi(self)

        if status == 'ERRO':
            pass

        elif status == 'AVISO':
            pass

        elif status == 'OK':
            pass

        else:
            logging.debug("O valor <" + status + "> não é um status válido para StatusDialog\n")

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_clicked)

    def definir_mensagem(self, mensagem, exception):
        logging.info(mensagem)
        logging.debug(exception)
        self.label.setText(mensagem)

    def close_clicked(self):
        self.close()
