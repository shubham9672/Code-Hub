import sqlite3

def Connect_ContactInfo():
    con = sqlite3.connect("contactInfo.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ContactInfo(id INTEGER PRIMARY KEY,contactTypeVar text,contactNo1Var text, \
        nameVar text,cityVar text,addressVar text,emailVar text)")
    con.commit()
    con.close()

def addRec(contactTypeVar,contactNo1Var,nameVar,cityVar,addressVar,emailVar):
    con = sqlite3.connect("contactInfo.db")
    cur = con.cursor()
    cur.execute("INSERT INTO ContactInfo(contactTypeVar,contactNo1Var,nameVar,cityVar,addressVar,emailVar)\
        VALUES(?,?,?,?,?,?)",(contactTypeVar,contactNo1Var,nameVar,cityVar,addressVar,emailVar))
    con.commit()
    con.close()

def displayRec():
    con = sqlite3.connect("contactInfo.db")
    cur = con.cursor()
    cur.execute("select * from ContactInfo")
    data = cur.fetchall()
    con.close()
    return data

def deleteRec(contact,name):
    con = sqlite3.connect("contactInfo.db")
    cur = con.cursor()
    cur.execute("DELETE FROM ContactInfo WHERE contactNo1Var=? OR nameVar=?",(contact,name,))
    con.commit()
    con.close()

def searchRec(contact,name):
    con=sqlite3.connect("contactInfo.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM ContactInfo WHERE contactNo1Var=? OR nameVar=?",(contact,name))
    data=cur.fetchall()
    con.close()
    return data
  
Connect_ContactInfo()