# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/CadastroMunicipio.ui',
# licensing of 'Resources/UI/CadastroMunicipio.ui' applies.
#
# Created: Mon Dec  2 23:33:24 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroMunicipio(object):
    def setupUi(self, CadastroMunicipio):
        CadastroMunicipio.setObjectName("CadastroMunicipio")
        CadastroMunicipio.resize(500, 270)
        CadastroMunicipio.setMinimumSize(QtCore.QSize(500, 270))
        CadastroMunicipio.setMaximumSize(QtCore.QSize(500, 270))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CadastroMunicipio)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_menu = QtWidgets.QFrame(CadastroMunicipio)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
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
        self.horizontalLayout_3.addWidget(self.pushButton_cadastrar)
        self.pushButton_editar = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_editar.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_editar.setFont(font)
        self.pushButton_editar.setCheckable(False)
        self.pushButton_editar.setDefault(False)
        self.pushButton_editar.setFlat(True)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.horizontalLayout_3.addWidget(self.pushButton_editar)
        self.pushButton_excluir = QtWidgets.QPushButton(self.frame_menu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_excluir.setFont(font)
        self.pushButton_excluir.setCheckable(False)
        self.pushButton_excluir.setDefault(False)
        self.pushButton_excluir.setFlat(True)
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.horizontalLayout_3.addWidget(self.pushButton_excluir)
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
        self.horizontalLayout_3.addWidget(self.pushButton_localizar)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame_menu)
        self.frame_contents = QtWidgets.QFrame(CadastroMunicipio)
        self.frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contents.setObjectName("frame_contents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_contents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame_contents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_ibge = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.lineEdit_ibge.setFont(font)
        self.lineEdit_ibge.setMaxLength(7)
        self.lineEdit_ibge.setObjectName("lineEdit_ibge")
        self.horizontalLayout_2.addWidget(self.lineEdit_ibge)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_uf = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_uf.setMinimumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.comboBox_uf.setFont(font)
        self.comboBox_uf.setObjectName("comboBox_uf")
        self.horizontalLayout_2.addWidget(self.comboBox_uf)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_municipio = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.lineEdit_municipio.setFont(font)
        self.lineEdit_municipio.setMaxLength(60)
        self.lineEdit_municipio.setObjectName("lineEdit_municipio")
        self.horizontalLayout_5.addWidget(self.lineEdit_municipio)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.frame_contents)
        self.frame_buttons = QtWidgets.QFrame(CadastroMunicipio)
        self.frame_buttons.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_buttons.setObjectName("frame_buttons")
        self.frame_buttonsLayout = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.frame_buttonsLayout.setObjectName("frame_buttonsLayout")
        self.label_id = QtWidgets.QLabel(self.frame_buttons)
        self.label_id.setText("")
        self.label_id.setObjectName("label_id")
        self.frame_buttonsLayout.addWidget(self.label_id)
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
        self.frame_buttonsLayout.addWidget(self.lineEdit_id)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_buttons)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame_buttonsLayout.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.frame_buttons)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CadastroMunicipio)
        QtCore.QMetaObject.connectSlotsByName(CadastroMunicipio)

    def retranslateUi(self, CadastroMunicipio):
        CadastroMunicipio.setWindowTitle(QtWidgets.QApplication.translate("CadastroMunicipio", "Cadastro de municípios", None, -1))
        self.pushButton_cadastrar.setText(QtWidgets.QApplication.translate("CadastroMunicipio", "Cadastrar", None, -1))
        self.pushButton_editar.setText(QtWidgets.QApplication.translate("CadastroMunicipio", "Editar", None, -1))
        self.pushButton_excluir.setText(QtWidgets.QApplication.translate("CadastroMunicipio", "Excluir", None, -1))
        self.pushButton_localizar.setText(QtWidgets.QApplication.translate("CadastroMunicipio", "Localizar", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("CadastroMunicipio", "Município", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CadastroMunicipio", "Cód. IBGE", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("CadastroMunicipio", "UF", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("CadastroMunicipio", "Nome", None, -1))

