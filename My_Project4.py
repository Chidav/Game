import tkinter as xoxo
from tkinter import messagebox
from tkinter import Menu

david = xoxo.Tk()
david.title("Tic Tac Toe")
david.geometry("222x264+500+150")
david.configure(bg="white")

clicked = True
count = 0
score1 = 0
times1 = 0
score2 = 0
times2 = 0

def disable_all_buttons():
    B1.config(state="disabled")
    B2.config(state="disabled")
    B3.config(state="disabled")
    B4.config(state="disabled")
    B5.config(state="disabled")
    B6.config(state="disabled")
    B7.config(state="disabled")
    B8.config(state="disabled")
    B9.config(state="disabled")


def check_won():
    global winner, score1, times1, score2, times2
    winner = False
    if B1["text"] == "X" and B2["text"] == "X" and B3["text"] == "X":
        B1.config(bg="red")
        B2.config(bg="red")
        B3.config(bg="red")
        winner = True
        score1 += 2
        times1 += 1
        messagebox.showinfo("You won", "X wins" + "\n" + "Your score is" + " " + str(score1))
        disable_all_buttons()

    elif B4["text"] == "X" and B5["text"] == "X" and B6["text"] == "X":
        B4.config(bg="red")
        B5.config(bg="red")
        B6.config(bg="red")
        winner = True
        score1 += 2
        times1 += 1
        messagebox.showinfo("You won", "X wins" + "\n" + "Your score is" + " " + str(score1))
        disable_all_buttons()

    elif B7["text"] == "X" and B8["text"] == "X" and B9["text"] == "X":
        B7.config(bg="red")
        B8.config(bg="red")
        B9.config(bg="red")
        winner = True
        score1 += 2
        times1 += 1
        messagebox.showinfo("You won", "X wins" + "\n" + "Your score is" + " " + str(score1))
        disable_all_buttons()

    elif B1["text"] == "X" and B4["text"] == "X" and B7["text"] == "X":
        B1.config(bg="red")
        B4.config(bg="red")
        B7.config(bg="red")
        winner = True
        score1 += 2
        times1 += 1
        messagebox.showinfo("You won", "X wins" + "\n" + "Your score is" + " " + str(score1))
        disable_all_buttons()

    elif B2["text"] == "X" and B5["text"] == "X" and B8["text"] == "X":
        B2.config(bg="red")
        B5.config(bg="red")
        B8.config(bg="red")
        winner = True
        score1 += 2
        times1 += 1
        messagebox.showinfo("You won", "X wins" + "\n" + "Your score is" + " " + str(score1))
        disable_all_buttons()

    elif B3["text"] == "X" and B6["text"] == "X" and B9["text"] == "X":
        B3.config(bg="red")
        B6.config(bg="red")
        B9.config(bg="red")
        winner = True
        score1 += 2
        times1 += 1
        messagebox.showinfo("You won", "X wins" + "\n" + "Your score is" + " " + str(score1))
        disable_all_buttons()

    elif B1["text"] == "X" and B5["text"] == "X" and B9["text"] == "X":
        B1.config(bg="red")
        B5.config(bg="red")
        B9.config(bg="red")
        winner = True
        score1 += 2
        times1 += 1
        messagebox.showinfo("You won", "X wins" + "\n" + "Your score is" + " " + str(score1))
        disable_all_buttons()

    elif B3["text"] == "X" and B5["text"] == "X" and B7["text"] == "X":
        B3.config(bg="red")
        B5.config(bg="red")
        B7.config(bg="red")
        winner = True
        score1 += 2
        times1 += 1
        messagebox.showinfo("You won", "X wins" + "\n" + "Your score is" + " " + str(score1))
        disable_all_buttons()

    elif B1["text"] == "O" and B2["text"] == "O" and B3["text"] == "O":
        B1.config(bg="red")
        B2.config(bg="red")
        B3.config(bg="red")
        winner = True
        score2 += 2
        times2 += 1
        messagebox.showinfo("You won", "O wins" + "\n" + "Your score is" + " " + str(score2))
        disable_all_buttons()

    elif B4["text"] == "O" and B5["text"] == "O" and B6["text"] == "O":
        B4.config(bg="red")
        B5.config(bg="red")
        B6.config(bg="red")
        winner = True
        score2 += 2
        times2 += 1
        messagebox.showinfo("You won", "O wins" + "\n" + "Your score is" + " " + str(score2))
        disable_all_buttons()

    elif B7["text"] == "O" and B8["text"] == "O" and B9["text"] == "O":
        B7.config(bg="red")
        B8.config(bg="red")
        B9.config(bg="red")
        winner = True
        score2 += 2
        times2 += 1
        messagebox.showinfo("You won", "O wins" + "\n" + "Your score is" + " " + str(score2))
        disable_all_buttons()

    elif B1["text"] == "O" and B4["text"] == "O" and B7["text"] == "O":
        B1.config(bg="red")
        B4.config(bg="red")
        B7.config(bg="red")
        winner = True
        score2 += 2
        times2 += 1
        messagebox.showinfo("You won", "O wins" + "\n" + "Your score is" + " " + str(score2))
        disable_all_buttons()

    elif B2["text"] == "O" and B5["text"] == "O" and B8["text"] == "O":
        B2.config(bg="red")
        B5.config(bg="red")
        B8.config(bg="red")
        winner = True
        score2 += 2
        times2 += 1
        messagebox.showinfo("You won", "O wins" + "\n" + "Your score is" + " " + str(score2))
        disable_all_buttons()

    elif B3["text"] == "O" and B6["text"] == "O" and B9["text"] == "O":
        B3.config(bg="red")
        B6.config(bg="red")
        B9.config(bg="red")
        winner = True
        score2 += 2
        times2 += 1
        messagebox.showinfo("You won", "O wins" + "\n" + "Your score is" + " " + str(score2))
        disable_all_buttons()

    elif B1["text"] == "O" and B5["text"] == "O" and B9["text"] == "O":
        B1.config(bg="red")
        B5.config(bg="red")
        B9.config(bg="red")
        winner = True
        score2 += 2
        times2 += 1
        messagebox.showinfo("You won", "O wins" + "\n" + "Your score is" + " " + str(score2))
        disable_all_buttons()

    elif B3["text"] == "O" and B5["text"] == "O" and B7["text"] == "O":
        B3.config(bg="red")
        B5.config(bg="red")
        B7.config(bg="red")
        winner = True
        score2 += 2
        times2 += 1
        messagebox.showinfo("You won", "O wins" + "\n" + "Your score is" + " " + str(score2))
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("A tie", "A draw" + "\n" + "No body wins")
        disable_all_buttons()


