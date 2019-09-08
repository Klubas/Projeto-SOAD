import logging

from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_StatusDialog import Ui_StatusDialog


class StatusDialog(QDialog, Ui_StatusDialog):

    def __init__(self, status='ERRO', mensagem='', exception=None, parent=None):
        super(StatusDialog, self).__init__(parent)
        self.setupUi(self)

        min_size = QSize(400, 150) # h, w

        # todo: definir características de cada tipo de alerta
        if status == 'ERRO':
            self.setWindowTitle("Mensagem de Erro")
            self.groupBox_mensagem.setVisible(True)
            min_size = QSize(250, 500)

        elif status == 'ALERTA':
            self.setWindowTitle("Mensagem de Alerta")
            self.label_mensagem.setAlignment(Qt.AlignCenter)
            self.groupBox_mensagem.setVisible(False)
            min_size = QSize(400, 150)

        elif status == 'OK':
            self.setWindowTitle("Mensagem de Confirmação")
            self.label_mensagem.setAlignment(Qt.AlignCenter)
            self.groupBox_mensagem.setVisible(False)
            min_size = QSize(150, 300)

        else:
            self.__definir_mensagem__("O valor " + status + " não é um status válido para StatusDialog\n")
            logging.debug("[StatusDialog] O valor " + status + " não é um status válido para StatusDialog\n")
            self.exec()

        max_size = QSize(min_size.height()*2, min_size.width()*2)

        self.setMinimumSize(min_size)
        self.setMaximumSize(max_size)
        self.setSizePolicy

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_clicked)

        self.__definir_mensagem__(mensagem, exception)

    def __definir_mensagem__(self, mensagem='', exception=None):

        logging.info('[StatusDialog] status_msg=' + str(mensagem))
        logging.debug('[StatusDialog] status_exception=' + str(exception))

        string_exception = ''
        string_mensagem = mensagem + '\n\n'

        print('exception=' + str(type(exception)))
        if type(exception) == tuple:
            print('exception[0]=' + str(type(exception[0])))
            print('exception[1]=' + str(type(exception[1])))
            print('exception[2]=' + str(type(exception[2])))

            if type(exception[1]) == list:
                if len(exception[1]) == 1:
                    print('exception[1][0]=' + str(type(exception[1][0])))

                    aux = str(exception[1][0]).split('CONTEXT:')

                    string_mensagem = string_mensagem + str(aux[0])

                    string_exception = string_exception + str(aux[0]) \
                                       + '\nCONTEXT:\n' + str(aux[1])

                else:
                    string_exception = string_exception + str(exception[1])

                string_exception = string_exception + '\n\n'

            if len(exception) == 3:
                string_exception = string_exception + 'SQL:\n' + str(exception[2])

        elif exception is None:
            pass

        else:
            string_exception = str(exception)
            logging.debug('[StatusDialog] Tipo de mensagem não tratado.')

        self.label_mensagem.setText(string_mensagem)
        self.textBrowser_exception.setText(string_exception)

    def close_clicked(self):
        self.close()
