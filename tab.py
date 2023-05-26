from tkinter import *
from tkinter import ttk

root = Tk()
root.title('tabs in tkinter')
root.geometry('888x555')

# create a tab/notebook
notebook = ttk.Notebook(root)

# first tab
tab1 = ttk.Frame(notebook)
ttk.Label(tab1, text='this is first tab').pack()
ttk.Button(tab1, text='Tab1').pack()

tab2 = ttk.Frame(notebook)
ttk.Label(tab2, text='This is tab 2').pack()

tab3 = ttk.Frame(notebook)
ttk.Label(tab3, text='This is tab 3. this is a paragraph for tab number 3').pack()

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')

notebook.pack()

root.mainloop()
