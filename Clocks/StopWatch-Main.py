# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StopWatch-Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from StopWatch_Storage import Ui_Dialog as Store


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(60, 130, 280, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(40, 190, 320, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(360, 110, 3, 80))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(40, 110, 320, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(40, 110, 3, 80))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 230, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 230, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 230, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        self.textBrowser.setFont(font)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "StopWatch"))
        self.label.setText(_translate("Dialog", "Stop Watch"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.pushButton_2.setText(_translate("Dialog", "Reset"))
        self.pushButton_3.setText(_translate("Dialog", "Save"))

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.reset)
        self.pushButton_3.clicked.connect(self.save_time)

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        self.run = False

        self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}:{str(self.milliseconds).zfill(2)}")

        timer = QTimer(Dialog)
        timer.timeout.connect(self.run_watch)
        timer.start(10)

    def start(self):
        if self.pushButton.text() == "Stop":
            self.run = False
            self.pushButton.setText("Start")

        else:
            self.pushButton.setText("Stop")
            self.run = True

    def run_watch(self):
        if self.run == False:
            pass

        elif self.run == True:
            self.milliseconds += 1

            if self.milliseconds == 100:
                self.seconds += 1
                self.milliseconds -= 100

            if self.milliseconds == 100 and self.seconds == 60:
                self.minutes += 1
                self.seconds -= 60
                self.milliseconds -= 100

            elif self.milliseconds == 100 and self.minutes == self.seconds == 60:
                self.hours += 1
                self.minutes -= 60
                self.seconds -= 60
                self.milliseconds -= 100

            self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}:{str(self.milliseconds).zfill(2)}")

    def reset(self):
        self.run = False

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}:{str(self.milliseconds).zfill(2)}")

    def save_time(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Store()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())