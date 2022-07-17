from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup
import random
import questions
from Quiz_Details import Ui_Dialog as Details


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 50))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 360, 110))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 220, 360, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 150, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 30, 150, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 70, 150, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 70, 150, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 350, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 350, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 350, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 10, 180, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 20, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Quiz !"))
        self.groupBox.setTitle(_translate("Dialog", "Options :"))
        self.pushButton_5.setText(_translate("Dialog", "Save and Next"))
        self.pushButton_6.setText(_translate("Dialog", "View"))
        self.pushButton_7.setText(_translate("Dialog", "Submit"))
        self.groupBox_2.setTitle(_translate("Dialog", "Time Left :"))

        self.pushButton_5.clicked.connect(lambda: self.save_and_next(self.selected_button))
        self.pushButton_6.clicked.connect(self.view)
        self.pushButton_7.clicked.connect(lambda: self.submit(self.selected_button))

        self.buttons_list = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4]

        self.seconds = 0
        self.minutes = 10

        self.run = True

        self.score = 0
        self.increment = 0

        random.shuffle(questions.questions)

        for i in range(10):
            questions.number = i
            questions.number = questions.questions[0][0]

        for i in self.buttons_list:
            i.setText(questions.questions[questions.number][2+self.increment])
            self.increment += 1
            i.clicked.connect(self.button_clicked)

        question_text = f"Question {questions.number+1} : {questions.questions[questions.number][1]}"
        self.textBrowser.setText(question_text)
        self.textBrowser_2.setText(f"{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}")

        timer = QtCore.QTimer(Dialog)
        timer.timeout.connect(self.timing)
        timer.start(1000)


    def timing(self):
        if self.run == True:
            if self.seconds == 0:
                self.minutes -= 1
                self.seconds += 60

            elif self.minutes == self.seconds == 0:
                self.save()
                self.submit(self.selected_button)

                self.textBrowser.setText("Time's Up !")
                self.textBrowser_2.setText("Time's Up !")

            self.seconds -= 1
            self.textBrowser_2.setText(f"{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}")

        else:
            pass


    def button_clicked(self):
        self.sender = Dialog.sender()
        self.selected_button = self.sender


    def save_and_next(self, button):
        if questions.number == 9:
            self.submit(self.selected_button)

        else:
            with open("Quiz_Data.txt","a") as writer:
                writer.write(f"Question {questions.number+1} : {questions.questions[questions.number][1]}\n\na. {self.pushButton.text()}\nb. {self.pushButton_2.text()}\nc. {self.pushButton_3.text()}\nd. {self.pushButton_4.text()}\n\nYour Answer : {button.text()}\nCorrect Answer : {questions.questions[questions.number][6]}\n\n{'='*81}\n\n")

            with open("temp_data.txt","a") as writer:
                writer.write(f"Question {questions.number+1} : {questions.questions[questions.number][1]}\n\na. {self.pushButton.text()}\nb. {self.pushButton_2.text()}\nc. {self.pushButton_3.text()}\nd. {self.pushButton_4.text()}\n\nYour Answer : {button.text()}\nCorrect Answer : {questions.questions[questions.number][6]}\n\n{'='*81}\n\n")

            if button.text() == questions.questions[questions.number][6]:
                self.score += 1        
        
            questions.number += 1
            question_text = f"Question {questions.number+1} : {questions.questions[questions.number][1]}"
            self.textBrowser.setText(question_text)

            self.increase = 0

            for i in self.buttons_list:
                i.setText(questions.questions[questions.number][2+self.increase])
                self.increase += 1


    def view(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Details()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()
    

    def submit(self, button):
        self.run = False

        self.pushButton_5.setDisabled(True)
        self.pushButton_7.setDisabled(True)

        with open("Quiz_Data.txt","a+") as writer:
            writer.write(f"Question {questions.number+1} : {questions.questions[questions.number][1]}\n\na. {self.pushButton.text()}\nb. {self.pushButton_2.text()}\nc. {self.pushButton_3.text()}\nd. {self.pushButton_4.text()}\n\nYour Answer : {button.text()}\nCorrect Answer : {questions.questions[questions.number][6]}\n\n{'='*81}\n\n")

        with open("temp_data.txt","a") as writer:
            writer.write(f"Question {questions.number+1} : {questions.questions[questions.number][1]}\n\na. {self.pushButton.text()}\nb. {self.pushButton_2.text()}\nc. {self.pushButton_3.text()}\nd. {self.pushButton_4.text()}\n\nYour Answer : {button.text()}\nCorrect Answer : {questions.questions[questions.number][6]}\n\n{'='*81}\n\n")        

        if button.text() == questions.questions[questions.number][6]:
            self.score += 1
            
        for i in self.buttons_list:
            i.setDisabled(True)
            i.setText("")

        self.textBrowser.setText(f"Your Score : {self.score}\n\nFor more details , click 'View' .")
 
        with open("temp_data.txt","w") as reader:
            reader.truncate()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
