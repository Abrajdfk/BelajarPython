from tkinter import  *

root = Tk()
root.title('Kalkulator')
root.geometry('400x200')

lb = Label(root, text='Masukan angka Pertama :',anchor='e',width=20)
lb.grid(column=0, row=0)

nilai1 = Entry(root, width=10)
nilai1.grid(column=1, row=0)

lb2 = Label(root, text='Masukan angka Pertama :',anchor='e',width=20)
lb2.grid(column=0, row=1)

nilai2 = Entry(root, width=10)
nilai2.grid(column=1, row=1)

lb3 = Label(root, text='Hasil :', anchor='e', width=20)
lb3.grid(column=0, row=2)

hasil = Label(root, text="0",anchor="w",width=10)
hasil.grid(column=1, row=2)


def tambah():
    hasil.configure(text=(int(nilai1.get()) + int(nilai2.get())))


def kurang():
    hasil.configure(text=(int(nilai1.get()) - int(nilai2.get())))


def kali():
    hasil.configure(text=(int(nilai1.get()) * int(nilai2.get())))


def bagi():
    hasil.configure(text=(int(nilai1.get()) / int(nilai2.get())))

btn = Button(root, text='Tambah', command=tambah)
btn.grid(column=0, row=3)

btn = Button(root, text='Kurang', command=kurang)
btn.grid(column=1, row=3)

btn = Button(root, text='Kali', command=kali)
btn.grid(column=0, row=4)

btn = Button(root, text='Bagi', command=bagi)
btn.grid(column=1, row=4)

mainloop()