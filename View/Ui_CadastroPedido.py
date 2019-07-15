# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroPedido.ui'
#
# Created: Mon Jul 15 07:35:42 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_CadastroPedido(object):
    def setupUi(self, CadastroPedido):
        CadastroPedido.setObjectName("CadastroPedido")
        CadastroPedido.setWindowModality(QtCore.Qt.NonModal)
        CadastroPedido.resize(578, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroPedido.sizePolicy().hasHeightForWidth())
        CadastroPedido.setSizePolicy(sizePolicy)
        CadastroPedido.setMinimumSize(QtCore.QSize(568, 559))
        self.horizontalLayoutWidget = QtWidgets.QWidget(CadastroPedido)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.retranslateUi(CadastroPedido)
        QtCore.QMetaObject.connectSlotsByName(CadastroPedido)

    def retranslateUi(self, CadastroPedido):
        CadastroPedido.setWindowTitle(QtWidgets.QApplication.translate("CadastroPedido", "Cadastrar Pedido", None, -1))

