from tkinter import *
root = Tk()
v = IntVar()

root.title('RadioButton')
Radiobutton(root, text='Male',variable = v,value=1).pack(anchor=W)
Radiobutton(root, text='Female',variable = v,value=2).pack(anchor=W)
mainloop()