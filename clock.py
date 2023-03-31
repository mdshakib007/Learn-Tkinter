import tkinter as tk 
from time import strftime

class Clock:
    """this class contains a simple digital calculator"""
    def __init__(self, master):
        self.master = master
        self.master.title('Clock')
        
        self.time_label = tk.Label(master, font=('Arial', 18), fg='black', bg='aqua')
        self.time_label.pack(padx=50, pady=50)
        
        #update time
        self.update_time()      
        
    def update_time(self):
        current_time = strftime('%H:%M:%S %p') #get current time
        self.time_label.config(text=current_time)
        self.master.after(200, self.update_time) #set 200 milisecond updatetime
        
root = tk.Tk()
root.geometry('333x200')
root.maxsize(333,200)
root.minsize(333,200)
clock = Clock(root)      
root.mainloop()