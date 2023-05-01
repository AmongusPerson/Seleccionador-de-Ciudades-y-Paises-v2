from tkinter import *
import random

pg = Tk()
pg.geometry("500x500")
pg.title("Selector de Ciudades y Paises")
pg.configure(background="#264653")
    
lb1 = Label(pg, text="Selector de Ciudades y Paises", bg="#e76f51", fg="white", font=200)
lb1.place(relx=0.5, rely=0.04, anchor=CENTER,)

ip1 = Entry(pg, bg="#2a9d8f", fg="white", font=15)
ip1.place(relx=0.5, rely=0.11, anchor=CENTER,)

lb2 = Label(pg, text="País:",bg="#2a9d8f", fg="white", font=15)
lb2.place(relx=0.41, rely=0.11, anchor=CENTER)

ip2 = Entry(pg, bg="#2a9d8f", fg="white", font=15)
ip2.place(relx=0.5, rely=0.18, anchor=CENTER,)

paises = []
capitales = []
def fnp():
    var1 = ip1.get()
    print(var1)
    paises.append(var1)
    lb4["text"] = "Paises: " + str(paises)
    var2 = ip2.get()
    print(var2)
    capitales.append(var2)
    lb5["text"] = "Ciudades: " + str(capitales)
    
def fns():
    var5 = len(paises)
    var3 = random.randint(0,var5)
    lb6["text"] = paises[var3]
    var6 = len(capitales)
    var4 = random.randint(0,var6)
    lb7["text"] = capitales[var4]

lb3 = Label(pg, text="Ciudad:",bg="#2a9d8f", fg="white", font=15)
lb3.place(relx=0.402, rely=0.18, anchor=CENTER)

bt1 = Button(pg, text="Agregar", bg="#e76f51", fg="white", command=fnp)
bt1.place(relx=0.5, rely=0.25, anchor=CENTER,)

lb4 = Label(pg, text=".", bg="#2a9d8f", fg="white", font=15)
lb4.place(relx=0.5, rely=0.32, anchor=CENTER,)

lb5 = Label(pg, text=".", bg="#2a9d8f", fg="white", font=15)
lb5.place(relx=0.5, rely=0.39, anchor=CENTER,)

bt2 = Button(pg, text="Seleccionar", bg="#e76f51", fg="white", command=fns)
bt2.place(relx=0.5, rely=0.46, anchor=CENTER,)

lb6 = Label(pg, text=".", bg="#2a9d8f", fg="white", font=15)
lb6.place(relx=0.5, rely=0.53, anchor=CENTER,)

lb7 = Label(pg, text=".", bg="#2a9d8f", fg="white", font=15)
lb7.place(relx=0.5, rely=0.6, anchor=CENTER,)












pg.mainloop()
