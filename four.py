from tkinter import *
root = Tk()
root.title('Visual Studio Code')
root.geometry('555x444')

#frame 1

frame1 = Frame(root, bg='black')
frame1.pack(side=TOP, fill='x')
label1 = Label(frame1, text='Untiteled-Folder-Visual Studio Code', bg='black', fg='white', font='monospace 8')
label1.pack()

#frame 1.1
f1 = Frame(root, bg='grey')
f1.pack(side=TOP, fill='x')
l1 = Label(f1, text='File', bg='grey',font='monospace 8')
l1.pack()

#frame 1.2
f2 = Frame(root, bg='black')
f2.pack(side=TOP, fill='x')
l2 = Label(f2, text='main.py', bg='black', fg='white', font='monospace 8')
l2.pack()

#frame 2
frame2 = Frame(root, bg='black')
frame2.pack(side=BOTTOM, fill='x')
label2 = Label(frame2, text='frame 3', bg='black', fg='white', font='monospace 8')
label2.pack(pady=50)

#frame 3
frame3 = Frame(root, bg='grey')
frame3.pack(side=LEFT, fill='y')
label3 = Label(frame3, text='main.py\nfile1.py\nfil.txt', bg='grey', font='monospace 8')
label3.pack(padx=30)

#frame 4
frame4 = Frame(root, bg='black')
frame4.pack(side=RIGHT, fill='y')
label4 = Label(frame4, text="Press 'Enter' to save", bg='black', fg='white', border=2)
label4.pack(padx=20000)
#button
button1 = Button(frame4, text='Exit', bg='red', command=root.destroy)
button1.pack()

root.mainloop()