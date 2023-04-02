from tkinter import *
root = Tk()
root.geometry('777x444')

def get_size():
    root.update()
    root.geometry(f'{ent1.get()}x{ent2.get()}')


# the message and indicators
Label(root, text='Enter the size of window:', font='Serif 20 bold', padx=50).grid(row=0, column=1)
Label(root, text='Enter Width:', font='Serif 12 bold').grid(row=1, column=0)
Label(root, text='Enter Height:', font='Serif 12 bold').grid(row=2, column=0)
#entry widgets to get height and width
ent1 = Entry(root)
ent2 = Entry(root)
#pack the entry widget's
ent1.grid(row=1, column=1)
ent2.grid(row=2, column=1)

#create the button for command
Button(root, text='Resize', bg='skyblue', border=3, command=get_size).grid(row=5, column=1)

root.mainloop()