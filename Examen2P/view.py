from tkinter import *
from tkinter import messagebox
from usuario import *

class View:
    def createView(self):
        window = Tk()
        window.title("Generador de Matrículas")
        window.geometry("400x300")
        
        def generarMatricula():
            usuario = Usuario(nombre.get(), apellidoP.get(), apellidoM.get(), nacimiento.get(), carrera.get())
            matricula = usuario.generarMatricula()
            print(messagebox.showinfo('Matricula:', matricula))
    
        seccion = Frame(window, bg = "lightblue")
        seccion.pack(expand = True, fill = "both")
        
        nombre = StringVar()
        labelNombre = Label(seccion, text = "Nombre: ")
        labelNombre.pack()
        inputNombre = Entry(seccion, textvariable = nombre)
        inputNombre.pack()
        
        apellidoP = StringVar()
        labelapellidoP = Label(seccion, text = "Apellido Paterno: ")
        labelapellidoP.pack()
        inputapellidoP = Entry(seccion, textvariable = apellidoP)
        inputapellidoP.pack()
        
        apellidoM = StringVar()
        labelapellidoM = Label(seccion, text = "Apellido Materno: ")
        labelapellidoM.pack()
        inputapellidoM = Entry(seccion, textvariable = apellidoM)
        inputapellidoM.pack()
        
        nacimiento = StringVar()
        labelNacimiento = Label(seccion, text = "Nacimiento: ")
        labelNacimiento.pack()
        inputNacimiento = Entry(seccion, textvariable = nacimiento)
        inputNacimiento.pack()
        
        carrera = StringVar()
        labelCarrera = Label(seccion, text = "Carrera: ")
        labelCarrera.pack()
        inputCarrera = Entry(seccion, textvariable = carrera)
        inputCarrera.pack()
        
        btn = Button(seccion, text = "Generar Matrícula", command = generarMatricula)
        btn.pack(pady = (0, 10))
        
        window.mainloop()

view = View()
view.createView()