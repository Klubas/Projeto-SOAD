# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/DescarteItems.ui',
# licensing of 'Resources/UI/DescarteItems.ui' applies.
#
# Created: Sun Nov 10 00:52:20 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DescarteItems(object):
    def setupUi(self, DescarteItems):
        DescarteItems.setObjectName("DescarteItems")
        DescarteItems.setWindowModality(QtCore.Qt.NonModal)
        DescarteItems.resize(700, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DescarteItems.sizePolicy().hasHeightForWidth())
        DescarteItems.setSizePolicy(sizePolicy)
        DescarteItems.setMinimumSize(QtCore.QSize(700, 300))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DescarteItems)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(DescarteItems)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalFrame)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formGroupBox.sizePolicy().hasHeightForWidth())
        self.formGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.formGroupBox.setFont(font)
        self.formGroupBox.setObjectName("formGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.formGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.formGroupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 654, 119))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_items = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_items.sizePolicy().hasHeightForWidth())
        self.label_items.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_items.setFont(font)
        self.label_items.setText("")
        self.label_items.setWordWrap(True)
        self.label_items.setObjectName("label_items")
        self.horizontalLayout_4.addWidget(self.label_items)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.formGroupBox)
        self.groupBox = QtWidgets.QGroupBox(self.horizontalFrame)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 22))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 658, 34))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_motivo = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_motivo.sizePolicy().hasHeightForWidth())
        self.textEdit_motivo.setSizePolicy(sizePolicy)
        self.textEdit_motivo.setToolTipDuration(10000)
        self.textEdit_motivo.setStyleSheet("border: 1px solid red;\n"
"")
        self.textEdit_motivo.setMaxLength(150)
        self.textEdit_motivo.setObjectName("textEdit_motivo")
        self.verticalLayout_3.addWidget(self.textEdit_motivo)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(self.horizontalFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox_descartar = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox_descartar.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_descartar.setObjectName("buttonBox_descartar")
        self.horizontalLayout_3.addWidget(self.buttonBox_descartar)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.horizontalFrame)

        self.retranslateUi(DescarteItems)
        QtCore.QMetaObject.connectSlotsByName(DescarteItems)

    def retranslateUi(self, DescarteItems):
        DescarteItems.setWindowTitle(QtWidgets.QApplication.translate("DescarteItems", "Descarte de Mercadoria", None, -1))
        self.formGroupBox.setTitle(QtWidgets.QApplication.translate("DescarteItems", "Items a serem descartados", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("DescarteItems", "Motivo", None, -1))
        self.textEdit_motivo.setToolTip(QtWidgets.QApplication.translate("DescarteItems", "O Motivo será aplicado a todos os items", None, -1))

