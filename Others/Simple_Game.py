 # Imports
if __name__ == "__main__":
    import random
    from tkinter import *
    import pyautogui
  
# Initials
if __name__ == "__main__":
    root_RPS_League = Tk()
    root_RPS_League.attributes('-fullscreen', True)
    root_RPS_League.config(bg='black')

    Label(root_RPS_League, text='RPS League', bg='black' ,fg='white', font=("CASTELLAR", 48, 'bold', 'underline')).place(relx=0.3, rely=0.02)

    Button(root_RPS_League, text='EXIT', command=root_RPS_League.destroy, width=5, bg='red', fg='white').place(relx=0, rely=0)

    scshot = "RPS League" ; plname = "Player" ; botname = "Bot"

    """
        Label(canvas_3, text='Rules', bg='black', fg='white', font=('Bookman Old Style', 24, 'underline', 'italic')).place(relx=0.3, rely=0.04)
        Label(canvas_3, text="1. rock vs rock >>> Tie", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.2)
        Label(canvas_3, text="2. rock vs paper >>> paper", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.27)
        Label(canvas_3, text="3. rock vs scissors >>> rock", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.34)
        Label(canvas_3, text="4. paper vs rock >>> paper", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.41)
        Label(canvas_3, text="5. paper vs paper >>> Tie", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.48)
        Label(canvas_3, text="6. paper vs scissors >>> scissors", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.55)
        Label(canvas_3, text="7. scissors vs rock >>> rock", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.62)
        Label(canvas_3, text="8. scissors vs paper >>> scissors", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.69)
        Label(canvas_3, text="9. scissors vs scissors >>> Tie", bg='black', fg='white', font=('Bookman Old Style', 16, 'italic')).place(relx=0.05, rely=0.76)
    """

# Variables
if __name__ == "__main__":
    text_position = 0.13
    text_increment = 0.089

    your_score = 0
    bot_score = 0

    i = 0
    x = 1
        
    line_space = 0.9

    winner = None

