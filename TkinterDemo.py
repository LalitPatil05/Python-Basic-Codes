import tkinter as tk

root = tk.Tk()
root.title("My App")

label = tk.Label(root, text="Hello Lalit")
label.pack()

btn = tk.Button(root, text="Click Me", command=lambda: print("Clicked"))
btn.pack()

root.mainloop()
