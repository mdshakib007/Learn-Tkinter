from tkinter import *
root = Tk()
root.geometry('444x333')

def get_val():
    print(f'Username: {user_in.get()}')
    print(f'Password: {pass_in.get()}')

label1 = Label(root, text='Username')
label1.grid()
label2 = Label(root, text='Password')
label2.grid(row=1)

user_in = StringVar()
pass_in = StringVar()

username = Entry(root, textvariable=user_in).grid(column=1, row=0)
password = Entry(root, textvariable=pass_in, show='*').grid(column=1, row=1)

Button(root, text='Submit', command=get_val).grid(row=2,column=1)

root.mainloop()