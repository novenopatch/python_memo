#affiche les clics et position souris
from tkinter import *

#clavier
def f(event):
    t=event.keysym
    print("Touche pressée :", t)
#souris
def g(event):
    x=event.x
    y=event.y
    print("Position :", x, y)
root = Tk()
root.bind("<Key>", f)
root.bind("<Motion>",g)
root.mainloop()
from tkinter import *

def touche(event):
    t=event.keysym
    print("Touche %s pressée" %t)


root = Tk()

root.bind("<Key>", touche)
root.mainloop()
