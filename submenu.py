from tkinter import *

root = Tk()

# create the top-level menu
menu = Menu(root)
root.config(menu=menu)

# create the File menu and add it to the top-level menu
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

# create the Edit menu and add it to the top-level menu
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)

# create a submenu for the File menu and add it to the File menu
new_menu = Menu(file_menu)
file_menu.add_cascade(label="New", menu=new_menu)

# add an item to the New submenu
new_menu.add_command(label="File", command=lambda: print("New File"))

# create a submenu for the Edit menu and add it to the Edit menu
undo_menu = Menu(edit_menu)
edit_menu.add_cascade(label="Undo", menu=undo_menu)

# add an item to the Undo submenu
undo_menu.add_command(label="undo", command=lambda: print("Undo"))

root.mainloop()
