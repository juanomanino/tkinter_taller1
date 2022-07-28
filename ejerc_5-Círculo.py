from tkinter import *
from tkinter import messagebox
import math

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    area=math.pi*int(rad.get())*int(rad.get())
    per=2*int(rad.get())*math.pi
    t_resultado.insert(INSERT, "Resultados:\n El valor del Radio es: "+rad.get()+"\n El valor del Área es: "+str(area)+"\n El valor del perímetro es "+str(per)+"\n")

def borrar():
    messagebox.showinfo("Circulo", "Los datos serán borrados...")
    rad.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Círculo", "La App se cerrará...")
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
rad=StringVar()
area=DoubleVar()
per=DoubleVar()

#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="peachpuff", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Área y Perímetro del Círculo")
titulo.config(bg="peachpuff", fg="maroon", font=("Times New Roman", 20))
titulo.place(x=240,y=10)

titulo= Label(frame_entrada, text="Juan Niño")
titulo.config(bg="cadetblue3", fg="maroon", font=("Times New Roman", 18))
titulo.place(x=670,y=200)

subtitulo2= Label(frame_entrada, text="Calcular el área y el perímetro de un círculo, dado su radio.\n")
subtitulo2.config(bg="peachpuff", fg="maroon", font=("Times New Roman", 15), anchor=CENTER)
subtitulo2.place(x=240,y=70)

logo= PhotoImage(file="hg.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="peachpuff")
etiq_logo.place(x=10,y=10)

etiq_a=Label(frame_entrada, text="Valor del Radio = ")
etiq_a.config(bg="peachpuff", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=145)

entry_a=Entry(frame_entrada, width=7, textvariable=rad)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=480,y=140)


#---------------------
# Frame Operaciones
#---------------------

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="cornflower blue", width=780, height=135)
frame_operaciones.place(x=10,y=260)


bt_sum= PhotoImage(file="equality.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=120, height=125, command=sumar)
bt_sumar.place(x=100, y=5)


bt_bor= PhotoImage(file="borrar.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=125, height=120, command=borrar)
bt_borrar.place(x=330, y=7)


bt_sal= PhotoImage(file="salida.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=125, height=120, command=salir)
bt_salir.place(x=585, y=7)

#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="indian red", width=780, height=100)
frame_resultados.place(x=10,y=400)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="gray70", fg="gray1", font=("Courier", 12))
t_resultado.pack(expand=True)


ventana_principal.mainloop()

