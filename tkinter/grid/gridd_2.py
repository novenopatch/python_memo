from tkinter import *

root=Tk()

a=Label(root, text="A", bg=’red’, width=20, height=5)
a.grid(row=0, column=0, padx=20)

b=Label(root, text="B", bg=’lightblue’, width=20, height=5)
b.grid(row=0, column=1, padx=50, pady=100)

c=Label(root, text="C", bg=’lime’, width=20, height=5)
c.grid(row=1, column=0)

d=Label(root, text="D", bg=’orange’, width=20, height=5)
d.grid(row=1, column=1)

root.mainloop()
