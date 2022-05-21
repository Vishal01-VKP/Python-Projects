from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import random
import functools


class GameWindow(QtWidgets.QDialog):
    def __init__(self):
        super(GameWindow, self).__init__()

        uic.loadUi("Game_Screen_PWF.ui", self)

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)

        self.numbers_list = []
        for num in range(1,26):self.numbers_list.append(str(num).zfill(2))
        random.shuffle(self.numbers_list)

        self.buttons_list = {num:QtWidgets.QPushButton(self.frame) for num in range(1,26)}

        for i in range(25):
            self.buttons_list[i+1].setGeometry((i//5)*60, (i%5)*60, 60, 60)
            self.buttons_list[i+1].setText(self.numbers_list[i])
            self.buttons_list[i+1].clicked.connect(functools.partial(self.play, self.buttons_list[i+1]))
            self.buttons_list[i+1].setAutoDefault(False)
            self.buttons_list[i+1].setFont(font)

        self.show()


    def play(self,button):
        button.setStyleSheet("QPushButton { color : blue }")
        button.setText("XX")

        self.verify()


    def verify(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow()
    app.exec_()