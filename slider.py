from tkinter import *
root = Tk()
root.title('slider in tkinter')
root.geometry('888x444')

#my_slider = Scale(root, from_=0, to=300)
#my_slider.pack()

def get_dollar():
    show['text'] = f'Successfully Collected ${my_slider2.get()}' #when an user can click the button  he/she can get this msg

Label(root, text='How many dollars do you need?', font='Arial 16 bold', bg='aqua').pack() # this is a text label

my_slider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50) #this is horizontal slider 
my_slider2.set(10)
my_slider2.pack()

Button(root, text='Get now', command=get_dollar, bg='green', border=5, fg='white').pack() # at last we defined a button to get dollars

show = Label(root,font='Arial 14 bold', bg='skyblue') # this is the output of the function get_dollars
show.pack()


root.mainloop()