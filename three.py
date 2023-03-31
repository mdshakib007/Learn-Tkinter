from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("My learning")

name = ttk.Button(frm, text="Name").grid(column=0,row=0)
e1 = ttk.Entry(root).grid(column=1,row=0)

pas = ttk.Button(root, text="Password").grid(column=0, row=1)
e2 = ttk.Entry(root).grid(column=1,row=1)

submit = ttk.Button(root, text="Submit").grid(column=1, row=3)






root.mainloop()