def b_click(B):
    global clicked, count
    if B["text"] == " " and clicked == True:
        B["text"] = "X"
        clicked = False
        count += 1
        check_won()
    elif B["text"] == " " and clicked == False:
        B["text"] = "O"
        clicked = True
        count += 1
        check_won()
    else:
        messagebox.showerror("Selection Error", "This box has already been clicked" + "\n" + "Pick another box.")


def reset():
    global B1, B2, B3, B4, B5, B6, B7, B8, B9
    global clicked, count
    clicked = True
    count = 0

    B1 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B1))
    B1.grid(row=0, column=0)
    B2 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B2))
    B2.grid(row=0, column=1)
    B3 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B3))
    B3.grid(row=0, column=2)

    B4 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B4))
    B4.grid(row=1, column=0)
    B5 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B5))
    B5.grid(row=1, column=1)
    B6 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B6))
    B6.grid(row=1, column=2)

    B7 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B7))
    B7.grid(row=2, column=0)
    B8 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B8))
    B8.grid(row=2, column=1)
    B9 = xoxo.Button(david, text=" ", height="2", width="4", bg="black", fg="white", font=("Helvetica", 20),
                     command=lambda: b_click(B9))
    B9.grid(row=2, column=2)


reset()


def pause():
    B1.config(state="disabled")
    B2.config(state="disabled")
    B3.config(state="disabled")
    B4.config(state="disabled")
    B5.config(state="disabled")
    B6.config(state="disabled")
    B7.config(state="disabled")
    B8.config(state="disabled")
    B9.config(state="disabled")

def play():
    B1.config(state="normal")
    B2.config(state="normal")
    B3.config(state="normal")
    B4.config(state="normal")
    B5.config(state="normal")
    B6.config(state="normal")
    B7.config(state="normal")
    B8.config(state="normal")
    B9.config(state="normal")


def Xes():
    global score1, times1
    messagebox.showinfo("Your ScoreBoard", "X has" + " " + str(score1) + " " + "points" + "\n"
                        + "X has won" + " " + str(times1) + " " + "times.")


def Oes():
    global score2, times2
    messagebox.showinfo("Your ScoreBoard", "O has" + " " + str(score2) + " " + "points" + "\n"
                        + "O has won" + " " + str(times2) + " " + "times.")


Menu_bar = Menu(david)
david.config(menu=Menu_bar)

Options_Menu = Menu(Menu_bar, tearoff=0)

Options_Menu.add_command(label="Pause", command=pause)
Options_Menu.add_command(label="Play", command=play)
Options_Menu.add_command(label="Reset", command=reset)
Options_Menu.add_separator()


def exiting():
    messagebox.showinfo("Exit", "Thank you for playing.")
    david.quit()
    david.destroy()
    exit()


Options_Menu.add_command(label="Exit", command=exiting)
Menu_bar.add_cascade(label="Options", menu=Options_Menu)

ScoreBoard_Menu = Menu(Menu_bar, tearoff=0)
ScoreBoard_Menu.add_command(label="X wins", command=Xes)
ScoreBoard_Menu.add_command(label="O wins", command=Oes)
Menu_bar.add_cascade(label="ScoreBoard", menu=ScoreBoard_Menu)


david.mainloop()
