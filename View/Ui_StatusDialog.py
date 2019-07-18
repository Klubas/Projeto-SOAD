# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\StatusDialog.ui'
#
# Created: Tue Jul 16 19:11:33 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
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
        self.verticalWidget = QtWidgets.QWidget(StatusDialog)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 750, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMinimumSize(QtCore.QSize(750, 271))
        self.verticalWidget.setSizeIncrement(QtCore.QSize(10, 10))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_mensagem = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_mensagem.setFont(font)
        self.label_mensagem.setObjectName("label_mensagem")
        self.verticalLayout.addWidget(self.label_mensagem)
        self.textBrowser_exception = QtWidgets.QTextBrowser(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.textBrowser_exception.sizePolicy().hasHeightForWidth())
        self.textBrowser_exception.setSizePolicy(sizePolicy)
        self.textBrowser_exception.setMinimumSize(QtCore.QSize(720, 175))
        self.textBrowser_exception.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_exception.setFont(font)
        self.textBrowser_exception.setObjectName("textBrowser_exception")
        self.verticalLayout.addWidget(self.textBrowser_exception)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalWidget)
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
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 10)

        self.retranslateUi(StatusDialog)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog)

    def retranslateUi(self, StatusDialog):
        StatusDialog.setWindowTitle(QtWidgets.QApplication.translate("StatusDialog", "Dialog", None, -1))
        self.label_mensagem.setText(QtWidgets.QApplication.translate("StatusDialog", "TextLabel", None, -1))

