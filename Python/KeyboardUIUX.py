from tkinter import *

def select(value):
    if value == 'Space':
        textarea.insert(INSERT, ' ')

    elif value == 'Enter':
        textarea.insert(INSERT, '\n')

    elif value == 'Tab':
        textarea.insert(INSERT, '\t')

    elif value == 'Del':
        textarea.delete(1.0, END)

    elif value == 'Backs':
        i = textarea.get(1.0, END)
        newtext = i[:-2]

        textarea.delete(1.0, END)
        textarea.insert(INSERT, newtext)

    elif value == 'Shift ↑':
        varRow = 2
        varColumn = 0

        for button in leftShiftButtons:

            command = lambda x=button: select(x)
            if button != 'Space':
                Button(root, text=button, command=command, width=10, ).grid(row=varRow, column=varColumn)

            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1

    elif value == '↑ Shift':
        varRow = 2
        varColumn = 0

        for button in buttons:

            command = lambda x=button: select(x)
            if button != 'Space':
                Button(root, text=button, command=command, width=10, ).grid(row=varRow, column=varColumn)

            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1

    elif value == 'Caps':

        varRow = 2
        varColumn = 0

        for button in capsButtons:

            command = lambda x=button: select(x)
            if button != 'Space':
                Button(root, text=button, command=command, width=10, ).grid(row=varRow, column=varColumn)

            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1

    elif value == 'CAPS':

        varRow = 2
        varColumn = 0

        for button in buttons:

            command = lambda x=button: select(x)
            if button != 'Space':
                Button(root, text=button, command=command, width=10, ).grid(row=varRow, column=varColumn)

            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1


    else:
        textarea.insert(INSERT, value)

    textarea.focus_set()

root = Tk()
root.title("EYE GAZE")
root.resizable(False,False)
root.config(bg='black')
root.resizable(0, 0)

titleLabel = Label(root, text='EYE GAZE KEYBOARD', font=('arial', 20, 'bold'), bg='black', fg='white')
titleLabel.grid(row=0, columnspan=15)

textarea = Text(root, font=('arial', 15, 'bold'), height=10, width=80, wrap='word',bd=9,relief=SUNKEN)
textarea.grid(row=1, columnspan=15)
textarea.focus_set()

buttons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
           'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', '7', '8', '9',
           'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
           'Shift ↑', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '↑ Shift', '1', '2', '3',
           'Space']

leftShiftButtons = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Backs', 'Del',
                    'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', ']', '7', '8', '9',
                    'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', 'Enter', '4', '5', '6',
                    'Shift ↑', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '?', '↑ Shift', '1', '2', '3',
                    'Space'

                    ]

capsButtons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
               'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', '7', '8', '9',
               'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 'Enter', '4', '5', '6',
               'Shift ↑', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', '↑ Shift', '1', '2', '3',
               'Space']

varRow = 2
varColumn = 0

for button in buttons:

    command = lambda x=button: select(x)
    if button != 'Space':
        Button(root, text=button, command=command, width=10, bg='white' ).grid(row=varRow, column=varColumn)

    if button == 'Space':
        Button(root, text=button, command=command, width=30, bg='white' ).grid(row=6, column=0, columnspan=14)

    varColumn += 1
    if varColumn > 14:
        varColumn = 0
        varRow += 1
root.mainloop()
