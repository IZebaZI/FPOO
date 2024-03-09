from tkinter import Tk, Frame, Button, Entry, Label, StringVar, Checkbutton, IntVar
from tkinter import messagebox
from functools import partial
from Contraseña import Password

Ventana = Tk()
Ventana.title("3 Frames")
Ventana.geometry("600x400")

Seccion1 = Frame(Ventana, bg = "lightblue")
Seccion1.pack(expand = True, fill = "both")

lenght = StringVar()
upper = IntVar()
specials = IntVar()
passwordValue = StringVar()

label2 = Label(Seccion1, text = "Longitud:")
label2.grid(row = 0, column = 0)
inputLongitud = Entry(Seccion1, textvariable = lenght)
inputLongitud.insert(0, 8)
inputLongitud.grid(row = 0, column = 1)

Checkbutton(Seccion1, text = "Mayúsculas", variable = upper, onvalue=1, offvalue=0).grid(row = 1, column = 0)
Checkbutton(Seccion1, text = "Carácteres Especiales", variable = specials, onvalue=1, offvalue=0).grid(row = 2, column = 0)
upper = upper.get()
specials = specials.get()
lenght = lenght.get()

label1 = Label(Seccion1, text = "Contraseña Creada:")
label1.grid(row = 3, column = 0)

inputPassword = Entry(Seccion1, textvariable = passwordValue)
inputPassword.grid(row = 3, column = 0)

def generarPassword(mayusculas, especiales, longitud):
    password = Password(mayusculas, especiales, longitud)
    generatedPassword = password.generarPassword()
    print(messagebox.showinfo('Contraseña generada', generatedPassword))
    inputLongitud.insert(0, generatedPassword)
    
btnNegro = Button(Seccion1, text = "Crear", fg = "white", bg = "black", command = partial(generarPassword, upper, specials, lenght))
btnNegro.configure(height = 1, width = 8)
btnNegro.grid(row = 4, column = 0)

Ventana.mainloop()