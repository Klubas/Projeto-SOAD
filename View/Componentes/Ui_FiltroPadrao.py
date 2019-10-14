# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\UI\Componentes\FiltroPadrao.ui',
# licensing of 'Resources\UI\Componentes\FiltroPadrao.ui' applies.
#
# Created: Mon Oct 14 01:04:39 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_FiltroPadrao(object):
    def setupUi(self, FiltroPadrao):
        FiltroPadrao.setObjectName("FiltroPadrao")
        FiltroPadrao.setWindowModality(QtCore.Qt.WindowModal)
        FiltroPadrao.resize(933, 495)
        FiltroPadrao.setMinimumSize(QtCore.QSize(0, 0))
        FiltroPadrao.setMaximumSize(QtCore.QSize(16777215, 16777215))
        FiltroPadrao.setSizeGripEnabled(True)
        FiltroPadrao.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(FiltroPadrao)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(FiltroPadrao)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(FiltroPadrao)
        QtCore.QMetaObject.connectSlotsByName(FiltroPadrao)

    def retranslateUi(self, FiltroPadrao):
        FiltroPadrao.setWindowTitle(QtWidgets.QApplication.translate("FiltroPadrao", "Filtro", None, -1))

