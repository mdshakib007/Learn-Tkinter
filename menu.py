from tkinter import *
root = Tk()
root.geometry('888x555')
root.title('more command')
Label(root, text='Output...', font='Serif 12 bold').pack()


def sorry():
    output['text'] = 'Sorry, this file cannot be save!'


def no_file():
    output['text'] = 'No file found!'


def no_computer():
    output['text'] = 'You have no computer or directory!'


output = Label()
output.pack()
# define the menubar
main_menu = Menu(root)
m1 = Menu(main_menu, tearoff=0)

m1.add_command(label='Save', command=sorry)
m1.add_command(label='Save as...', command=sorry)
m1.add_command(label='Save all', command=no_file)
m1.add_separator()
m1.add_command(label='Open file', command=no_computer)
m1.add_command(label='Open folder', command=no_computer)

main_menu.add_cascade(label='File', menu=m1)
root.config(menu=main_menu)

# picture
image1 = PhotoImage(file='news2.png')
Label(root, image=image1).pack()


root.mainloop()
