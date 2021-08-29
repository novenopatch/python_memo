from tkinter import *
from turtle import Vec2D

def rot(C, t, M):
    CM=Vec2D(*M)-Vec2D(*C)
    return Vec2D(*C)+CM.rotate(t)

root = Tk()
cnv = Canvas(root, width=400, height=400)
cnv.pack()

# Le centre
C=(200, 200)

# Un triangle
P=(250, 200)
Q=(300, 100)
R=(380, 200)
tr=cnv.create_polygon(P, Q, R, width=8, fill="blue")

cnv.create_oval(200-2, 200-2, 200+2, 200+2, fill="black")

def rotate(t):
    PP=rot(C, float(t), P)
    QQ=rot(C, float(t), Q)
    RR=rot(C, float(t), R)
    cnv.coords(tr, *PP, *QQ, *RR)

curseur = Scale(root, orient = "horizontal", command=rotate, from_=0, to=360)
curseur.pack()

root.mainloop()

"""
— Lignes 4-6 : la fonction rot calcule les coordonnées du transformé de M par la rotation de
centre C et d’angle t.
— Lignes 13 : on crée un centre de rotation C et (ligne 21) on le marque avec un petit disque de
2 pixels de rayon.
— Lignes 16-19 : on crée un motif triangulaire PQR qui va tourner autour du centre.
— Ligne 29 : un curseur permettant de choisir l’angle de rotation (entre 0 et 360°) autour de C
par rapport à la position initiale.
— ligne 23 : chaque fois que le curseur est déplacé (command à la ligne 29), le triangle doit tourner
depuis sa position au lancement de l’application d’un certain angle t. On calcule la nouvelle
position PP, QQ et RR de chacun des sommets (ligne 24-26) et on déplace le triangle avec la
méthode coords à sa nouvelle position (ligne 27).
Le code ci-dessus est adapté d’un message du forum Python d’OpenClassroom.
"""