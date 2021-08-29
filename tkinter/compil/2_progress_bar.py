
"""
progress = ttk.Progressbar(root, length=400,maximum= 300)
progress.pack(pady=30)


progress.start(10)
"""
from tkinter import Tk, ttk, StringVar, Label
root = Tk()
progress = ttk.Progressbar(root, length=400, maximum=300)
progress.pack(pady=30)
progress.start(10)
message = StringVar()
w = Label(root, textvariable=message, font="Arial 30 bold")
w.pack()
seconds = 0
delay = 1000
def anim(ms):
    message.set(str(ms // 1000))
    root.after(delay, anim, ms + delay)
    anim(0)
root.mainloop()
