import logging
import os

from PySide2.QtCore import QSize
from PySide2.QtGui import QImage, QPixmap, QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_StatusDialog import Ui_StatusDialog


class StatusDialog(QDialog, Ui_StatusDialog):

    def __init__(self, status='ERRO', mensagem='', exception=None, parent=None, esconder_detalhes=False):
        super(StatusDialog, self).__init__(parent)
        self.setupUi(self)
        self.status = status

        self.__definir_mensagem__(mensagem, exception)
        self.definir_tipo(self.status)

        self.min_size = QSize(650, 230)
        self.resize(self.min_size)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_clicked)

        if esconder_detalhes:
            self.toolButton_detalhes.setVisible(False)

    def definir_tipo(self, status):
        status = status.upper()

        icon_path = os.path.join("Resources", "icons", status.lower() + ".png")
        self.setWindowIcon(QIcon(icon_path))

        icone = QImage(icon_path).smoothScaled(60, 60)
        self.label_imagem.setPixmap(QPixmap.fromImage(icone))

        self.toolButton_detalhes.clicked.connect(self.mostrar_detalhes)

        self.groupBox_mensagem.setVisible(False)

        if status == 'ERRO':
            self.setWindowTitle("Mensagem de Erro")
            self.toolButton_detalhes.setVisible(True)

        elif status == 'ALERTA':
            self.setWindowTitle("Mensagem de Alerta")
            self.toolButton_detalhes.setVisible(True)

        elif status == 'OK':
            self.setWindowTitle("Mensagem de Confirmação")
            self.toolButton_detalhes.setVisible(False)

        else:
            self.__definir_mensagem__("O valor " + status + " não é um status válido para StatusDialog\n")
            logging.debug("[StatusDialog] O valor " + status + " não é um status válido para StatusDialog\n")
            self.exec()

    def __definir_mensagem__(self, mensagem='', exception=None):

        logging.info('[StatusDialog] status_msg=' + str(mensagem))
        logging.debug('[StatusDialog] status_exception=' + str(exception))

        string_exception = ''
        string_mensagem = mensagem + '\n\n'

        print('exception=' + str(type(exception)))
        if isinstance(exception, tuple):
            for i in range(0, len(exception)):
                print('exception[' + str(i) + ']=' + str(type(exception[i])))

            if isinstance(exception[1], list):

                if len(exception[1]) == 1:

                    if isinstance(exception[1][0], dict):
                        string_exception = string_exception + str(exception[1])
                    else:

                        print('exception[1][0]=' + str(type(exception[1][0])))

                        aux = str(exception[1][0]).split('CONTEXT:')

                        string_mensagem = string_mensagem + str(aux[0])

                        if len(aux) == 2:
                            string_exception = string_exception + str(aux[0]) \
                                           + '\nCONTEXT:\n' + str(aux[1])
                        elif len(aux) == 1:
                            string_exception = string_exception + str(aux[0])
                        else:
                            string_exception = string_exception + str(aux)
                else:
                    string_exception = string_exception + str(exception[1])

                string_exception = string_exception + '\n\n'

            else:
                print(exception[0])

            if len(exception) == 3:
                string_exception = string_exception + 'SQL:\n' + str(exception[2])

            self.status = 'ALERTA' if self.status != 'OK' else 'OK'

        elif isinstance(exception, str):
            string_exception = string_exception + str(exception)

        elif exception is None:
            string_exception = string_mensagem + string_exception
            self.groupBox_mensagem.setVisible(False)

        else:
            self.status = 'ERRO'
            string_exception = string_exception + str(exception)
            logging.debug('[StatusDialog] Tipo de mensagem não tratado.')

        self.label_mensagem.setText(string_mensagem.replace('P0001', ''))
        self.textBrowser_exception.setText(string_exception)

    def mostrar_detalhes(self):

        if self.toolButton_detalhes.isChecked():
            self.groupBox_mensagem.setVisible(True)

        else:
            self.resize(self.min_size)
            self.groupBox_mensagem.setVisible(False)

    def close_clicked(self):
        self.accept()
