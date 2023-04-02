from tkinter import *
import tkinter.messagebox as tmsg
import os

#define all function that will be execute by command
def new_text_file():
    pass

def new_file():
    pass

def open():
    pass

def recent():
    pass

def save():
    pass

def save_as():
    pass

def save_all():
    pass

def share():
    pass

def undo():
    pass

def redo():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def expand():
    pass

def change_bg():
    pass

def font_color():
    pass

def font():
    pass

def size():
    pass

def bold():
    pass

def italic():
    pass

def underline():
    pass

def welcome():
    pass

def doc():
    pass

def tutorial():
    pass

def source():
    pass

def github():
    pass

def report():
    pass

def update():
    pass

def about():
    pass

root = Tk()
root.configure(bg='#B9B8B8')
root.geometry('888x555')
root.minsize(400,222)
root.title('Untitled - Text Editor')

#make menubar's
main_menu = Menu(root) # main horizontal menubar

m1 = Menu(main_menu, tearoff=0) #this is the vertical menubar
m1.add_command(label='New Text File', command=new_text_file)
m1.add_command(label='New File...', command=new_file)
m1.add_command(label='Open File', command=open)
m1.add_command(label='Open Recent', command=recent)
m1.add_separator()
m1.add_command(label='Save', command=save)
m1.add_command(label='Save As...', command=save_as)
m1.add_command(label='Save All', command=save_all)
m1.add_separator()
m1.add_command(label='Share', command=share)
m1.add_separator()
m1.add_command(label='Exit', command=root.destroy) # 'quit' and 'root.destroy' is same

main_menu.add_cascade(label='File', menu=m1, font='lucida 10 bold')
root.config(menu=main_menu) #done configuration of first menu bar

#menu 2
m2 = Menu(main_menu, tearoff=0) #this is the vertical menubar
m2.add_command(label='Undo', command=undo)
m2.add_command(label='Redo',command=redo)
m2.add_separator()
m2.add_command(label='Cut', command=cut)
m2.add_command(label='Copy', command=copy)
m2.add_command(label='Paste', command=paste)
m2.add_separator()
m2.add_command(label='Expand Editor', command=expand)
m2.add_separator()
m2.add_command(label='Close Editor', command=quit) # 'quit' and 'root.destroy' is same

main_menu.add_cascade(label='Edit', menu=m2, font='lucida 10 bold')
root.config(menu=main_menu) #done configuration of second menu bar

#menu 3
m3 = Menu(main_menu, tearoff=0) #this is the vertical menubar
m3.add_command(label='Change Background', command=change_bg)
m3.add_command(label='Change Font Color', command=font_color)
m3.add_separator()
m3.add_command(label='Font', command=font)
m3.add_command(label='Size', command=size)
m3.add_command(label='Bold', command=bold)
m3.add_command(label='Italic', command=italic)
m3.add_command(label='Underline', command=underline)
m3.add_separator()
m3.add_command(label='Close', command=quit)

main_menu.add_cascade(label='Help', menu=m3, font='lucida 10 bold')
root.config(menu=main_menu) # done configuration of third menu bar

#menu 4
m4 = Menu(main_menu, tearoff=0) #this is the vertical menubar
m4.add_command(label='Welcome', command=welcome)
m4.add_command(label='Documentation', command=doc)
m4.add_separator()
m4.add_command(label='Tutorial', command=tutorial)
m4.add_command(label='Source Code', command=source)
m4.add_command(label='GitHub', command=github)
m4.add_separator()
m4.add_command(label='Report Issue', command=report)
m4.add_separator()
m4.add_command(label='Check For Updates...', command=update)
m4.add_separator()
m4.add_command(label='About', command=about)

main_menu.add_cascade(label='Help', menu=m4, font='lucida 10 bold')
root.config(menu=main_menu) # done configuration of 4th menu bar


#define the text area
text_area = Text(root, bg='#B0A1A1', fg='black', font='Arial 14')
text_area.pack(fill='both', expand=True)

#define the vertical scroller 
scroll = Scrollbar(text_area)
scroll.pack(side='right', fill='y')
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)


root.mainloop()