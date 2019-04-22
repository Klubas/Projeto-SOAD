# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Resources\CadastroPessoa.ui'
#
# Created: Mon Apr 22 00:35:06 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroPessoa(object):
    def setupUi(self, CadastroPessoa):
        CadastroPessoa.setObjectName("CadastroPessoa")
        CadastroPessoa.setWindowModality(QtCore.Qt.ApplicationModal)
        CadastroPessoa.resize(416, 341)
        CadastroPessoa.setFocusPolicy(QtCore.Qt.StrongFocus)
        CadastroPessoa.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(CadastroPessoa)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(CadastroPessoa)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CadastroPessoa.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CadastroPessoa.reject)
        QtCore.QMetaObject.connectSlotsByName(CadastroPessoa)

    def retranslateUi(self, CadastroPessoa):
        CadastroPessoa.setWindowTitle(QtWidgets.QApplication.translate("CadastroPessoa", "Cadastro de Pessoa", None, -1))

