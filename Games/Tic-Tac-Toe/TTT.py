from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import random
from functools import partial
from PyQt5.QtGui import QPainter, QBrush, QPen


class TTT_App(QtWidgets.QDialog):
    def __init__(self):
        super(TTT_App, self).__init__()

        uic.loadUi("TTT.ui", self)

        self.you = "X"

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Times New Roman")

        self.textBrowser.setFont(font)

        self.pushButton_01.clicked.connect(self.game_start)
        self.pushButton_02.clicked.connect(self.reset)

        self.your_sign = "O"
        self.bot_sign = "X"

        self.grand_list = [self.pushButton_03, self.pushButton_04, self.pushButton_05, self.pushButton_06, self.pushButton_07, self.pushButton_08, self.pushButton_09, self.pushButton_10, self.pushButton_11]

        self.increment = 0

        for i in self.grand_list:
            i.setStyleSheet('QPushButton {background-color: white; color: white}')
            i.clicked.connect(partial(self.gameplay, i))
            i.setText(f"{self.increment}")

            self.increment += 1

        self.numbers = [0,1,2,3,4,5,6,7,8]

        self.show()

    def game_start(self):
        self.bot_sign = "X"
        self.you = "O"

        self.bot_choice = int(random.choice(self.numbers))

        self.grand_list[self.bot_choice].setText(self.bot_sign)
        self.grand_list[self.bot_choice].setStyleSheet('QPushButton {background-color: white; color: black}')
        self.numbers.remove(self.bot_choice)

        self.pushButton_01.setDisabled(True)

    def gameplay(self, button):
        if self.you == "O":
            self.your_sign = "O" ; self.bot_sign = "X"
        elif self.you == "X":
            self.your_sign = "X" ; self.bot_sign = "O"

        self.position = int(button.text())
        self.grand_list[self.position].setText(self.your_sign)
        self.grand_list[self.position].setStyleSheet('QPushButton {background-color: white; color: black}')
        self.numbers.remove(self.position)

        def win_check(self):
            box1 = self.pushButton_03.text() ; box2 = self.pushButton_04.text() ; box3 = self.pushButton_05.text() ; 
            box4 = self.pushButton_06.text() ; box5 = self.pushButton_07.text() ; box6 = self.pushButton_08.text() ; 
            box7 = self.pushButton_09.text() ; box8 = self.pushButton_10.text() ; box9 = self.pushButton_11.text()

            self.win = "Neutral"

            if box1 == box2 == box3 == self.you : self.win = "True"
            if box1 == box2 == box3 != self.you : self.win = "False"

            if box4 == box5 == box6 == self.you : self.win = "True"
            if box4 == box5 == box6 != self.you : self.win = "False"

            if box7 == box8 == box9 == self.you : self.win = "True"
            if box7 == box8 == box9 != self.you : self.win = "False"

            if box1 == box4 == box7 == self.you : self.win = "True"
            if box1 == box4 == box7 != self.you : self.win = "False"

            if box2 == box5 == box8 == self.you : self.win = "True"
            if box2 == box5 == box8 != self.you : self.win = "False"

            if box3 == box6 == box9 == self.you : self.win = "True"
            if box3 == box6 == box9 != self.you : self.win = "False"

            if box1 == box5 == box9 == self.you : self.win = "True"
            if box1 == box5 == box9 != self.you : self.win = "False"

            if box3 == box5 == box7 == self.you : self.win = "True"
            if box3 == box5 == box7 != self.you : self.win = "False"

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

        self.pushButton_01.setDisabled(True)


    def reset(self):
        self.increment = 0

        for i in self.grand_list:
            i.setStyleSheet('QPushButton {background-color: white; color: white}')
            i.setText(f"{self.increment}")

            self.increment += 1

        self.numbers = [0,1,2,3,4,5,6,7,8]
        self.textBrowser.setText("")

        self.pushButton_01.setDisabled(False)
        

app = QtWidgets.QApplication(sys.argv)
window = TTT_App()
app.exec_()