
from tkinter import *

SIDE=400

root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE,
bg="light blue")
cnv.pack()

def fading_color(r,g,b, N):
    return (255-r)//N,(255-g)//N, (255-b)//N

def fading(rect, r, g, b, N):
    if N<=0:
        return
    s=cnv.itemcget(rect,"fill")[1:]
    R,G,B=[int("".join(u),base=16) for u in zip(s[0::2],s[1::2])]
    rr=str(hex(min(R+r, 255)))[2:]
    gg=str(hex(min(G+g, 255)))[2:]
    bb=str(hex(min(B+b, 255)))[2:]
    color="#"+str(rr+gg+bb)
    cnv.delete(rect)
    rect=cnv.create_rectangle(100, 100, 300, 300,fill=color, outline="")
    
    cnv.after(200, fading, rect, r, g, b, N-1)

rect= cnv.create_rectangle(100, 100, 300, 300,
fill="#f0e68c", outline="")

r, g, b=fading_color(0xf0,0xe6, 0x8c, 10)
fading(rect, r, g, b, 10)
root.mainloop()
"""
— Lignes 13-23 : la fonction d"animation.
— Ligne 30 : on calcule au préalalble trois tranches r, g et b de composantes RGB que l"on va
additionner (lignes 18-20) à la couleur courante à chaque étape de l"animation.
— Ligne 25 : l"animation est relancée tous les 200 ms.
— Ligne 16 : on lit les couleurs courantes du rectangle en accédant aux options de l"item grâce
à son id (ici rect) qui est un paramètre de la fonction fading.
— Ligne 22-24 : on efface le carré courant et on le remplace par le carré avec la nouvelle couleur.
"""
