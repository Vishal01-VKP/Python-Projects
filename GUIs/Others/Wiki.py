from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys
import wikipedia
import requests


class Class(QtWidgets.QDialog):

    def __init__(self):
        super(Class, self).__init__()

        uic.loadUi("Wiki.ui", self)

        self.pushButton.clicked.connect(self.search)

        self.show()


    def search(self):
        self.text = self.lineEdit.text()

        try:
            self.summary = wikipedia.summary(self.text, sentences=4)
            self.textBrowser.setText(self.summary)

        except wikipedia.exceptions.DisambiguationError as error1:
            self.textBrowser.setText(f"Can't print result . Try referring it's type in brackets . For example : Use India (country) insstead of India . \n\n{error1}")

        except requests.exceptions.ConnectionError as error2:
            self.textBrowser.setText("No Internet Connection !")


app = QtWidgets.QApplication(sys.argv)
window = Class()
app.exec_()