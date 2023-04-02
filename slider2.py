from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('666x444')
root.title('slider 2')

def get_dollar():
    tmsg.showinfo('Message', f'Successfully collected ${scale1.get()}.')

Label(root, text='How many dollars do you need from this app?', bg='skyblue', font='Arial 16 bold').pack()

scale1 = Scale(root, from_=0, to=100, highlightbackground='blue', tickinterval=50, orient=HORIZONTAL)
scale1.pack() # this is a simple scale

Button(root, text='Get Now', border=5, bg='green', command=get_dollar).pack()



root.mainloop()