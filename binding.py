from tkinter import *
root = Tk()
root.title('the event')
root.geometry('666x444')


def shakib(event):
    print(f'good night at {event.x}, {event.y}')


widget = Button(root, text='click here!')
widget.pack()

widget.bind('<Button-1>', shakib)


root.mainloop()
