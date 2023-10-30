from tkinter import *

root = Tk()
s = Scale(root, from_=0, to=50)
s.pack()
s = Scale(root, from_=0, to=200, orient=HORIZONTAL)
s.pack()
mainloop()