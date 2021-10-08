from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import Backend

root=Tk()
root.title("Contact Management System")
root.geometry("950x630")
root.resizable(width=False,height=False)
root.configure(bg="#00091a")
#******************************************FUNCTIONS********************************************************************
def SelectRecord(event):
    selected = data_listBox.focus()
    data = data_listBox.item(selected)
    row = data["values"]
    contactTypeVar.set(row[0])
    contactNo1Var.set(row[1])
    nameVar.set(row[2])
    cityVar.set(row[3])
    addressVar.set(row[4])
    emailVar.set(row[5])

def clear():
    contactTypeVar.set("Select Contact Type")
    contactNo1Var.set("")
    nameVar.set("")
    emailVar.set("")
    addressVar.set("")
    cityVar.set("")
    data_listBox.delete(*data_listBox.get_children())
    noContacts_Lbl.configure(text="No Contacts")

def exit():
    msg=messagebox.askyesno("Contact Management System","Confirm you want to exit")
    if msg:
        root.destroy()

def addNew():
    if (len(contactNo1Var.get()) == 0):
        messagebox.showwarning("Warning","Fill in missing details")
    elif (len(contactNo1Var.get()) != 0):
        noContacts_Lbl.configure(text="All Contacts")
        Backend.addRec(contactTypeVar.get(), contactNo1Var.get(),nameVar.get()\
            ,cityVar.get(),addressVar.get(),emailVar.get())
        messagebox.showinfo("Contact Management System","Contact added successfully !")
        clear()

def Delete():
    if (len(contactNo1Var.get()) == 0 and len(nameVar.get()) == 0):
        messagebox.showwarning("Warning","Fill in ContactNo. or Name to delete")
    elif (len(contactNo1Var.get()) != 0 or len(nameVar.get()) != 0):
        Backend.deleteRec(contactNo1Var.get(),nameVar.get())
        messagebox.showinfo("Contact Management System","Contact deleted successfully !")
        clear()
        display()

def display():
    clear()
    noContacts_Lbl.configure(text="All Contacts")
    for i in Backend.displayRec():
        data_listBox.insert("","end",text=str(i[0]),values=(str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6])))
        
def search():
    if (len(contactNo1Var.get()) == 0 and len(nameVar.get())==0):
        messagebox.showwarning("Warning","Enter name or contact no. to search")
    elif (len(contactNo1Var.get()) != 0 or len(nameVar.get())!=0):
        for i in Backend.searchRec(contactNo1Var.get(),nameVar.get()):
            clear()
            data_listBox.insert("","end",text=str(i[0]),values=(str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6])))
        
               
#***************************************************************************************************************************
optionList=["Home","Office","Personal","Other"]
contactImg = PhotoImage(file="contact.png")

contactTypeVar=StringVar()
contactTypeVar.set("Select Contact Type")
contactNo1Var=StringVar()
nameVar=StringVar()
addressVar=StringVar()
cityVar=StringVar()
emailVar=StringVar()

#********************************HEADING FRAME and LABEL************************************************************

headFrame = Frame(root,width=940,height=80,bg="#001133",bd=4,relief=RAISED)
headFrame.place(x=5,y=5)

heading = Label(headFrame,text="CONTACT BOOK",font="mssanserif 30 bold",bg="#001133",fg="white")
heading.place(x=290,y=10)

contactImg_Lbl = Label(headFrame,bd=3,relief=SUNKEN,image=contactImg)
contactImg_Lbl.place(x=230,y=3)

#**********************************LEFT FRAME and ENTRIES ,LABELS***********************************************************************
leftFrame = Frame(root,width=480,height=420,bg="#001133",bd=4,relief=RAISED)
leftFrame.place(x=5,y=95)

#Labels
contactType_Lbl=Label(leftFrame,text="Contact Type : ",font="verdana 15 bold",bg="#001133",fg="white")
contactType_Lbl.place(x=10,y=60)
contactNo1_Lbl=Label(leftFrame,text="Contact No. : ",font="verdana 15 bold",bg="#001133",fg="white")
contactNo1_Lbl.place(x=10,y=110)
name_Lbl=Label(leftFrame,text="Name : ",font="verdana 15 bold",bg="#001133",fg="white")
name_Lbl.place(x=10,y=160)
city_Lbl=Label(leftFrame,text="City : ",font="verdana 15 bold",bg="#001133",fg="white")
city_Lbl.place(x=10,y=210)
address_Lbl=Label(leftFrame,text="Address : ",font="verdana 15 bold",bg="#001133",fg="white")
address_Lbl.place(x=10,y=260)
email_Lbl=Label(leftFrame,text="Email : ",font="verdana 15 bold",bg="#001133",fg="white")
email_Lbl.place(x=10,y=310)

