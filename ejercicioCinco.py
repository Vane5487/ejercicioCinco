# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejercicioCinco.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1088, 891)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(110, 160, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.lblApelido = QtWidgets.QLabel(self.centralwidget)
        self.lblApelido.setGeometry(QtCore.QRect(110, 220, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblApelido.setFont(font)
        self.lblApelido.setObjectName("lblApelido")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setEnabled(True)
        self.lblNome.setGeometry(QtCore.QRect(450, 220, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(320, 440, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(480, 440, 75, 23))
        self.btnSalir.setObjectName("btnSalir")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 410, 641, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 90, 641, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDNI.setGeometry(QtCore.QRect(180, 160, 113, 20))
        self.lineDNI.setObjectName("lineDNI")
        self.lineApelidos = QtWidgets.QLineEdit(self.centralwidget)
        self.lineApelidos.setGeometry(QtCore.QRect(180, 220, 251, 21))
        self.lineApelidos.setObjectName("lineApelidos")
        self.lineNome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNome.setGeometry(QtCore.QRect(500, 220, 251, 20))
        self.lineNome.setObjectName("lineNome")
        self.lblVal = QtWidgets.QLabel(self.centralwidget)
        self.lblVal.setGeometry(QtCore.QRect(300, 160, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(14)
        self.lblVal.setFont(font)
        self.lblVal.setText("")
        self.lblVal.setObjectName("lblVal")
        self.lblSexo = QtWidgets.QLabel(self.centralwidget)
        self.lblSexo.setGeometry(QtCore.QRect(110, 340, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.lblPago = QtWidgets.QLabel(self.centralwidget)
        self.lblPago.setGeometry(QtCore.QRect(410, 340, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setMouseTracking(False)
        self.lblPago.setTabletTracking(False)
        self.lblPago.setObjectName("lblPago")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 280, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineApelidos_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineApelidos_2.setGeometry(QtCore.QRect(180, 280, 251, 21))
        self.lineApelidos_2.setObjectName("lineApelidos_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 280, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cmbProv = QtWidgets.QComboBox(self.centralwidget)
        self.cmbProv.setGeometry(QtCore.QRect(520, 280, 231, 22))
        self.cmbProv.setObjectName("cmbProv")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(530, 340, 223, 19))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horlayPago = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horlayPago.setContentsMargins(0, 0, 0, 0)
        self.horlayPago.setObjectName("horlayPago")
        self.cbEfectivo = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbEfectivo.setObjectName("cbEfectivo")
        self.horlayPago.addWidget(self.cbEfectivo)
        self.cbTarjeta = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbTarjeta.setObjectName("cbTarjeta")
        self.horlayPago.addWidget(self.cbTarjeta)
        self.cbTarnsferencia = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbTarnsferencia.setObjectName("cbTarnsferencia")
        self.horlayPago.addWidget(self.cbTarnsferencia)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(180, 340, 146, 19))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horlaySex = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horlaySex.setContentsMargins(0, 0, 0, 0)
        self.horlaySex.setObjectName("horlaySex")
        self.rbtRemenino = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbtRemenino.setObjectName("rbtRemenino")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbtRemenino)
        self.horlaySex.addWidget(self.rbtRemenino)
        self.rbtMasculino = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbtMasculino.setObjectName("rbtMasculino")
        self.buttonGroup.addButton(self.rbtMasculino)
        self.horlaySex.addWidget(self.rbtMasculino)
        self.lblCalendar = QtWidgets.QLabel(self.centralwidget)
        self.lblCalendar.setGeometry(QtCore.QRect(330, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCalendar.setFont(font)
        self.lblCalendar.setObjectName("lblCalendar")
        self.lineCalendar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCalendar.setGeometry(QtCore.QRect(410, 160, 151, 20))
        self.lineCalendar.setObjectName("lineCalendar")
        self.btnCalendar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalendar.setGeometry(QtCore.QRect(570, 160, 21, 21))
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calendario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setObjectName("btnCalendar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.lblApelido.setText(_translate("MainWindow", "Apelidos:"))
        self.lblNome.setText(_translate("MainWindow", "Nome:"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.label_4.setText(_translate("MainWindow", "XESTION CLIENTES"))
        self.lblSexo.setText(_translate("MainWindow", "Sexo:"))
        self.lblPago.setText(_translate("MainWindow", "Métodos de Pago:"))
        self.label.setText(_translate("MainWindow", "Dirección:"))
        self.label_2.setText(_translate("MainWindow", "Provincia:"))
        self.cbEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.cbTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.cbTarnsferencia.setText(_translate("MainWindow", "Transferencia"))
        self.rbtRemenino.setText(_translate("MainWindow", "Femenino"))
        self.rbtMasculino.setText(_translate("MainWindow", "Masculino"))
        self.lblCalendar.setText(_translate("MainWindow", "Fecha Alta:"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+S"))
