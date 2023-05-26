# this is a simple tkinter calculator
from tkinter import *
root = Tk()
root.title('Calculator')
root.maxsize(480, 688)
root.minsize(480, 688)


# functions
def clear_widget():
    result.delete(0, END)


def clear_one():
    current = result.get()
    result.delete(0, END)
    result.insert(0, current[:-1])


def button_click(value):
    current = result.get()

    if value == '=':
        try:
            # if the button is equal then we evaluate the expression
            res = eval(current)

            result.delete(0, END)
            result.insert(0, res)
        except:
            result.delete(0, END)
            result.insert(0, 'Error')

    else:
        result.delete(0, END)
        result.insert(0, str(current) + str(value))


# this is result showing window
result = Entry(root, width=25, font='Arial 24')
result.grid(columnspan=5, pady=10, padx=10)
# clear button
clear_button = Button(root, text='C', height=3, width=8,
                      font='Arial 16 bold', border=2, command=clear_one)
clear_button.grid(row=5, column=2, padx=2, pady=2, columnspan=2)

# clear all button
clear_all = Button(root, text='AC', height=3, width=5,
                   font='Arial 14 bold', border=2, command=clear_widget)
clear_all.grid(row=5, column=0, padx=2, pady=2)


# define button list
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '+', '=']
]

for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col], width=5, height=3, border=2,
                        font='Arial 14 bold', command=lambda row=row, col=col: button_click(buttons[row][col]))
        button.grid(row=row+1, column=col, padx=2, pady=2)

root.mainloop()
