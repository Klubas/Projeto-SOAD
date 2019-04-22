# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\Resources\CadastroProduto.ui'
#
# Created: Mon Apr 22 00:21:54 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroProduto(object):
    def setupUi(self, CadastroProduto):
        CadastroProduto.setObjectName("CadastroProduto")
        CadastroProduto.setWindowModality(QtCore.Qt.ApplicationModal)
        CadastroProduto.resize(400, 300)
        CadastroProduto.setFocusPolicy(QtCore.Qt.StrongFocus)
        CadastroProduto.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(CadastroProduto)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(CadastroProduto)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CadastroProduto.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CadastroProduto.reject)
        QtCore.QMetaObject.connectSlotsByName(CadastroProduto)

    def retranslateUi(self, CadastroProduto):
        CadastroProduto.setWindowTitle(QtWidgets.QApplication.translate("CadastroProduto", "Cadastro de Produto", None, -1))

