import sys
from tkinter import *
import time


def times():

    current_time = time.strftime("%Y/%m/%d\n %I:%M:%S")
    clock.config(text=current_time)
    clock.after(200, times)


root = Tk()
root.geometry("500x250")
clock = Label(root, font=("times", 50, "bold"))
clock.grid(row=2, column=2, pady=25, padx=50)
times()
digi = Label(root, text="Digital Clock \nMade By Gautam", font="times 24 bold")
digi.grid(row=0, column=2)

nota = Label(root, text="hours  minute  seconds", font="times 15 bold")
nota.grid(row=3, column=2)

root.mainloop()
