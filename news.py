from tkinter import *

root = Tk()
root.title('The daily star')
root.geometry('1000x800')

Label(root, text='The Daily Star', font='Serif 22 bold').pack()
Label(root, text='01 April, 2023\n', font='Serif 15 bold').pack()


# add text in a list
texts = []
for i in range(3):
    with open(f'news{i+1}.txt') as f:
        text = f.read()
        texts.append(text)

# create first widget of news
f1 = Frame(root)
f1.pack(fill='x')
# first label
label1 = Label(f1, text=texts[0], font='Arial 12')
label1.pack(side='left')
# first image
image1 = PhotoImage(file='news1.png')
Label(f1, image=image1).pack(side="left")

# a blank line
Label(root, pady=10).pack()

# Create second widget of news
f2 = Frame(root)
f2.pack(fill='x')
# label
label2 = Label(f2, text=texts[1], font='Arial 12')
label2.pack(side='right')
# second image
image2 = PhotoImage(file='news2.png')
Label(f2, image=image2).pack(side='right')

#another blank line
Label(root, pady=10).pack()

#create third widget of news
f3 = Frame(root)
f3.pack(fill='x')
#label
label3 = Label(f3, text=texts[2], font='Arial 12')
label3.pack(side='left')
#third image
image3 = PhotoImage(file='news3.png')
Label(f3, image=image3).pack(side='left')

root.mainloop()