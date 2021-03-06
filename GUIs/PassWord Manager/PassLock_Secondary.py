# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PassLock_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 61, 341, 211))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Californian FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(370, 60, 20, 211))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.listWidget.setVerticalScrollBar(self.verticalScrollBar)

        def conversion(binary):
            def bin_to_int(binary):
                string = int(binary, 2)
                return string

            result = ''

            for i in range(0, len(binary), 7):
                temp_data = binary[i:i+7]
                decimal_data = bin_to_int(temp_data)
                result = result + chr(decimal_data)

            return result


        with open("Passwords.txt", "r") as read:
            data = read.read().split("\n")
            for i in data:
                x = conversion(i)
                self.listWidget.addItem(x)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password Storage"))
        self.label.setText(_translate("Dialog", "Passwords :"))

