from tkinter import *
from tkinter import messagebox

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    z=int(x.get())*(int(x.get())+1)/2
    t_resultado.insert(INSERT, "Resultados:\n La suma de los primeros "+x.get()+" enteros positivos es : "+str(z)+"\n")

def borrar():
    messagebox.showinfo("N Enteros", "Lyos datos serán borrados...")
    x.set("")
    t_resultado.delete("N Enteros", "end")

def salir():
    messagebox.showinfo("N Enteros", "La App se cerrará...")
    ventana_principal.destroy()


#---------------------
# Ventana Principal
#---------------------

#Se declara una varaiable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("Juano Niño")

#Establecer tamaño a la pantalla
ventana_principal.geometry("800x500")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana principal
ventana_principal.config(bg="snow")

#---------------------
# Variables Globales
#---------------------  
x=StringVar()
z=IntVar()

#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Suma de N enteros")
titulo.config(bg="ivory2", fg="maroon", font=("Times New Roman", 20))
titulo.place(x=240,y=10)

titulo= Label(frame_entrada, text="Juan Niño")
titulo.config(bg="cadetblue3", fg="maroon", font=("Times New Roman", 18))
titulo.place(x=670,y=200)

subtitulo2= Label(frame_entrada, text="Determinar la suma de los primeros \n N enteros positivos usando la fórmula.")
subtitulo2.config(bg="ivory2", fg="maroon", font=("Times New Roman", 15), anchor=CENTER)
subtitulo2.place(x=240,y=70)

logo= PhotoImage(file="er.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=80)

etiq_a=Label(frame_entrada, text="Número N = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=145)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=480,y=140)


#---------------------
# Frame Operaciones
#---------------------

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="cornflower blue", width=780, height=135)
frame_operaciones.place(x=10,y=260)


bt_sum= PhotoImage(file="plus.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=130, height=125, command=sumar)
bt_sumar.place(x=100, y=5)


bt_bor= PhotoImage(file="eraser.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=125, height=120, command=borrar)
bt_borrar.place(x=330, y=7)


bt_sal= PhotoImage(file="log.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=125, height=120, command=salir)
bt_salir.place(x=585, y=7)


#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="indian red", width=780, height=100)
frame_resultados.place(x=10,y=400)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="sienna2", fg="grey2", font=("Courier", 12))
t_resultado.pack(expand=True)


ventana_principal.mainloop()

