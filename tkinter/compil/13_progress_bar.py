"""
Construire sa propre barre de progression
Tkinter ne propose pas de barre de progression, pour cela il faut utiliser son extension (standard)
Ttk. Néanmoins, la barre de Ttk n"est pas facilement personnalisable (il faut utiliser un style Ttk
et cela n"empêche pas certaines limitations). On peut donc être tenté de créer sa propre barre de
progression. Pour cela, on utilise un canevas et, périodiquement, on modifie la longueur d"un
rectangle gris emboîté dans un rectangle blanc :
"""

from tkinter import *

DELAY = 100

root = Tk()

# Le canevas
cnv = Canvas(root, width=400, height=100, bg="ivory")
cnv.pack()

# Label
message = StringVar()
w = Label(root, textvariable=message, font="Arial 30 bold")
w.pack()
#largeur de la barre
W = 300

# Durées
period_s = 10
period_ms = period_s * 1000
DELAY_BAR = int(round(period_ms / W))

# Les deux rectangles
A = (50, 50)
B = (50 + W , 30)
bg = cnv.create_rectangle(A, B, outline="gray", fill="white")
bar = cnv.create_rectangle(A, B, outline="gray", fill="gray", width=0)

def animate(L, bar):
    if L >= 0:
        cnv.delete(bar)
        newbar = cnv.create_rectangle(50, 50, 50 + L, 30, outline="gray", fill="gray", width=0)
        L -= 1
        cnv.after(DELAY_BAR, animate, L, newbar)


def chrono(s, message):
    if s >= 0:
        message.set(str(s))
        root.after(1000, chrono, s - 1, message)
animate(W, bar)
chrono(period_s, message)


root.mainloop()

"""
— Lignes 27-28 : Le rectangle gris fait office de barre de progression. Quand il évolue, le fond
blanc de la barre se découvre.
— Ligne 22 : on précalcule la durée de rafraîchissement du rectangle pour 1 pixel.
— Lignes 31-37 : on fait évoluer la barre pixel par pixel (la longueur L). Pour cela, on remplace
le rectangle gris par un rectangle ayant 1 pixel de moins de longueur.
— Lignes 40-43 : on fait évoluer le compteur seconde par seconde jusqu’à écoulement de la
période donnée initialement (period_s, ligne 20).

"""