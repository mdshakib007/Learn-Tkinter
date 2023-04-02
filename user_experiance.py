from tkinter import *
import tkinter.messagebox as tmsg
import csv

root = Tk()
root.title('problem 2')
root.geometry('800x500')

def get_data():
    # collect all user inputed values
    user_name = name.get()
    user_email = email.get()
    user_phone = phone.get()
    user_pass = password.get()

    # open a csv file
    with open('data2.csv', 'a', newline='') as f:
        head = ['Name', 'Email', 'Phone', 'Password'] # define head
        writer = csv.DictWriter(f, fieldnames=head)
        
        #check if the file is empty then write head
        if f.tell() == 0:
            writer.writeheader()
            
        #write user input data
        writer.writerow({
            'Name' : user_name,
            'Email' : user_email,
            'Phone' : user_phone,
            'Password' : user_pass
        })
        # show confirmation message 
        tmsg.showinfo('Information', 'Your form submited successfully!')
        
    # clear the window
    name.delete(0, END)
    email.delete(0, END)
    phone.delete(0, END)
    password.delete(0, END)


Label(root, text='Welcome to Area-51', bg='skyblue', font='Serif 20 bold').grid(column=1, padx=20) # welcome message 

Label(root, text='Name', font='Arial 13 bold').grid(row=1) # defalt column=0
Label(root, text='Email', font='Arial 13 bold').grid(row=2) # defalt column=0
Label(root, text='Phone', font='Arial 13 bold').grid(row=3) # defalt column=0
Label(root, text='Password', font='Arial 13 bold').grid(row=4) # defalt column=0

# User inputs
name = Entry(root)
email = Entry(root)
phone = Entry(root)
password = Entry(root, show='*')
# pack entries 
name.grid(row=1, column=1)
email.grid(row=2, column=1)
phone.grid(row=3, column=1)
password.grid(row=4, column=1)

Checkbutton(root, text='Accept all terms & condition.').grid(row=5, column=1) # A checkbutton

Button(root, text='Submit', bg='aqua', border=3, command=get_data).grid(row=6, column=1)   # submit button


root.mainloop()