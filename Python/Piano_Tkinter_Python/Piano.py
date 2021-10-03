# Piano -Python Tkinter
from tkinter import*
import pygame
import sys

pygame.init()

root = Tk()
root.title("PIANO")
root.geometry("850x450")

#*********************************************FUNCTIONS***********************************************************
def val_btnup1():
    val.set("C#")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/C_s.wav")
    sound.play()
    return

def val_btnup2():
    val.set("D#")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/D_s.wav")
    sound.play()
    return

def val_btnup3():
    val.set("F#")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/F_s.wav")
    sound.play()
    return

def val_btnup4():
    val.set("G#")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/G_s.wav")
    sound.play()
    return

def val_btnup5():
    val.set("Bb")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/Bb.wav")
    sound.play()
    return

def val_btnup6():
    val.set("C#1")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/C_s1.wav")
    sound.play()
    return

def val_btnup7():
    val.set("D#1")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/D_s1.wav")
    sound.play()
    return
#***********************************************************************************************************************

def val_btnC():
    val.set("C")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/C.wav")
    sound.play()
    return

def val_btnD():
    val.set("D")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/D.wav")
    sound.play()
    return

def val_btnE():
    val.set("E")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/E.wav")
    sound.play()
    return

def val_btnF():
    val.set("F")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/F.wav")
    sound.play()
    return

def val_btnG():
    val.set("G")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/G.wav")
    sound.play()
    return

def val_btnA():
    val.set("A")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/A.wav")
    sound.play()
    return

def val_btnB():
    val.set("B")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/B.wav")
    sound.play()
    return

def val_btnC1():
    val.set("C1")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/C1.wav")
    sound.play()
    return

def val_btnD1():
    val.set("D1")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/D1.wav")
    sound.play()
    return

def val_btnE1():
    val.set("E1")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/E1.wav")
    sound.play()
    return

def val_btnF1():
    val.set("F1")
    sound = pygame.mixer.Sound("/home/karim/PROJECTS/Piano_Tkinter/Z_Music_Notes/Music_Notes/F1.wav")
    sound.play()
    return




#******************************************************************************************************************

val = StringVar()
val.set(0)
mainframe = Frame(root,height=450,width=850,bg="powder blue",bd=8,relief=RIDGE)
mainframe.place(x=0,y=0)

valueEntry = Entry(mainframe,textvar=val,width=5,bd=8,relief=RIDGE,font="calibri 15 bold")
valueEntry.place(x=380,y=5)

#****************************************BLACK BUTTONS*************************************************************

btnup1 = Button(mainframe,text="C#",height=8,width=3,bd=4,relief=RAISED,font="msserif 12 bold",bg="black",\
activebackground="black",activeforeground="white",fg="white",command=val_btnup1)
btnup1.place(x=143,y=60)

btnup2 = Button(mainframe,text="D#",height=8,width=3,bd=4,relief=RAISED,font="msserif 12 bold",bg="black",\
activebackground="black",activeforeground="white",fg="white",command=val_btnup2)
btnup2.place(x=210,y=60)

btnup3 = Button(mainframe,text="F#",height=8,width=3,bd=4,relief=RAISED,font="msserif 12 bold",bg="black",\
activebackground="black",activeforeground="white",fg="white",command=val_btnup3)
btnup3.place(x=327,y=60)

btnup4 = Button(mainframe,text="G#",height=8,width=3,bd=4,relief=RAISED,font="msserif 12 bold",bg="black",\
activebackground="black",activeforeground="white",fg="white",command=val_btnup4)
btnup4.place(x=393,y=60)

btnup5 = Button(mainframe,text="Bb",height=8,width=3,bd=4,relief=RAISED,font="msserif 12 bold",bg="black",\
    activebackground="black",activeforeground="white",fg="white",command=val_btnup5)
btnup5.place(x=460,y=60)

btnup6 = Button(mainframe,text="C#1",height=8,width=3,bd=4,relief=RAISED,font="msserif 12 bold",bg="black",\
activebackground="black",activeforeground="white",fg="white",command=val_btnup6)
btnup6.place(x=580,y=60)

btnup7 = Button(mainframe,text="D#1",height=8,width=3,bd=4,relief=RAISED,font="msserif 12 bold",bg="black",\
activebackground="black",activeforeground="white",fg="white",command=val_btnup7)
btnup7.place(x=647,y=60)

#*************************************WHITE BUTTONS****************************************************************

btn1 = Button(mainframe,text="C",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnC)
btn1.place(x=60,y=240)

btn2 = Button(mainframe,text="D",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnD)
btn2.place(x=127,y=240)

btn3 = Button(mainframe,text="E",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnE)
btn3.place(x=194,y=240)

btn4 = Button(mainframe,text="F",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnF)
btn4.place(x=260,y=240)

btn5 = Button(mainframe,text="G",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnG)
btn5.place(x=327,y=240)

btn6 = Button(mainframe,text="A",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnA)
btn6.place(x=393,y=240)

btn7 = Button(mainframe,text="B",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnB)
btn7.place(x=460,y=240)

btn8 = Button(mainframe,text="C1",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnC1)
btn8.place(x=527,y=240)

btn9 = Button(mainframe,text="D1",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnD1)
btn9.place(x=593,y=240)

btn10 = Button(mainframe,text="E1",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnE1)
btn10.place(x=661,y=240)

btn11 = Button(mainframe,text="F1",height=9,width=3,bd=4,relief=RAISED,font="msserif 12 bold",command=val_btnF1)
btn11.place(x=728,y=240)



root.mainloop()
