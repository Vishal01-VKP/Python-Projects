from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys
import STT_Main


class Sub(QtWidgets.QDialog):

    def __init__(self):
        super(Sub, self).__init__()

        uic.loadUi("Speed_Typing_Report.ui",self)

        self.wpm = STT_Main.window.correct_words
        self.cpm = STT_Main.window.correct_characters

        self.label_3.setText(str(self.wpm))
        self.label_5.setText(str(self.cpm))

        if self.wpm < 25:
            self.label_6.setText("Needs improvement .")

        elif 25 < self.wpm < 50:
            self.label_6.setText("Well done .")

        elif 50 < self.wpm:
            self.label_6.setText("Excellent !") 

        self.show()