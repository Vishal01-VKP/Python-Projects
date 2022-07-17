from PyQt5 import QtWidgets, QtGui, QtCore, uic

import sys
import webbrowser

import StopWatch_Main as Main
import StopWatch_Storage as Store
import StopWatch_Details as Details
import Timer


class ClockWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ClockWindow, self).__init__()

        uic.loadUi("Clock.ui", self)

        self.pushButton.clicked.connect(self.func1)
        self.pushButton_2.clicked.connect(self.func2)
        self.pushButton_3.clicked.connect(self.func3)
        self.pushButton_4.clicked.connect(self.func4)
        self.pushButton_6.clicked.connect(self.func5)

        self.show()


    def func1(self):
        function1 = Timer.TimerWindow()
        function1.exec_()


    def func2(self):
        function2 = Main.StopWatch_Main()
        function2.exec_()


    def func3(self):
        function3 = Store.StopWatch_Storage()
        function3.exec_()


    def func4(self):
        function4 = Details.DetailsWindow()
        function4.exec_()


    def func5(self):
        webbrowser.open("www.vkp001.blogspot.com")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ClockWindow()
    app.exec_()