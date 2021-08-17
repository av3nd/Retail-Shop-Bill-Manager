import sqlite3


def create():
    con = sqlite3.connect("bills.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tableAccount(id INTEGER PRIMARY KEY,name TEXT, phoneNo TEXT, productName TEXT, productRate TEXT,productQuantity TEXT, date TEXT)")
    con.commit()
    con.close()


def viewall():
    con = sqlite3.connect("bills.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tableAccount")
    rows = cur.fetchall()
    con.close()
    return rows


# def search(name="", phoneNo="", productName="", productRate="", productQuantity="",date=""):
#     con = sqlite3.connect("bills.db")
#     cur = con.cursor()
#     cur.execute("SELECT * FROM tableAccount WHERE name=? or phoneNo=? OR productName=? OR productRate=? OR productQuantity=? OR date=?",(name, phoneNo, productName, productRate, productQuantity,date))
#     rows = cur.fetchall()
#     con.close()
#     return rows


def add(name,phoneNo, productName, productRate, productQuantity, date):
    con = sqlite3.connect("bills.db")
    cur = con.cursor()
    cur.execute("INSERT INTO tableAccount VALUES(NULL,?,?,?,?,?,?)", (name,phoneNo, productName, productRate, productQuantity, date))
    con.commit()
    con.close()


create()
