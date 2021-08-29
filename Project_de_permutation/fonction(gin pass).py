from random import randint,choice
import string
def generateur(pass_min = 6, pass_max =14, ponctiation=True ):

    if  pass_min == 6 and pass_max == 14 and ponctiation :
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password ="".join(choice(all_chars) for i in range(randint(pass_min, pass_max)))

    elif ponctiation ==False:
        all_chars= string.ascii_letters + string.digits
        password ="".join(choice(all_chars) for i in range(randint(pass_min, pass_max)))

    else:
        all_chars= string.ascii_letters + string.digits + string.punctuation
        password ="".join(choice(all_chars) for i in range(randint(pass_min, pass_max)))
    password_entry.delete(0,END)
    pasword_entry.insert(0,password)
