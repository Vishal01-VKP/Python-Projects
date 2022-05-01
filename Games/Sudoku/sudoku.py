import random
from tabulate import tabulate

base = 3
side = base**2
level = 5
win = False


def create_table(row,column):
    return (base * (row % base) + row // base + column ) % side


def shuffling(s):
    return random.sample(s, len(s))


row_base = range(base)

rows = [var1*base + row for var1 in shuffling(row_base) for row in shuffling(row_base)]
cols = [var1*base + column for var1 in shuffling(row_base) for column in shuffling(row_base)]
nums = shuffling(range(1,side+1))

board = [[nums[create_table(row, column)] for column in cols] for row in rows]

for x in range(level):
    for i in range(0,81,x+4):
        board[i//9][i%9] = "."


def table_print():
    row_no_01 = [board[0][0],board[0][1],board[0][2]]
    row_no_02 = [board[1][0],board[1][1],board[1][2]]
    row_no_03 = [board[2][0],board[2][1],board[2][2]]
    row_no_04 = [board[3][0],board[3][1],board[3][2]]
    row_no_05 = [board[4][0],board[4][1],board[4][2]]
    row_no_06 = [board[5][0],board[5][1],board[5][2]]
    row_no_07 = [board[6][0],board[6][1],board[6][2]]
    row_no_08 = [board[7][0],board[7][1],board[7][2]]
    row_no_09 = [board[8][0],board[8][1],board[8][2]]

    row_no_10 = [board[0][3],board[0][4],board[0][5]]
    row_no_11 = [board[1][3],board[1][4],board[1][5]]
    row_no_12 = [board[2][3],board[2][4],board[2][5]]
    row_no_13 = [board[3][3],board[3][4],board[3][5]]
    row_no_14 = [board[4][3],board[4][4],board[4][5]]
    row_no_15 = [board[5][3],board[5][4],board[5][5]]
    row_no_16 = [board[6][3],board[6][4],board[6][5]]
    row_no_17 = [board[7][3],board[7][4],board[7][5]]
    row_no_18 = [board[8][3],board[8][4],board[8][5]]

    row_no_19 = [board[0][6],board[0][7],board[0][8]]
    row_no_20 = [board[1][6],board[1][7],board[1][8]]
    row_no_21 = [board[2][6],board[2][7],board[2][8]]
    row_no_22 = [board[3][6],board[3][7],board[3][8]]
    row_no_23 = [board[4][6],board[4][7],board[4][8]]
    row_no_24 = [board[5][6],board[5][7],board[5][8]]
    row_no_25 = [board[6][6],board[6][7],board[6][8]]
    row_no_26 = [board[7][6],board[7][7],board[7][8]]
    row_no_27 = [board[8][6],board[8][7],board[8][8]]

    table1 = tabulate([row_no_01,row_no_02,row_no_03], tablefmt="plain")
    table2 = tabulate([row_no_04,row_no_05,row_no_06], tablefmt="plain")
    table3 = tabulate([row_no_07,row_no_08,row_no_09], tablefmt="plain")
    table4 = tabulate([row_no_10,row_no_11,row_no_12], tablefmt="plain")
    table5 = tabulate([row_no_13,row_no_14,row_no_15], tablefmt="plain")
    table6 = tabulate([row_no_16,row_no_17,row_no_18], tablefmt="plain")
    table7 = tabulate([row_no_19,row_no_20,row_no_21], tablefmt="plain")
    table8 = tabulate([row_no_22,row_no_23,row_no_24], tablefmt="plain")
    table9 = tabulate([row_no_25,row_no_26,row_no_27], tablefmt="plain")

    table10 = [[table1,table4,table7],[table2,table5,table8],[table3,table6,table9]]
    sudoku_table = tabulate(table10, tablefmt="grid")

    for line in board:
        print(line)

    print(sudoku_table)


table_print()


def win_check():
    pass


while True:
    your_command = input("Enter your command : ").split(",")

    function = your_command[0]
    entered_number = int(your_command[1])
    row_number = int(your_command[2])
    column_number = int(your_command[3])

    if function.lower() == "enter":
        board[row_number-1][column_number-1] = entered_number

        table_print()

        win_check()

        if win == True:
            print("You win")
            break

        else:
            pass

    else:
        pass
