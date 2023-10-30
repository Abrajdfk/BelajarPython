from tkinter import *
#NAMA ROOT BISA DI UBAH JADI APA SAJA
root = Tk()
menu = Menu(root)


root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About',)

viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Tool Windows')
viewmenu.add_command(label='Appearance')
viewmenu.add_separator()
viewmenu.add_command(label='Quick Defenition')
viewmenu.add_command(label='Quick Type Defenition')
viewmenu.add_command(label='Parameter info')
viewmenu.add_command(label='Type info')
viewmenu.add_command(label='Context info')
mainloop()
