import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic

import sys
import tabulate


class Chess_App(QtWidgets.QMainWindow):
    def __init__(self):
        super(Chess_App, self).__init__()

        uic.loadUi("CHESS.ui", self)

        self.Chess_Board = {f"button{n+1}":QtWidgets.QPushButton() for n in range(64)}

        self.lineEdit_2.setDisabled(True)

        for var1 in range(8):
            if var1 % 2 == 0:
                for i in range(0,8,2):
                    self.Chess_Board[f"button{(var1*8)+i+1}"].setStyleSheet("QPushButton {background-color : brown}")
                    self.Chess_Board[f"button{(var1*8)+i+2}"].setStyleSheet("QPushButton {background-color : white}")
            elif var2 % 2 == 1:
                for i in range(1,9,2):
                    self.Chess_Board[f"button{(var1*8)+i+1}"].setStyleSheet("QPushButton {background-color : brown}")
                    self.Chess_Board[f"button{(var1*8)+i+0}"].setStyleSheet("QPushButton {background-color : white}")

            for var2 in range(8):
                self.Chess_Board[f"button{(var1*8)+var2+1}"].setGeometry(60+var1*50,140+var2*50,50,50)

        self.lineEdit.isReadOnly()
        self.pushButton_A.clicked.connect(self.play_move)

        self.board = chess.Board()
        self.chessboard()

    def chessboard(self):
        self.pgn = self.board.epd()

        self.final_list = []

        pieces = self.pgn.split(" ", 1)[0]
        rows = pieces.split("/")

        for row in rows:
            self.initial_list = []

            # indices = '♚ /♛ /♜ /♝ /♞ /♟ /. /♙ /♘ /♗ /♖ /♕ /♔ '.split("/")

            for chessmen in row:
                if chessmen.isdigit():
                    for i in range(0, int(chessmen)):
                        self.initial_list.append(".")
                else:
                    self.initial_list.append(chessmen)
                
            self.final_list.append(self.initial_list)
                
        self.chesstable = tabulate.tabulate(self.final_list, tablefmt="grid", stralign="left")

    def play_move(self):
        if self.lineEdit.isEnabled():    
            move = self.lineEdit.text()
            self.lineEdit.setDisabled(True)
            self.lineEdit_2.setDisabled(False)

        elif self.lineEdit_2.isEnabled():    
            move = self.lineEdit_2.text()
            self.lineEdit.setDisabled(False)
            self.lineEdit_2.setDisabled(True)

        try:
            self.board.push_san(move)

        except Exception as ex:
            print("Illegal Move , Play Again !")

        # print(chessboard())
        
        # if board.is_checkmate():
        #     print("Checkmate !")

        # if board.is_variant_draw():
        #     print("Draw !")

        # if board.is_stalemate():
        #     print("Stalemate !")

        # if board.is_fifty_moves():
        #     print("Draw by fifty-move rule !")

        # if board.is_repetition():
        #     print("Draw by three-fold repitition !")

        self.chessboard()

        for x in range(8):
            for y in range(8):
                if self.final_list[x][y].isupper():
                    self.Chess_Board[f"button{(y*8)+x+1}"].setIcon(QtGui.QIcon(f"{self.final_list[x][y]}#.png"))

                elif self.final_list[x][y].islower():
                    self.Chess_Board[f"button{(y*8)+x+1}"].setIcon(QtGui.QIcon(f"{self.final_list[x][y]}.png"))

                elif self.final_list[x][y] == ".":
                    self.Chess_Board[f"button{(y*8)+x+1}"].setIcon(QtGui.QIcon())


app = QtWidgets.QApplication(sys.argv)
window = Chess_App()
app.exec_()
