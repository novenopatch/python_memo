 #import necessary modules
from tkinter import *

def touchez():
    
    var= 1
    print("The check button works."+ str(var))
def clique_d():
    print("Vous avez cliquer.")
root = Tk()
root.title("Using Pack")
root.geometry("300x100") 
root.config(bg="skyblue")
 

button1 = Button(root, text="Click me", command= clique_d)
button1.pack(side="left")
 
# Example of how to arrange Label widgets using pack
label1 = Label(root, text="Read me", bg="skyblue")
label1.pack(side="right")


label2 = Label(root, text="Hello", bg="purple")
label2.pack(side="right")
 

 

var = IntVar() 
var= 0
check = Checkbutton(root, text="Click me", bg="skyblue", command=touchez, variable=var)
print(var)
check.pack(side="bottom")
 
root.mainloop()