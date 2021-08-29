"""
Dessiner un dégradé
Par défaut, Tkinter ne permet pas de créer des gradients. Toutefois, on peut réaliser une forme
de gradient en écrivant soi-même le code.
Voici un exemple avec un gradient rouge :
"""
from tkinter import *
LENGTH = 800
TOP_RED = 120
root = Tk()
cnv = Canvas(root, width=400, height=400, bg="white")
cnv.pack()
def rgb_10to16(r, g, b):
    return ("#%.02x" % r) + ("%.02x" % g) + ("%.02x" % b)
def gradient(x):
    y = int((-255 + TOP_RED) / LENGTH * (int(x)) + 255)
    cnv["bg"] = rgb_10to16(255, y, y)
curseur = Scale(root,orient="horizontal",command=gradient,length=400,from_=0,to=LENGTH)
curseur.pack()
root.mainloop()



#Voici un exemple avec des niveaux de gris

from tkinter import Tk, Canvas
SIDE=600
root=Tk()
cnv=Canvas(root, width=SIDE, height=SIDE*0.3, background="ivory")
cnv.pack()
top=50
H=100
a=10
N=100
W=0.95*SIDE//N
gris0=40
gris1=200
h=(gris1-gris0)//N

def toHex(v):
    z=hex(v)[2:]
    return "0"*(len(z)==1)+z

for i in range(N):
    color=toHex(gris1-i*h)
    cnv.create_rectangle(a, top, a+W, top+H, outline="",fill="#%s%s%s" %(color, color, color))
    a+=W

root.mainloop()