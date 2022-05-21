from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys


class DetailsWindow(QtWidgets.QDialog):
    def __init__(self):
        super(DetailsWindow, self).__init__()

        uic.loadUi("StopWatch_Details.ui", self)

        with open("TimeRecords.txt", "r") as reader:
            records = reader.read()

        self.textBrowser.setText(records)

        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DetailsWindow()
    app.exec_()