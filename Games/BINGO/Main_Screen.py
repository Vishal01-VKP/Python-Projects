from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from BINGO import BINGO_App
from Play_Friends import IntroWindow


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi("Main.ui", self)

        self.pushButton.clicked.connect(self.play_against_AI)
        self.pushButton_2.clicked.connect(self.play_with_friends)

        self.show()


    def play_against_AI(self):
        screen1 = BINGO_App()
        screen1.exec_()


    def play_with_friends(self):
        screen2 = IntroWindow()
        screen2.exec_()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()