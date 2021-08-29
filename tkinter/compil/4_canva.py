
#

from tkinter import *

WIDTH=400
HEIGHT=200
COTE=40

root = Tk()

cnv = Canvas(root, width=WIDTH, height=HEIGHT, background="ivory")
cnv.pack()

DIR={"Left":(-1,0),"Right":(1,0),"Up":(0,-1),"Down":(0,1)}

def bouge(event):
    key=event.keysym
    dx, dy=DIR[key]
    a,b, segment=pile[-1]
    if len(pile)>=2 and a+dx==pile[-2][0] and b+dy==pile[-2][1] :
        pile.pop()
        print("back")
        cnv.delete(segment)
    else:
        segment=cnv.create_line(a*COTE+COTE//2, b*COTE+COTE//2,
                                a*COTE+COTE//2+dx*COTE,
                                b*COTE+COTE//2+dy*COTE,
                                fill="blue", width=4, capstyle=ROUND)
        pile.append([a+dx, b+dy, segment])
    cnv.move("perso", dx*COTE, dy*COTE)

perso=cnv.create_rectangle(0, 0,COTE, COTE, fill="blue",
        outline="", tag="perso")

pile=[(0,0, perso)]
for key in ["<Left>", "<Right>", "<Up>", "<Down>"]:
        root.bind(key, bouge)

root.mainloop()

"""
— Ligne 34 : l"appui sur une des 4 flèches du clavier est détecté par le canevas.
— Ligne 30 : un carré bleu indique la position courante sur le canevas (utile si on repasse sur un
chemin déjà parcouru)
— Ligne 35 : le canevas a le focus car la fenêtre entière (root) a le focus quand l"application est
lancée.
— Lignes 34-35 : tout appui sur une des touches du clavier exécute la fonction bouge.
— Ligne 11 : chaque appui sur une des flèches du clavier est associé à un décalage suivant le
repère du canevas. Par exemple, à un appui sur la flèche bas est associé la direction corres-
pondante, ici le couple (0, -1). C"est juste une facilité pour coder la fonction bouge.
— Ligne 32 : les différents mouvements de l"utilisateur sont enregistrés dans une pile. La pile
permet (en dépilant) de revenir en arrière et d"effacer le trajet de retour.
— Ligne 17-19 : la détection d"une marche arrière. le segment est effacé (ligne 19)
— Lignes 22-26 : si pas de retour en arrière, le segment pour le nouveau déplacement est rendu
visible et rajouté dans la pile.
— Ligne 28 : la sortie du canevas n"est pas gérée par le programme.
"""
