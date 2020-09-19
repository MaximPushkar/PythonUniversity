from tkinter import *

root = Tk()

cvar1 = BooleanVar()
cvar1.set(0)
c1 = Checkbutton(text="First", variable=cvar1, onvalue=1, offvalue=0)
c1.pack(anchor=W)

cvar2 = BooleanVar()
cvar2.set(0)
c2 = Checkbutton(text="Second", variable=cvar2, onvalue=1, offvalue=0)
c2.pack(anchor=W)

root.mainloop()
