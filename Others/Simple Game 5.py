from tkinter import *
import random

root_3t = Tk()
root_3t.attributes('-fullscreen', True)
root_3t.configure(bg='black')


if __name__ == '__main__': # Variables
    positions = [0,1,2,3,4,5,6,7,8]
    row_1 = [9,9,9] ; row_2 = [9,9,9] ; row_3 = [9,9,9]
    win = None
    boxes = 9
    my_score = 0
    bot1_score = 0


if __name__ == '__main__': # Game Play Algorithm
    def game(event):
        global places, boxes, my_score, bot1_score
        text = event.widget.cget('text')
        coordinate = int(text)

        places = [canvas1, canvas2, canvas3, canvas4, canvas5, canvas6, canvas7, canvas8, canvas9]


        def win_check():
            global win, score_board

            if row_1[0] == row_1[1] == row_1[2] :

                if row_1[0] == 1:
                    Label(score_board, text='You Win !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)
                    win = True
                elif row_1[0] == 0:
                    Label(score_board, text='You Lose !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)                
                    win = False

            elif row_2[0] == row_2[1] == row_2[2] :                

                if row_2[0] == 1:
                    Label(score_board, text='You Win !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)
                    win = True
                elif row_2[0] == 0:
                    Label(score_board, text='You Lose !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)                
                    win = False

            elif row_3[0] == row_3[1] == row_3[2] :
                
                if row_3[0] == 1:
                    Label(score_board, text='You Win !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)
                    win = True
                elif row_3[0] == 0:
                    Label(score_board, text='You Lose !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)                
                    win = False

            elif row_1[0] == row_2[0] == row_3[0] :              

                if row_1[0] == 1:
                    Label(score_board, text='You Win !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)
                    win = True
                elif row_1[0] == 0:
                    Label(score_board, text='You Lose !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)                
                    win = False

            elif row_1[1] == row_2[1] == row_3[1] :
                
                if row_1[1] == 1:
                    Label(score_board, text='You Win !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)
                    win = True
                elif row_1[1] == 0:
                    Label(score_board, text='You Lose !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)                
                    win = False
                    
            elif row_1[2] == row_2[2] == row_3[2] :
                
                if row_1[2] == 1:
                    Label(score_board, text='You Win !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)
                    win = True
                elif row_1[2] == 0:
                    Label(score_board, text='You Lose !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)                
                    win = False

            elif row_1[0] == row_2[1] == row_3[2] :
                
                if row_1[0] == 1:
                    Label(score_board, text='You Win !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)
                    win = True
                elif row_1[0] == 0:
                    Label(score_board, text='You Lose !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)                
                    win = False

            elif row_1[2] == row_2[1] == row_3[0] :               

                if row_1[2] == 1:
                    Label(score_board, text='You Win !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)
                    win = True
                elif row_1[2] == 0:
                    Label(score_board, text='You Lose !', bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.4, rely=0.15)                
                    win = False


        Label(places[coordinate], text='X', font='CASTELLAR 48 bold').place(relx=0.3, rely=0.25)
        if 0<=coordinate<3 :
            row_1[coordinate] = 1
        elif 3<=coordinate<6 :
            row_2[coordinate-3] = 1
        elif 6<=coordinate<9 :
            row_3[coordinate-6] = 1
        boxes -= 1
        positions.remove(coordinate)

        win_check()

        if win == True:
            my_score += 1
            Label(score_board, text=f" {my_score} ", bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.25, rely=0.65) 

            for i in range(0, len(positions)):
                positions.remove(positions[i])
                                
        if boxes == 0 and win == None:
            Label(root_3t, text='Draw', bg='black', fg='white', font='Baskerville 16').place(relx=0.6, rely=0.85)

        try:
            bot_choice = random.choice(positions)
            Label(places[bot_choice], text='0', font='CASTELLAR 48 bold').place(relx=0.3, rely=0.25)
            if 0<=bot_choice<3 :
                row_1[bot_choice] = 0
            elif 3<=bot_choice<6 :
                row_2[bot_choice-3] = 0
            elif 6<=bot_choice<9 :
                row_3[bot_choice-6] = 0
            boxes -= 1
            positions.remove(bot_choice)

        except IndexError:
            print("Game Over !")
    
        win_check()

        if win == False:
            bot1_score += 1
                                
            Label(score_board, text=f" {bot1_score} ", bg='grey', fg='black', font='Baskerville 14 bold').place(relx=0.75, rely=0.65)              


if __name__ == '__main__': # Game Restart Algorithm
    def reset_game():
        global positions, row_1, row_2, row_3, win, boxes

        for i in range(0,9):
            Label(places[i], text="  "*2, font='CASTELLAR 52 bold').place(relx=0.2, rely=0.3)

        Label(score_board, text="  "*10, font='Baskerville 20', bg='grey').place(relx=0.4, rely=0.15)
    
        positions = [0,1,2,3,4,5,6,7,8]
        row_1 = [9,9,9] ; row_2 = [9,9,9] ; row_3 = [9,9,9]
        win = None
        boxes = 9


if __name__ == '__main__': # Heading
    heading_frame = Canvas(root_3t, bg='black', borderwidth=15, relief=FLAT, highlightbackground='silver', height=100)

    Button(heading_frame, text='RESET', command=reset_game, font='Elephant 12').place(relx=0.92, rely=0.25)
    Label(heading_frame, text='4T -- Tic-Tac-Toe Tournaments', font='CASTELLAR 28 bold', bg='black', fg='white').pack(anchor=CENTER, padx=30, pady=10)
    Button(heading_frame, text='EXIT', bg='red', fg='black', command=root_3t.destroy, font='Elephant 12').place(relx=0.02, rely=0.25)

    heading_frame.pack(fill=X)


if __name__ == '__main__': # Game Play Buttons
    button_frame = Canvas(root_3t, bg='grey', highlightbackground='black')

    increase = 0
    for b in range(0,3):
        button = Button(button_frame, text=f"{b}", width=6)
        button.place(relx=0.06+increase*2, rely=0.1)
        button.bind('<Button-1>', game)

        button = Button(button_frame, text=f"{b+3}", width=6)
        button.place(relx=0.06+increase*2, rely=0.38)
        button.bind('<Button-1>', game)

        button = Button(button_frame, text=f"{b+6}", width=6)
        button.place(relx=0.06+increase*2, rely=0.66)
        button.bind('<Button-1>', game)

        increase += 0.15

    button_frame.place(relx=0.82, rely=0.85, width=200, height=100)


if __name__ == '__main__': # Game Play Screen
    main_screen = Canvas(root_3t)

    canvas1 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas1.place(x=0,y=0,height=130,width=200)    
    canvas2 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas2.place(x=200,y=0,height=130,width=200)    
    canvas3 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas3.place(x=400,y=0,height=130,width=200)    
    canvas4 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas4.place(x=0,y=130,height=130,width=200)    
    canvas5 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas5.place(x=200,y=130,height=130,width=200)    
    canvas6 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas6.place(x=400,y=130,height=130,width=200)    
    canvas7 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas7.place(x=0,y=260,height=130,width=200)    
    canvas8 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas8.place(x=200,y=260,height=130,width=200)    
    canvas9 = Canvas(main_screen, borderwidth=2, highlightbackground='black', relief=FLAT)
    canvas9.place(x=400,y=260,height=130,width=200)

    main_screen.place(relx=0.52, rely=0.3, width=600, height=390)


if __name__ == '__main__': # Score Board
    score_board = Canvas(root_3t, bg='grey', highlightbackground='black', borderwidth=5, relief=FLAT)
    Label(score_board, text='Result : ', bg='grey', font='Baskerville 14 bold').place(relx=0.15, rely=0.15)
    Label(score_board, text='-'*56, bg='grey', font='Baskerville 14 bold').place(relx=0.005, rely=0.4)

    score_board.create_line(170, 40, 170, 100)

    Label(score_board, text='You : ', bg='grey', font='Baskerville 14 bold').place(relx=0.05, rely=0.65)
    Label(score_board, text='Bot : ', bg='grey', font='Baskerville 14 bold').place(relx=0.55, rely=0.65)
    score_board.place(relx=0.52, rely=0.85, width=350, height=100)


if __name__ == '__main__': # Tool Bar
    tool_bar = Canvas(root_3t, bg='black', highlightbackground='silver', borderwidth=15)
    Label(tool_bar, text='Rules', bg='black',fg='white', font='Elephant 24 underline').place(relx=0.4, rely=0.02)
    Label(tool_bar, text='1. First , pick your side [either as X or 0] before starting the game .', bg='black',fg='white', font='Ariel 14').place(relx=0.01, rely=0.12)
    Label(tool_bar, text='2. Then , pick your choice from the buttons below .', bg='black',fg='white', font='Ariel 14').place(relx=0.01, rely=0.18)
    Label(tool_bar, text='3. Reset your game before starting a new game [Points will not be erased] .', bg='black',fg='white', font='Ariel 14').place(relx=0.01, rely=0.24)
    Label(tool_bar, text='Enjoy your games', bg='black',fg='white', font='Elephant 14 italic').place(relx=0.3, rely=0.32)
    tool_bar.place(relx=0, rely=0.11, height=670, width=650)


root_3t.mainloop()
