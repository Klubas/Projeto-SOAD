# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/AjusteEstoque.ui',
# licensing of 'Resources/UI/AjusteEstoque.ui' applies.
#
# Created: Mon Dec  2 23:33:25 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AjusteEstoque(object):
    def setupUi(self, AjusteEstoque):
        AjusteEstoque.setObjectName("AjusteEstoque")
        AjusteEstoque.setWindowModality(QtCore.Qt.NonModal)
        AjusteEstoque.resize(500, 304)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AjusteEstoque.sizePolicy().hasHeightForWidth())
        AjusteEstoque.setSizePolicy(sizePolicy)
        AjusteEstoque.setMinimumSize(QtCore.QSize(500, 300))
        AjusteEstoque.setMaximumSize(QtCore.QSize(500, 304))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(AjusteEstoque)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(AjusteEstoque)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalFrame)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox_mercadoria = QtWidgets.QGroupBox(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formGroupBox_mercadoria.sizePolicy().hasHeightForWidth())
        self.formGroupBox_mercadoria.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.formGroupBox_mercadoria.setFont(font)
        self.formGroupBox_mercadoria.setObjectName("formGroupBox_mercadoria")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox_mercadoria)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_mercadoria_id = QtWidgets.QLineEdit(self.formGroupBox_mercadoria)
        self.lineEdit_mercadoria_id.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.lineEdit_mercadoria_id.setFont(font)
        self.lineEdit_mercadoria_id.setObjectName("lineEdit_mercadoria_id")
        self.horizontalLayout_6.addWidget(self.lineEdit_mercadoria_id)
        self.toolButton_mercadoria = QtWidgets.QToolButton(self.formGroupBox_mercadoria)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.toolButton_mercadoria.setFont(font)
        self.toolButton_mercadoria.setText("")
        self.toolButton_mercadoria.setObjectName("toolButton_mercadoria")
        self.horizontalLayout_6.addWidget(self.toolButton_mercadoria)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_mercadoria = QtWidgets.QLineEdit(self.formGroupBox_mercadoria)
        self.lineEdit_mercadoria.setEnabled(False)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.lineEdit_mercadoria.setFont(font)
        self.lineEdit_mercadoria.setObjectName("lineEdit_mercadoria")
        self.horizontalLayout_4.addWidget(self.lineEdit_mercadoria)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.formGroupBox_mercadoria)
        self.frame_central = QtWidgets.QFrame(self.horizontalFrame)
        self.frame_central.setObjectName("frame_central")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_central)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_operacao = QtWidgets.QGroupBox(self.frame_central)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_operacao.setFont(font)
        self.groupBox_operacao.setObjectName("groupBox_operacao")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_operacao)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.comboBox_operacao = QtWidgets.QComboBox(self.groupBox_operacao)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.comboBox_operacao.setFont(font)
        self.comboBox_operacao.setObjectName("comboBox_operacao")
        self.comboBox_operacao.addItem("")
        self.comboBox_operacao.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_operacao)
        self.horizontalLayout_7.addWidget(self.groupBox_operacao)
        self.groupBox_quantidade = QtWidgets.QGroupBox(self.frame_central)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_quantidade.setFont(font)
        self.groupBox_quantidade.setObjectName("groupBox_quantidade")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_quantidade)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.spinBox_quantidade = QtWidgets.QSpinBox(self.groupBox_quantidade)
        self.spinBox_quantidade.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.spinBox_quantidade.setFont(font)
        self.spinBox_quantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_quantidade.setObjectName("spinBox_quantidade")
        self.horizontalLayout_9.addWidget(self.spinBox_quantidade)
        self.horizontalLayout_7.addWidget(self.groupBox_quantidade)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_central)
        self.groupBox_motivo = QtWidgets.QGroupBox(self.horizontalFrame)
        self.groupBox_motivo.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_motivo.setFont(font)
        self.groupBox_motivo.setObjectName("groupBox_motivo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_motivo)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_motivo)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 22))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 440, 22))
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
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.textEdit_motivo.setFont(font)
        self.textEdit_motivo.setToolTipDuration(10000)
        self.textEdit_motivo.setStyleSheet("border: 1px solid red;\n"
"")
        self.textEdit_motivo.setMaxLength(150)
        self.textEdit_motivo.setObjectName("textEdit_motivo")
        self.verticalLayout_3.addWidget(self.textEdit_motivo)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.verticalLayout.addWidget(self.groupBox_motivo)
        self.frame_botoes = QtWidgets.QFrame(self.horizontalFrame)
        self.frame_botoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_botoes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_botoes.setObjectName("frame_botoes")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_botoes)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox_confirmar = QtWidgets.QDialogButtonBox(self.frame_botoes)
        self.buttonBox_confirmar.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_confirmar.setObjectName("buttonBox_confirmar")
        self.horizontalLayout_3.addWidget(self.buttonBox_confirmar)
        self.verticalLayout.addWidget(self.frame_botoes)
        self.horizontalLayout_2.addWidget(self.horizontalFrame)

        self.retranslateUi(AjusteEstoque)
        QtCore.QMetaObject.connectSlotsByName(AjusteEstoque)

    def retranslateUi(self, AjusteEstoque):
        AjusteEstoque.setWindowTitle(QtWidgets.QApplication.translate("AjusteEstoque", "Ajuste de Estoque", None, -1))
        self.formGroupBox_mercadoria.setTitle(QtWidgets.QApplication.translate("AjusteEstoque", "Mercadoria", None, -1))
        self.groupBox_operacao.setTitle(QtWidgets.QApplication.translate("AjusteEstoque", "Operação", None, -1))
        self.comboBox_operacao.setItemText(0, QtWidgets.QApplication.translate("AjusteEstoque", "Entrada", None, -1))
        self.comboBox_operacao.setItemText(1, QtWidgets.QApplication.translate("AjusteEstoque", "Saída", None, -1))
        self.groupBox_quantidade.setTitle(QtWidgets.QApplication.translate("AjusteEstoque", "Quantidade", None, -1))
        self.groupBox_motivo.setTitle(QtWidgets.QApplication.translate("AjusteEstoque", "Motivo", None, -1))
        self.textEdit_motivo.setToolTip(QtWidgets.QApplication.translate("AjusteEstoque", "O Motivo será aplicado a todos os items", None, -1))

