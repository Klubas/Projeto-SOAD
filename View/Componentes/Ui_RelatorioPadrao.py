# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\UI\Componentes\RelatorioPadrao.ui',
# licensing of 'Resources\UI\Componentes\RelatorioPadrao.ui' applies.
#
# Created: Sun Sep  8 02:12:57 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_RelatorioPadrao(object):
    def setupUi(self, RelatorioPadrao):
        RelatorioPadrao.setObjectName("RelatorioPadrao")
        RelatorioPadrao.setWindowModality(QtCore.Qt.NonModal)
        RelatorioPadrao.resize(578, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RelatorioPadrao.sizePolicy().hasHeightForWidth())
        RelatorioPadrao.setSizePolicy(sizePolicy)
        RelatorioPadrao.setMinimumSize(QtCore.QSize(568, 559))
        RelatorioPadrao.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.horizontalLayoutWidget = QtWidgets.QWidget(RelatorioPadrao)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.retranslateUi(RelatorioPadrao)
        QtCore.QMetaObject.connectSlotsByName(RelatorioPadrao)

    def retranslateUi(self, RelatorioPadrao):
        RelatorioPadrao.setWindowTitle(QtWidgets.QApplication.translate("RelatorioPadrao", "Relatório", None, -1))