#Entries
contactType_list = OptionMenu(leftFrame,contactTypeVar,*optionList)
contactType_list.place(x=200,y=60)
E_contactNo1=Entry(leftFrame,textvar=contactNo1Var,font="verdana 14 bold",width=17,bd=2,relief=RAISED)
E_contactNo1.place(x=200,y=110)
E_name=Entry(leftFrame,textvar=nameVar,font="verdana 14 bold",width=17,bd=2,relief=RAISED)
E_name.place(x=200,y=160)
E_city=Entry(leftFrame,textvar=cityVar,font="verdana 14 bold",width=17,bd=2,relief=RAISED)
E_city.place(x=200,y=210)
E_address=Entry(leftFrame,textvar=addressVar,font="verdana 14 bold",width=17,bd=2,relief=RAISED)
E_address.place(x=200,y=260)
E_email=Entry(leftFrame,textvar=emailVar,font="verdana 14 bold",width=17,bd=2,relief=RAISED)
E_email.place(x=200,y=310)


#**********************************RIGHT FRAME and LISTBOX***********************************************************************
rightFrame = Frame(root,width=450,height=450,bg="black",bd=4,relief=RAISED)
rightFrame.place(x=492,y=135)

yscrollbar = Scrollbar(rightFrame,orient=VERTICAL)
yscrollbar.pack(side=RIGHT,fill=Y)
xscrollbar = Scrollbar(rightFrame,orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM,fill=X)

data_listBox = ttk.Treeview(rightFrame,height=17,columns=("ContactType","ContactNo","Name","City","Address","Email")\
    ,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
data_listBox.bind("<ButtonRelease-1>",SelectRecord)
data_listBox.column("#0",width=40,minwidth=30,anchor="c")
data_listBox.column("ContactType",width=60,minwidth=30,anchor="c")
data_listBox.column("ContactNo",width=85,minwidth=30,anchor="c")
data_listBox.column("Name",width=60,minwidth=30,anchor="c")
data_listBox.column("City",width=50,minwidth=30,anchor="c")
data_listBox.column("Address",width=60,minwidth=30,anchor="c")
data_listBox.column("Email",width=70,minwidth=30,anchor="c")

data_listBox.heading("#0",text="No.")
data_listBox.heading("ContactType",text="Type")
data_listBox.heading("ContactNo",text="Contact")
data_listBox.heading("Name",text="Name")
data_listBox.heading("City",text="City")
data_listBox.heading("Address",text="Address")
data_listBox.heading("Email",text="Email")

data_listBox.pack(side=TOP,fill=X)
yscrollbar.config(command=data_listBox.yview)
xscrollbar.config(command=data_listBox.xview)

noContacts_Lbl=Label(root,text="NO CONTACTS",font="mssanserif 16 bold",fg="white",bg="#00091a")
noContacts_Lbl.place(x=630,y=100)

#**********************************BUTTON FRAME and BUTTONS ***********************************************************************
BtnFrame = Frame(root,width=940,height=100,bg="#001133",bd=4,relief=RAISED)
BtnFrame.place(x=5,y=522)


addBtn = Button(BtnFrame,text="Add New",font="mssanserif 15 bold",bg="black",fg="white",width=9,height=3,command=addNew)
addBtn.place(x=3,y=4)
displayBtn = Button(BtnFrame,text="Display",font="mssanserif 15 bold",bg="black",fg="white",width=9,height=3,command=display)
displayBtn.place(x=158,y=4)
deleteBtn = Button(BtnFrame,text="Delete",font="mssanserif 15 bold",bg="black",fg="white",width=9,height=3,command=Delete)
deleteBtn.place(x=313,y=4)
searchBtn = Button(BtnFrame,text="Search",font="mssanserif 15 bold",bg="black",fg="white",width=9,height=3,command=search)
searchBtn.place(x=468,y=4)
clearBtn = Button(BtnFrame,text="Clear",font="mssanserif 15 bold",bg="black",fg="white",width=9,height=3,command=clear)
clearBtn.place(x=623,y=4)
exitBtn = Button(BtnFrame,text="Exit",font="mssanserif 15 bold",bg="black",fg="white",width=9,height=3,command=exit)
exitBtn.place(x=779,y=4)

#***********************************************************************************************************************

root.mainloop()
