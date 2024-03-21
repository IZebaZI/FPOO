from tkinter import *
from tkinter import ttk
import tkinter as tk

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

Button(page1, text="Guardar Usuario").pack(pady=(10,0))

ventana.mainloop()