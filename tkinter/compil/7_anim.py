from tkinter import Tk, Canvas, Button
from random import randrange

def anim(cpt):
        global id_anim
        cnv.delete("all")
        cnv.create_text(SIDE//2, SIDE//2, text =int(cpt), font="Arial 200 bold")
        id_anim=cnv.after(500, anim, cpt+1)
       

def go():
    cnv.after_cancel(id_anim)
    anim(1)

SIDE=400
root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE, bg="ivory")
cnv.pack()
btn=Button(root, text="Reset", command=go)
btn.pack()

id_anim=None
anim(1)

root.mainloop()
"""
— Lignes 4-8 : la fonction d"animation : elle efface tout (ligne 6) et crée le nombre suivant du
compteur. La foncion est relancée toutes les demi secondes (ligne 8). Le rappel provoque la
création d"un identifiant (ligne 8). Pour pouvoir agir sur cet identifiant, il est placé dans une
variable globale (ligne 5).
242— Ligne 18 : Création d"un bouton. Lorsqu"on clique sur ce bouton, il lance la fonction go.
— Lignes 10-12 : le clic sur le bouton entraîne l"annulation de l"animation en cours : la méthode
d"annulation after_cancel (ligne 11) est appelée. Puis une animation est aussitôt relancée
(ligne 12).
"""
