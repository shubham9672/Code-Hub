# Tic Tac Toe Game Using Python Tkinter

import tkinter.messagebox
from tkinter import *

# Window Creation.
win = Tk()
win.geometry("1150x800")
win.title("TIC TAC TOE")
win.configure(background="cyan")

# Inseting values of X and O in buttons
buttons = StringVar()
click = True


def butinsrt(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        ScoreChecker("X", colorX)

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        ScoreChecker("O", colorO)


colorX = "light sky blue"
colorO = "salmon"


# Function to assign the winner

def ScoreChecker(var, colorXO):
    if button1["text"] == var and button2["text"] == var and button3["text"] == var:
        button1.configure(background=colorXO)
        button2.configure(background=colorXO)
        button3.configure(background=colorXO)
        if var == "X":
            s = float(XPlayer.get())
            XPlayer.set(s + 1)
        else:
            s = float(OPlayer.get())
            OPlayer.set(s + 1)
        tkinter.messagebox.showinfo(f"Player {var} WINS.", f"Congratulations Player {var} for Winning The Round.")
        Reset()
    elif button4["text"] == var and button5["text"] == var and button6["text"] == var:
        button4.configure(background=colorXO)
        button5.configure(background=colorXO)
        button6.configure(background=colorXO)
        if var == "X":
            s = float(XPlayer.get())
            XPlayer.set(s + 1)
        else:
            s = float(OPlayer.get())
            OPlayer.set(s + 1)
        tkinter.messagebox.showinfo(f"Player {var} WINS.", f"Congratulations Player {var} for Winning The Round.")
        Reset()
    elif button7["text"] == var and button8["text"] == var and button9["text"] == var:
        button7.configure(background=colorXO)
        button8.configure(background=colorXO)
        button9.configure(background=colorXO)
        if var == "X":
            s = float(XPlayer.get())
            XPlayer.set(s + 1)
        else:
            s = float(OPlayer.get())
            OPlayer.set(s + 1)
        tkinter.messagebox.showinfo(f"Player {var} WINS.", f"Congratulations Player {var} for Winning The Round.")
        Reset()
    elif button1["text"] == var and button5["text"] == var and button9["text"] == var:
        button1.configure(background=colorXO)
        button5.configure(background=colorXO)
        button9.configure(background=colorXO)
        if var == "X":
            s = float(XPlayer.get())
            XPlayer.set(s + 1)
        else:
            s = float(OPlayer.get())
            OPlayer.set(s + 1)
        tkinter.messagebox.showinfo(f"Player {var} WINS.", f"Congratulations Player {var} for Winning The Round.")
        Reset()
    elif button3["text"] == var and button5["text"] == var and button7["text"] == var:
        button3.configure(background=colorXO)
        button5.configure(background=colorXO)
        button7.configure(background=colorXO)
        if var == "X":
            s = float(XPlayer.get())
            XPlayer.set(s + 1)
        else:
            s = float(OPlayer.get())
            OPlayer.set(s + 1)
        tkinter.messagebox.showinfo(f"Player {var} WINS.", f"Congratulations Player {var} for Winning The Round.")
        Reset()
    elif button1["text"] == var and button4["text"] == var and button7["text"] == var:
        button1.configure(background=colorXO)
        button4.configure(background=colorXO)
        button7.configure(background=colorXO)
        if var == "X":
            s = float(XPlayer.get())
            XPlayer.set(s + 1)
        else:
            s = float(OPlayer.get())
            OPlayer.set(s + 1)
        tkinter.messagebox.showinfo(f"Player {var} WINS.", f"Congratulations Player {var} for Winning The Round.")
        Reset()
    elif button2["text"] == var and button5["text"] == var and button8["text"] == var:
        button2.configure(background=colorXO)
        button5.configure(background=colorXO)
        button8.configure(background=colorXO)
        if var == "X":
            s = float(XPlayer.get())
            XPlayer.set(s + 1)
        else:
            s = float(OPlayer.get())
            OPlayer.set(s + 1)
        tkinter.messagebox.showinfo(f"Player {var} WINS.", f"Congratulations Player {var} for Winning The Round.")
        Reset()
    elif button3["text"] == var and button6["text"] == var and button9["text"] == var:
        button3.configure(background=colorXO)
        button6.configure(background=colorXO)
        button9.configure(background=colorXO)
        if var == "X":
            s = float(XPlayer.get())
            XPlayer.set(s + 1)
        else:
            s = float(OPlayer.get())
            OPlayer.set(s + 1)
        tkinter.messagebox.showinfo(f"Player {var} WINS.", f"Congratulations Player {var} for Winning The Round.")
        Reset()

    # Reset Function


def Reset():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background="lemon chiffon")
    button2.configure(background="lemon chiffon")
    button3.configure(background="lemon chiffon")
    button4.configure(background="lemon chiffon")
    button5.configure(background="lemon chiffon")
    button6.configure(background="lemon chiffon")
    button7.configure(background="lemon chiffon")
    button8.configure(background="lemon chiffon")
    button9.configure(background="lemon chiffon")
    click = True


