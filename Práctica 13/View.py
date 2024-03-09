from tkinter import *
from tkinter import messagebox
from Password import *

class View:
    def createView(self, objectPassword):
        window = Tk()
        window.title("Generador de Contraseñas")
        window.geometry("400x300")
        
        def generarPassword():
            newPassword = objectPassword.generarPassword(upper.get(), special.get(), int(lenght.get()))
            print(messagebox.showinfo('Contraseña:', newPassword))
            inputPassword.delete(0, END)
            inputPassword.insert(0, newPassword)
        
        def comprobarFortaleza():
            fortaleza = objectPassword.comprobarFortaleza(upper.get(), special.get(), int(lenght.get()))
            if fortaleza == False:
                print(messagebox.showerror('Fortaleza', "No se ha registrado ninguna contraseña"))
            elif "Fuerte" in fortaleza:
                print(messagebox.showinfo('Fortaleza', "La contraseña tiene una fortaleza: " + fortaleza))
            elif "Media" in fortaleza:
                print(messagebox.showwarning('Fortaleza', "La contraseña tiene una fortaleza: " + fortaleza))
            elif "Baja" in fortaleza:
                print(messagebox.showwarning('Fortaleza', "La contraseña tiene una fortaleza: " + fortaleza))
            elif "Muy Débil" in fortaleza:
                print(messagebox.showerror('Fortaleza', "La contraseña tiene una fortaleza: " + fortaleza))
            else:
                print(messagebox.showerror('Fortaleza', + fortaleza))
    
        seccion = Frame(window, bg = "lightblue")
        seccion.pack(expand = True, fill = "both")
        
        lenght = StringVar()
        labelLongitud = Label(seccion, text = "Longitud: ")
        labelLongitud.pack()
        inputLongitud = Entry(seccion, textvariable = lenght)
        inputLongitud.pack()
        inputLongitud.insert(0, 8)
        
        upper = BooleanVar()
        special = BooleanVar()
        Checkbutton(seccion, offvalue=False, onvalue=True, text = "Mayúsculas", variable = upper).pack(pady = (10, 0))
        Checkbutton(seccion, offvalue=False, onvalue=True, text = "Carácteres Especiales", variable = special).pack()
        
        labelNewPassword = Label(seccion, text = "Contraseña Creada: ")
        labelNewPassword.pack(pady = (10, 0))
        inputPassword = Entry(seccion)
        inputPassword.pack(pady = (0, 10))
        
        btn = Button(seccion, text = "Generar", command = generarPassword)
        btn.pack(pady = (0, 10))
        
        btnComprobar = Button(seccion, text = "Comprobar Fortaleza", command = comprobarFortaleza)
        btnComprobar.pack()
        
        window.mainloop()
