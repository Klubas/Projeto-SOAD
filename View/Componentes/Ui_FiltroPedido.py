# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/FiltroPedido.ui',
# licensing of 'Resources/UI/Componentes/FiltroPedido.ui' applies.
#
# Created: Sun Nov  3 01:30:15 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FiltroPedido(object):
    def setupUi(self, FiltroPedido):
        FiltroPedido.setObjectName("FiltroPedido")
        FiltroPedido.resize(600, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FiltroPedido.sizePolicy().hasHeightForWidth())
        FiltroPedido.setSizePolicy(sizePolicy)
        FiltroPedido.setMinimumSize(QtCore.QSize(600, 190))
        FiltroPedido.setMaximumSize(QtCore.QSize(645, 190))
        FiltroPedido.setSizeIncrement(QtCore.QSize(100, 50))
        FiltroPedido.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        FiltroPedido.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(FiltroPedido)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(FiltroPedido)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formFrame.sizePolicy().hasHeightForWidth())
        self.formFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.formFrame.setFont(font)
        self.formFrame.setObjectName("formFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.formFrame)
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.formFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_pessoa = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_pessoa.sizePolicy().hasHeightForWidth())
        self.groupBox_pessoa.setSizePolicy(sizePolicy)
        self.groupBox_pessoa.setCheckable(False)
        self.groupBox_pessoa.setObjectName("groupBox_pessoa")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_pessoa)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_pessoa_documento = QtWidgets.QLineEdit(self.groupBox_pessoa)
        self.lineEdit_pessoa_documento.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_pessoa_documento.setObjectName("lineEdit_pessoa_documento")
        self.horizontalLayout_2.addWidget(self.lineEdit_pessoa_documento)
        self.lineEdit_pessoa = QtWidgets.QLineEdit(self.groupBox_pessoa)
        self.lineEdit_pessoa.setEnabled(False)
        self.lineEdit_pessoa.setObjectName("lineEdit_pessoa")
        self.horizontalLayout_2.addWidget(self.lineEdit_pessoa)
        self.verticalLayout_5.addWidget(self.groupBox_pessoa)
        self.widget_4 = QtWidgets.QWidget(self.frame_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_entrada = QtWidgets.QGroupBox(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_entrada.sizePolicy().hasHeightForWidth())
        self.groupBox_entrada.setSizePolicy(sizePolicy)
        self.groupBox_entrada.setCheckable(True)
        self.groupBox_entrada.setChecked(False)
        self.groupBox_entrada.setObjectName("groupBox_entrada")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_entrada)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit_data_entrada1 = QtWidgets.QDateEdit(self.groupBox_entrada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_data_entrada1.sizePolicy().hasHeightForWidth())
        self.dateEdit_data_entrada1.setSizePolicy(sizePolicy)
        self.dateEdit_data_entrada1.setWrapping(False)
        self.dateEdit_data_entrada1.setFrame(False)
        self.dateEdit_data_entrada1.setReadOnly(False)
        self.dateEdit_data_entrada1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_data_entrada1.setCalendarPopup(True)
        self.dateEdit_data_entrada1.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit_data_entrada1.setObjectName("dateEdit_data_entrada1")
        self.horizontalLayout.addWidget(self.dateEdit_data_entrada1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_entrada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateEdit_data_entrada2 = QtWidgets.QDateEdit(self.groupBox_entrada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_data_entrada2.sizePolicy().hasHeightForWidth())
        self.dateEdit_data_entrada2.setSizePolicy(sizePolicy)
        self.dateEdit_data_entrada2.setWrapping(False)
        self.dateEdit_data_entrada2.setFrame(False)
        self.dateEdit_data_entrada2.setReadOnly(False)
        self.dateEdit_data_entrada2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_data_entrada2.setCalendarPopup(True)
        self.dateEdit_data_entrada2.setDate(QtCore.QDate(2019, 12, 31))
        self.dateEdit_data_entrada2.setObjectName("dateEdit_data_entrada2")
        self.horizontalLayout.addWidget(self.dateEdit_data_entrada2)
        self.horizontalLayout_6.addWidget(self.groupBox_entrada)
        self.groupBox_saida = QtWidgets.QGroupBox(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_saida.sizePolicy().hasHeightForWidth())
        self.groupBox_saida.setSizePolicy(sizePolicy)
        self.groupBox_saida.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_saida.setCheckable(True)
        self.groupBox_saida.setChecked(False)
        self.groupBox_saida.setObjectName("groupBox_saida")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_saida)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateEdit_data_saida1 = QtWidgets.QDateEdit(self.groupBox_saida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_data_saida1.sizePolicy().hasHeightForWidth())
        self.dateEdit_data_saida1.setSizePolicy(sizePolicy)
        self.dateEdit_data_saida1.setWrapping(False)
        self.dateEdit_data_saida1.setFrame(False)
        self.dateEdit_data_saida1.setReadOnly(False)
        self.dateEdit_data_saida1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_data_saida1.setCalendarPopup(True)
        self.dateEdit_data_saida1.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit_data_saida1.setObjectName("dateEdit_data_saida1")
        self.horizontalLayout_4.addWidget(self.dateEdit_data_saida1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_saida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.dateEdit_data_saida2 = QtWidgets.QDateEdit(self.groupBox_saida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_data_saida2.sizePolicy().hasHeightForWidth())
        self.dateEdit_data_saida2.setSizePolicy(sizePolicy)
        self.dateEdit_data_saida2.setWrapping(False)
        self.dateEdit_data_saida2.setFrame(False)
        self.dateEdit_data_saida2.setReadOnly(False)
        self.dateEdit_data_saida2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_data_saida2.setCalendarPopup(True)
        self.dateEdit_data_saida2.setDate(QtCore.QDate(2019, 12, 31))
        self.dateEdit_data_saida2.setObjectName("dateEdit_data_saida2")
        self.horizontalLayout_4.addWidget(self.dateEdit_data_saida2)
        self.horizontalLayout_6.addWidget(self.groupBox_saida)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.formFrame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(FiltroPedido)
        QtCore.QMetaObject.connectSlotsByName(FiltroPedido)

    def retranslateUi(self, FiltroPedido):
        FiltroPedido.setWindowTitle(QtWidgets.QApplication.translate("FiltroPedido", "Filtro de Pedido", None, -1))
        self.groupBox_pessoa.setTitle(QtWidgets.QApplication.translate("FiltroPedido", "Fornecedor", None, -1))
        self.groupBox_entrada.setTitle(QtWidgets.QApplication.translate("FiltroPedido", "Data do pedido", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("FiltroPedido", "até", None, -1))
        self.groupBox_saida.setTitle(QtWidgets.QApplication.translate("FiltroPedido", "Data para entrega", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("FiltroPedido", "até", None, -1))

