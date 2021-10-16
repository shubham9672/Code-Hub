# Detection click mouse on a window :

from tkinter import*

def click(event):
    lab.configure(text = "Detected click on X =" + str(event.x) +", Y =" + str(event.y))
    can.create_oval (event.x-5, event.y-5, event.x+5, event.y+5, fill = "orange")

# === MAIN === #   
win = Tk()
can = Canvas (win, width =300, height =250, bg="light yellow")
can.bind("<Button-1>", click)
can.pack()
lab = Label(win)
lab.pack()

win.mainloop()
