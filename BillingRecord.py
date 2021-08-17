# importing modules
# ----------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import database_account
import sqlite3

# creating window setting icon and background
# -----------------------------------------------------------------------------
window = Tk()
window.title("Retail Store Bill management System")
window.config(bg="grey")
window.geometry('1280x750')
window.iconbitmap('bill.ico')
bg = PhotoImage(file="lion.png")
my_label = Label(window, image = bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
frame_colour = '#176385'

# functions for buttons
# --------------------------------------------------------------------------------

def view():
    lb.delete(0, END)
    for row in database_account.viewall():
        lb.insert(END, row)


def search():
    # lb.delete(0, END)
    # for row in database_account.search(name=name.get(), phoneNo=phoneNo.get(), productName=productName.get(), productRate=productRate.get(), productQuantity=productQuantity.get()):
    #     lb.insert(END, row)
    #     break
    con = sqlite3.connect("bills.db")
    cur = con.cursor()
    record_id = EntrySelectId.get()
    cur.execute("SELECT * FROM tableAccount WHERE oid = " + record_id)
    rows = cur.fetchall()
    for row in rows:
        lb.insert(END, row)
        break
    con.close()


def add():
    database_account.add(name.get(), phoneNo.get(), productName.get(), productRate.get(), productQuantity.get(),
                         date.get())
    messagebox.showinfo("Add", "New Account Added Successfully")
    lb.delete(0, END)
    lb.insert(END, name.get(), phoneNo.get(), productName.get(), productRate.get(), productQuantity.get(), date.get())


# def update():
#     database_account.update(name.get(), phoneNo.get(), productName.get(), productRate.get(), productQuantity.get(), date.get())
#     messagebox.showinfo("Update", "Bill Has Been Updated Successfully")
#     view()
def save():
    con = sqlite3.connect("bills.db")
    cur = con.cursor()
    record_id = EntrySelectId.get()
    cur.execute("""UPDATE tableAccount SET
        name = :name,
        phoneNo= :phoneNo,
        productName = :productName,
        productRate = :productRate,
        productQuantity = :productQuantity,
        date = :date
        
        WHERE oid = :oid""",
                {
                    'name': EntryName_editor.get(),
                    'phoneNo': EntryPhonenumber_editor.get(),
                    'productName': EntryproductName_editor.get(),
                    'productRate': EntryproductRate_editor.get(),
                    'productQuantity': EntryproductQuantity_editor.get(),
                    'date': EntryDate_editor.get(),

                    'oid': record_id
                })
    con.commit()
    con.close()
    editor.destroy()


def update():
    global editor
    editor = Tk()
    editor.title("update client and product info")
    editor.geometry("600x600")
    editor.configure(bg='#176385')
    frame_colour = '#176385'

    # database
    con = sqlite3.connect("bills.db")
    cur = con.cursor()
    record_id = EntrySelectId.get()
    cur.execute("SELECT * FROM tableAccount WHERE oid = " + record_id)
    rows = cur.fetchall()

    # global function for search
    global EntryName_editor
    global EntryPhonenumber_editor
    global EntryproductName_editor
    global EntryproductRate_editor
    global EntryproductQuantity_editor
    global EntryDate_editor

    # name
    lblname_editor = Label(editor, text="Name : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
    lblname_editor.grid(row=0, column=0, padx=30, pady=20)

    EntryName_editor = Entry(editor, font=("Calibri", 14, "italic"), width=30)
    EntryName_editor.grid(row=0, column=1, padx=10, pady=20)

    # phoneNo
    lblPhonenumber_editor = Label(editor, text="Phone Number: ", font=("Calibri", 14, "bold"), bg=frame_colour,
                                  fg="white")
    lblPhonenumber_editor.grid(row=1, column=0, padx=30, pady=20)

    EntryPhonenumber_editor = Entry(editor, font=("Calibri", 14, "italic"), width=30)
    EntryPhonenumber_editor.grid(row=1, column=1, padx=10, pady=20)

    # productName
    lblproductName_editor = Label(editor, text="Product name : ", font=("Calibri", 14, "bold"), bg=frame_colour,
                                  fg="white")
    lblproductName_editor.grid(row=2, column=0, padx=30, pady=20)
    EntryproductName_editor = Entry(editor, font=("Calibri", 14, "italic"), width=30)
    EntryproductName_editor.grid(row=2, column=1, padx=10, pady=20)

    # productRate
    lblproductRate_editor = Label(editor, text="Product Rate : ", font=("Calibri", 14, "bold"), bg=frame_colour,
                                  fg="white")
    lblproductRate_editor.grid(row=3, column=0, padx=30, pady=20)

    EntryproductRate_editor = Entry(editor, font=("Calibri", 14, "italic"), width=30)
    EntryproductRate_editor.grid(row=3, column=1, padx=10, pady=20)

    # productQuantity
    lblproductQuantity_editor = Label(editor, text="Product Quantity : ", font=("Calibri", 14, "bold"), bg=frame_colour,
                                      fg="white")
    lblproductQuantity_editor.grid(row=4, column=0, padx=30, pady=20)

    EntryproductQuantity_editor = Entry(editor, font=("Calibri", 14, "italic"), width=30)
    EntryproductQuantity_editor.grid(row=4, column=1, padx=10, pady=20)

    # date
    lbldate_editor = Label(editor, text="Date : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
    lbldate_editor.grid(row=5, column=0, padx=30, pady=20)

    EntryDate_editor = Entry(editor, font=("Calibri", 14, "italic"), width=30)
    EntryDate_editor.grid(row=5, column=1, padx=10, pady=20)

    # SelectId
    lblSelectId_editor = Label(editor, text="Select Id : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
    lblSelectId_editor.grid(row=6, column=0, padx=30, pady=20)

    EntrySelectId_editor = Entry(editor, font=("Calibri", 14, "italic"), width=30)
    EntrySelectId_editor.grid(row=6, column=1, padx=10, pady=20)

    # save button
    SaveButton = Button(editor, text="Save Record", width=12, command=save, font=("Calibri", 10, "bold"), fg="black",
                        bg="navajo white", padx=5, pady=10)
    SaveButton.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

    # loop trough rows
    for row in rows:
        EntryName_editor.insert(0, row[0])
        EntryPhonenumber_editor.insert(0, row[1])
        EntryproductName_editor.insert(0, row[2])
        EntryproductRate_editor.insert(0, row[3])
        EntryproductQuantity_editor.insert(0, row[4])
        EntryDate_editor.insert(0, row[5])
        EntrySelectId_editor.insert(0, row[6])
    # con.commit()
    # con.close()
    editor.mainloop()


def delete():
    con = sqlite3.connect("bills.db")
    cur = con.cursor()
    cur.execute("DELETE FROM tableAccount WHERE oid= " + EntrySelectId.get())
    con.commit()
    con.close()
    messagebox.showinfo("Delete Account", 'Account Has Been Deleted Successfully')
    view()
    # lb.delete(END, get_selected_row.selected_tuple)


def clear():
    lb.delete(0, END)
    EntryName.delete(0, END)
    EntryPhonenumber.delete(0, END)
    EntryproductName.delete(0, END)
    EntryproductRate.delete(0, END)
    EntryproductQuantity.delete(0, END)
    EntryDate.delete(0, END)


# Design
# -----------------------------------------------------------------------------------------


# Title of the app
# --------------------------------------------------------------------------------
title = Label(window, pady=2, text="Bill Management System", bd=12, bg=frame_colour, fg='white', font=('cambria', 30, 'bold'))
title.pack(fill=X)

# coustomer information
# ----------------------------------------------------
F1 = LabelFrame(window, text="Customer's information", font=('cambria', 18, 'bold'), fg='black', bg=frame_colour)
F1.place(x=0, y=80, relwidth=1)

# name
lblname = Label(F1, text="Name : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
lblname.grid(row=0, column=0, padx=20, pady=5)
name = StringVar()
EntryName = Entry(F1, textvariable=name, font=("Calibri", 14, "italic"), width=30)
EntryName.grid(row=0, column=1, padx=10, pady=5)

# phoneNo
lblPhonenumber = Label(F1, text="Phone Number: ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
lblPhonenumber.grid(row=0, column=2, padx=20, pady=5)
phoneNo = StringVar()
EntryPhonenumber = Entry(F1, textvariable=phoneNo, font=("Calibri", 14, "italic"), width=30)
EntryPhonenumber.grid(row=0, column=3, padx=10, pady=5)

# product information
# -----------------------------------------------
F2 = LabelFrame(window, text='Product Information', font=('cambria', 18, 'bold'), fg='black', bg=frame_colour)
F2.place(x=0, y=180, width=660, height=600)

# productName
lblproductName = Label(F2, text="Product name : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
lblproductName.grid(row=0, column=0, padx=30, pady=20)
productName = StringVar()
EntryproductName = Entry(F2, textvariable=productName, font=("Calibri", 14, "italic"), width=30)
EntryproductName.grid(row=0, column=1, padx=10, pady=20)

# productRate
lblproductRate = Label(F2, text="Product Rate : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
lblproductRate.grid(row=1, column=0, padx=30, pady=20)
productRate = StringVar()
EntryproductRate = Entry(F2, textvariable=productRate, font=("Calibri", 14, "italic"), width=30)
EntryproductRate.grid(row=1, column=1, padx=10, pady=20)

# productQuantity
lblproductQuantity = Label(F2, text="Product Quantity : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
lblproductQuantity.grid(row=2, column=0, padx=30, pady=20)
productQuantity = StringVar()
EntryproductQuantity = Entry(F2, textvariable=productQuantity, font=("Calibri", 14, "italic"), width=30)
EntryproductQuantity.grid(row=2, column=1, padx=10, pady=20)

# date
lbldate = Label(F2, text="Date : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
lbldate.grid(row=3, column=0, padx=30, pady=20)
date = StringVar()
EntryDate = Entry(F2, textvariable=date, font=("Calibri", 14, "italic"), width=30)
EntryDate.grid(row=3, column=1, padx=10, pady=20)

# SelectId
lblSelectId = Label(F2, text="Select Id : ", font=("Calibri", 14, "bold"), bg=frame_colour, fg="white")
lblSelectId.grid(row=5, column=0, padx=30, pady=20)
SelectId = StringVar()
EntrySelectId = Entry(F2, textvariable=SelectId, font=("Calibri", 14, "italic"), width=30)
EntrySelectId.grid(row=5, column=1, padx=10, pady=20)

# Buttons to save customer and product iformation
# ---------------------------------------------------------------------------------------------------------------
AddButton = Button(F2, text="Add", width=12, command=add, font=("Calibri", 10, "bold"), fg="black", bg="#ad4c7d",
                   padx=5, pady=5)
AddButton.grid(row=4, column=1, padx=5, pady=5)

UpdateButton = Button(F2, text="Update", width=12, command=update, font=("Calibri", 10, "bold"), fg="black",
                      bg="#6ccc91", padx=5, pady=5)
UpdateButton.grid(row=6, column=0, padx=5, pady=5)

SearchButton = Button(F2, text="Search", width=12, command=search, font=("Calibri", 10, "bold"), fg="black",
                      bg="#68aed9", padx=15, pady=15)
SearchButton.grid(row=7, column=0, padx=15, pady=15)

ViewAllButton = Button(F2, text="View All", width=12, command=view, font=("Calibri", 10, "bold"), fg="black",
                       bg="#6ccc91", padx=5, pady=5)
ViewAllButton.grid(row=6, column=1, padx=5, pady=5)

DeleteButton = Button(F2, text="Delete", width=12, command=delete, font=("Calibri", 10, "bold"), fg="black",
                      bg="#6ccc91", padx=5, pady=5)
DeleteButton.grid(row=6, column=2, padx=5, pady=5)

ClearAllButton = Button(F2, text="Clear All", width=12, command=clear, font=("Calibri", 10, "bold"), fg="black",
                        bg="#68aed9", padx=15, pady=15)
ClearAllButton.grid(row=7, column=1, padx=15, pady=15)

# Bill showing area
# -------------------------------------------------------------------------------------------------------------------
F3 = Frame(window)
F3.place(x=700, y=180, width=550, height=500)

sb = Scrollbar(F3, orient=VERTICAL)
lb = Listbox(F3, height=20, width=94, yscrollcommand=sb.set)

sb.configure(command=lb.yview)
sb.pack(side=RIGHT, fill=Y)
lb.pack(pady=15)


window.mainloop()
