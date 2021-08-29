from tkinter import *
 
root = Tk()
root.title("Login UI using Pack")
root.geometry("780x620") # set starting size of window
root.maxsize(1080, 920) # width x height
root.config(bg="#6FAFE7") # set background color of root window
 
login_label = Label(root, text="Login", bg="#2176C1", fg='white', relief=RAISED)
login_label.pack(ipady=5, fill='x')
login_label.config(font=("Font", 30)) # change font and size of label
 
# login image
image = PhotoImage(file="1.gif")
img_resize = image.subsample(-10,-10)
label_image= Label(root, image=img_resize, bg="white", relief=SUNKEN)
label_image.pack(pady=5)
 
def checkInput():
    '''check that the username and password match'''
    usernm = "root"
    pswrd = "root"
 
    entered_usernm = username_entry.get() # get username from Entry widget
    entered_pswrd = password_entry.get() # get password from Entry widget
 
    if (usernm == entered_usernm) and (pswrd == entered_pswrd):
        print("Hello!")
        root.destroy()  
    else:
        print("Login failed: Invalid username or password.")
 
def toggled():
    print("The check button works.")
 
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
 
Label(password_frame, text="Password", bg="#6FAFE7").pack(side='left', padx=7)
password_entry = Entry(password_frame, bd=3, show="*")
password_entry.pack(side='right')
 
# Create Go! Button
go_button = Button(root, text="GO!", command=checkInput, bg="#6FAFE7", width=15)
go_button.pack(pady=5)
 
# Remember me and forgot password
bottom_frame = Frame(root, bg="#6FAFE7")
bottom_frame.pack()
 
var = IntVar()
remember_me = Checkbutton(bottom_frame, text="Remember me", bg="#6FAFE7", command=toggled, variable=var)
remember_me.pack(side='left', padx=19)
 


# The forgot password Label is just a placeholder, has no function currently
forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="#6FAFE7")
forgot_pswrd.pack(side="right", padx=19)
 
root.mainloop()