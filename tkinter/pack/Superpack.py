from tkinter import *

fen=Tk()

Label(fen,
text="order=1\ndir=LEFT\nfill=NONE\nanchor=n\nexpand=1\npadx=2 pady=5",
font="Arial 10 bold", bg="light sky blue", justify=LEFT
).pack(side=LEFT, padx=2, pady=5, fill=NONE, anchor="n", expand=1)

Label(fen,
text="order=2\ndir=RIGHT\nfill=Y\nanchor=se\nexpand=1\npadx=4 pady=2",
font="Arial 10 bold", bg="ivory", justify=LEFT
).pack(side=RIGHT, padx=4, pady=2, fill=Y, anchor="se", expand=1)

Label(fen,
text="order=3\ndir=TOP\nfill=X\nanchor=sw\nexpand=0\npadx=6 pady=4",
font="Arial 10 bold", bg="orange", justify=LEFT
).pack(side=TOP, padx=6, pady=4, fill=X, anchor="sw", expand=0)

Label(fen,
text="order=4\ndir=RIGHT\nfill=NONE\nanchor=sw\nexpand=1\npadx=4 pady=4",
font="Arial 10 bold", bg="orange", justify=LEFT
).pack(side=RIGHT, padx=4, pady=4, fill=NONE, anchor="sw", expand=1)

Label(fen,
text="order=5\ndir=LEFT\nfill=X\nanchor=nw\nexpand=0\npadx=11 pady=4",
font="Arial 10 bold", bg="cyan", justify=LEFT
).pack(
side=LEFT, padx=11, pady=4, fill=X, anchor="nw", expand=0)

Label(fen,
text="order=6\ndir=LEFT\nfill=X\nanchor=sw\nexpand=1\npadx=2 pady=3",
font="Arial 10 bold", bg="salmon", justify=LEFT
).pack(
side=LEFT, padx=2, pady=3, fill=X, anchor="sw", expand=1)

Label(fen,
text="order=7\ndir=TOP\nfill=Y\nanchor=w\nexpand=1\npadx=10 pady=3",
font="Arial 10 bold", bg="red", justify=LEFT
).pack(
side=TOP, padx=10, pady=3, fill=Y, anchor="w", expand=1)

Label(fen,
text="order=8\ndir=RIGHT\nfill=X\nanchor=se\nexpand=1\npadx=9 pady=2",
font="Arial 10 bold", bg="red", justify=LEFT
).pack(side=RIGHT, padx=9, pady=2, fill=X, anchor="se", expand=1)

Label(fen,
text="order=9\ndir=TOP\nfill=BOTH\nanchor=se\nexpand=0\npadx=8 pady=4",
font="Arial 10 bold", bg="salmon", justify=LEFT
).pack(side=TOP, padx=8, pady=4, fill=BOTH, anchor="se", expand=0)

Label(fen,
text="order=10\ndir=LEFT\nfill=BOTH\nanchor=w\nexpand=1\npadx=8 pady=5",
font="Arial 10 bold", bg="orange", justify=LEFT
).pack(side=LEFT, padx=8, pady=5, fill=BOTH, anchor="w", expand=1)

Label(fen,
text="order=11\ndir=RIGHT\nfill=NONE\nanchor=sw\nexpand=1\npadx=2 pady=4",
font="Arial 10 bold", bg="brown", justify=LEFT
).pack(side=RIGHT, padx=2, pady=4, fill=NONE, anchor="sw", expand=1)

Label(fen,
text="order=12\ndir=TOP\nfill=NONE\nanchor=center\nexpand=0\npadx=4 pady=3",
font="Arial 10 bold", bg="green", justify=LEFT
).pack(side=TOP, padx=4, pady=3, fill=NONE, anchor="center", expand=0)

Label(fen,
text="order=13\ndir=BOTTOM\nfill=BOTH\nanchor=nw\nexpand=0\npadx=4 pady=3",
font="Arial 10 bold", bg="blue", justify=LEFT
).pack(
side=BOTTOM, padx=4, pady=3, fill=BOTH, anchor="nw", expand=0)

Label(fen,
text="order=14\ndir=TOP\nfill=NONE\nanchor=w\nexpand=1\npadx=9 pady=5",
font="Arial 10 bold", bg="ivory", justify=LEFT
).pack(side=TOP, padx=9, pady=5, fill=NONE, anchor="w", expand=1)

fen.mainloop()