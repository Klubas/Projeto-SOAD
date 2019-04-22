# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Resources\CadastroToner.ui'
#
# Created: Mon Apr 22 00:21:54 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroToner(object):
    def setupUi(self, CadastroToner):
        CadastroToner.setObjectName("CadastroToner")
        CadastroToner.setWindowModality(QtCore.Qt.ApplicationModal)
        CadastroToner.resize(400, 300)
        CadastroToner.setFocusPolicy(QtCore.Qt.StrongFocus)
        CadastroToner.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(CadastroToner)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(CadastroToner)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CadastroToner.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CadastroToner.reject)
        QtCore.QMetaObject.connectSlotsByName(CadastroToner)

    def retranslateUi(self, CadastroToner):
        CadastroToner.setWindowTitle(QtWidgets.QApplication.translate("CadastroToner", "Cadastro de Toner", None, -1))