# New Game Function

def NewGame():
    Reset()
    XPlayer.set(0)
    OPlayer.set(0)


# Frames
Top = Frame(win, bg="cyan", pady=2, width=1150, height=100, relief=RIDGE)
Top.grid(row=0, column=0)

Gtitle = Label(Top, font=("Times", 50, "bold"), text="Tic Tac Toe Game", bd=21, bg="cyan", fg="black", justify=CENTER)
Gtitle.grid(row=0, column=0)

MainFrame = Frame(win, bd=10, bg="green yellow", pady=2, width=1150, height=600, padx=2, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=650, height=500, pady=2, padx=2, bg="green yellow", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=460, height=500, pady=2, padx=2, bg="green yellow", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=460, height=300, pady=2, padx=2, bg="green yellow", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=460, height=100, pady=2, padx=2, bg="green yellow", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

BottomFrame = Frame(win, bg="cyan", pady=2, width=1150, height=50, relief=RIDGE)
BottomFrame.grid(row=2, column=0)

Btitle = Label(BottomFrame, font=("Times", 20, "bold"), text="Created By: Tanmay Pandey", bd=21, bg="cyan", fg="black",
               justify=CENTER)
Btitle.grid(row=0, column=0)

XPlayer = IntVar()
OPlayer = IntVar()

XPlayer.set(0)
OPlayer.set(0)

Score = Label(RightFrame1, font=("arial 40 bold"), text="Scores ", padx=2, pady=2, bg="green yellow", fg="violet red",
              justify=CENTER)
Score.grid(row=0, column=0, sticky=W)

P1Title = Label(RightFrame1, font=("arial", 30, "bold"), text="Player X : ", padx=2, pady=2, bg="green yellow",
                fg="orange red")
P1Title.grid(row=1, column=0, sticky=W)

TextPX = Entry(RightFrame1, font=("arial", 30, "bold"), bd=2, fg="black", textvariable=XPlayer, width=13, justify=LEFT)
TextPX.grid(row=1, column=1, sticky=W)

P2Title = Label(RightFrame1, font=("arial 30 bold"), text="Player O : ", padx=2, pady=2, bg="green yellow",
                fg="orange red")
P2Title.grid(row=2, column=0, sticky=W)

TextPO = Entry(RightFrame1, font=("arial", 30, "bold"), bd=2, fg="black", textvariable=OPlayer, width=13, justify=LEFT)
TextPO.grid(row=2, column=1, sticky=W)

# Tic tac Toe Buttons
button1 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(LeftFrame, text=" ", font=("Times 26 bold"), height=3, width=8, bg="lemon chiffon",
                 command=lambda: butinsrt(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

# New Game Button
button10 = Button(RightFrame2, text=" NEW GAME ", font=("Times 26 bold"), height=1, width=23, bg="lemon chiffon",
                  command=NewGame)
button10.grid(row=0, column=0)

button10 = Button(RightFrame2, text=" RESET ", font=("Times 26 bold"), height=1, width=23, bg="lemon chiffon",
                  command=Reset)
button10.grid(row=1, column=0)

win.mainloop()
