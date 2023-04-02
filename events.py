from tkinter import *
root = Tk()
root.title('the events in tkinter')
root.geometry('666x444')


def click(event):  # 'event' is the defalt argument, just like 'self' in Class
    show['text'] = "Love Bangladesh!"


widget = Button(root, text='Click here')
widget.pack()

widget.bind('<Button-1>', click)

show = Label(root, font='Arial 20 bold')  # defined function's 'show' variable 
show.pack()


root.mainloop()
