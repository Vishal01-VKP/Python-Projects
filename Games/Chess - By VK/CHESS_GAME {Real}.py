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

        self.move_name = ""

        self.board_rows = [8,7,6,5,4,3,2,1]
        self.board_columns = 'a b c d e f g h'.split(" ")
        # variable_needed = f"{self.board_columns[7-(n//8)]}{self.board_rows[n%8]}"

        font = QtGui.QFont()
        font.setPointSize(1)

        self.win = None
        self.draw = None
        self.valid_move = True

        self.Chess_Board = {n:QtWidgets.QPushButton(self) for n in range(64)}

        for i in range(64):
            self.Chess_Board[i].setStyleSheet("QPushButton {background-color : lightgreen ; color : lightgreen}")
            self.Chess_Board[i].setFont(font)
            self.Chess_Board[i].setObjectName(f"{self.board_columns[i%8]}{self.board_rows[i//8]}")

        self.lineEdit_2.setDisabled(True)

        for i in range(64):
            if (i // 8) % 2 == 0:
                if i % 2 == 0:
                    self.Chess_Board[i].setStyleSheet("QPushButton {background-color : white}")

            if (i // 8) % 2 == 1:
                if i % 2 == 1:
                    self.Chess_Board[i].setStyleSheet("QPushButton {background-color : white}")
                
            self.Chess_Board[i].setGeometry(60+((i%8)*50),140+((i//8)*50),50,50)
            self.Chess_Board[i].clicked.connect(self.initiate_move)

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


    def initiate_move(self):
        self.move = ""

        for i in range(64):
            self.Chess_Board[i].setStyleSheet("QPushButton {background-color : lightgreen ; color : lightgreen}")

            if (i // 8) % 2 == 0:
                if i % 2 == 0:
                    self.Chess_Board[i].setStyleSheet("QPushButton {background-color : white}")

            if (i // 8) % 2 == 1:
                if i % 2 == 1:
                    self.Chess_Board[i].setStyleSheet("QPushButton {background-color : white}")

        self.value = self.sender()
        self.move = self.value.text().upper()

        if self.move == "":
            pass

        elif len(self.move) == 1:
            if self.move == "P":
                pass
            else:
                self.move_name += self.move

            self.value.setStyleSheet("QPushButton {background-color : cyan}")

        for i in range(64):
            self.Chess_Board[i].clicked.connect(self.play_move)        


    def play_move(self):
        self.textBrowser.setText("")
        self.valid_move = True

        self.button = self.sender()

        if len(self.button.text()) == 1:
            self.move_name += f"x{self.button.objectName()}"

        elif self.button.text() == "":
            self.move_name += self.button.objectName()

        # if self.lineEdit.isEnabled():
        #     self.move = self.lineEdit.text()

        # elif self.lineEdit_2.isEnabled():
        #     self.move = self.lineEdit_2.text()

        try:
            self.board.push_san(self.move_name)

        except Exception as ex:
            self.textBrowser.setText(f"{ex}")
            self.valid_move = False

        if self.valid_move == True:
            if self.lineEdit.isEnabled():  
                self.lineEdit.setDisabled(True)
                self.lineEdit_2.setDisabled(False)

            else:
                self.lineEdit.setDisabled(False)
                self.lineEdit_2.setDisabled(True)

        elif self.valid_move == False:    
            self.move_name = ""
       
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

        for i in range(64):
            self.Chess_Board[i].clicked.connect(self.initiate_move)

        self.move = ""
        self.move_name = ""


    def show_board(self):
        for x in range(8):
            for y in range(8):
                if self.final_list[x][y].isupper():
                    self.Chess_Board[x*8+y].setText(f"{self.final_list[x][y]}".upper())
                    self.Chess_Board[x*8+y].setIcon(QtGui.QIcon(f"{self.final_list[x][y]}@.png"))
                    self.Chess_Board[x*8+y].setIconSize(QtCore.QSize(40,40))

                elif self.final_list[x][y].islower():
                    self.Chess_Board[x*8+y].setText(f"{self.final_list[x][y]}".upper())
                    self.Chess_Board[x*8+y].setIcon(QtGui.QIcon(f"{self.final_list[x][y]}&.png"))
                    self.Chess_Board[x*8+y].setIconSize(QtCore.QSize(40,40))

                elif self.final_list[x][y] == ".":
                    self.Chess_Board[x*8+y].setIcon(QtGui.QIcon())
                    self.Chess_Board[x*8+y].setText("")


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
