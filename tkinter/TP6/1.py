from tkinter import*
from tkinter import messagebox
from random import randint

pass_r = ["carlos", "joseph"]

def verification():#*args):
    if entry_v in pass_r:
        messagebox.showinfo("Resultat","Mot de passe correct. Au revoir!")
        print("salut")
        
    else:
        messagebox.showwarning("Resultat", "Mot de passe incorrect. Veillez recommencer!")
    




root= Tk()

label_m = Label(root,text="Mot de passe")
label_m.pack(side= LEFT)

entry_v = StringVar()
entry_m = Entry(root,textvariable= entry_v)#, show="*")
#entry_m.bind("<Return>", verification)
entry_m.pack(side= LEFT)

bouton_v = Button(root, text="Valider", command= verification)
bouton_v.pack(side= LEFT)


root.mainloop()


"""
def lance_f ():
    nb_r = randint(1, 6)
    bouton_r.set("resultat ->{}".format(nb_r))
    
root = Tk()

bouton_l = Button(root,text="Lancer", command= lance_f)
bouton_l.pack(side= LEFT,padx=5)

bouton_Q = Button(root, text="Quiter", command= root.quit)
bouton_Q.pack(side= LEFT, padx=5)

bouton_r = StringVar()
bouton_r.set("resultat ->")

bouton_resultat = Button(root, textvariable= bouton_r, fg="red", bg= "white")
bouton_resultat.pack(side= LEFT, padx= 5)





root.mainloop()
"""
