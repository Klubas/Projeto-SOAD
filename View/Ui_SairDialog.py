# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\SairDialog.ui'
#
# Created: Sat Jul 13 03:29:01 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SairDialog(object):
    def setupUi(self, SairDialog):
        SairDialog.setObjectName("SairDialog")
        SairDialog.resize(400, 300)
        SairDialog.setModal(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(SairDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 341, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SairDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SairDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SairDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SairDialog)

    def retranslateUi(self, SairDialog):
        SairDialog.setWindowTitle(QtWidgets.QApplication.translate("SairDialog", "Dialog", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SairDialog", "Existem janelas abertas, tem certeza que deseja sair?", None, -1))

