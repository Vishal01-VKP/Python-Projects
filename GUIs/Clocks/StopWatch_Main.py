from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QTimer
from StopWatch_Storage import StopWatch_Storage as Store

import sys


class StopWatch_Main(QtWidgets.QDialog):
    def __init__(self):
        super(StopWatch_Main, self).__init__()

        uic.loadUi("StopWatch_Main.ui", self)

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.reset)
        self.pushButton_3.clicked.connect(self.save_time)

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        self.run = False

        font = QtGui.QFont()
        font.setPointSize(19)
        font.setFamily("Times New Roman")
        font.setBold(True)

        self.textBrowser.setFont(font)
        self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}:{str(self.milliseconds).zfill(2)}")
        self.textBrowser.setStyleSheet("QTextBrowser {color : black}")

        timer = QTimer(self)
        timer.timeout.connect(self.run_watch)
        timer.start(10)

        self.show()


    def start(self):
        if self.pushButton.text() == "Stop":
            self.run = False
            self.pushButton.setText("Start")
            self.textBrowser.setStyleSheet("QTextBrowser {color : red}")

        else:
            self.run = True
            self.pushButton.setText("Stop")


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
            self.textBrowser.setStyleSheet("QTextBrowser {color : blue}")


    def reset(self):
        self.run = False
        self.pushButton.setText("Start")

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        self.textBrowser.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}:{str(self.milliseconds).zfill(2)}")
        self.textBrowser.setStyleSheet("QTextBrowser {color : black}")


    def save_time(self):
        dialog = Store()
        dialog.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StopWatch_Main()
    app.exec_()