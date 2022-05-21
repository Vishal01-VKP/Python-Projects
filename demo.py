from PyQt5 import QtWidgets, QtCore, QtGui, uic
import sys


class Main(QtWidgets.QDialog):
    def __init__(self):
        super(Main, self).__init__()

        uic.loadUi("demo.ui", self)

        buttons_list = {num:QtWidgets.QPushButton(self.frame) for num in range(36)}

        for i in range(36):
            buttons_list[i].setGeometry(60*(i//6),60*(i%6),60,60)
            buttons_list[i].setStyleSheet("QPushButton {background-color : white}")

        self.show()


app = QtWidgets.QApplication(sys.argv)
ui = Main()
app.exec_()