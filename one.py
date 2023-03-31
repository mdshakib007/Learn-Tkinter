from tkinter import *

root = Tk()
root.title('this is my learning page!')
root.geometry('733x434') #widthxheight
root.minsize(333,222) #width, height
#root.maxsize(1000,800) we don't need this

lbl = Label(text='Welcome to my GUI!')
lbl.pack()


root.mainloop()