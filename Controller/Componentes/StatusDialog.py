import logging
import os

from PySide2.QtCore import QSize
from PySide2.QtGui import QImage, QPixmap, QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from View.Componentes.Ui_StatusDialog import Ui_StatusDialog


class StatusDialog(QDialog, Ui_StatusDialog):

    def __init__(self, status='ERRO', mensagem='', exception=None, parent=None):
        super(StatusDialog, self).__init__(parent)
        self.setupUi(self)

        status = status.upper()

        icon_path = os.path.join("Resources", "icons", status.lower() + ".png")
        self.setWindowIcon(QIcon(icon_path))

        icone = QImage(icon_path).smoothScaled(60, 60)
        self.label_imagem.setPixmap(QPixmap.fromImage(icone))

        self.toolButton_detalhes.clicked.connect(
            lambda: self.groupBox_mensagem.setVisible(
                self.toolButton_detalhes.isChecked())
        )

        self.groupBox_mensagem.setVisible(False)

        min_size = QSize(300, 150) # h, w

        # todo: definir características de cada tipo de alerta
        if status == 'ERRO':
            self.setWindowTitle("Mensagem de Erro")
            self.toolButton_detalhes.setVisible(True)
            min_size = QSize(200, 200)

        elif status == 'ALERTA':
            self.setWindowTitle("Mensagem de Alerta")
            self.toolButton_detalhes.setVisible(True)
            min_size = QSize(150, 200)

        elif status == 'OK':
            self.setWindowTitle("Mensagem de Confirmação")
            self.toolButton_detalhes.setVisible(False)
            min_size = QSize(90, 200)

        else:
            self.__definir_mensagem__("O valor " + status + " não é um status válido para StatusDialog\n")
            logging.debug("[StatusDialog] O valor " + status + " não é um status válido para StatusDialog\n")
            self.exec()

        max_size = QSize(
            int(min_size.height()*2), min_size.width()*2)

        self.setMinimumSize(min_size)
        #self.setMaximumSize(max_size)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.close_clicked)

        self.__definir_mensagem__(mensagem, exception)

    def __definir_mensagem__(self, mensagem='', exception=None):

        logging.info('[StatusDialog] status_msg=' + str(mensagem))
        logging.debug('[StatusDialog] status_exception=' + str(exception))

        string_exception = ''
        string_mensagem = mensagem + '\n\n'

        print('exception=' + str(type(exception)))
        if type(exception) == tuple:
            for i in range(0, len(exception)):
                print('exception[' + str(i) + ']=' + str(type(exception[i])))

            if type(exception[1]) == list:
                if len(exception[1]) == 1:
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
                print('AQUI')

            if len(exception) == 3:
                string_exception = string_exception + 'SQL:\n' + str(exception[2])

        elif exception is None:
            string_exception = string_mensagem + string_exception
            self.groupBox_mensagem.setVisible(False)

        else:
            string_exception = string_exception + str(exception)
            logging.debug('[StatusDialog] Tipo de mensagem não tratado.')

        self.label_mensagem.setText(string_mensagem)
        self.textBrowser_exception.setText(string_exception)

    def close_clicked(self):
        self.close()
