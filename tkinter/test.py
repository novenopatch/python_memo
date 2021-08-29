import tkinter
import random
screen = tkinter.Tk()

"""
def Rectangle_aleatoire(largeur, hauteur, coul_rempl) :
    x1= random.randrange(largeur)
    y1 = random.randrange(hauteur)
    x2= x1 + random.randrange(largeur)
    y2 = y1 + random.randrange(hauteur)
    canva.create_rectangle(x1,y1,x2,y2, fill=coul_rempl)
canva = tkinter.Canvas(screen, width= 500, height=500)
canva.pack()
canva.create_line(0,0, 500, 500)
canva.create_rectangle(30,30, 60,60)
canva.create_rectangle(90,90, 120,120)

for x in range(0,80):
    Rectangle_aleatoire(80,80,"cyan")#green,red,blue,orange,yellow,pink,purple,violet,magenta,cyan,or=#ffd800
"""
canva_t = tkinter.Canvas(screen, width= 800, height=800)
canva_t.pack()
canva_t = tkinter.create_text(150,100, text="Soyez fort",fill="red")







screen.mainloop()