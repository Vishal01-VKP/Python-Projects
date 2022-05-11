# """The code I used from GeeksForGeeks"""
#         def isinRange(board):

#             N = 9

#             for i in range(0, N):
#                 for j in range(0, N):
                
#                     if ((board[i][j] <= 0) or (board[i][j] > 9)):
#                         return False
            
#         return True

#         def isValidSudoku(board):
#             N = 9

#             if (isinRange(board) == False):
#                 return False

#             unique = [False] * (N + 1)

#             for i in range(0, N):
#                 for m in range(0, N + 1):
#                     unique[m] = False

#                 for j in range(0, N):
#                     Z = board[i][j]

#                 if (unique[Z] == True):
#                     return False
                
#                 unique[Z] = True

#             for i in range(0, N):
#                 for m in range(0, N + 1):
#                     unique[m] = False

#                 for j in range(0, N):
#                     Z = board[j][i]

#                 if (unique[Z] == True):
#                     return False
                
#                 unique[Z] = True

#             for i in range(0, N - 2, 3):
#                 for j in range(0, N - 2, 3):
#                     for m in range(0, N + 1):
#                         unique[m] = False

#                 for k in range(0, 3):
#                     for l in range(0, 3):
  
#                         X = i + k
#                         Y = j + l
#                         Z = board[X][Y]

#                     if (unique[Z] == True):
#                         return False
                    
#                     unique[Z] = True
                    
#             return True

#         if (isValidSudoku(self.board)):
#             print("Valid")
#         else:
#             print("Not Valid")

#         """The code I tried , but failed"""
	
#         grand_list = []
#         check_list = ['1','2','3','4','5','6','7','8','9']
#         for num in range(81):
#             grand_list.append(self.mega_dict[f"lineEdit_{num+1}"].text())

#         for var in grand_list:
#             if var == "":
#                 self.textBrowser.setText("The table is not yet completed .")

#             elif var not in check_list:
#                 self.textBrowser.setText("Invalid entry / entries .")

#             else:
#                 row1 = set(self.board[0])
#                 row2 = set(self.board[1])
#                 row3 = set(self.board[2])
#                 row4 = set(self.board[3])
#                 row5 = set(self.board[4])
#                 row6 = set(self.board[5])
#                 row7 = set(self.board[6])
#                 row8 = set(self.board[7])
#                 row9 = set(self.board[8])

#                 column1 = {self.board[num][0] for num in range(9)}
#                 column2 = {self.board[num][1] for num in range(9)}
#                 column3 = {self.board[num][2] for num in range(9)}
#                 column4 = {self.board[num][3] for num in range(9)}
#                 column5 = {self.board[num][4] for num in range(9)}
#                 column6 = {self.board[num][5] for num in range(9)}
#                 column7 = {self.board[num][6] for num in range(9)}
#                 column8 = {self.board[num][7] for num in range(9)}
#                 column9 = {self.board[num][8] for num in range(9)}

#                 grid1 = {self.board[0][0],self.board[0][1],self.board[0][2],self.board[1][0],self.board[1][1],self.board[1][2],self.board[2][0],self.board[2][1],self.board[2][2]}
#                 grid2 = {self.board[0][3],self.board[0][4],self.board[0][5],self.board[1][3],self.board[1][4],self.board[1][5],self.board[2][3],self.board[2][4],self.board[2][5]}
#                 grid3 = {self.board[0][6],self.board[0][7],self.board[0][8],self.board[1][6],self.board[1][7],self.board[1][8],self.board[2][6],self.board[2][7],self.board[2][8]}
#                 grid4 = {self.board[3][0],self.board[3][1],self.board[3][2],self.board[4][0],self.board[4][1],self.board[4][2],self.board[5][0],self.board[5][1],self.board[5][2]}
#                 grid5 = {self.board[3][3],self.board[3][4],self.board[3][5],self.board[4][3],self.board[4][4],self.board[4][5],self.board[5][3],self.board[5][4],self.board[5][5]}
#                 grid6 = {self.board[3][6],self.board[3][7],self.board[3][8],self.board[4][6],self.board[4][7],self.board[4][8],self.board[5][6],self.board[5][7],self.board[5][8]}
#                 grid7 = {self.board[6][0],self.board[6][1],self.board[6][2],self.board[7][0],self.board[7][1],self.board[7][2],self.board[8][0],self.board[8][1],self.board[8][2]}
#                 grid8 = {self.board[6][3],self.board[6][4],self.board[6][5],self.board[7][3],self.board[7][4],self.board[7][5],self.board[8][3],self.board[8][4],self.board[8][5]}
#                 grid9 = {self.board[6][6],self.board[6][7],self.board[6][8],self.board[7][6],self.board[7][7],self.board[7][8],self.board[8][6],self.board[8][7],self.board[8][8]}

#                 if len(row1) == len(row2) == len(row3) == len(row4) == len(row5) == len(row6) == len(row7) == len(row8) == len(row9) == len(column1) == len(column2) == len(column3) == len(column4) == len(column5) == len(column6) == len(column7) == len(column8) == len(column9) == len(grid1) == len(grid2) == len(grid3) == len(grid4) == len(grid5) == len(grid6) == len(grid7) == len(grid8) == len(grid9) == 9:
#                     self.textBrowser.setText("You won")

#                 else:
#                     self.textBrowser.setText("There are still recurring numbers available .")
