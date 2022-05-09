import tkinter as Guess
from tkinter import messagebox
import random

guessing = Guess.Tk()
guessing.title("Guessing Game")
guessing.geometry("500x450+500+120")
guessing.configure(bg="orange")


# Labels
label1 = Guess.Label(guessing, text="Welcome to the guessing game", bg="orange", font=("MS Sans Serif", 14))
label1.pack()

label2 = Guess.Label(guessing, text="Instruction: You are given the chance to play against a computer. The range of "
                                    "numbers", bg="orange")
label2.pack()

label3 = Guess.Label(guessing, text="are from 1 to 10, guess the choice of the computer and score two ""points.",
                     bg="orange")
label3.pack()

label4 = Guess.Label(guessing, text="An endless game of fun and luck. Are you up for the task?", bg="orange")
label4.pack()

label5 = Guess.Label(guessing, text="Enter your number", font=("Times", 10), bg="red", fg="black")
label5.pack(pady=10, padx=3)

label6 = Guess.Entry(guessing, bg="white", fg="black")
label6.pack(pady=5, padx=3)

# Button
score = 0
def run():
    if int(label6.get()) in range(1, 11):
        number = random.randint(1, 10)
        label8.insert(0, number)
        if label6.get() == label8.get():
            global score
            score += 2
            messagebox.showinfo("Correct:","Your score is: " + str(score))
        elif label6.get() != label8.get():
            messagebox.showinfo("You failed!!", "try again.")
    else:
        messagebox.showinfo("Error", "Pick Integer from range 1 to 10")


button1 = Guess.Button(guessing, text="Submit", width="9", height="1", bg="white", fg="black", command=run)
button1.pack(pady=10)

label7 = Guess.Label(guessing, text="Computer's Choice", font=("Times", 10), bg="red", fg="black")
label7.pack(pady=10, padx=3)


label8 = Guess.Entry(guessing, bg="white", fg="black")
label8.pack(pady=5, padx=3)

def clean():
    label6.delete(0, "end")
    label8.delete(0, "end")


button2 = Guess.Button(guessing, text="Clear", width="7", height="1", bg="white", fg="black", command=clean)
button2.pack(pady=10)

def end():
    messagebox.showinfo("Ending game", "Your Total Score is: " + str(score))
    with open("Register.txt", "a") as writer:
        register = str(score)
        writer.write(register)
    guessing.destroy()


button3 = Guess.Button(guessing, text="End game", width="10", height="1", bg="white", fg="black", command=end)
button3.pack(pady=15)

def next_game():
    messagebox.showinfo("Going to the next game", "Your Total Score is: " + str(score))
    guessing.destroy()
    import My_Project3


button4 = Guess.Button(guessing, text="Next Game", width="8", height="1", bg="white", fg="black", command=next_game)
button4.pack(pady=10)


guessing.mainloop()
