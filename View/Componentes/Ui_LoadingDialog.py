# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/LoadingDialog.ui',
# licensing of 'Resources/UI/Componentes/LoadingDialog.ui' applies.
#
# Created: Tue Oct 15 19:39:30 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_LoadingDialog(object):
    def setupUi(self, LoadingDialog):
        LoadingDialog.setObjectName("LoadingDialog")
        LoadingDialog.setWindowModality(QtCore.Qt.NonModal)
        LoadingDialog.resize(300, 140)
        LoadingDialog.setMinimumSize(QtCore.QSize(300, 140))
        LoadingDialog.setMaximumSize(QtCore.QSize(300, 140))
        LoadingDialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        LoadingDialog.setSizeGripEnabled(False)
        LoadingDialog.setModal(False)
        self.verticalFrame = QtWidgets.QFrame(LoadingDialog)
        self.verticalFrame.setEnabled(True)
        self.verticalFrame.setGeometry(QtCore.QRect(10, 10, 281, 128))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.progressBar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.progressBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.progressBar.setMinimum(5)
        self.progressBar.setProperty("value", 5)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(LoadingDialog)
        QtCore.QMetaObject.connectSlotsByName(LoadingDialog)

    def retranslateUi(self, LoadingDialog):
        LoadingDialog.setWindowTitle(QtWidgets.QApplication.translate("LoadingDialog", "Dialog", None, -1))

