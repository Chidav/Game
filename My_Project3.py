import tkinter as RPC
from tkinter import messagebox
import random


rpc = RPC.Tk()
rpc.title("ROCK  PAPER  SCISSORS")
rpc.geometry("530x520+450+110")
rpc.configure(bg="indigo")


score = 0
computer = 0

label1 = RPC.Label(rpc, text="Welcome to a game of Rock Paper Scissors, the instructions are simple...", bg="indigo",
                   fg="white", font=("MS Sans Sarif", 11))
label1.grid(row=0, column=0)

label2 = RPC.Label(rpc, text="You are given unlimited chances to play against computer, each win carries 2 points",
                   bg="indigo", fg="white", font=("MS Sarif", 10))
label2.grid(row=1, column=0)

label3 = RPC.Label(rpc, text="Do you think you're up for it? Play and find out!",
                   bg="indigo", fg="white", font=("MS Sarif", 10))
label3.grid(row=2, column=0)

label4 = RPC.Label(rpc, bg="indigo", fg="white", font=("MS Sarif", 10))
label4.grid(row=3, column=0)


def rocky():
    game = ["ROCK", "PAPER", "SCISSORS"]
    for i in range(1):
        games = random.choice(game)
        label5.insert(0, games)
        label7.insert(0, "ROCK")
    if label7.get() == label5.get():
        messagebox.showinfo("Draw", "No one gets a score")
    elif label5.get() == "PAPER" and label7.get() == "ROCK":
        global computer
        computer += 2
        messagebox.showinfo("You Lose", "Paper covers rock" + "\n" + str(computer) + " points to computer")
    elif label5.get() == "SCISSORS" and label7.get() == "ROCK":
        global score
        score += 2
        messagebox.showinfo("You Win", "Rock breaks scissors" + "\n" + str(score) + " points to player")
    else:
        messagebox.showinfo("Error", "Inaccurate")


button1 = RPC.Button(rpc, text="ROCK", width="14", height="2", bg="grey", fg="black", font=("Times", 8), command=rocky)
button1.grid(row=4, column=0, padx=10, pady=10)


def paps():
    game = ["ROCK", "PAPER", "SCISSORS"]
    for i in range(1):
        games = random.choice(game)
        label5.insert(0, games)
        label7.insert(0, "PAPER")
    if label5.get() == "ROCK" and label7.get() == "PAPER":
        global score
        score += 2
        messagebox.showinfo("You Win", "Paper covers rock" + "\n" + str(score) + " points to player")
    elif label5.get() == label7.get():
        messagebox.showinfo("Draw", "No one gets a score")
    elif label5.get() == "SCISSORS" and label7.get() == "PAPER":
        global computer
        computer += 2
        messagebox.showinfo("You Lose", "Scissors cuts paper" + "\n" + str(computer) + " points to computer")
    else:
        messagebox.showinfo("Error", "Inaccurate")


button2 = RPC.Button(rpc, text="PAPER", width="14", height="2", bg="cyan", fg="green", font=("Times", 8), command=paps)
button2.grid(row=5, column=0, padx=10, pady=10)


def sci():
    game = ["ROCK", "PAPER", "SCISSORS"]
    for i in range(1):
        games = random.choice(game)
        label5.insert(0, games)
        label7.insert(0, "SCISSORS")
    if label5.get() == "ROCK" and label7.get() == "SCISSORS":
        global computer
        computer += 2
        messagebox.showinfo("You lose", "Rock destroys scissors" + "\n" + str(computer) + " points to computer")
    elif label7.get() == "SCISSORS" and label5.get() == "PAPER":
        global score
        score += 2
        messagebox.showinfo("You win", "Scissors cuts paper" + "\n" + str(score) + " points to player")
    elif label5.get() == label7.get():
        messagebox.showinfo("Draw", "No one gets a score")
    else:
        messagebox.showinfo("Error", "Inaccurate")


button3 = RPC.Button(rpc, text="SCISSORS", width="14", height="2", bg="magenta", fg="white", font=("Times", 8),
                     command=sci)
button3.grid(row=6, column=0, padx=10, pady=10)

label6 = RPC.Label(rpc, text="My Choice", width="10", height="1", bg="grey", fg="white")
label6.grid(row=7, column=0)

label7 = RPC.Entry(rpc, bg="white", fg="black")
label7.grid(row=8, column=0)

label8 = RPC.Label(rpc, text="VS", bg="indigo", fg="white", font=("MS Sarif", 10))
label8.grid(row=9, column=0)

label5 = RPC.Entry(rpc, bg="white", fg="black")
label5.grid(row=10, column=0, padx=5)


def clean():
    label5.delete(0, "end")
    label7.delete(0, "end")


button4 = RPC.Button(rpc, text="Clear", width="7", height="1", bg="white", fg="black", command=clean)
button4.grid(row=11, column=0, padx=10, pady=10)


def end():
    messagebox.showinfo("Ending game", "Your Total Score is: " + str(score) + "\n" + "Computer's Total score is: " +
                        str(computer))
    if str(score) > str(computer):
        messagebox.showinfo("You win", "You were Victorious")
    elif str(score) < str(computer):
        messagebox.showinfo("You lose", "Computer was victorious")
    elif str(score) == str(computer):
        messagebox.showinfo("Draw", "The game ends with a draw")
    with open("Register.txt", "a") as writer:
        register = str(score)
        writer.write(register)
    rpc.destroy()


button5 = RPC.Button(rpc, text="End game", width="14", height="2", bg="white", fg="black", command=end)
button5.grid(row=12, column=0, padx=10, pady=10)


def main():
    messagebox.showinfo("Going to Main Menu", "Your Total Score is: " + str(score))
    rpc.destroy()
    import My_Project1


button6 = RPC.Button(rpc, text="Main Menu", width="8", height="1", bg="white", fg="black", command=main)
button6.grid(row=13, column=0, padx=10, pady=10)


rpc.mainloop()
