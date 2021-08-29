from tkinter import *

SIZE=200
NBUTTONS=5

root = Tk()
cnv = Canvas(root, width=SIZE, height=SIZE, background="ivory")
cnv.grid(row=0,columnspan=NBUTTONS)

def make_clic(i):
    def clic():
        cnv.delete(ALL)
        cnv.create_text(SIZE/2, SIZE/2, text=i, font="Arial 90 bold")
    return clic
for i in range(NBUTTONS):
    btni=Button(root, text=i, command=make_clic(i))
    btni.grid(row=1, column=i)


root.mainloop()

"""
— Lignes 17-19 : dans une boucle parcourue par un indice i, on génère le bouton portant la
valeur i. Non seulement le texte dépend de i mais aussi la façon de réagir du bouton. En effet,
chaque commande est le retour d’un appel de fonction qui renvoie une fonction mémorisant
i.
— Lignes 11-15 : cette fonction génère une fonction de rappel personnalisée pour chaque bou-
ton. Cette fonction est appelée avec un numéro de bouton. Pour chaque numéro, elle crée
une fonction (lignes 12-14) qui réagit au clic sur le bouton i. Cette fonction est créée dans
le corps de la fonction et est renvoyée (ligne 15) après sa création. Cette fonction, nommée
clic mémorise un contexte, en particulier le numéro i.
— Ligne 11 : une telle fonction est appelée une clôture (closure).
"""

"""
Alternative avec paramètre par défaut
J’ai vu cette autre façon de faire dans un message de RedTenZ sur le forum Python d’Openclass-
rooms. Voici l’adaptation de son code :
"""
from tkinter import *
SIZE=200
NBUTTONS=5
root = Tk()
cnv = Canvas(root, width=SIZE, height=SIZE, background="ivory")
cnv.grid(row=0,columnspan=NBUTTONS)
for i in range(NBUTTONS):
    def clic(i=i):
        cnv.delete(ALL)
        cnv.create_text(SIZE/2, SIZE/2, text=i, font="Arial 90 bold")
    btni=Button(root, text=i, command=clic)
    btni.grid(row=1, column=i)
root.mainloop()

"""
Toute l’astuce est dans le paramètre par défaut i dans la définiton de clic (l’auteur avait utilisé
une fonction lambda qui risque d’être peu lisible dans le code ci-dessus).
"""

"""
Alternative identifiant le widget
Une autre façon de faire est d’associer avec bind chaque bouton au clic de souris sur le bou-
ton à une même fonction (ci-dessous clic). Cette fonction sera appelée lorsqu’on cliquera sur
un des boutons en générant un événement, disons event. Et event permet d’identifier le wid-
get associé par l’attribut event.widget. Il ne reste plus qu’à récupérer le texte du bouton via
event.widget["text"] pour identifier la valeur. D’où le code :
"""
from tkinter import *
SIZE=200
NBUTTONS=5
root = Tk()
cnv = Canvas(root, width=SIZE, height=SIZE, background="ivory")
cnv.grid(row=0,columnspan=NBUTTONS)
def clic(event):
    i=event.widget["text"]
    cnv.delete(ALL)
    cnv.create_text(SIZE/2, SIZE/2, text=i, font="Arial 90 bold")
for i in range(NBUTTONS):
    btni=Button(root, text=i)
    btni.grid(row=1, column=i)
    btni.bind("<Button>", clic)
root.mainloop()