from tkinter import *
import ttkbootstrap as ttk
import tkinter.messagebox as tmsg
import mysql.connector
import store_data as std

root = ttk.Window()
root.geometry('430x430')
root.title('Submit Report')
root.maxsize(430, 430)
root.minsize(430, 430)

def submit():
    name_data = name_entry.get()
    email_data = email_entry.get()
    report_data = message_entry.get(1.0, END).replace('\n', ' ')
    if name_data == '':
        tmsg.showerror('Error', 'Name cannot be empty!')
        
    elif email_data == '':
        tmsg.showerror('Error', 'Email cannot be empty!')

    else:
        insertdata = std.Data()
        insertdata.insert_into(name_data, email_data, report_data)
        
        tmsg.showinfo('Submitted', 'Your report sumitted successfully.')
        
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        message_entry.delete(1.0, END)
        


ttk.Label(root, text='Report an issue_', font='Arial 25 bold').grid(
    row=0, column=1, columnspan=2, pady=20)

name = StringVar()
email = StringVar()
ttk.Label(root, text='Name').grid(row=1, column=0, pady=10)
ttk.Label(root, text='Email').grid(row=2, column=0, pady=10)
ttk.Label(root, text='Issue').grid(row=3, column=0, pady=10)

name_entry = Entry(root, textvariable=name, width=40)
email_entry = Entry(root, textvariable=email,width=40 )
message_entry = Text(root, width=40, height=5)

name_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
message_entry.grid(row=3, column=1,)


# relief = ["raised", "sunken", "flat", "ridge", "solid", "groove"] 
b1 = ttk.Button(root, text='Submit', command=submit)
b1.grid(row=4, column=1, pady=10,)


root.mainloop()
