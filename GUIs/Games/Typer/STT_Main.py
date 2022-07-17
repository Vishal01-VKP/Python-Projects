from PyQt5 import QtWidgets, QtGui, QtCore, uic

import sys
import random
import string
import re
import webbrowser

import STT_Report as STR


class Class(QtWidgets.QDialog):
    def __init__(self):
        super(Class, self).__init__()

        uic.loadUi("Speed_Typing_Test.ui", self)

        self.run = False

        self.correct_words = 0
        self.correct_characters = 0

        self.seconds = 61 ; self.milliseconds = 0

        self.back_end()
            
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.start)
        timer.start(10)

        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)

        self.plainTextEdit.setReadOnly(True)
        
        self.pushButton.clicked.connect(self.initiate)
        self.pushButton_2.clicked.connect(self.blog)
        self.pushButton_3.clicked.connect(self.github)

        self.show()


    def back_end(self):
        with open("Sample.txt", "r", encoding="utf-8") as sample:
            self.word_list = sample.read().split(" ")

            for i in self.word_list:
                if len(i) < 3 or len(i) > 7:
                    self.word_list.remove(i)

            random.shuffle(self.word_list)

            self.word_list = set(self.word_list)
            self.word_list = list(self.word_list)

            self.word_list = [''.join(e for e in string if e.isalnum()) for string in self.word_list]

            for i in range(len(self.word_list)):
                self.word_list[i] += ' '

            self.word_list = ''.join(map(str, self.word_list))
            self.textBrowser.setText(self.word_list[:1500])


    def initiate(self):
        self.run = True
        

    def start(self):
        if self.run == True:
            self.plainTextEdit.setReadOnly(False)
            
            if self.seconds == self.milliseconds == 0:
                self.check()

                dialog = STR.Sub()
                dialog.exec_()

                self.run = False
                self.reset()

                self.word_list = self.word_list.split(" ")

                for i in range(len(self.word_list)):
                    self.word_list[i] += ' '

                random.shuffle(self.word_list)

                self.word_list = ''.join(map(str, self.word_list))
                self.textBrowser.setText(self.word_list[:1500])
                


            else:
                if self.milliseconds == 0:
                    self.seconds -= 1
                    self.milliseconds += 99

                else:
                    self.milliseconds -= 1

                self.textBrowser_2.setText(f"{str(self.seconds).zfill(2)}:{str(self.milliseconds).zfill(2)}")


        else:
            pass


    def check(self):
        self.words = self.plainTextEdit.toPlainText().split(" ")
        self.copy_list = []

        self.listed_words = self.word_list.split(" ")

        for i in self.words:
            if i == self.listed_words[self.words.index(i)]:
                self.correct_words += 1
                self.copy_list.append(i)

            else:
                self.correct_words += 0

        self.resultant = ''.join(map(str, self.copy_list))

        self.correct_characters += len(self.resultant)


    def reset(self):
        self.back_end()

        self.correct_words = 0 ; self.correct_characters = 0
        self.seconds = 61 ; self.milliseconds = 0

        self.plainTextEdit.clear()
        self.plainTextEdit.setReadOnly(True)
        self.textBrowser_2.setText("61:00")

        self.pushButton.clicked.connect(self.initiate)


    def blog(self):
        webbrowser.open("www.vkpythonprojects.blogspot.com")


    def github(self):
        webbrowser.open("https://github.com/Vishal01-VKP/Python-Projects")


app = QtWidgets.QApplication(sys.argv)
window = Class()
app.exec_()