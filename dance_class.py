from tkinter import *
import tkinter.messagebox as tmsg
import csv

root = Tk()
root.title('submit data to a csv file')
root.geometry('600x350')
root.minsize(600, 350)
root.maxsize(600, 350)

def get_data():
    # Get user input data from Entry widgets
    username_data = name.get()
    email_data = email_entry.get()
    password_data = password.get()

    # Write user input data to CSV file
    with open('data.csv', 'a', newline='') as f:
        fieldnames = ['Username', 'Email', 'Password']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Write header row if file is empty
        if f.tell() == 0:
            writer.writeheader()

        # Write user input data
        writer.writerow({'Username': username_data, 'Email': email_data, 'Password': password_data})

        # Print confirmation message 
        tmsg.showinfo('Information', 'Your form submited successfully!')

    # Clear Entry widgets
    name.delete(0, END)
    email_entry.delete(0, END)
    password.delete(0, END)

#welcome message
welcome = Label(root, text='Welcome to the Dance-Mania!',
                borderwidth=50, bg='skyblue', font=('Serif', 20))
welcome.grid(row=0, column=0, columnspan=2, padx=50, pady=20)

#labels of the entry
Label(root, text='Username').grid(row=1, column=0)
Label(root, text='Email').grid(row=2, column=0)
Label(root, text='Password').grid(row=3, column=0)

#entries
name = Entry(root)
name.grid(row=1, column=1)
email_entry = Entry(root)
email_entry.grid(row=2, column=1)
password = Entry(root, show='*')
password.grid(row=3, column=1)

#buttons
Button(root, text='Cancel', border=2, bg='red', command=root.destroy).grid(row=5, column=0)
Button(root, text='Submit', border=2, bg='skyblue', command=get_data).grid(row=5, column=1)
#checkbox 
Checkbutton(root, text='Accept terms & condition', font='serief 7').grid(row=4, column=1)

root.mainloop()
