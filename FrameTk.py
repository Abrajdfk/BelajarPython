from tkinter import *
root = Tk()

frame = Frame(root)
frame.pack()
buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM)
redbutton = Button(frame,text='RED', fg='RED')
brownbutton = Button(frame,text='BROWN', fg='brown')
greenbutton = Button(frame,text='GREEN', fg='green')
redbutton.pack(side=LEFT)
brownbutton.pack(side=LEFT)
greenbutton.pack(side=LEFT)
mainloop()