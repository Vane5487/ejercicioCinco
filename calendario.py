# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendario.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venCalendar(object):
    def setupUi(self, venCalendar):
        venCalendar.setObjectName("venCalendar")
        venCalendar.resize(400, 300)
        self.calendar = QtWidgets.QCalendarWidget(venCalendar)
        self.calendar.setGeometry(QtCore.QRect(1, 2, 391, 291))
        self.calendar.setObjectName("calendar")

        self.retranslateUi(venCalendar)
        QtCore.QMetaObject.connectSlotsByName(venCalendar)

    def retranslateUi(self, venCalendar):
        _translate = QtCore.QCoreApplication.translate
        venCalendar.setWindowTitle(_translate("venCalendar", "Dialog"))
