from PyQt5 import QtCore, QtGui, QtWidgets
import random
from functools import partial
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtGui import QPainter, QPen


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_01 = QtWidgets.QPushButton(Dialog)
        self.pushButton_01.setGeometry(QtCore.QRect(10, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_02 = QtWidgets.QPushButton(Dialog)
        self.pushButton_02.setGeometry(QtCore.QRect(60, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_03 = QtWidgets.QPushButton(Dialog)
        self.pushButton_03.setGeometry(QtCore.QRect(110, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setObjectName("pushButton_03")
        self.pushButton_04 = QtWidgets.QPushButton(Dialog)
        self.pushButton_04.setGeometry(QtCore.QRect(160, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_04.setFont(font)
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_05 = QtWidgets.QPushButton(Dialog)
        self.pushButton_05.setGeometry(QtCore.QRect(210, 70, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_05.setFont(font)
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_08 = QtWidgets.QPushButton(Dialog)
        self.pushButton_08.setGeometry(QtCore.QRect(110, 120, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_08.setFont(font)
        self.pushButton_08.setObjectName("pushButton_08")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 120, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_06 = QtWidgets.QPushButton(Dialog)
        self.pushButton_06.setGeometry(QtCore.QRect(10, 120, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_06.setFont(font)
        self.pushButton_06.setObjectName("pushButton_06")
        self.pushButton_09 = QtWidgets.QPushButton(Dialog)
        self.pushButton_09.setGeometry(QtCore.QRect(160, 120, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_09.setFont(font)
        self.pushButton_09.setObjectName("pushButton_09")
        self.pushButton_07 = QtWidgets.QPushButton(Dialog)
        self.pushButton_07.setGeometry(QtCore.QRect(60, 120, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_07.setFont(font)
        self.pushButton_07.setObjectName("pushButton_07")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 170, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(60, 170, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(110, 170, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(160, 170, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(210, 170, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(60, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(110, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(Dialog)
        self.pushButton_19.setGeometry(QtCore.QRect(160, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(210, 220, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(Dialog)
        self.pushButton_21.setGeometry(QtCore.QRect(10, 270, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(Dialog)
        self.pushButton_22.setGeometry(QtCore.QRect(60, 270, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(Dialog)
        self.pushButton_23.setGeometry(QtCore.QRect(110, 270, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(Dialog)
        self.pushButton_24.setGeometry(QtCore.QRect(160, 270, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(Dialog)
        self.pushButton_25.setGeometry(QtCore.QRect(210, 270, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setObjectName("pushButton_25")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(280, 70, 110, 250))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_A = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_A.setGeometry(QtCore.QRect(10, 50, 91, 41))
        self.pushButton_A.setObjectName("pushButton_A")
        self.pushButton_B = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_B.setGeometry(QtCore.QRect(10, 100, 91, 41))
        self.pushButton_B.setObjectName("pushButton_B")
        self.result_box = QtWidgets.QTextBrowser(self.groupBox)
        self.result_box.setGeometry(QtCore.QRect(10, 150, 90, 90))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.result_box.setFont(font)
        self.result_box.setObjectName("result_box")
        self.note_box = QtWidgets.QTextBrowser(Dialog)
        self.note_box.setGeometry(QtCore.QRect(10, 340, 380, 50))
        self.note_box.setObjectName("note_box")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BINGO !"))
        self.label.setText(_translate("Dialog", "Play BINGO against bot !"))

        self.groupBox.setTitle(_translate("Dialog", "Menu"))
        self.pushButton_A.setText(_translate("Dialog", "Start"))
        self.pushButton_B.setText(_translate("Dialog", "Reset"))
        self.result_box.setText(_translate("Dialog", "Points : 0"))
        self.note_box.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Note : Computer will </span><span style=\" font-size:12pt; font-weight:600;\">always</span><span style=\" font-size:12pt;\"> move first , and will be </span><span style=\" font-size:12pt; font-weight:600;\">considered the winner</span><span style=\" font-size:12pt;\"> if there\'s a tie .</span></p></body></html>"))

        self.pushButton_A.clicked.connect(self.game)
        self.pushButton_B.clicked.connect(self.reset)

        self.grand_list = [self.pushButton_01,self.pushButton_02,self.pushButton_03,self.pushButton_04,self.pushButton_05,self.pushButton_06,self.pushButton_07,self.pushButton_08,self.pushButton_09,self.pushButton_10,self.pushButton_11,self.pushButton_12,self.pushButton_13,self.pushButton_14,self.pushButton_15,self.pushButton_16,self.pushButton_17,self.pushButton_18,self.pushButton_19,self.pushButton_20,self.pushButton_21,self.pushButton_22,self.pushButton_23,self.pushButton_24,self.pushButton_25]

        for i in self.grand_list:
            i.setText("")
            i.clicked.connect(partial(self.play, i))

        self.numbers = [] ; self.numlist = [] ; self.botlist = [] ; self.removed = []

        self.var01 = True ; self.var02 = True ; self.var03 = True ; self.var04 = True ; self.var05 = True ; self.var06 = True
        self.var07 = True ; self.var08 = True ; self.var09 = True ; self.var10 = True ; self.var11 = True ; self.var12 = True 
        self.var13 = True ; self.var14 = True ; self.var15 = True ; self.var16 = True ; self.var17 = True ; self.var18 = True 
        self.var19 = True ; self.var20 = True ; self.var21 = True ; self.var22 = True ; self.var23 = True ; self.var24 = True

        self.bot_points = 0 ; self.my_points = 0

        for i in range(1,26):
            self.numlist.append(str(i).zfill(2)) ; self.botlist.append(str(i).zfill(2)) ; self.numbers.append(i)

        random.shuffle(self.numlist) ; random.shuffle(self.botlist)            

    def game(self):
        self.pushButton_A.setDisabled(True)

        for i in range(25):
            self.grand_list[i].setText(self.numlist[i])

        list1 = [] ; list2 = [] ; list3 = [] ; list4 = [] ; list5 = []
        list6 = [] ; list7 = [] ; list8 = [] ; list9 = [] ; list0 = []

        for i in range(5):
            list1.append(self.numlist[i]) , list6.append(self.botlist[i])
            list2.append(self.numlist[i+5]) ,list7.append(self.botlist[i+5]) 
            list3.append(self.numlist[i+10]) ,list8.append(self.botlist[i+10]) 
            list4.append(self.numlist[i+15]) ,list9.append(self.botlist[i+15]) 
            list5.append(self.numlist[i+20]) ,list0.append(self.botlist[i+20])

        self.megalist1 = [list1 , list2 , list3 , list4 , list5]
        self.megalist2 = [list6 , list7 , list8 , list9 , list0]

        self.choice1 = random.choice(self.numbers)
        self.bot_choice = str(self.choice1).zfill(2)

        if self.bot_choice in self.botlist :
            position = self.botlist.index(self.bot_choice)
            self.megalist2[(position//5)][(position%5)] = "XX"

        if self.bot_choice in self.numlist:
            position = self.numlist.index(self.bot_choice)
            self.megalist1[(position//5)][(position%5)] = "XX"

        for i in range(25):
            self.grand_list[i].setText(self.megalist1[i//5][i%5])
            if self.grand_list[i].text() == "XX":
                self.grand_list[i].setStyleSheet('QPushButton {color : blue}')

        self.numbers.remove(self.choice1)
        self.removed.append(self.choice1)

    def play(self, button):
        def points(self):
            self.pointlist1 = set(self.megalist1[0])
            self.pointlist2 = set(self.megalist1[1])
            self.pointlist3 = set(self.megalist1[2])
            self.pointlist4 = set(self.megalist1[3])
            self.pointlist5 = set(self.megalist1[4])

            self.pointlista = {self.megalist1[0][0],self.megalist1[1][0],self.megalist1[2][0],self.megalist1[3][0],self.megalist1[4][0]}
            self.pointlistb = {self.megalist1[0][1],self.megalist1[1][1],self.megalist1[2][1],self.megalist1[3][1],self.megalist1[4][1]}
            self.pointlistc = {self.megalist1[0][2],self.megalist1[1][2],self.megalist1[2][2],self.megalist1[3][2],self.megalist1[4][2]}
            self.pointlistd = {self.megalist1[0][3],self.megalist1[1][3],self.megalist1[2][3],self.megalist1[3][3],self.megalist1[4][3]}
            self.pointliste = {self.megalist1[0][4],self.megalist1[1][4],self.megalist1[2][4],self.megalist1[3][4],self.megalist1[4][4]}

            self.pointlista1 = {self.megalist1[0][0],self.megalist1[1][1],self.megalist1[2][2],self.megalist1[3][3],self.megalist1[4][4]}
            self.pointliste5 = {self.megalist1[4][0],self.megalist1[3][1],self.megalist1[2][2],self.megalist1[1][3],self.megalist1[0][4]}

            self.pointlist6 = set(self.megalist2[0])
            self.pointlist7 = set(self.megalist2[1])
            self.pointlist8 = set(self.megalist2[2])
            self.pointlist9 = set(self.megalist2[3])
            self.pointlist0 = set(self.megalist2[4])

            self.pointlistf = {self.megalist2[0][0],self.megalist2[1][0],self.megalist2[2][0],self.megalist2[3][0],self.megalist2[4][0]}
            self.pointlistg = {self.megalist2[0][1],self.megalist2[1][1],self.megalist2[2][1],self.megalist2[3][1],self.megalist2[4][1]}
            self.pointlisth = {self.megalist2[0][2],self.megalist2[1][2],self.megalist2[2][2],self.megalist2[3][2],self.megalist2[4][2]}
            self.pointlisti = {self.megalist2[0][3],self.megalist2[1][3],self.megalist2[2][3],self.megalist2[3][3],self.megalist2[4][3]}
            self.pointlistj = {self.megalist2[0][4],self.megalist2[1][4],self.megalist2[2][4],self.megalist2[3][4],self.megalist2[4][4]}

            self.pointlistf6 = {self.megalist2[0][0],self.megalist2[1][1],self.megalist2[2][2],self.megalist2[3][3],self.megalist2[4][4]}
            self.pointlistj0 = {self.megalist2[4][0],self.megalist2[3][1],self.megalist2[2][2],self.megalist2[1][3],self.megalist2[0][4]}

            if len(self.pointlist1) == 1 and self.var01 == True : self.my_points += 1 ; self.var01 = False
            if len(self.pointlist2) == 1 and self.var02 == True : self.my_points += 1 ; self.var02 = False
            if len(self.pointlist3) == 1 and self.var03 == True : self.my_points += 1 ; self.var03 = False
            if len(self.pointlist4) == 1 and self.var04 == True : self.my_points += 1 ; self.var04 = False
            if len(self.pointlist5) == 1 and self.var05 == True : self.my_points += 1 ; self.var05 = False
            if len(self.pointlista) == 1 and self.var06 == True : self.my_points += 1 ; self.var06 = False
            if len(self.pointlistb) == 1 and self.var07 == True : self.my_points += 1 ; self.var07 = False
            if len(self.pointlistc) == 1 and self.var08 == True : self.my_points += 1 ; self.var08 = False
            if len(self.pointlistd) == 1 and self.var09 == True : self.my_points += 1 ; self.var09 = False
            if len(self.pointliste) == 1 and self.var10 == True : self.my_points += 1 ; self.var10 = False
            if len(self.pointlista1) == 1 and self.var11 == True : self.my_points += 1 ; self.var11 = False
            if len(self.pointliste5) == 1 and self.var12 == True : self.my_points += 1 ; self.var12 = False

            if len(self.pointlist6) == 1 and self.var13 == True : self.bot_points += 1 ; self.var13 = False
            if len(self.pointlist7) == 1 and self.var14 == True : self.bot_points += 1 ; self.var14 = False
            if len(self.pointlist8) == 1 and self.var15 == True : self.bot_points += 1 ; self.var15 = False
            if len(self.pointlist9) == 1 and self.var16 == True : self.bot_points += 1 ; self.var16 = False
            if len(self.pointlist0) == 1 and self.var17 == True : self.bot_points += 1 ; self.var17 = False
            if len(self.pointlistf) == 1 and self.var18 == True : self.bot_points += 1 ; self.var18 = False
            if len(self.pointlistg) == 1 and self.var19 == True : self.bot_points += 1 ; self.var19 = False
            if len(self.pointlisth) == 1 and self.var20 == True : self.bot_points += 1 ; self.var20 = False
            if len(self.pointlisti) == 1 and self.var21 == True : self.bot_points += 1 ; self.var21 = False
            if len(self.pointlistj) == 1 and self.var22 == True : self.bot_points += 1 ; self.var22 = False
            if len(self.pointlistf6) == 1 and self.var23 == True : self.bot_points += 1 ; self.var23 = False
            if len(self.pointlistj0) == 1 and self.var24 == True : self.bot_points += 1 ; self.var24 = False

        if self.pushButton_A.isEnabled():
            pass
        
        else:
            self.my_input = button.text()
            self.choice2 = int(self.my_input)

            if self.my_input in self.numlist:
                position = self.numlist.index(self.my_input)
                self.megalist1[(position//5)][(position%5)] = "XX"

            if self.my_input in self.botlist :
                position = self.botlist.index(self.my_input)
                self.megalist2[(position//5)][(position%5)] = "XX"

            for i in range(25):
                self.grand_list[i].setText(self.megalist1[i//5][i%5])
                if self.grand_list[i].text() == "XX":
                    self.grand_list[i].setStyleSheet('QPushButton {color : blue}')

            self.numbers.remove(self.choice2)
            self.removed.append(self.choice2)

            points(self)

            self.result_box.setText(f"Points : {self.my_points}")

            if self.bot_points >= 5:
                self.result_box.setStyleSheet('QTextBrowser {color : red}')
                self.result_box.setText("You lost the game")

            elif self.my_points >= 5:
                self.result_box.setStyleSheet('QTextBrowser {color : green}')
                self.result_box.setText("You won the game")

            else:
                loop = QEventLoop()
                QTimer.singleShot(1000, loop.quit)
                loop.exec_()

                self.choice1 = random.choice(self.numbers)
                self.bot_choice = str(self.choice1).zfill(2)

                if self.bot_choice in self.botlist :
                    position = self.botlist.index(self.bot_choice)
                    self.megalist2[(position//5)][(position%5)] = "XX"

                if self.bot_choice in self.numlist:
                    position = self.numlist.index(self.bot_choice)
                    self.megalist1[(position//5)][(position%5)] = "XX"

                for i in range(25):
                    self.grand_list[i].setText(self.megalist1[i//5][i%5])
                    if self.grand_list[i].text() == "XX":
                        self.grand_list[i].setStyleSheet('QPushButton {color : blue}')

                self.numbers.remove(self.choice1)
                self.removed.append(self.choice1)

                points(self)

                self.result_box.setText(f"Points : {self.my_points}")

                if self.bot_points >= 5:
                    self.result_box.setStyleSheet('QTextBrowser {color : red}')
                    self.result_box.setText("You lost the game")

                elif self.my_points >= 5:
                    self.result_box.setStyleSheet('QTextBrowser {color : green}')
                    self.result_box.setText("You won the game")

    def reset(self):
        for i in self.grand_list:
            i.setText("")
            i.setStyleSheet('QPushButton {color : black}')
            
        self.result_box.setText("Points : 0")
        self.result_box.setStyleSheet('QTextBrowser {color : black}')

        self.pushButton_A.setDisabled(False)

        self.numbers = [] ; self.numlist = [] ; self.botlist = [] ; self.removed = []

        self.var01 = True ; self.var02 = True ; self.var03 = True ; self.var04 = True ; self.var05 = True ; self.var06 = True
        self.var07 = True ; self.var08 = True ; self.var09 = True ; self.var10 = True ; self.var11 = True ; self.var12 = True 
        self.var13 = True ; self.var14 = True ; self.var15 = True ; self.var16 = True ; self.var17 = True ; self.var18 = True 
        self.var19 = True ; self.var20 = True ; self.var21 = True ; self.var22 = True ; self.var23 = True ; self.var24 = True

        self.bot_points = 0 ; self.my_points = 0

        for i in range(1,26):
            self.numlist.append(str(i).zfill(2)) ; self.botlist.append(str(i).zfill(2)) ; self.numbers.append(i)

        random.shuffle(self.numlist) ; random.shuffle(self.botlist)
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