# canvas_4 -> Toolbar
if __name__ == "__main__":
    canvas_4 = Canvas(root_RPS_League, bg='black', width=200)
    canvas_4.pack(side=RIGHT, padx=5, pady=10, fill=Y)

    def screen_shot():      
        pyautogui.screenshot(f'{scshot}.png')
        
    def settings():
        settings_window = Toplevel(root_RPS_League)
        settings_window.attributes("-fullscreen", True)
        settings_window.config(bg='black')

        def save_edits():
            global scshot, plname, botname
            scshot = screen_shot_name.get()
            plname = player_name.get()
            botname = bot_name.get()

        Button(settings_window, text='EXIT', bg='red', fg='white', command=settings_window.destroy).place(relx=0, rely=0)

        screen_shot_name = StringVar(value="RPSL")
        player_name = StringVar(value="Player")
        bot_name = StringVar(value="Bot")

        entry1 = Entry(settings_window, textvariable=screen_shot_name)
        entry1.place(relx=0.6, rely=0.3)

        entry2 = Entry(settings_window, textvariable=player_name)
        entry2.place(relx=0.6, rely=0.5)

        entry3 = Entry(settings_window, textvariable=bot_name)
        entry3.place(relx=0.6, rely=0.7)

        Button(settings_window, text='Edit', bg='red', fg='white', command=save_edits).place(relx=0, rely=0.85)

        settings_window.mainloop()

    def reset_game():
        global your_score, bot_score, i

        for x in range(0,10):
            Label(canvas_1, text=" " * 18, bg='black', font=("Calibri", 14, "bold")).place(relx=0.08, rely=text_position+x*text_increment)
            Label(canvas_1, text=" " * 18, bg='black', font=("Calibri", 14, "bold")).place(relx=0.58, rely=text_position+x*text_increment)
            Label(canvas_1b, text=" " * 30, bg='black', font=("Calibri", 14, "bold")).place(relx=0.1, rely=text_position+x*text_increment)
      
        Label(canvas_2, text=" " * 12, bg='black', font=("Calibri", 14, "bold")).place(relx=0.2, rely=0.55)
        Label(canvas_2, text=" " * 12, bg='black', font=("Calibri", 14, "bold")).place(relx=0.7, rely=0.55)
        Label(canvas_3, text=" " * 50, bg='black', font=("Calibri", 14, "bold")).place(relx=0.25, rely=0.2)

        Message(canvas_3, text=" "*1200, font=("Bookman Old Style", 60, "italic"), bg='black', fg='white').place(relx=0.5, rely=0.4)

        your_score = 0
        bot_score = 0

        i = 0
    
    def help():
        help_window = Toplevel(root_RPS_League)
        help_window.attributes("-fullscreen", True)
        help_window.config(bg='black')

        Button(help_window, text='EXIT', bg='red', fg='white', command=help_window.destroy).place(relx=0, rely=0)

        help_window.mainloop()

    def about():
        about_window = Toplevel(root_RPS_League)
        about_window.attributes("-fullscreen", True)
        about_window.config(bg='black')

        Button(about_window, text='EXIT', bg='red', fg='white', command=about_window.destroy).place(relx=0, rely=0)

        about_window.mainloop()

    Button(canvas_4, text='Screenshot', command=screen_shot, width=9).place(relx=0.6, rely=0.2)
    Button(canvas_4, text='Settings', command=settings).place(relx=0.5, rely=0.8)
    Button(canvas_4, text='Reset', command=reset_game).place(relx=0.6, rely=0.4)
    Button(canvas_4, text='About Us', command=about).place(relx=0.5, rely=0.6)

    Label(canvas_4, text='Options', font=("Bookman Old Style", 24, "bold", "italic", "underline"), bg='black', fg='white').place(relx=0.15, rely=0.04)

    Label(canvas_4, text=f'{"_"*24}', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.02, rely=0.12)
    
    Label(canvas_4, text='Screenshot : ', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.2)
    Label(canvas_4, text='Reset game : ', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.4)
    Label(canvas_4, text='About Us : ', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.6)
    Label(canvas_4, text='Settings : ', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.8)

    Label(canvas_4, text='It will help to take a', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.26)
    Label(canvas_4, text='screenshot and save it .', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.3)
    Label(canvas_4, text=f'{"_"*24}', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.02, rely=0.34)
       
    Label(canvas_4, text='It will help to reset', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.46)
    Label(canvas_4, text='the game to re-play it .', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.5)
    Label(canvas_4, text=f'{"_"*24}', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.02, rely=0.54)
       
    Label(canvas_4, text='It will take us to our', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.66)
    Label(canvas_4, text='contributor page .', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.7)
    Label(canvas_4, text=f'{"_"*24}', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.02, rely=0.74)
       
    Label(canvas_4, text='It will take us to the', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.86)
    Label(canvas_4, text='settings of this GUI .', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.05, rely=0.9)       

