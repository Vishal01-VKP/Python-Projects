from PyQt5 import QtCore, QtGui, QtWidgets, uic
import random
import sys
from functools import partial
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtGui import QPainter, QPen


class BINGO_App(QtWidgets.QDialog):
    def __init__(self):
        super(BINGO_App, self).__init__()

        uic.loadUi("BINGO.ui", self)

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

        self.show()
            

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

            try:
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

            except Exception as ex:
                self.result_box.setText("Invalid Move !")

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


# app = QtWidgets.QApplication(sys.argv)
# window = BINGO_App()
# app.exec_()