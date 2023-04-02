from tkinter import *
root = Tk()
root.geometry('888x555')
root.title('Menubar tutorial')

main_menu = Menu(root) #this is the main horizontal menubar

menu1 = Menu(root, tearoff=0)
menu1.add_command(label='Save as..')
menu1.add_command(label='Edit')
menu1.add_separator()
menu1.add_command(label='View')
main_menu.add_cascade(label='File', menu=menu1)
root.config(menu=main_menu)

menu2 = Menu(root, tearoff=0)
menu2.add_command(label='Edit')
menu2.add_command(label='ME')
menu2.add_command(label='mytest')
menu2.add_separator()
menu2.add_command(label='About me')
main_menu.add_cascade(label='View', menu=menu2)
root.config(menu=main_menu)

root.mainloop()