# Calculation Process
if __name__ == "__main__":
    def confirmation(event):
        global text_position, text_increment, your_score, bot_score, i, winner
        your_choice = event.widget.cget("text")
      
        signs = ['rock', 'paper', 'scissors']
        bot_choice = random.choice(signs)
        
        if your_choice == 'rock' and bot_choice == 'rock' or your_choice == 'paper' and bot_choice == 'paper' or your_choice == 'scissors' and bot_choice == 'scissors':
            your_score += 0.5 ; bot_score += 0.5
            Label(canvas_1b, text="It's a draw", bg='black', fg='white', font=("Times New Roman", 14, "bold")).place(relx=0.1, rely=text_position+i*text_increment)

        elif your_choice == 'rock' and bot_choice == 'paper' or your_choice == 'paper' and bot_choice == 'scissors' or your_choice == 'scissors' and bot_choice == 'rock':
            bot_score += 1
            Label(canvas_1b, text="You lost !", bg='black', fg='white', font=("Times New Roman", 14, "bold")).place(relx=0.1, rely=text_position+i*text_increment)

        elif your_choice == 'rock' and bot_choice == 'scissors' or your_choice == 'paper' and bot_choice == 'rock' or your_choice == 'scissors' and bot_choice == 'paper':
            your_score += 1
            Label(canvas_1b, text="You won !", bg='black', fg='white', font=("Times New Roman", 14, "bold")).place(relx=0.1, rely=text_position+i*text_increment)

        elif your_choice != "rock" and your_choice != "paper" and your_choice != "scissors":
            Label(canvas_1b, text="Illegal !", bg='black', fg='white', font=("Times New Roman", 14, "bold")).place(relx=0.1, rely=text_position+i*text_increment)

        Label(canvas_1, text=your_choice, bg='black', fg='white', font=("Times New Roman", 14, 'bold')).place(relx=0.08, rely=text_position+i*text_increment)      
        Label(canvas_1, text=bot_choice, bg='black', fg='white', font=("Times New Roman", 14, 'bold')).place(relx=0.58, rely=text_position+i*text_increment)

        Label(canvas_2, text=your_score, bg='black', fg='white', font=("Times New Roman", 20, 'bold')).place(relx=0.2, rely=0.55)
        Label(canvas_2, text=bot_score, bg='black', fg='white', font=("Times New Roman", 20, 'bold')).place(relx=0.7, rely=0.55)
   
        if your_score + bot_score == 10:
            if your_score > bot_score:
                Label(canvas_3, text="  Result  :  You won :)     ", bg='black', fg='white', font=("Baskerville", 12, "bold")).place(relx=0.25, rely=0.2)
                winner = plname
                if your_score-bot_score <= 2:
                    Message(canvas_3, text=f"What a complete thriller ! {winner} really took the game apart from the other side .", bg='black', fg='white', font=("Baskerville", 12, "bold")).place(relx=0.5, rely=0.4)
                elif 2 < your_score-bot_score < 4:
                    Message(canvas_3, text=f"It was a nice performance by {winner} , a good game and even a greater victory .", bg='black', fg='white', font=("Baskerville", 12, "bold")).place(relx=0.5, rely=0.4)
                else:
                    Message(canvas_3, text=f"It was a complete one-sider , {winner} really dominated throughout the game and won it easily .", bg='black', fg='white', font=("Baskerville", 12, "bold")).place(relx=0.5, rely=0.4)

            elif your_score < bot_score:
                Label(canvas_3, text="  Result  :  You lost :(    ", bg='black', fg='white', font=("Baskerville", 12, "bold")).place(relx=0.25, rely=0.2)
                winner = botname
                if bot_score-your_score <= 2:
                    Message(canvas_3, text=f"What a complete thriller ! {winner} really took the game apart from the other side .", bg='black', fg='white', font=("Bookman Old Style", 12, "italic")).place(relx=0.5, rely=0.4)
                elif 2 < bot_score-your_score < 4:
                    Message(canvas_3, text=f"It was a nice performance by {winner} , a good game and even a greater victory .", bg='black', fg='white', font=("Bookman Old Style", 12, "italic")).place(relx=0.5, rely=0.4)
                else:
                    Message(canvas_3, text=f"It was a complete one-sider , {winner} really dominated throughout the game and won it easily .", bg='black', fg='white', font=("Bookman Old Style", 12, "italic")).place(relx=0.5, rely=0.4)

            elif your_score == bot_score == 5:
                Label(canvas_3, text="  Result  : It's a tie !!!    ", bg='black', fg='white', font=("Baskerville", 12, "bold")).place(relx=0.25, rely=0.2)
                Message(canvas_3, text=f"A tie !! This is what was left to see in a rock-paper-scissors game ! Both sides really deserved it .", bg='black', fg='white', font=("Bookman Old Style", 12, "italic")).place(relx=0.5, rely=0.4)

        else:
            Label(canvas_3, text="Result  :  No result yet", bg='black', fg='white', font=("Baskerville", 12, "bold")).place(relx=0.25, rely=0.2)

        i += 1

        your_choice.set("")
        bot_choice = ""

