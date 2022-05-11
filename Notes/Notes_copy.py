from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Fonts_copy import Fonts
from PyQt5.QtWidgets import QFileDialog

import sys
import os


class Notes(QtWidgets.QMainWindow, Fonts):
    def __init__(self):
        super(Notes, self).__init__()

        uic.loadUi("Notes-1.ui", self)

        self.path = None

        self.menuFonts.aboutToShow.connect(self.new_screen)
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.check_font)
        timer.start(100)

        self.set_title()

        self.show()


    def new_screen(self):
        dialog = Fonts()
        dialog.exec_()


    def open_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Text Documents (*.txt)")

        if path:
            with open(path[0], "r") as f:
                text = f.read()

            self.path = path[0]
            self.textEdit.setText(text)
            self.set_title()


    def save_file(self):
        if self.path is None:
            return self.save_as_option()

        self.save_option(self.path)


    def save_option(self, path):
        text = self.textEdit.toPlainText()

        with open(path[0], "w") as f:
            f.write(text)

            self.path = path[0]
            self.set_title()


    def save_as_option(self):
        path =  QFileDialog.getSaveFileName(self, "Save File", "", "Text Documents (*.txt)")

        if not path:
            return

        self.save_option(path)


    def set_title(self):
        self.setWindowTitle(f"{os.path.basename(self.path)} - Notes" if self.path else "Notes")


    def new_file(self):
        self.path = None
        self.textEdit.clear()


    def check_font(self):

        font = QtGui.QFont()
        
        with open("fonts_data.txt", "r") as reader:
            data = reader.read().split("\n")

            font.setFamily(data[0])
            font.setPointSize(int(data[1]))

            self.textEdit.setFont(font)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Notes()
    app.exec_()