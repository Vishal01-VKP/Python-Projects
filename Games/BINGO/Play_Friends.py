from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from Game_Screen_PWF import GameWindow


class IntroWindow(QtWidgets.QDialog):
    def __init__(self):
        super(IntroWindow, self).__init__()

        uic.loadUi("Play_Friends.ui", self)

        self.database = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5, 
                        self.lineEdit_6, self.lineEdit_7, self.lineEdit_8, self.lineEdit_9, self.lineEdit_10]

        self.pushButton_11.clicked.connect(self.play_with_friends)

        self.show()


    def play_with_friends(self):
        with open("GameData.txt","w") as writer:
            for i in self.database:
                if i != "":
                    writer.write(i)

        screen1 = GameWindow()
        screen1.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = IntroWindow()
    app.exec_()