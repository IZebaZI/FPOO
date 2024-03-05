from tkinter import Tk, Frame, Button, messagebox

#Método para Mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo', 'Information'))
    print(messagebox.showerror('showerror', 'Error'))
    print(messagebox.showwarning('showinfo', 'Warning'))
    print(messagebox.askyesnocancel(message = "¿Desea continuar?", title = "Soy un título"))

def addbtn():
    botonVerde.config(text = "+")
    botonRosa = Button(Seccion3, text = "Nuevo", bg = "pink")
    botonRosa.configure(height = 2, width = 10)
    botonRosa.pack()
    

#1. Creamos la ventana
Ventana = Tk() #Uso de POO creando un objeto Ventana
Ventana.title("3 Frames")
Ventana.geometry("600x400")

#2. Colocamos Frames de la ventana
# Pack
Seccion1 = Frame(Ventana, bg = "lightblue")
Seccion1.pack(expand = True, fill = "both")

Seccion2 = Frame(Ventana, bg = "red")
Seccion2.pack(expand = True, fill = "both")

Seccion3 = Frame(Ventana, bg = "lightgreen")
Seccion3.pack(expand = True, fill = "both")

#3. Botones
#Place
botonAzul = Button(Seccion1, text = "Azul", fg = "darkblue")
botonAzul.place(x = 60, y = 60, width = 100, height = 30)

#Grid
botonNegro = Button(Seccion2, text = "Negro", fg = "white", bg = "black")
botonNegro.configure(height = 2, width = 10)
botonNegro.grid(row = 0, column = 1)

botonAmarillo = Button(Seccion2, text = "Amarillo", bg = "yellow", command = mostrarMensajes)
botonAmarillo.configure(height = 2, width = 10)
botonAmarillo.grid(row = 0, column = 2)

#Pack
botonVerde = Button(Seccion3, text = "Verde", fg = "darkgreen", command = addbtn)
botonVerde.configure(height = 2, width = 10)
botonVerde.pack()
botonVerde2 = Button(Seccion3, text = "Verde 2", fg = "white", bg = "darkgreen")
botonVerde2.configure(height = 2, width = 10)
botonVerde2.pack()

# Ejecutamos
Ventana.mainloop()