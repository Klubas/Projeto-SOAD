# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/LoginDialog.ui',
# licensing of 'Resources/UI/LoginDialog.ui' applies.
#
# Created: Sun Oct 13 10:57:26 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(440, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        LoginDialog.setMinimumSize(QtCore.QSize(440, 195))
        LoginDialog.setMaximumSize(QtCore.QSize(440, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        LoginDialog.setPalette(palette)
        self.gridLayout = QtWidgets.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalFrame = QtWidgets.QFrame(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalFrame.setObjectName("verticalFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.verticalFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalGroupBox_servidor = QtWidgets.QGroupBox(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalGroupBox_servidor.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_servidor.setSizePolicy(sizePolicy)
        self.verticalGroupBox_servidor.setMinimumSize(QtCore.QSize(400, 30))
        self.verticalGroupBox_servidor.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.verticalGroupBox_servidor.setFont(font)
        self.verticalGroupBox_servidor.setObjectName("verticalGroupBox_servidor")
        self.formLayout_2 = QtWidgets.QFormLayout(self.verticalGroupBox_servidor)
        self.formLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_servidor = QtWidgets.QLabel(self.verticalGroupBox_servidor)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_servidor.setFont(font)
        self.label_servidor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_servidor.setObjectName("label_servidor")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_servidor)
        self.comboBox_servidor = QtWidgets.QComboBox(self.verticalGroupBox_servidor)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.comboBox_servidor.setFont(font)
        self.comboBox_servidor.setObjectName("comboBox_servidor")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_servidor)
        self.verticalLayout_2.addWidget(self.verticalGroupBox_servidor)
        self.groupBox_login = QtWidgets.QGroupBox(self.verticalFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_login.setFont(font)
        self.groupBox_login.setObjectName("groupBox_login")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_login)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget_login = QtWidgets.QWidget(self.groupBox_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_login.sizePolicy().hasHeightForWidth())
        self.verticalWidget_login.setSizePolicy(sizePolicy)
        self.verticalWidget_login.setMaximumSize(QtCore.QSize(224, 165))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.verticalWidget_login.setFont(font)
        self.verticalWidget_login.setObjectName("verticalWidget_login")
        self.formLayout = QtWidgets.QFormLayout(self.verticalWidget_login)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_usuario = QtWidgets.QLabel(self.verticalWidget_login)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_usuario.setFont(font)
        self.label_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.label_usuario.setObjectName("label_usuario")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_usuario)
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.verticalWidget_login)
        self.lineEdit_usuario.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.lineEdit_usuario.setFont(font)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_usuario)
        self.label_senha = QtWidgets.QLabel(self.verticalWidget_login)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_senha.setFont(font)
        self.label_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.label_senha.setObjectName("label_senha")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_senha)
        self.lineEdit_senha = QtWidgets.QLineEdit(self.verticalWidget_login)
        self.lineEdit_senha.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
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
        font.setWeight(50)
        font.setBold(False)
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
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_logo = QtWidgets.QScrollArea(self.groupBox_login)
        self.scrollArea_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_logo.setWidgetResizable(True)
        self.scrollArea_logo.setObjectName("scrollArea_logo")
        self.scrollAreaWidgetContents_logo = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_logo.setEnabled(True)
        self.scrollAreaWidgetContents_logo.setGeometry(QtCore.QRect(0, 0, 146, 163))
        self.scrollAreaWidgetContents_logo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.scrollAreaWidgetContents_logo.setObjectName("scrollAreaWidgetContents_logo")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_logo)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_logo = QtWidgets.QLabel(self.scrollAreaWidgetContents_logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_logo.setFont(font)
        self.label_logo.setAutoFillBackground(True)
        self.label_logo.setScaledContents(False)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.gridLayout_4.addWidget(self.label_logo, 0, 0, 1, 1)
        self.scrollArea_logo.setWidget(self.scrollAreaWidgetContents_logo)
        self.gridLayout_3.addWidget(self.scrollArea_logo, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_login)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.verticalFrame, 3, 0, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtWidgets.QApplication.translate("LoginDialog", "SOAD - Login", None, -1))
        self.verticalGroupBox_servidor.setTitle(QtWidgets.QApplication.translate("LoginDialog", "Host", None, -1))
        self.label_servidor.setText(QtWidgets.QApplication.translate("LoginDialog", "Servidor", None, -1))
        self.groupBox_login.setTitle(QtWidgets.QApplication.translate("LoginDialog", "Login", None, -1))
        self.label_usuario.setText(QtWidgets.QApplication.translate("LoginDialog", "Usuário", None, -1))
        self.label_senha.setText(QtWidgets.QApplication.translate("LoginDialog", "Senha", None, -1))
        self.label_logo.setText(QtWidgets.QApplication.translate("LoginDialog", "LOGO", None, -1))

