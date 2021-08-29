
from tkinter import *
root = Tk()

lbl = Label(root, text="Mot de\npasse ", font="Times 15 bold")
lbl.pack(side="left", padx=20)

my_entry = Entry(
root, font="Courier 20 bold", width=20, bg="lavender", show="")

my_entry.pack(padx=20, pady=40, side="left")
my_entry.focus_set()

def update_entry():
    global hidden
    if hidden:
        my_entry["show"] = "\u25CF"
        btn["image"] = hide
    else:
        my_entry["show"] = ""
        btn["image"] = view
        hidden = not hidden

hidden = True

hide = PhotoImage(file="11.png")
view = PhotoImage(file="12.png")

btn = Button(root,image=hide,width=90,font="Times 15 bold",command=update_entry)
btn.pack(side="left")
root.mainloop()

"""
— ligne 7 : une entrée dans laquelle est écrit le mot de passe
— ligne 30 : un bouton qui va démasquer/masquer le mot de passe
— ligne 4 : un label pour indiquer qu’il faut entrer un mot de passe.
Lorsque le mot de passe est caché, chaque caractère est remplacé par un disque noir •. Pour que
l’écriture du mot de passe ne montre que le caractère •, il faut activer l’option show de Entry en
posant show=" • ", cf. ligne 8. On peut écrire tel quel le caractère entre guillemets, par exemple
en faisant un copier-coller. Ce caractère est connu sous le nom Unicode de Black Circle. En
Python 3, on peut aussi produire ce caractère avec une séquence d’échappement unicode :
print("\u25CF")
L’option command du bouton (ligne 35) référence une fonction update_entry (ligne 14) qui va
se charger :
— de masquer/démasquer l’entrée (lignes 20 et 17)
— de changer l’icône du bouton (lignes 18 et 21).
L’état de visibilité du mot de passe est enregistré dans une variable globale hidden (ligne 25)
qui vaut initialement False afin que le mot de passe soit invisible. Comme cette variable est
modifiée par la fonction update_entry (ligne 22), elle y est déclarée global (ligne 15).
Pour cacher chaque caractère de l’entrée, on a vu qu’il fallait que l’option show du bouton réfé-
rence la chaîne qui va remplacer chaque caractère. Pour que les caractères soient normalement
visible, il faut que cette option soit à la chaine vide "". Comme on le ferait pour toute option de
widget, on peut changer l’option show avec une affectation de my_entry["show"] (lignes 17 et
20).
Pour changer l’image du bouton, c’est le même principe, on réaffecte btn["image"] (lignes 18
et 21). L’image doit pointer vers un objet de type PhotoImage que l’on aura créé au préalable
(lignes 27 et 28).
"""

