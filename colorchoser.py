from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import colorchooser

def select_font():
    font = askopenfilename()
    # Code to set selected font

def select_color():
    color = colorchooser.askcolor()
    # Code to set selected color

root = Tk()
menu_bar = Menu(root)

font_menu = Menu(menu_bar, tearoff=0)
font_menu.add_command(label="Select Font", command=select_font)

color_menu = Menu(menu_bar, tearoff=0)
color_menu.add_command(label="Select Color", command=select_color)

menu_bar.add_cascade(label="Font", menu=font_menu)
menu_bar.add_cascade(label="Color", menu=color_menu)

root.config(menu=menu_bar)
root.mainloop()
