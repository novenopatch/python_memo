from tkinter import *

def estValide() :
    if user.get() == "moi" and mdp.get()=="3.14":
        label_login["text"]="Login correct"
    else:
        label_login["text"]="Login incorrect"

app = Tk()

user=StringVar()
mdp=StringVar()

label_user = Label(app,text="Identifiant")
label_mdp = Label(app,text="Mot de passe")
label_login = Label(app, font="Arial 20 bold")

btn = Button(app,text="Valider",command=estValide, width=20)
entry_user = Entry(app, textvariable=user)
entry_mdp = Entry(app, textvariable=mdp, show="*")

label_user.pack()
entry_user.pack()

label_mdp.pack()
entry_mdp.pack()

btn.pack(padx=100)
label_login.pack()
app.mainloop()