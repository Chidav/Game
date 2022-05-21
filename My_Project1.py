import tkinter as dave
import sqlite3

david = dave.Tk()
david.title("Play a game")
david.geometry("500x500+500+150")
david.configure(bg="brown")


def Guessing():
    david.destroy()
    import My_Project2

def RPS():
    david.destroy()
    import My_Project3


# Label
label = dave.Label(david, text="Register Here", bg="brown", fg="white", font=("MS Serif", 12, "underline"))
label.pack(pady=8)


# Frame, Entry and Button
frame = dave.Frame(david, borderwidth=8, relief=dave.SUNKEN)
frame.pack()

entry = dave.Entry(frame)
entry.pack()


def save_name():
    print(entry.get())
    label2.configure(text="Welcome " + entry.get() + ", " + "Select a game")
    with open("Register.txt", "w") as writer:
        register = entry.get()
        writer.write(register)
    entry.delete(0, "end")


button = dave.Button(frame, text="Register", command=save_name)
button.pack(pady=6)

# Label2
label2 = dave.Label(david, text="", bg="brown", fg="white", font=("Times", 15))
label2.pack(pady=5)

# Frame2
frame2 = dave.Frame(david, borderwidth=10, relief=dave.GROOVE, bg="brown")
frame2.pack(pady=8)

# Label3
label3 = dave.Label(frame2, text="Single Player Game", bg="brown", fg="white", font=("Times", 10, "underline"))
label3.pack(pady=8)


# Button 2
button2 = dave.Button(frame2, text="Guessing game", width=12, height=3, bg="green", fg="white", command=Guessing)
button2.pack(pady=12, padx=5)

# Button 3
button3 = dave.Button(frame2, text="Rock Paper Scissors", width=18, height=3, bg="sky blue", fg="grey", command=RPS)
button3.pack(pady=12, padx=5)

# frame 3
frame3 = dave.Frame(david, borderwidth=6, relief=dave.RIDGE, bg="brown")
frame3.pack()

label3 = dave.Label(frame3, text="Two Players Game", bg="brown", fg="white", font=("Times", 10, "underline"))
label3.pack(pady=8, padx=5)

def TTT():
    david.destroy()
    import My_Project4


button4 = dave.Button(frame3, text="Tic Tac Toe", width=18, height=3, bg="grey", fg="white", command=TTT)
button4.pack(pady=12, padx=5)

david.mainloop()

