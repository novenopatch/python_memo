from tkinter import *
from random import randrange

WIDTH=400
HEIGHT=200
NBUTTONS=5

root = Tk()
cnv = Canvas(root, width=WIDTH, height=HEIGHT, background="ivory")
cnv.grid(row=0,columnspan=NBUTTONS)

def clic():
    print("Clic")
for i in range(NBUTTONS):
    Button(root, text="Bouton\n%s" %i, command=clic).grid(row=1, column=i)

root.mainloop()