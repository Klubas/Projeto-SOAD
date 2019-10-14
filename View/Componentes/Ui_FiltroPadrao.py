# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/FiltroPadrao.ui',
# licensing of 'Resources/UI/Componentes/FiltroPadrao.ui' applies.
#
# Created: Sun Oct 13 10:57:28 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FiltroPadrao(object):
    def setupUi(self, FiltroPadrao):
        FiltroPadrao.setObjectName("FiltroPadrao")
        FiltroPadrao.setWindowModality(QtCore.Qt.WindowModal)
        FiltroPadrao.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(FiltroPadrao)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(FiltroPadrao)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), FiltroPadrao.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), FiltroPadrao.reject)
        QtCore.QMetaObject.connectSlotsByName(FiltroPadrao)

    def retranslateUi(self, FiltroPadrao):
        FiltroPadrao.setWindowTitle(QtWidgets.QApplication.translate("FiltroPadrao", "Filtro", None, -1))

