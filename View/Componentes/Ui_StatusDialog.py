# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/StatusDialog.ui',
# licensing of 'Resources/UI/Componentes/StatusDialog.ui' applies.
#
# Created: Thu Sep  5 20:25:44 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_StatusDialog(object):
    def setupUi(self, StatusDialog):
        StatusDialog.setObjectName("StatusDialog")
        StatusDialog.setWindowModality(QtCore.Qt.WindowModal)
        StatusDialog.setEnabled(True)
        StatusDialog.resize(750, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatusDialog.sizePolicy().hasHeightForWidth())
        StatusDialog.setSizePolicy(sizePolicy)
        StatusDialog.setMinimumSize(QtCore.QSize(750, 300))
        StatusDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        StatusDialog.setSizeGripEnabled(True)
        StatusDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(StatusDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalWidget = QtWidgets.QWidget(StatusDialog)
        self.verticalWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalWidget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.verticalWidget.setFont(font)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_status = QtWidgets.QGroupBox(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_status.sizePolicy().hasHeightForWidth())
        self.groupBox_status.setSizePolicy(sizePolicy)
        self.groupBox_status.setObjectName("groupBox_status")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_status)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_status)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 700, 69))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_mensagem = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mensagem.sizePolicy().hasHeightForWidth())
        self.label_mensagem.setSizePolicy(sizePolicy)
        self.label_mensagem.setMaximumSize(QtCore.QSize(16777214, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_mensagem.setFont(font)
        self.label_mensagem.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_mensagem.setTextFormat(QtCore.Qt.PlainText)
        self.label_mensagem.setWordWrap(True)
        self.label_mensagem.setObjectName("label_mensagem")
        self.gridLayout_3.addWidget(self.label_mensagem, 1, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_status)
        self.groupBox_mensagem = QtWidgets.QGroupBox(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_mensagem.sizePolicy().hasHeightForWidth())
        self.groupBox_mensagem.setSizePolicy(sizePolicy)
        self.groupBox_mensagem.setFlat(False)
        self.groupBox_mensagem.setCheckable(False)
        self.groupBox_mensagem.setChecked(False)
        self.groupBox_mensagem.setObjectName("groupBox_mensagem")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_mensagem)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_mensagem)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 720, 106))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_exception = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_exception.sizePolicy().hasHeightForWidth())
        self.textBrowser_exception.setSizePolicy(sizePolicy)
        self.textBrowser_exception.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser_exception.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser_exception.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.textBrowser_exception.setFont(font)
        self.textBrowser_exception.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.textBrowser_exception.setToolTipDuration(1)
        self.textBrowser_exception.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_exception.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_exception.setLineWidth(1)
        self.textBrowser_exception.setObjectName("textBrowser_exception")
        self.gridLayout_2.addWidget(self.textBrowser_exception, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_mensagem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalWidget)
        self.buttonBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addWidget(self.verticalWidget, 0, 0, 1, 1)

        self.retranslateUi(StatusDialog)
        QtCore.QMetaObject.connectSlotsByName(StatusDialog)

    def retranslateUi(self, StatusDialog):
        StatusDialog.setWindowTitle(QtWidgets.QApplication.translate("StatusDialog", "Dialog", None, -1))
        self.groupBox_status.setTitle(QtWidgets.QApplication.translate("StatusDialog", "Status", None, -1))
        self.label_mensagem.setText(QtWidgets.QApplication.translate("StatusDialog", "TextLabel", None, -1))
        self.groupBox_mensagem.setTitle(QtWidgets.QApplication.translate("StatusDialog", "Mensagem", None, -1))

