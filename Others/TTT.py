# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TTT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random
from functools import partial
from PyQt5.QtGui import QPainter, QBrush, QPen


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 360, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 360, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 100, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 100, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 100, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 170, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 170, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(230, 170, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 240, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(160, 240, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(230, 240, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(110, 360, 170, 30))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_1.setText(_translate("Dialog", "Play !"))
        self.pushButton_2.setText(_translate("Dialog", "Reset"))
        self.label.setText(_translate("Dialog", "Play against bot !"))

        self.pushButton_1.clicked.connect(self.game_start)
        self.pushButton_2.clicked.connect(self.reset)

        self.your_sign = "O"
        self.bot_sign = "X"

        self.grand_list = [self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10, self.pushButton_11]
        self.increment = 0

        for i in self.grand_list:
            i.setStyleSheet('QPushButton {background-color: white; color: white}')
            i.clicked.connect(partial(self.gameplay, i))
            i.setText(f"{self.increment}")

            self.increment += 1

        self.numbers = [0,1,2,3,4,5,6,7,8]

    def game_start(self):
        self.bot_choice = int(random.choice(self.numbers))

        self.grand_list[self.bot_choice].setText(self.bot_sign)
        self.grand_list[self.bot_choice].setStyleSheet('QPushButton {background-color: white; color: black}')
        self.numbers.remove(self.bot_choice)

        self.pushButton_1.setDisabled(True)

    def gameplay(self, button):
        if self.pushButton_1.isEnabled() == "False":
            self.your_sign = "O" ; self.bot_sign = "X"
        elif self.pushButton_1.isEnabled() == "True":
            self.your_sign = "X" ; self.bot_sign = "O"

        self.position = int(button.text())
        self.grand_list[self.position].setText(self.your_sign)
        self.grand_list[self.position].setStyleSheet('QPushButton {background-color: white; color: black}')
        self.numbers.remove(self.position)

        def win_check(self):
            box1 = self.pushButton_3.text() ; box2 = self.pushButton_4.text() ; box3 = self.pushButton_5.text() ; 
            box4 = self.pushButton_6.text() ; box5 = self.pushButton_7.text() ; box6 = self.pushButton_8.text() ; 
            box7 = self.pushButton_9.text() ; box8 = self.pushButton_10.text() ; box9 = self.pushButton_11.text()

            self.win = "Neutral"

            if box1 == box2 == box3 == "O" : self.win = "True"
            if box1 == box2 == box3 == "X" : self.win = "False"

            if box4 == box5 == box6 == "O" : self.win = "True"
            if box4 == box5 == box6 == "X" : self.win = "False"

            if box7 == box8 == box9 == "O" : self.win = "True"
            if box7 == box8 == box9 == "X" : self.win = "False"

            if box1 == box4 == box7 == "O" : self.win = "True"
            if box1 == box4 == box7 == "X" : self.win = "False"

            if box2 == box5 == box8 == "O" : self.win = "True"
            if box2 == box5 == box8 == "X" : self.win = "False"

            if box3 == box6 == box9 == "O" : self.win = "True"
            if box3 == box6 == box9 == "X" : self.win = "False"

            if box1 == box5 == box9 == "O" : self.win = "True"
            if box1 == box5 == box9 == "X" : self.win = "False"

            if box3 == box5 == box7 == "O" : self.win = "True"
            if box3 == box5 == box7 == "X" : self.win = "False"

        win_check(self)

        if self.win == "True":
            self.textBrowser.setText("You won the match")

        elif len(self.numbers) == 0 and self.win == "Neutral":
            self.textBrowser.setText("It's a draw")

        else:
            self.bot_choice = int(random.choice(self.numbers))
            self.grand_list[self.bot_choice].setText(self.bot_sign)
            self.grand_list[self.bot_choice].setStyleSheet('QPushButton {background-color: white; color: black}')
            self.numbers.remove(self.bot_choice)

            win_check(self)

            if self.win == "False":
                self.textBrowser.setText("You lost the match")

            elif len(self.numbers) == 0 and self.win == "Neutral":
                self.textBrowser.setText("It's a draw")

        self.pushButton_1.setDisabled(True)


    def reset(self):
        self.increment = 0

        for i in self.grand_list:
            i.setStyleSheet('QPushButton {background-color: white; color: white}')
            i.setText(f"{self.increment}")

            self.increment += 1

        self.numbers = [0,1,2,3,4,5,6,7,8]
        self.textBrowser.setText("")

        self.pushButton_1.setDisabled(False)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
