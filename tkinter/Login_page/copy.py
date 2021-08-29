from tkinter import *
 
 
dict= {"root_u":"root_u", "H.john":"carlos"} 


def checkInput(event=None):
    '''check that the username and password match'''
 
    entered_usernm = username_entry.get() # get username from Entry widget
    entered_pswrd = password_entry.get() # get password from Entry widget
    if len(entered_usernm) <=4 or len(entered_pswrd) <=4:
        if (entered_usernm and entered_pswrd) != "" :
            rr= "Identifiant ou password inferieur ou egale a 4!"
            label_r.set(rr)
            result_label.config(font=("Font", 10),fg="red")
            login_label.config(fg="red")
        else:
            rip="Identifiant ou password invalide!"
            label_r.set(rip)
            login_label.config(fg="red")
            result_label.config(font=("Font", 10),fg="red")

    elif (entered_usernm and entered_pswrd) != "" and  len(entered_usernm) >=4 and len(entered_pswrd) >=4:
        
        for k, v in dict.items():
            if (k != entered_usernm) and (v != entered_pswrd):
                
                to="Invalid username or password."
                label_r.set(to)
                result_label.config(font=("Font", 10),fg="red")
                login_label.config(fg="red")
                
            elif (k==entered_usernm) and (v == entered_pswrd):
                result_label.config(font=("Font", 10), fg= "green")
                login_label.config(fg="green")
               
                bi ="Hello!"
                ti="clé : {} - valeur : {}".format(k , v)
                label_r.set(bi + ti)
                clear_widget()
                test_mo()
                
               
def test_mo():
    label_test = Label(root,text="albatrosss")
    label_test.pack()

def clear_widget():
    list = root.pack_slaves()
    for w in list:
        w.destroy()  



def toggled():
    print("The check button works.")




root = Tk()
root.title("Login UI using Pack")
root.geometry("1080x920") # set starting size of window
root.maxsize(1080, 920) # width x height
root.config(bg="#6FAFE7") # set background color of root window

login_label_v = StringVar()
login_label_v.set("Login ")
login_label = Label(root, textvariable=login_label_v, bg="#2176C1", fg='white', relief=RAISED)
login_label.pack(ipady=5, fill='x')
login_label.config(font=("Font", 30)) # change font and size of label
 
# login image
image = PhotoImage(file="1.gif")
img_resize = image.subsample(-10,-10)
label_image= Label(root, image=img_resize, bg="white", relief=SUNKEN)
label_image.pack(pady=5)
# Username Entry
username_frame = Frame(root, bg="#6FAFE7")
username_frame.pack()
 
label_u = Label(username_frame, text="Username", bg="#6FAFE7")
label_u.pack(side='left', padx=5)
username_entry = Entry(username_frame, bd=3)
username_entry.pack(side='right')
 
# Password entry
password_frame = Frame(root, bg="#6FAFE7")
password_frame.pack()


frame_test2= Frame(password_frame,bg="#6FAFE7")
frame_test2.pack(side=LEFT)#padx=55)
Label(frame_test2, text="Password", bg="#6FAFE7").grid(row=1,column=4)#pack(side=LEFT)#, padx=7)#(password_frame, text="Password", bg="#6FAFE7").pack(side='left', padx=7)


frame_test = Frame(password_frame,bg="#6FAFE7")
frame_test.pack(side= RIGHT)

password_entry = Entry(frame_test, bd=3, show="*")#password_frame, bd=3, show="*")
password_entry.pack(side=LEFT,padx=10)#(side='right')

show_pass = Checkbutton(frame_test,bg="#6FAFE7")#password_frame,text="Show",bg="#6FAFE7")
show_pass.pack(side=RIGHT)
# Create Go! Button

 
# Remember me and forgot password
avant_F = Frame(root, bg="#6FAFE7")
avant_F.pack()


go_button = Button(avant_F, text="GO!", command=checkInput, bg="#6FAFE7", width=15)
go_button.pack(expand=TRUE,side=TOP,pady=5,padx=70)

label_r = StringVar()
result_label = Label(avant_F,textvariable=label_r,bg="#6FAFE7")
result_label.pack(side= LEFT)


bottom_frame = Frame(root, bg="#6FAFE7")
bottom_frame.pack()




var = IntVar()
remember_me = Checkbutton(bottom_frame, text="Remember me", bg="#6FAFE7", command=toggled, variable=var)
remember_me.pack(side='left', padx=19)
 


# pour l'instant pas encor fonctionelle
forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="#6FAFE7")
forgot_pswrd.pack( side="right", padx=19)


    
root.mainloop()