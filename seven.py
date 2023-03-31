from tkinter import *
root = Tk()
root.title('tutorial seven')
root.maxsize(400,222)
root.minsize(400,222)

#the entries label
Label(root, text='welcome', font='serief 20 bold').grid(column=1)
Label(root, text='Name').grid(row=1)
Label(root, text='Phone').grid(row=2)
Label(root, text='Email').grid(row=3)

#entries
namevar = StringVar()
phonevar = IntVar()
emailvar = StringVar()

name = Entry(root, textvariable=namevar)
name.grid(row=1,column=1)
phone = Entry(root, textvariable=phonevar)
phone.grid(row=2, column=1)
email = Entry(root, textvariable=emailvar)
email.grid(row=3, column=1)


a = Checkbutton(root, text='Accept terms & condition', font='serief 6')
a.grid(row=4, column=1)
Button(root, text='Submit').grid(row=5,column=1)

root.mainloop()