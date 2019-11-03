# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/MenuCadastro.ui',
# licensing of 'Resources/UI/Componentes/MenuCadastro.ui' applies.
#
# Created: Sat Nov  2 22:03:25 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_MenuCadastro(object):
    def setupUi(self, MenuCadastro):
        MenuCadastro.setObjectName("MenuCadastro")
        MenuCadastro.resize(1013, 78)
        MenuCadastro.setMaximumSize(QtCore.QSize(1013, 82))
        self.horizontalLayout = QtWidgets.QHBoxLayout(MenuCadastro)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu = Ui_MenuCadastro(MenuCadastro)
        self.frame_menu.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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
        self.pushButton_localizar = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_localizar.setCheckable(False)
        self.pushButton_localizar.setDefault(False)
        self.pushButton_localizar.setFlat(True)
        self.pushButton_localizar.setObjectName("pushButton_localizar")
        self.horizontalLayout_3.addWidget(self.pushButton_localizar)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.frame_menu)

        self.retranslateUi(MenuCadastro)
        QtCore.QMetaObject.connectSlotsByName(MenuCadastro)

    def retranslateUi(self, MenuCadastro):
        MenuCadastro.setWindowTitle(QtWidgets.QApplication.translate("MenuCadastro", "Form", None, -1))
        self.pushButto_cadastrar.setText(QtWidgets.QApplication.translate("MenuCadastro", "Cadastrar", None, -1))
        self.pushButton_editar.setText(QtWidgets.QApplication.translate("MenuCadastro", "Editar", None, -1))
        self.pushButton_excluir.setText(QtWidgets.QApplication.translate("MenuCadastro", "Excluir", None, -1))
        self.pushButton_localizar.setText(QtWidgets.QApplication.translate("MenuCadastro", "Localizar", None, -1))

from View.Componentes.Ui_MenuCadastro import Ui_MenuCadastro
