from tkinter import *

root = Tk()

# create the top-level menu
menu = Menu(root)
root.config(menu=menu)

# create the Edit menu and add it to the top-level menu
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)

# create a submenu for the Edit menu and add it to the Edit menu
undo_menu = Menu(edit_menu)
edit_menu.add_cascade(label="Undo", menu=undo_menu)

# add an item to the Undo submenu
undo_menu.add_command(label="undo", command=lambda: print("Undo"))

root.mainloop()
