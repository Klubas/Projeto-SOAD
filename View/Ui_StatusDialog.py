# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\StatusDialog.ui',
# licensing of 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\StatusDialog.ui' applies.
#
# Created: Thu Aug  1 00:21:54 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_StatusDialog(object):
    def setupUi(self, StatusDialog):
        StatusDialog.setObjectName("StatusDialog")
        StatusDialog.resize(750, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatusDialog.sizePolicy().hasHeightForWidth())
        StatusDialog.setSizePolicy(sizePolicy)
        StatusDialog.setMinimumSize(QtCore.QSize(750, 270))
        StatusDialog.setSizeGripEnabled(True)
        StatusDialog.setModal(True)
        self.verticalFrame = QtWidgets.QFrame(StatusDialog)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 750, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(750, 271))
        self.verticalFrame.setSizeIncrement(QtCore.QSize(10, 10))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_mensagem = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mensagem.sizePolicy().hasHeightForWidth())
        self.label_mensagem.setSizePolicy(sizePolicy)
        self.label_mensagem.setMaximumSize(QtCore.QSize(16777214, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_mensagem.setFont(font)
        self.label_mensagem.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_mensagem.setTextFormat(QtCore.Qt.PlainText)
        self.label_mensagem.setWordWrap(True)
        self.label_mensagem.setObjectName("label_mensagem")
        self.verticalLayout.addWidget(self.label_mensagem)
        self.textEdit_exception = QtWidgets.QTextEdit(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.textEdit_exception.sizePolicy().hasHeightForWidth())
        self.textEdit_exception.setSizePolicy(sizePolicy)
        self.textEdit_exception.setMinimumSize(QtCore.QSize(720, 175))
        self.textEdit_exception.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_exception.setFont(font)
        self.textEdit_exception.setObjectName("textEdit_exception")
        self.verticalLayout.addWidget(self.textEdit_exception)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(2, 10)

        self.retranslateUi(StatusDialog)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog)

    def retranslateUi(self, StatusDialog):
        StatusDialog.setWindowTitle(QtWidgets.QApplication.translate("StatusDialog", "Dialog", None, -1))
        self.label_mensagem.setText(QtWidgets.QApplication.translate("StatusDialog", "TextLabel", None, -1))

