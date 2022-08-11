from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
Font_tuple = ("Comic Sans MS", 20, "bold")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font = Font_tuple)
label.pack(anchor='center')

time()
mainloop()