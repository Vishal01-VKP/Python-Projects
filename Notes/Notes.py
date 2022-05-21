from PyQt5 import QtCore, QtGui, QtWidgets, uic
import Fonts

import sys
import os


class Notes(QtWidgets.QMainWindow):
    def __init__(self):
        super(Notes, self).__init__()

        uic.loadUi("Notes-1.ui", self)

        self.path = None

        self.menuFonts.aboutToShow.connect(self.new_screen)
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

        self.textBox = self.textEdit.toPlainText()

        self.show()


    def new_screen(self):
        dialog = Fonts.Fonts(Notes.Notes)
        dialog.exec_()


    def open_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Text Documents (*.txt)")

        if path:
            with open(path[0], "r") as f:
                text = f.read()

            self.path = path[0]
            self.textEdit.setText(text)


    def save_file(self):
        if self.path is None:
            return self.save_as_option()

        self.save_option(self.path)


    def save_option(self, path):
        text = self.textBox

        with open(path[0], "w") as f:
            f.write(text)

            self.path = path[0]


    def save_as_option(self):
        path =  QFileDialog.getSaveFileName(self, "Save File", "", "Text Documents (*.txt)")

        if not path:
            return

        self.save_option(path)


    def new_file(self):
        self.path = None
        self.textEdit.clear()


app = QtWidgets.QApplication(sys.argv)
ui = Notes()
app.exec_()