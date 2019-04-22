# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Resources\CadastroInsumo.ui'
#
# Created: Mon Apr 22 00:21:53 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroInsumo(object):
    def setupUi(self, CadastroInsumo):
        CadastroInsumo.setObjectName("CadastroInsumo")
        CadastroInsumo.setWindowModality(QtCore.Qt.ApplicationModal)
        CadastroInsumo.resize(400, 300)
        CadastroInsumo.setFocusPolicy(QtCore.Qt.StrongFocus)
        CadastroInsumo.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(CadastroInsumo)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(CadastroInsumo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CadastroInsumo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CadastroInsumo.reject)
        QtCore.QMetaObject.connectSlotsByName(CadastroInsumo)

    def retranslateUi(self, CadastroInsumo):
        CadastroInsumo.setWindowTitle(QtWidgets.QApplication.translate("CadastroInsumo", "Cadastro de Insumo", None, -1))

