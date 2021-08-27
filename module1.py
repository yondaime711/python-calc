from tkinter import*
import math
import parser
import tkinter.messagebox
import tkinter as tk
import os

root = Tk()
root.title("Kalkulator")
root.configure(background = "light blue")
root.resizable(width=False,height=False)
root.geometry("230x250")
calc = Frame(root)
calc.grid()
operator=""
tekst=StringVar()






#przycisk klikniety
def klik(numer):
    global operator
    operator=operator+str(numer)
    tekst.set(operator)
#czyszczenie
def czysc():
    global operator
    operator=""
    tekst.set("")
#rowna sie
def rowny():
    global operator
    suma=str(eval(wyswietlany.get()))
    wyswietlany.insert(tk.END," = "+str(suma))
    #zapis do pliku
    pliktekst=open('historia.txt','a')
    print(wyswietlany.get(),file=pliktekst)
    pliktekst.close()

#pamiec
def memc():
    global pamiec
    memory=''
def memr():
    global pamiec
    global operator
    wyswietlany.insert(tk.END,pamiec)
def mems():
    global pamiec
    pamiec=wyswietlany.get()

#backspace

def bac():
    wyswietlany.delete('1',END)
def sqrt():
    a=int(str(wyswietlany.get()))
    b=math.sqrt(a)
    wyswietlany.insert(tk.END,'√')
    b=str(b)
    wyswietlany.insert(tk.END,'='+b)

def proc():

    a=float(str(wyswietlany.get()))
    b=a*0.1
    wyswietlany.insert(tk.END,'%')
    b=str(b)
    wyswietlany.insert(tk.END,'='+b)
def odw():
    global operator
    a=int(eval(operator))
    b=a**-1
    wyswietlany.insert(tk.END,'odw')
    a=b
    wyswietlany.insert(tk.END,'='+str(a))
def znak():
    try:
        if wyswietlany.get():
            wyswietlany.insert(0,'-')
    except IndexError:
        pass

#wyswietlacz

wyswietlany = Entry(root,font=('arial',14,'bold'),textvariable=tekst,bg="light blue",width=20,bd=5,justify=RIGHT)
wyswietlany.grid(columnspan=5, row=0,column=0,pady=1)
wyswietlany.insert(0,"0")



#tworzenie klawiszy

#1rzad
przycisk_MC = Button(root, text="MC",command=memc, width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=2,column=0,pady=2)
przycisk_MR = Button(root, text="MR",command=memr, width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=2,column=1,pady=2)
przycisk_MS = Button(root, text="MS",command=mems,width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=2,column=2,pady=2)
przycisk_CE = Button(root, text="CE",command=czysc,width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=2,column=3,pady=2)
przycisk_C = Button(root, text="C",command=czysc,width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=2,column=4,pady=2)
#2rzad
przycisk_bac = Button(root, text="←",command=bac,width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=3,column=0,pady=2)
przycisk_sqrt = Button(root, text="√",command=sqrt,width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=3,column=1,pady=2)
przycisk_proc = Button(root, text="%",command=proc,width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=3,column=2,pady=2)
przycisk_odw = Button(root, text="odw",command=odw,width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=3,column=3,pady=2)
przycisk_znak = Button(root, text="±",command=znak,width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=3,column=4,pady=2)
#3rzad
przycisk_7 = Button(root, text="7",command=lambda:klik(7),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=4,column=0,pady=2)
przycisk_8 = Button(root, text="8",command=lambda:klik(8),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=4,column=1,pady=2)
przycisk_9 = Button(root, text="9",command=lambda:klik(9),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=4,column=2,pady=2)
przycisk_mnoz = Button(root, text="*",command=lambda:klik("*"),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=4,column=3,pady=2)
przycisk_dziel = Button(root, text="/",command=lambda:klik("/"),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=4,column=4,pady=2)
#4rzad
przycisk_4 = Button(root, text="4",command=lambda:klik(4),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=5,column=0,pady=2)
przycisk_5 = Button(root, text="5",command=lambda:klik(5),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=5,column=1,pady=2)
przycisk_6 = Button(root, text="6",command=lambda:klik(6),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=5,column=2,pady=2)
przycisk_odej = Button(root, text="-",command=lambda:klik("-"),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=5,column=3,pady=2)
przycisk_doda = Button(root, text="+",command=lambda:klik("+"),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=5,column=4,pady=2)
#5rzad
przycisk_1 = Button(root, text="1",command=lambda:klik(1),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=6,column=0,pady=2)
przycisk_2 = Button(root, text="2",command=lambda:klik(2),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=6,column=1,pady=2)
przycisk_3 = Button(root, text="3",command=lambda:klik(3),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=6,column=2,pady=2)
przycisk_rowna = Button(root, text="=",command=rowny,width=9,height=4,fg="black",bg="light blue",font=('arial',10)).grid(row=6,column=3,pady=2,rowspan=2,columnspan=2)
#6rzad
przycisk_0 = Button(root, text="0",command=lambda:klik(0),width=9,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=7,column=0,pady=2,rowspan=2,columnspan=2)
przycisk_przec = Button(root, text=",",command=lambda:klik("."),width=3,height=1,fg="black",bg="light blue",font=('arial',10)).grid(row=7,column=2,pady=2)


#menu

def Exit():
    Exit = tkinter.messagebox.askyesno("Kalkulator","Chcesz wyjsc?")
    if Exit > 0:
        root.destroy()
        return
def autor():
    autor=tkinter.messagebox.showinfo("Autor","Marcin KMWTW 97 pdk")

def otworz():
    os.system("notepad.exe historia.txt")

pasek = Menu(calc)

plik = Menu(pasek, tearoff =0)
pasek.add_cascade(label = "Plik", menu=plik)
plik.add_command(label = "O autorze", command= autor)
plik.add_command(label = "Historia obliczeń", command= otworz )
plik.add_separator()
plik.add_command(label = "Wyjscie", command = Exit)

#rozruch

root.config(menu=pasek)
root.mainloop()