from tkinter import *
root = Tk()
root.geometry('999x777')
root.title('this is menubar class')

main_menu = Menu(root) #this is the main horizontal menu

#first vertical menu
m1 = Menu(main_menu, tearoff=0)
m1.add_command(label='New')
m1.add_command(label='Open')
m1.add_command(label='New window')
m1.add_separator() #this method gives a horizontal rool
m1.add_command(label='Save')
m1.add_command(label='Save as')
m1.add_command(label='Save all')

main_menu.add_cascade(label='File', menu=m1)
root.config(menu=main_menu)

#another vertical menu
m2 = Menu(main_menu, tearoff= 0)
m2.add_command(label='About')
m2.add_command(label='Go')
m2.add_command(label='Contact us')
m2.add_command(label='Show all command')
m2.add_separator()
m2.add_command(label='Report an issue')
m2.add_command(label='Exit', command=quit)

main_menu.add_cascade(label='Help', menu=m2)
root.config(menu=main_menu)


root.mainloop()