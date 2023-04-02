from tkinter import *
root = Tk()
root.title('canvas')

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0, 0, 800, 400, fill='blue')
can_widget.create_line(0, 400, 800, 0, fill='blue')

can_widget.create_rectangle(300,200, 500, 700, fill='aqua')
can_widget.create_rectangle(3, 7, 300, 100)

can_widget.create_text(200, 200, text='python')

can_widget.create_oval(44, 33, 32, 22) #oval

can_widget.create_arc(2,3, 566, 435)

can_widget.create_polygon(4,54,323,345,123,67, 34,54)






root.mainloop()