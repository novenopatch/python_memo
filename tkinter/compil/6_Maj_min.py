
#Evénement du clavier : majuscule vs minuscule
"""
On peut distinguer (automatiquement) l"appui sur une touche et l"appui sur la même touche mais
en majuscule (on appuie simultanément sur la touche MAJ), comme le montre le code ci-dessous :
"""
from tkinter import Tk, Canvas
2
root = Tk()
cnv = Canvas(root, width=400, height=100, bg="ivory")
cnv.pack()
cnv.focus_set()
x=0

def texte(event):
    global x
    cnv.create_text(x, 40, text =event.keysym, font="Arial 50 bold")
    x+=30


cnv.bind("<Key-a>", texte)
cnv.bind("<Key-B>", texte)

root.mainloop()
"""
— Ligne 14 : détection de l"appui simple sur une touche.
— Ligne 15 : détection de l"appui simultané sur une touche et la touche MAJ.
"""

