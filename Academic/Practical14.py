# Develop Program to Learn GUI Programming using Tkinter.

from tkinter import *

def submit():
    name = entry.get()
    label.config(text=f"Hello, {name}!")   

root = Tk()
root.title("Simple GUI")
root.geometry("300x200")   

label = Label(root, text="Enter your name:")
label.pack(pady=10)

entry = Entry(root)
entry.pack(pady=5)

button = Button(root, text="Submit", command=submit)
button.pack(pady=10)

root.mainloop() 