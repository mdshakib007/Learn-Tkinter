from tkinter import *
import tkinter.messagebox as tmsg 
root = Tk()
root.geometry('777x444')
root.title('Message box in tkinter')

#message for tap anywhere 
def sorry():
    value = tmsg.askquestion('Message', 'Do you want to save change?')
    if value == 'yes':
        msg = 'Your file was saved successfully!'
    else:
        msg = 'File not saved.'
    tmsg.showinfo('Message', msg)
    
def file_not_found():
    tmsg.showerror('Error', 'Sorry, no such file or directory!')
    
def nothing():
    tmsg.askretrycancel('Nothing to save!', 'There is no file or directory to save!')
    
def experiance():
    ans = tmsg.askquestion('What was wrong', 'Was your experiance bad?')
    if ans == 'yes':
        msg = 'Sorry, Please feedback us.'
    else:
        msg = 'Please rate us on app store!'
    tmsg.showinfo('Feedback', msg)

#creating menubars
main_menu = Menu(root)
m1 = Menu(main_menu, tearoff=0)

m1.add_command(label='Save', command=sorry)
m1.add_command(label='Save as...', command=file_not_found)
m1.add_command(label='Save all', command=nothing)
m1.add_separator()
m1.add_command(label='Report', command=experiance)
m1.add_command(label='Exit', command=quit)

main_menu.add_cascade(label='File', menu=m1)
root.config(menu=main_menu)


root.mainloop()