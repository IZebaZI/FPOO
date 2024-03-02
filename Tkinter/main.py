from tkinter import Tk, Frame

#1. Creamos la ventana
Ventana = Tk() #Uso de POO creando un objeto Ventana
Ventana.title("3 Frames")
Ventana.geometry("600x400")

#2. Colocamos Frames de la ventana
Seccion1 = Frame(Ventana, bg = "lightblue")
Seccion1.pack(expand = True, fill = "both")

Seccion2 = Frame(Ventana, bg = "red")
Seccion2.pack(expand = True, fill = "both")

Seccion3 = Frame(Ventana, bg = "lightgreen")
Seccion3.pack(expand = True, fill = "both")

# Ejecutamos
Ventana.mainloop()