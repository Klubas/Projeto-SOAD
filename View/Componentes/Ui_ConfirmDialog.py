# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\UI\Componentes\ConfirmDialog.ui',
# licensing of 'Resources\UI\Componentes\ConfirmDialog.ui' applies.
#
# Created: Wed Oct 30 00:10:28 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ConfirmDialog(object):
    def setupUi(self, ConfirmDialog):
        ConfirmDialog.setObjectName("ConfirmDialog")
        ConfirmDialog.setWindowModality(QtCore.Qt.WindowModal)
        ConfirmDialog.resize(430, 163)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfirmDialog.sizePolicy().hasHeightForWidth())
        ConfirmDialog.setSizePolicy(sizePolicy)
        ConfirmDialog.setMinimumSize(QtCore.QSize(430, 120))
        ConfirmDialog.setMaximumSize(QtCore.QSize(430, 300))
        font = QtGui.QFont()
        ConfirmDialog.setFont(font)
        ConfirmDialog.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(ConfirmDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalFrame = QtWidgets.QFrame(ConfirmDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalFrame.setFont(font)
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.verticalFrame.setObjectName("verticalFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalFrame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_imagem = QtWidgets.QLabel(self.verticalFrame)
        self.label_imagem.setMinimumSize(QtCore.QSize(60, 60))
        self.label_imagem.setMaximumSize(QtCore.QSize(60, 60))
        self.label_imagem.setObjectName("label_imagem")
        self.gridLayout.addWidget(self.label_imagem, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.verticalFrame, 0, 0, 1, 1)

        self.retranslateUi(ConfirmDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfirmDialog)

    def retranslateUi(self, ConfirmDialog):
        ConfirmDialog.setWindowTitle(QtWidgets.QApplication.translate("ConfirmDialog", "Diálogo de confirmação", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ConfirmDialog", "Existem janelas abertas, tem certeza que deseja sair?", None, -1))
        self.label_imagem.setText(QtWidgets.QApplication.translate("ConfirmDialog", "label_imagem", None, -1))

