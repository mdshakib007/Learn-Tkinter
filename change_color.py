from tkinter import *
import tkinter.colorchooser

root = Tk()
root.title('change color')
# define commands


def change_bg():
    # if i import 'from tkinter import colorchooser' this then the command 'colorchooser.askcolor()' simply
    color = tkinter.colorchooser.askcolor()
    text_area.config(bg=color[1])  # then we just change the bg color


def change_fg():
    color = tkinter.colorchooser.askcolor()
    text_area.config(fg=color[1])


text_area = Text(root)
text_area.pack()  # defined a text area

b1 = Button(root, text='Change Background', command=change_bg)
b2 = Button(root, text='Change Forground', command=change_fg)

b1.pack()
b2.pack()


root.mainloop()
