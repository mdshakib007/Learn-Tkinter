from tkinter import *
root = Tk()
root.geometry('544x433')

def wish():
    print('Good morning!')

def hello():
    print('Hello, shakib!')
    

frame1 = Frame(root, bg='grey')
frame1.pack(side=TOP)

b1 = Button(frame1, bg='green', text='Wish', command=wish)
b1.pack()

b2 = Button(frame1, text='call', bg='aqua', command=hello)
b2.pack()

b3 = Button(frame1, text='Exit', bg='red', command=root.destroy)
b3.pack()

root.mainloop()