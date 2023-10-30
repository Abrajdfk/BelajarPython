from tkinter import *

master = Tk()
w = Canvas(master, width=60, height=80)
w.pack()
Canvas_height= 40
Canvas_width= 200
y = int(Canvas_height/2)
w.create_line(0, y,Canvas_width,y)
mainloop()