# canvas_1 -> Result
if __name__ == "__main__":
    canvas_1 = Canvas(root_RPS_League, width=300, height=500, bg='black')

    line_1 = canvas_1.create_line(155, 0, 155, 750, fill='white')

    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.09)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.18)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.27)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.36)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.45)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.54)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.63)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.72)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.81)
    Label(canvas_1, text=f"{'-'*58}", bg='black', fg='white').place(relx=0.01, rely=0.90)

    Label(canvas_1, text="Your Choice", bg='black', fg='white', font="Baskerville 12 bold").place(relx=0.08, rely=0.03)
    Label(canvas_1, text="Bot's Choice", bg='black', fg='white', font="Baskerville 12 bold").place(relx=0.58, rely=0.03)

    canvas_1.place(relx=0.05, rely=0.3)

# canvas_1b -> Live Score
if __name__ == "__main__":
    canvas_1b = Canvas(root_RPS_League, bg='black', width=201, height=500)

    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.09)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.18)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.27)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.36)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.45)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.54)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.63)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.72)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.81)
    Label(canvas_1b, text=f"{'-'*39}", bg='black', fg='white').place(relx=0.008, rely=0.90)

    Label(canvas_1b, text="Outcome", bg='black', fg='white', font="Baskerville 12 bold").place(relx=0.3, rely=0.03)

    canvas_1b.place(relx=0.3, rely=0.3)

# canvas_2 -> Scoreboard
if __name__ == "__main__":
    canvas_2 = Canvas(root_RPS_League, width=400, height=120, bg='black')

    line_3 = canvas_2.create_line(200, 0, 200, 120, fill='white')

    Label(canvas_2, text=f"{'-'*78}", bg='black', fg='white').place(relx=0.01, rely=0.4)

    Label(canvas_2, text='YOUR SCORE', bg='black', fg='white', font="Baskerville 16 bold").place(relx=0.06, rely=0.1)
    Label(canvas_2, text='BOT SCORE', bg='black', fg='white', font="Baskerville 16 bold").place(relx=0.58, rely=0.1)
    
    canvas_2.place(relx=0.48, rely=0.79)

# canvas_3 -> More Info
if __name__ == "__main__":
    canvas_3 = Canvas(root_RPS_League, width=400, height=350, bg='black')

    rock_button = Button(canvas_3, text="rock", bg='black', fg='white', width=8)
    rock_button.place(rely=0.045, relx=0.38)
    rock_button.bind("<Button-1>", confirmation)

    paper_button = Button(canvas_3, text="paper", bg='black', fg='white', width=8)
    paper_button.place(rely=0.045, relx=0.58)
    paper_button.bind('<Button-1>', confirmation)

    scissors_button = Button(canvas_3, text="scissors", bg='black', fg='white', width=8)
    scissors_button.place(rely=0.045, relx=0.78)
    scissors_button.bind('<Button-1>', confirmation)

    label1 = Label(canvas_3, text='Your choice :', bg='black', fg='white', font=('CASTELLAR', 8, 'bold'))
    label1.place(relx=0.05,rely=0.05)

    Label(canvas_3, text=f'{"_"*48}', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.02, rely=0.12)
    Label(canvas_3, text=f'{"_"*48}', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.02, rely=0.25)

    Label(canvas_3, text="Post", bg='black', fg='white', font='CASTELLAR 16 bold').place(relx=0.05, rely=0.37)
    Label(canvas_3, text="Match", bg='black', fg='white', font='CASTELLAR 16 bold').place(relx=0.05, rely=0.52)
    Label(canvas_3, text="Analysis", bg='black', fg='white', font='CASTELLAR 16 bold').place(relx=0.05, rely=0.67)

    line_4 = canvas_3.create_line(175, 120, 175, 280, fill='white')

    Label(canvas_3, text=f'{"_"*48}', font=("Bookman Old Style", 11, "bold"), bg='black', fg='white').place(relx=0.02, rely=0.78)


    Button(canvas_3, text='Help', bg='black', fg='white', font=('Bookman Old Style', 10, 'italic'), width=8, height=1, command=help).place(relx=0.75, rely=0.88)
    Label(canvas_3, text="To know more , click here >>> ", bg='black', fg='white', font=('Bookman Old Style', 14, 'italic')).place(relx=0.04, rely=0.88)

    canvas_3.place(relx=0.48, rely=0.3)

root_RPS_League.mainloop()
