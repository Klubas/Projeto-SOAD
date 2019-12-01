# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/FiltroPadrao.ui',
# licensing of 'Resources/UI/Componentes/FiltroPadrao.ui' applies.
#
# Created: Sun Dec  1 16:51:23 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QFrame(self.frame)
        self.widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.widget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout.addWidget(self.widget)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_2)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(FiltroPadrao)
        QtCore.QMetaObject.connectSlotsByName(FiltroPadrao)

    def retranslateUi(self, FiltroPadrao):
        FiltroPadrao.setWindowTitle(QtWidgets.QApplication.translate("FiltroPadrao", "Filtro", None, -1))

