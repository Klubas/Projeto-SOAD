# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\EstornoPedido.ui',
# licensing of 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\EstornoPedido.ui' applies.
#
# Created: Thu Aug  8 00:08:22 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_EstornoPedido(object):
    def setupUi(self, Descarte):
        Descarte.setObjectName("Descarte")
        Descarte.setWindowModality(QtCore.Qt.NonModal)
        Descarte.setGeometry(QtCore.QRect(0, 0, 578, 560))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Descarte.sizePolicy().hasHeightForWidth())
        Descarte.setSizePolicy(sizePolicy)
        Descarte.setMinimumSize(QtCore.QSize(568, 559))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Descarte)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.retranslateUi(Descarte)
        QtCore.QMetaObject.connectSlotsByName(Descarte)

    def retranslateUi(self, Descarte):
        Descarte.setWindowTitle(QtWidgets.QApplication.translate("EstornoPedido", "Estornar Pedido", None, -1))
