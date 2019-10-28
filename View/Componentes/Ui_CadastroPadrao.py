# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/CadastroPadrao.ui',
# licensing of 'Resources/UI/Componentes/CadastroPadrao.ui' applies.
#
# Created: Mon Oct 28 13:37:17 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroPadrao(object):
    def setupUi(self, CadastroPadrao):
        CadastroPadrao.setObjectName("CadastroPadrao")
        CadastroPadrao.setWindowModality(QtCore.Qt.WindowModal)
        CadastroPadrao.setEnabled(True)
        CadastroPadrao.resize(1041, 591)
        CadastroPadrao.setCursor(QtCore.Qt.ArrowCursor)
        self.gridLayout_5 = QtWidgets.QGridLayout(CadastroPadrao)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget = QtWidgets.QWidget(CadastroPadrao)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_menu = QtWidgets.QFrame(self.widget)
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_menu)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButto_cadastrar = QtWidgets.QPushButton(self.frame_menu)
        self.pushButto_cadastrar.setCheckable(False)
        self.pushButto_cadastrar.setDefault(False)
        self.pushButto_cadastrar.setFlat(True)
        self.pushButto_cadastrar.setObjectName("pushButto_cadastrar")
        self.horizontalLayout_3.addWidget(self.pushButto_cadastrar)
        self.pushButton_editar = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_editar.setCheckable(False)
        self.pushButton_editar.setDefault(False)
        self.pushButton_editar.setFlat(True)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.horizontalLayout_3.addWidget(self.pushButton_editar)
        self.pushButton_excluir = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_excluir.setCheckable(False)
        self.pushButton_excluir.setDefault(False)
        self.pushButton_excluir.setFlat(True)
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.horizontalLayout_3.addWidget(self.pushButton_excluir)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_menu)
        self.frame_contents = QtWidgets.QFrame(self.widget)
        self.frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contents.setObjectName("frame_contents")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_contents)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_content = QtWidgets.QWidget(self.frame_contents)
        self.widget_content.setObjectName("widget_content")
        self.gridLayout.addWidget(self.widget_content, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_contents)
        self.frame_buttons = QtWidgets.QFrame(self.widget)
        self.frame_buttons.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_buttons)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_buttons)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_buttons)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(CadastroPadrao)
        QtCore.QMetaObject.connectSlotsByName(CadastroPadrao)

    def retranslateUi(self, CadastroPadrao):
        CadastroPadrao.setWindowTitle(QtWidgets.QApplication.translate("CadastroPadrao", "Cadastro - ", None, -1))
        self.pushButto_cadastrar.setText(QtWidgets.QApplication.translate("CadastroPadrao", "Cadastrar", None, -1))
        self.pushButton_editar.setText(QtWidgets.QApplication.translate("CadastroPadrao", "Editar", None, -1))
        self.pushButton_excluir.setText(QtWidgets.QApplication.translate("CadastroPadrao", "Excluir", None, -1))

