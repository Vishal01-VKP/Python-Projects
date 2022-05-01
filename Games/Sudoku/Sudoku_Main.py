import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import uic

import sys
import random


class Sudoku_App(QtWidgets.QDialog):
    def __init__(self):
        super(Sudoku_App, self).__init__()

        uic.loadUi('sudoku.ui', self)

        self.mega_dict = {f"lineEdit_{num+1}":QtWidgets.QLineEdit(self.widget) for num in range(81)}

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.run_timer = False
        
        self.font = QtGui.QFont()
        self.font.setPointSize(16)
        self.font.setFamily("Times New Roman")
        self.font.setBold(True)

        for num in range(81):
            self.mega_dict[f"lineEdit_{num+1}"].setGeometry((num%9)*40,(num//9)*40,40,40)
            self.mega_dict[f"lineEdit_{num+1}"].setDisabled(True)

        self.textBrowser_2.setText("00:00:00")

        self.pushButton.clicked.connect(self.play_game)
        self.pushButton_2.clicked.connect(self.reset_game)

        timer = QtCore.QTimer()
        timer.timeout.connect(self.timing)
        timer.start(1000)  

        self.show()

    
    def play_game(self):
        self.pushButton.setDisabled(True)
        self.run_timer = True

        base = 3
        side = base**2

        self.level = self.spinBox.value()
        self.win = False

        def create_table(row,column):
            return (base * (row % base) + row // base + column ) % side

        def shuffling(s):
            return random.sample(s, len(s))

        row_base = range(base)

        rows = [var1*base + row for var1 in shuffling(row_base) for row in shuffling(row_base)]
        cols = [var1*base + column for var1 in shuffling(row_base) for column in shuffling(row_base)]
        nums = shuffling(range(1,side+1))

        self.board = [[nums[create_table(row, column)] for column in cols] for row in rows]

        for x in range(self.level):
            for i in range(0,81,x+4):
                self.board[i//9][i%9] = "."

        for line in self.board : print(line)

        self.complete_board = sum(self.board, [])

        for num in range(81):
            self.mega_dict[f"lineEdit_{num+1}"].setFont(self.font)
            self.mega_dict[f"lineEdit_{num+1}"].setText(str(self.complete_board[num]))
            self.mega_dict[f"lineEdit_{num+1}"].setAlignment(QtCore.Qt.AlignCenter)
            
            if self.mega_dict[f"lineEdit_{num+1}"].text() != ".":
                self.mega_dict[f"lineEdit_{num+1}"].setDisabled(True)

            elif self.mega_dict[f"lineEdit_{num+1}"].text() == ".":
                self.mega_dict[f"lineEdit_{num+1}"].setDisabled(False)

        
    def finish_game(self):
        pass


    def reset_game(self):
        self.complete_board = []
        self.pushButton.setDisabled(False)

        for num in range(81):
            self.mega_dict[f"lineEdit_{num+1}"].setText("")
            self.mega_dict[f"lineEdit_{num+1}"].setDisabled(True)


    def timing(self):
        if self.run_timer == True:
            self.seconds += 1

            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0

            elif self.seconds == self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                self.seconds = 0

            self.textBrowser_2.setText(f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}")

        elif self.run_timer == False:
            pass
            
            
app = QtWidgets.QApplication(sys.argv)
window = Sudoku_App()
app.exec_()
