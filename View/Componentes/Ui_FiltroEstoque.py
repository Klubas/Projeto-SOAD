# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\UI\Componentes\FiltroEstoque.ui',
# licensing of 'Resources\UI\Componentes\FiltroEstoque.ui' applies.
#
# Created: Mon Oct 14 01:04:39 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_FiltroEstoque(object):
    def setupUi(self, FiltroEstoque):
        FiltroEstoque.setObjectName("FiltroEstoque")
        FiltroEstoque.resize(550, 350)
        FiltroEstoque.setMinimumSize(QtCore.QSize(550, 350))
        FiltroEstoque.setMaximumSize(QtCore.QSize(550, 350))
        FiltroEstoque.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(FiltroEstoque)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(FiltroEstoque)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(FiltroEstoque)
        QtCore.QMetaObject.connectSlotsByName(FiltroEstoque)

    def retranslateUi(self, FiltroEstoque):
        FiltroEstoque.setWindowTitle(QtWidgets.QApplication.translate("FiltroEstoque", "Dialog", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("FiltroEstoque", "GroupBox", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("FiltroEstoque", "PushButton", None, -1))

