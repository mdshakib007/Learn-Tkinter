from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# define all function that will be execute by command


def new_text_file():
    global file
    root.title('Untitled-1 - NotePaaD')
    # clear the text area and change the name of file
    text_area.delete(1.0, END)


def new_file():
    global file
    root.title('Untitled-1 - NotePaaD')
    text_area.delete(1.0, END)


def open_file():
    global file  # defining file as global then we can change the value of file argument in a specific function
    file = askopenfilename(defaultextension='.txt', filetypes=[
        ('All Files', '*.*'), ('Text Document', '*.txt'), ('Python File', '*.py')
    ])   # Defined supported file types

    if file == '':
        file = None
    else:
        # change the file name as path's main file name
        root.title(os.path.basename(file) + ' - NotePaaD')
        # when we open a file, the text area should be empty
        text_area.delete(1.0, END)

        # try to open a file as read mode, because we just need to read file and insert the file in text_area.
        f = open(file, 'r')
        # after open a file, we read all of the content of file and insert 1st column and 0th text to end of file
        text_area.insert(1.0, f.read())
        f.close()  # then simply close the file


def recent():  # same like open_file() function
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[
        ('All Files', '*.*'), ('Text Document', '*.txt'), ('Python File', '*.py')
    ])

    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + ' - NotePaaD')
        text_area.delete(1.0, END)

        f = open(file, 'r')
        text_area.insert(1.0, f.read())
        f.close()


def save():
    global file  # define file is global, sothat we can change the value of file method
    if file == None:
        file = asksaveasfilename(
            initialfile='Untitled.txt',
            defaultextension='.txt',
            filetypes=[('All Files', '*.*'), ('Text Document',
                                              '*.txt'), ('Python File', '*.py')]
        )  # we initialize the file name to Untitled.txt then give diff file extensions

        if file == '':
            file = None
        else:
            # at this time i opened file as 'write' mode, because i want to append/write all content in new opened file from text_area
            f = open(file, 'w')
            # the get() method/function give us all content from text_area and write opend file
            f.write(text_area.get(1.0, END))
            f.close()

            # at last we changed the title
            root.title(os.path.basename(file) + ' - NotePaaD')

    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()


def save_as():  # just like previous function
    global file
    if file == None:
        file = asksaveasfilename(
            initialfile='Untitled-1.txt',
            defaultextension='.txt',
            filetypes=[('All Files', '*.*'), ('Text Document',
                                              '*.txt'), ('Python File', '*.py')]
        )

        if file == '':
            file = None
        else:
            f = open(file, 'w')
            f.write(text_area.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + ' - NotePaaD')

    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()


def save_all():
    tmsg.showerror('Error', 'No such file or directory found to save')


def share():
    tmsg.askokcancel(
        'Share', 'Please share this app with other!\nFacebook: https://facebook.com\nGitHub: https://github.com')


def undo():
    try:
        text_area.edit_undo() # just i defined undo=True in text_area 
    except: #this undo and redo method show error when nothing to undo and redo.
        tmsg.showerror('Error', 'Nothing to Undo!')


def redo():
    try:
        text_area.edit_redo()
    except:
        tmsg.showerror('Error', 'Nothinh to Redo!')


def cut():
    # the cut, copy and paste is pre-maked, so just write the syntax
    text_area.event_generate('<<Cut>>')


def copy():
    text_area.event_generate('<<Copy>>')


def paste():
    text_area.event_generate('<<Paste>>')


def resize():
    root.geometry('888x555')  # define the size of editor to default


def expand():
    root.geometry('1400x700')


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
    tmsg.showinfo('Welcome Message',
                  'Welcome to this text editor!\n\nShakib is developing this.\n\nThis is not completed yet!')


def doc():
    tmsg.showinfo('Documentation', 'We have no Documantation at this time,\nBut Shakib is working on it!')


def tutorial():
    tmsg.askyesnocancel('Tutorial', 'Follow me on GitHub to get tutorial-\nlink: https://github.com/mdshakib007')


def source():
    tmsg.askquestion('Source Code', 'Source Code: https://github.com/mdshakib007/Tkinter-Projects/blob/master/texteditor.py')


def github():
    tmsg.showinfo('GitHub', 'Github: https://github.com/mdshakib007')


def report():
    tmsg.askokcancel('Report an issue', 'Report an issue: shakibahmed00777@gmail.com')


def update():
    tmsg.showerror('Check for updates', 'Nothing to update!\nyou are using the latest version of NotePaaD!')


def about():
    tmsg.askokcancel('About NotePaaD', 'This is a simple text editor, made with python(Tkinter), by Md Shakib Ahmed.')


root = Tk()
root.configure(bg='#B9B8B8')
root.geometry('888x555')
root.minsize(400, 222)
root.title('Untitled - NotePaaD  -by @Md Shakib Ahmed')

# make menubar's
main_menu = Menu(root)  # main horizontal menubar

m1 = Menu(main_menu, tearoff=0)  # this is the vertical menubar
m1.add_command(label='New Text File', command=new_text_file)
m1.add_command(label='New File...', command=new_file)
m1.add_command(label='Open File', command=open_file)
m1.add_command(label='Open Recent', command=recent)
m1.add_separator()
m1.add_command(label='Save', command=save)
m1.add_command(label='Save As...', command=save_as)
m1.add_command(label='Save All', command=save_all)
m1.add_separator()
m1.add_command(label='Share', command=share)
m1.add_separator()
# 'quit' and 'root.destroy' is same
m1.add_command(label='Exit', command=root.destroy)

main_menu.add_cascade(label='File', menu=m1, font='lucida 10 bold')
root.config(menu=main_menu)  # done configuration of first menu bar

# menu 2
m2 = Menu(main_menu, tearoff=0)  # this is the vertical menubar
m2.add_command(label='Undo', command=undo)
m2.add_command(label='Redo', command=redo)
m2.add_separator()
m2.add_command(label='Cut', command=cut)
m2.add_command(label='Copy', command=copy)
m2.add_command(label='Paste', command=paste)
m2.add_separator()
m2.add_command(label='Resize Editor', command=resize)
m2.add_command(label='Expand Editor', command=expand)
m2.add_separator()
# 'quit' and 'root.destroy' is same
m2.add_command(label='Close Editor', command=quit)

main_menu.add_cascade(label='Edit', menu=m2, font='lucida 10 bold')
root.config(menu=main_menu)  # done configuration of second menu bar

# menu 3
m3 = Menu(main_menu, tearoff=0)  # this is the vertical menubar
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

main_menu.add_cascade(label='Selection', menu=m3, font='lucida 10 bold')
root.config(menu=main_menu)  # done configuration of third menu bar

# menu 4
m4 = Menu(main_menu, tearoff=0)  # this is the vertical menubar
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
root.config(menu=main_menu)  # done configuration of 4th menu bar


# define the text area
text_area = Text(root, bg='white', fg='black', font='Arial 14', undo=True)
text_area.pack(fill='both', expand=True)

file = None  # define the file to none

# define the vertical scroller
scroll = Scrollbar(text_area)
scroll.pack(side='right', fill='y')
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)


root.mainloop()
