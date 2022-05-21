import PyQt5
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import uic

import chess

import sys
import tabulate


class Chess_App(QtWidgets.QMainWindow):
    def __init__(self):
        super(Chess_App, self).__init__()

        uic.loadUi("CHESS.ui", self)

        self.win = None
        self.draw = None
        self.valid_move = True

        self.Chess_Board = {n+1:QtWidgets.QPushButton(self) for n in range(64)}

        self.lineEdit_2.setDisabled(True)

        for var1 in range(8):
            if var1 % 2 == 0:
                for i in range(0,8,2):
                    self.Chess_Board[(var1*8)+i+1].setStyleSheet("QPushButton {background-color : lightgreen}")
                    self.Chess_Board[(var1*8)+i+2].setStyleSheet("QPushButton {background-color : white}")
            elif var2 % 2 == 1:
                for i in range(1,9,2):
                    self.Chess_Board[(var1*8)+i+1].setStyleSheet("QPushButton {background-color : lightgreen}")
                    self.Chess_Board[(var1*8)+i+0].setStyleSheet("QPushButton {background-color : white}")

            for var2 in range(8):
                self.Chess_Board[(var1*8)+var2+1].setGeometry(60+var1*50,140+var2*50,50,50)

        self.lineEdit.isReadOnly()
        self.pushButton_A.clicked.connect(self.play_move)
        self.pushButton_B.clicked.connect(self.resignation)
        self.pushButton_C.clicked.connect(self.draw_game)
        self.pushButton_D.clicked.connect(self.save_game)
        self.pushButton_E.clicked.connect(self.reset_game)

        self.board = chess.Board()
        self.chessboard()
        self.show_board()

        self.show()


    def chessboard(self):
        self.pgn = self.board.epd()

        self.final_list = []
        self.printable_list = []

        pieces = self.pgn.split(" ", 1)[0]
        rows = pieces.split("/")

        for row in rows:
            self.initial_list = []

            for chessmen in row:
                if chessmen.isdigit():
                    for i in range(0, int(chessmen)):
                        self.initial_list.append(".")

                else:
                    self.initial_list.append(chessmen)
               
            self.final_list.append(self.initial_list)
                

    def play_move(self):
        self.textBrowser.setText("")
        self.valid_move = True

        if self.lineEdit.isEnabled():
            self.move = self.lineEdit.text()

        elif self.lineEdit_2.isEnabled():
            self.move = self.lineEdit_2.text()

        try:
            self.board.push_san(self.move)

        except Exception as ex:
            self.textBrowser.setText("Invalid move !")
            self.valid_move = False

        if self.valid_move == True:
            if self.lineEdit.isEnabled():  
                self.lineEdit.setDisabled(True)
                self.lineEdit_2.setDisabled(False)

            else:
                self.lineEdit.setDisabled(False)
                self.lineEdit_2.setDisabled(True)

        elif self.valid_move == False:    
            pass
       
        if self.board.is_checkmate():
            self.textBrowser.setText("Checkmate !")
            self.win = True
            self.end_the_game()

        if self.board.is_variant_draw():
            self.textBrowser.setText("Draw !")
            self.draw = True
            self.end_the_game()

        if self.board.is_stalemate():
            self.textBrowser.setText("Stalemate !")
            self.draw = True
            self.end_the_game()

        if self.board.is_fifty_moves():
            self.textBrowser.setText("Draw by fifty-move rule !")
            self.draw = True
            self.end_the_game()

        if self.board.is_repetition():
            self.textBrowser.setText("Draw by three-fold repitition !")
            self.draw = True
            self.end_the_game()

        self.chessboard()
        self.show_board()


    def show_board(self):
        for x in range(8):
            for y in range(8):
                if self.final_list[x][y].isupper():
                    self.Chess_Board[(y*8)+x+1].setIcon(QtGui.QIcon(f"{self.final_list[x][y]}@.png"))
                    self.Chess_Board[(y*8)+x+1].setIconSize(QtCore.QSize(45,45))

                elif self.final_list[x][y].islower():
                    self.Chess_Board[(y*8)+x+1].setIcon(QtGui.QIcon(f"{self.final_list[x][y]}&.png"))
                    self.Chess_Board[(y*8)+x+1].setIconSize(QtCore.QSize(45,45))

                elif self.final_list[x][y] == ".":
                    self.Chess_Board[(y*8)+x+1].setIcon(QtGui.QIcon())


    def reset_game(self):
        self.board.reset()

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        
        self.lineEdit.setDisabled(False)
        self.lineEdit_2.setDisabled(True)

        self.textBrowser.setText("")

        self.chessboard()
        self.show_board()
        self.end_the_game()


    def draw_game(self):
        self.draw = True
        self.end_the_game()
        self.textBrowser.setText("It's a draw .")


    def resignation(self):
        if self.lineEdit.text() == self.lineEdit_2.text() == "":
            self.textBrowser.setText("Match Aborted")

        else:
            if self.move == self.lineEdit.text():
                self.win = True
                self.end_the_game()
                who_resigned = "Black"

            elif self.move == self.lineEdit_2.text():
                self.win = False
                self.end_the_game()
                who_resigned = "White"

            self.textBrowser.setText(f"{who_resigned} resigned")


    def save_game(self):
        self.chesstable = tabulate.tabulate(self.final_list, tablefmt="grid", stralign="left")

        with open("chess_save_list.txt","a") as writer:
            writer.write(self.chesstable)


    def end_the_game(self):
        if self.win != self.draw:
            self.pushButton_A.setDisabled(True)
            self.pushButton_B.setDisabled(True)
            self.pushButton_C.setDisabled(True)

            self.win, self.draw = None, None

        elif self.win == self.draw:
            self.pushButton_A.setDisabled(False)
            self.pushButton_B.setDisabled(False)
            self.pushButton_C.setDisabled(False)


app = QtWidgets.QApplication(sys.argv)
window = Chess_App()
app.exec_()
