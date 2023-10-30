from tkinter import *

main = Tk()
ourMessage = "Tulis Pesan Disini"
messageVar = Message(main, text= ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
mainloop()