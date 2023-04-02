from tkinter import *
from PIL import Image,ImageTk

root = Tk()

root.title('Simple calculator')
root.geometry('370x565')
root.minsize(370,565)

image = Image.open('one.png')
photo = PhotoImage(image)

lbl = Label(text='this is my new GUI').pack()

root.mainloop()