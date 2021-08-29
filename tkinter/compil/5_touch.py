#Evénement du clavier : press vs release
"""
On a parfois besoin de distinguer entre une pression sur une touche du clavier et un relâchement
de cette touche. Cela correspond à deux événements différents, comme le montre le code ci-
dessous (en mode texte, pas véritablement de fenêtre pertinente ici) :
"""
from tkinter import Tk, Canvas

root = Tk()


def press(event):
    print("press:", event.keysym)


def release(event):
    print("release:", event.keysym)

root.bind("<KeyPress>", press)
root.bind("<KeyRelease>", release)
root.mainloop()
"""
qui peut afficher

release: Return
press: a
release: a
press: space
release: space
press: Return
release: Return

Un évènement press correspond à l"appui sur une touche. Quand on relâche la touche, on ob-
tient un évènement release. Dans la sortie ci-dessus, la première ligne correspond au relâche-
ment de la touche ENTRÉE qui a servi à lancer le programme en console.
Concernant la question des événements d"appui vs relâchement, on pourra lire le fil de discussion
"""

