

import tkinter
from collections import Counter
from tkinter import messagebox
from PIL import ImageTk, Image

palabra=[]

letra=[]

ventana = tkinter.Tk()
ventana.geometry("500x500")
ventana.title("ahorcado")
ventana.config(bg="sky blue" ,cursor="cross")
titulop = tkinter.Label(ventana, text = 'ingrese la palabra', bg = 'aquamarine2',)

letras = tkinter.StringVar()

entrypalabra = tkinter.Entry(ventana , show="?" ,textvariable = letras,width=22)
titulo = tkinter.Label(ventana, text = 'ingrese la letra', bg = 'aquamarine2')
titulop.pack()
entrypalabra.pack()


entrytodo= tkinter.Entry(ventana  ,width=22)
todo=tkinter.Label(ventana, text = 'adivinar palabra', bg = 'aquamarine2')
todo.pack()
entrytodo.pack()


titulo.pack()
pa= tkinter.StringVar()
entryadivinar = tkinter.Entry(ventana,textvariable = pa,width=2)

def limite(pa):
    if len(pa.get())>0:
        pa.set(pa.get()[:1])
pa.trace("w",lambda*args:limite(pa))

entryadivinar.pack()
palabra.append(entrypalabra.get)

imagen= ImageTk.PhotoImage(Image.open(r'C:\imga\todo.jpg'))             
cargar=tkinter.Label(ventana,image=imagen).place(x=50,y=200)



espacio=True

def lista():
    palabra.append(entrypalabra.get())
    print(palabra)

    global espacio


    espacio=[tkinter.Label(ventana, text="_") for _ in entrypalabra.get() ]
    posicionx=200

    for i in range(len(entrypalabra.get())):
        espacio[i].place(x=posicionx, y= 200)
        posicionx += 50  

vidas=7

correcto=0  


def todo():
    global vidas
    if entrytodo.get()==entrypalabra.get():
        
        messagebox.showinfo(message="ganaste: "+ entrypalabra.get(), title="ganaste")
        entrytodo.delete(0, 'end')

    else:

         messagebox.showinfo(message="ERROR -3 vidas: " ,title="error")
         entrytodo.delete(0, 'end')

         vidas-=3

def on_button():

    global vidas

    global correcto

    letra.append(entryadivinar.get())
    print(letra)
    
     
    if entryadivinar.get() in entrypalabra.get():

        if entrypalabra.get().count(entryadivinar.get())>1:

            correcto+=entrypalabra.get().count(entryadivinar.get())

            for i in range(len(entrypalabra.get())):
                
                if entrypalabra.get()[i]==entryadivinar.get():
                    espacio[i].config(text=""+entryadivinar.get())
        
                    
        else:
            correcto+=1
            espacio[entrypalabra.get().index(entryadivinar.get())].config(text=""+entryadivinar.get())
        if correcto==len(entrypalabra.get()):
            messagebox.showinfo(message="ganaste: "+ entrypalabra.get(), title="ganaste")

            
    else:
        vidas-=1
        if vidas==6:
            entryadivinar.delete(0, 'end')

            imagen1= ImageTk.PhotoImage(Image.open(r'C:\imga\juego2.jpg'))             
            cargar=tkinter.Label(ventana,image=imagen1).place(x=50,y=200)
            imagen1.pack()
            
        if vidas==5:
            entryadivinar.delete(0, 'end')

            imagen3= ImageTk.PhotoImage(Image.open(r'C:\imga\juego3.jpg'))             
            cargar=tkinter.Label(ventana,image=imagen3).place(x=50,y=200)
            imagen3.pack()

        if vidas==4:
            entryadivinar.delete(0, 'end')

            imagen4= ImageTk.PhotoImage(Image.open(r'C:\imga\todo4.jpg'))             
            cargar=tkinter.Label(ventana,image=imagen4).place(x=50,y=200)
            imagen4.pack()

        if vidas==3:
            entryadivinar.delete(0, 'end')

            imagen5= ImageTk.PhotoImage(Image.open(r'C:\imga\todo5.jpg'))             
            cargar=tkinter.Label(ventana,image=imagen5).place(x=50,y=200)
            imagen5.pack()

        if vidas==2:
            entryadivinar.delete(0, 'end')
            imagen6= ImageTk.PhotoImage(Image.open(r'C:\imga\todo6.jpg'))             
            cargar=tkinter.Label(ventana,image=imagen6).place(x=50,y=200)
            imagen6.pack()

            
        if vidas<=1:
            entryadivinar.delete(0, 'end')

            messagebox.showinfo(message="perdiste, la palabra era: "+ entrypalabra.get(), title="derrota")
            # messagebox.askretrycancel(message="¿Desea reintentar?", title="Título")

            imagen7= ImageTk.PhotoImage(Image.open(r'C:\imga\todo7.jpg'))             
            cargar=tkinter.Label(ventana,image=imagen7).place(x=50,y=200)
            imagen7.pack()

            
        
    entryadivinar.delete(0, 'end')

    
 


button2 = tkinter.Button(ventana, text="confirmar palabra",  bg = 'aquamarine2',command=lista)
button2.place(x=320, y=20, width=100, height=20) 

button1 = tkinter.Button(ventana, text="confirmar letra",bg = 'aquamarine2', command=on_button)
button1.place(x=320, y=100, width=100, height=20) 

button3= tkinter.Button(ventana, text="adivinar",bg = 'aquamarine2', command=todo)
button3.place(x=320, y=60, width=100, height=20) 




ventana.mainloop()



