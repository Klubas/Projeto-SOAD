# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\LoginDialog.ui',
# licensing of 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\LoginDialog.ui' applies.
#
# Created: Tue Aug  6 22:23:10 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(440, 245)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        LoginDialog.setMinimumSize(QtCore.QSize(440, 195))
        LoginDialog.setMaximumSize(QtCore.QSize(440, 245))
        self.gridLayout = QtWidgets.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalFrame = QtWidgets.QFrame(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMaximumSize(QtCore.QSize(422, 227))
        self.verticalFrame.setObjectName("verticalFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget_servidor = QtWidgets.QWidget(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_servidor.sizePolicy().hasHeightForWidth())
        self.verticalWidget_servidor.setSizePolicy(sizePolicy)
        self.verticalWidget_servidor.setMinimumSize(QtCore.QSize(400, 30))
        self.verticalWidget_servidor.setMaximumSize(QtCore.QSize(400, 50))
        self.verticalWidget_servidor.setObjectName("verticalWidget_servidor")
        self.formLayout_2 = QtWidgets.QFormLayout(self.verticalWidget_servidor)
        self.formLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_servidor = QtWidgets.QLabel(self.verticalWidget_servidor)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_servidor.setFont(font)
        self.label_servidor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_servidor.setObjectName("label_servidor")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_servidor)
        self.comboBox_servidor = QtWidgets.QComboBox(self.verticalWidget_servidor)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_servidor.setFont(font)
        self.comboBox_servidor.setObjectName("comboBox_servidor")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_servidor)
        self.verticalLayout_2.addWidget(self.verticalWidget_servidor)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget_login = QtWidgets.QWidget(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_login.sizePolicy().hasHeightForWidth())
        self.verticalWidget_login.setSizePolicy(sizePolicy)
        self.verticalWidget_login.setMaximumSize(QtCore.QSize(224, 165))
        self.verticalWidget_login.setObjectName("verticalWidget_login")
        self.formLayout = QtWidgets.QFormLayout(self.verticalWidget_login)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_usuario = QtWidgets.QLabel(self.verticalWidget_login)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_usuario.setFont(font)
        self.label_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.label_usuario.setObjectName("label_usuario")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_usuario)
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.verticalWidget_login)
        self.lineEdit_usuario.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_usuario.setFont(font)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_usuario)
        self.label_senha = QtWidgets.QLabel(self.verticalWidget_login)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_senha.setFont(font)
        self.label_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.label_senha.setObjectName("label_senha")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_senha)
        self.lineEdit_senha = QtWidgets.QLineEdit(self.verticalWidget_login)
        self.lineEdit_senha.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_senha.setFont(font)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lineEdit_senha)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalWidget_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QtCore.QSize(200, 0))
        self.buttonBox.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.buttonBox)
        self.horizontalLayout.addWidget(self.verticalWidget_login)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMaximumSize(QtCore.QSize(150, 110))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.verticalFrame, 3, 0, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtWidgets.QApplication.translate("LoginDialog", "SOAD - Login", None, -1))
        self.label_servidor.setText(QtWidgets.QApplication.translate("LoginDialog", "Servidor", None, -1))
        self.label_usuario.setText(QtWidgets.QApplication.translate("LoginDialog", "Usuário", None, -1))
        self.label_senha.setText(QtWidgets.QApplication.translate("LoginDialog", "Senha", None, -1))

