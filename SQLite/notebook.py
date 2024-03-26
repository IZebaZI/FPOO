from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

controlador = Controlador()

def ejecutarInsert():
    controlador.insertUsuario(nombre.get(), correo.get(), password.get())

def ejecutarSelect():
    usuarioBD = controlador.buscarUsuario(id.get())
    if usuarioBD == [] or usuarioBD == None:
        messagebox.showwarning("Usuario Inexistente", "El usuario no fue encontrado")
    else:
        print(usuarioBD)
        infoUsuario.delete("1.0", END)
        infoUsuario.insert(END, usuarioBD)

# Creación de la ventana
ventana = Tk()
ventana.title("Crud Usuarios")
ventana.geometry("500x300")

# Preparación del notebook para las pestañas
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

# Definir las pestañas del notebook
page1 = ttk.Frame(panel)
page2 = ttk.Frame(panel)
page3 = ttk.Frame(panel)
page4 = ttk.Frame(panel)
page5 = ttk.Frame(panel)

# Agregamos las pestañas
panel.add(page1, text="Crear Usuario")
panel.add(page2, text="Buscar Usuario")
panel.add(page3, text="Consultar Usuarios")
panel.add(page4, text="Editar Usuario")
panel.add(page5, text="Borrar Usuario")

# Pestaña 1: Crear Usuario
Label(page1, text="Registrar Usuarios", fg="blue", font=("Modern", 18)).pack()

nombre = tk.StringVar()
Label(page1, text="Nombre: ").pack()
Entry(page1, textvariable=nombre).pack()

correo = tk.StringVar()
Label(page1, text="Correo: ").pack()
Entry(page1, textvariable=correo).pack()

password = tk.StringVar()
Label(page1, text="Password: ").pack()
Entry(page1, textvariable=password).pack()

Button(page1, text="Guardar Usuario", command=ejecutarInsert).pack(pady=(10,0))

# Pestaña 2: Buscar Usuario
Label(page2, text="Buscar Usuario", fg="blue", font=("Modern", 18)).pack()

id = tk.StringVar()
Label(page2, text="ID: ").pack()
Entry(page2, textvariable=id).pack()

Button(page2, text="Buscar Usuario", command=ejecutarSelect).pack(pady=(10,10))

Label(page2, text="Registrado:", fg="blue", font=("Modern", 16)).pack()
infoUsuario = Text(page2, height=5, width=52)
infoUsuario.pack()

ventana.mainloop()