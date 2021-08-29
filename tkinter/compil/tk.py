from tkinter import *
from random import randrange

def tracer():
	cnv.delete("all")
	u, v = randrange(SIDE), randrange(SIDE)
	R=SIDE//4
	cnv.create_oval(u-R,v-R,u+R, v+R, fill="orange")


SIDE=400
root=Tk()
cnv=Canvas(root, width=SIDE, height=SIDE, background="ivory")
cnv.pack(side=LEFT)

bouton=Button(root, text="Tracer", command=tracer)
bouton.pack()

root.mainloop()
