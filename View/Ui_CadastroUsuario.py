# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/CadastroUsuario.ui',
# licensing of 'Resources/UI/CadastroUsuario.ui' applies.
#
# Created: Tue Oct 29 00:55:58 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroUsuario(object):
    def setupUi(self, CadastroUsuario):
        CadastroUsuario.setObjectName("CadastroUsuario")
        CadastroUsuario.setWindowModality(QtCore.Qt.NonModal)
        CadastroUsuario.resize(350, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroUsuario.sizePolicy().hasHeightForWidth())
        CadastroUsuario.setSizePolicy(sizePolicy)
        CadastroUsuario.setMinimumSize(QtCore.QSize(350, 200))
        CadastroUsuario.setMaximumSize(QtCore.QSize(500, 250))
        self.gridLayout = QtWidgets.QGridLayout(CadastroUsuario)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(CadastroUsuario)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.gridLayout.addWidget(self.frame, 2, 1, 1, 1)
        self.frame_menu = QtWidgets.QFrame(CadastroUsuario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.frame_menu.setFont(font)
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_cadastrar = QtWidgets.QPushButton(self.frame_menu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_cadastrar.setFont(font)
        self.pushButton_cadastrar.setCheckable(False)
        self.pushButton_cadastrar.setDefault(False)
        self.pushButton_cadastrar.setFlat(True)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.horizontalLayout_4.addWidget(self.pushButton_cadastrar)
        self.pushButton_localizar = QtWidgets.QPushButton(self.frame_menu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_localizar.setFont(font)
        self.pushButton_localizar.setCheckable(False)
        self.pushButton_localizar.setDefault(False)
        self.pushButton_localizar.setFlat(True)
        self.pushButton_localizar.setObjectName("pushButton_localizar")
        self.horizontalLayout_4.addWidget(self.pushButton_localizar)
        self.gridLayout.addWidget(self.frame_menu, 1, 1, 1, 1)
        self.frame_buttons = QtWidgets.QFrame(CadastroUsuario)
        self.frame_buttons.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_id = QtWidgets.QLineEdit(self.frame_buttons)
        self.lineEdit_id.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_id.setSizePolicy(sizePolicy)
        self.lineEdit_id.setAutoFillBackground(False)
        self.lineEdit_id.setFrame(False)
        self.lineEdit_id.setDragEnabled(False)
        self.lineEdit_id.setReadOnly(False)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.horizontalLayout_2.addWidget(self.lineEdit_id)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_buttons)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.gridLayout.addWidget(self.frame_buttons, 3, 1, 1, 1)

        self.retranslateUi(CadastroUsuario)
        QtCore.QMetaObject.connectSlotsByName(CadastroUsuario)

    def retranslateUi(self, CadastroUsuario):
        CadastroUsuario.setWindowTitle(QtWidgets.QApplication.translate("CadastroUsuario", "Cadastro de usuários", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CadastroUsuario", "Usuário", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("CadastroUsuario", "Ativo", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("CadastroUsuario", "Senha", None, -1))
        self.pushButton_cadastrar.setText(QtWidgets.QApplication.translate("CadastroUsuario", "Cadastrar", None, -1))
        self.pushButton_localizar.setText(QtWidgets.QApplication.translate("CadastroUsuario", "Localizar", None, -1))
