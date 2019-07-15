# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\LoginDialog.ui'
#
# Created: Mon Jul 15 07:35:42 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(317, 196)
        self.verticalLayoutWidget = QtWidgets.QWidget(LoginDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 281, 176))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget_servidor = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.verticalWidget_servidor.setObjectName("verticalWidget_servidor")
        self.verticalLayout_servidor = QtWidgets.QVBoxLayout(self.verticalWidget_servidor)
        self.verticalLayout_servidor.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_servidor.setObjectName("verticalLayout_servidor")
        self.label_servidor = QtWidgets.QLabel(self.verticalWidget_servidor)
        self.label_servidor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_servidor.setObjectName("label_servidor")
        self.verticalLayout_servidor.addWidget(self.label_servidor)
        self.comboBox_servidor = QtWidgets.QComboBox(self.verticalWidget_servidor)
        self.comboBox_servidor.setObjectName("comboBox_servidor")
        self.verticalLayout_servidor.addWidget(self.comboBox_servidor)
        self.verticalLayout.addWidget(self.verticalWidget_servidor)
        self.verticalWidget_login = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.verticalWidget_login.setObjectName("verticalWidget_login")
        self.verticalLayout_login = QtWidgets.QVBoxLayout(self.verticalWidget_login)
        self.verticalLayout_login.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_login.setObjectName("verticalLayout_login")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_login.addItem(spacerItem)
        self.label_usuario = QtWidgets.QLabel(self.verticalWidget_login)
        self.label_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.label_usuario.setObjectName("label_usuario")
        self.verticalLayout_login.addWidget(self.label_usuario)
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.verticalWidget_login)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.verticalLayout_login.addWidget(self.lineEdit_usuario)
        self.label_senha = QtWidgets.QLabel(self.verticalWidget_login)
        self.label_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.label_senha.setObjectName("label_senha")
        self.verticalLayout_login.addWidget(self.label_senha)
        self.lineEdit_senha = QtWidgets.QLineEdit(self.verticalWidget_login)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.verticalLayout_login.addWidget(self.lineEdit_senha)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_login.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalWidget_login)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_login.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.verticalWidget_login)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtWidgets.QApplication.translate("LoginDialog", "SOAD - Login", None, -1))
        self.label_servidor.setText(QtWidgets.QApplication.translate("LoginDialog", "Servidor", None, -1))
        self.label_usuario.setText(QtWidgets.QApplication.translate("LoginDialog", "Usuário", None, -1))
        self.label_senha.setText(QtWidgets.QApplication.translate("LoginDialog", "Senha", None, -1))

