import chess
import tabulate

board = chess.Board()

def chessboard():
    pgn = board.epd()

    final_list = []

    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")

    for row in rows:
        initial_list = []

        indices = '♚ /♛ /♜ /♝ /♞ /♟ /. /♙ /♘ /♗ /♖ /♕ /♔ '.split("/")

        for chessmen in row:
            if chessmen.isdigit():
                for i in range(0, int(chessmen)):
                    initial_list.append(indices[6])
            else:
                if chessmen == "K":
                    initial_list.append(indices[0])
                if chessmen == "Q":
                    initial_list.append(indices[1])
                if chessmen == "R":
                    initial_list.append(indices[2])
                if chessmen == "B":
                    initial_list.append(indices[3])
                if chessmen == "N":
                    initial_list.append(indices[4])
                if chessmen == "P":
                    initial_list.append(indices[5])
                if chessmen == "p":
                    initial_list.append(indices[7])
                if chessmen == "n":
                    initial_list.append(indices[8])
                if chessmen == "b":
                    initial_list.append(indices[9])
                if chessmen == "r":
                    initial_list.append(indices[10])
                if chessmen == "q":
                    initial_list.append(indices[11])
                if chessmen == "k":
                    initial_list.append(indices[12])
            
        final_list.append(initial_list)
            
    chesstable = tabulate.tabulate(final_list, tablefmt="grid", stralign="left")
    return chesstable

print(chessboard())

while True:
    move = input("Enter your move : ")

    try:
        board.push_san(move)

    except Exception as ex:
        print("Illegal Move , Play Again !")

    print(chessboard())
    
    if board.is_checkmate():
        print("Checkmate !")
        break

    if board.is_variant_draw():
        print("Draw !")
        break

    if board.is_stalemate():
        print("Stalemate !")
        break

    if board.is_fifty_moves():
        print("Draw by fifty-move rule !")
        break

    if board.is_repetition():
        print("Draw by three-fold repitition !")
        break
