# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroProduto.ui',
# licensing of 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroProduto.ui' applies.
#
# Created: Thu Aug  1 00:21:52 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_CadastroProduto(object):
    def setupUi(self, CadastroProduto):
        CadastroProduto.setObjectName("CadastroProduto")
        CadastroProduto.setWindowModality(QtCore.Qt.NonModal)
        CadastroProduto.resize(578, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroProduto.sizePolicy().hasHeightForWidth())
        CadastroProduto.setSizePolicy(sizePolicy)
        CadastroProduto.setMinimumSize(QtCore.QSize(568, 559))
        self.horizontalLayoutWidget = QtWidgets.QWidget(CadastroProduto)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.retranslateUi(CadastroProduto)
        QtCore.QMetaObject.connectSlotsByName(CadastroProduto)

    def retranslateUi(self, CadastroProduto):
        CadastroProduto.setWindowTitle(QtWidgets.QApplication.translate("CadastroProduto", "Cadastrar Produto", None, -1))

