# This is just a template to provide logic to a '.ui' file . Do not run this file .

from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys


class Class(x): # 'x' can either be 'QtWidgets.QMainWindow' or 'QtWidgets.QDialog'

    def __init__(self):
        super(Class, self).__init__()

        uic.loadUi("")

        self.show()

    # Other functions will be written below this function , in this indentation .

app = QtWidgets.QApplication(sys.argv)
window = Class()
app.exec_() # This will execute the application you've made .