# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\SairDialog.ui',
# licensing of 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\SairDialog.ui' applies.
#
# Created: Wed Aug  7 00:52:42 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SairDialog(object):
    def setupUi(self, SairDialog):
        SairDialog.setObjectName("SairDialog")
        SairDialog.resize(430, 120)
        SairDialog.setMinimumSize(QtCore.QSize(430, 120))
        SairDialog.setMaximumSize(QtCore.QSize(430, 150))
        font = QtGui.QFont()
        SairDialog.setFont(font)
        SairDialog.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(SairDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalFrame = QtWidgets.QFrame(SairDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalFrame.setFont(font)
        self.verticalFrame.setObjectName("verticalFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalFrame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.verticalFrame, 0, 0, 1, 1)

        self.retranslateUi(SairDialog)
        QtCore.QMetaObject.connectSlotsByName(SairDialog)

    def retranslateUi(self, SairDialog):
        SairDialog.setWindowTitle(QtWidgets.QApplication.translate("SairDialog", "Dialog", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SairDialog", "Existem janelas abertas, tem certeza que deseja sair?", None, -1))

