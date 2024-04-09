from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *
from GeneradorPDF import *
import os

controlador = Controlador()
pdf = GeneradorPDF()

def ejecutarInsert():
    controlador.insertUsuario(nombre.get(), correo.get(), password.get())

def ejecutarSelect():
    usuarioBD = controlador.buscarUsuario(id.get())
    if usuarioBD == [] or usuarioBD == None:
        messagebox.showwarning("Usuario Inexistente", "El usuario no fue encontrado")
    else:
        infoUsuario.delete("1.0", END)
        infoUsuario.insert(END, usuarioBD)

def listaUsuarios():
    listaUsuarios = controlador.listaUsuarios()
    if listaUsuarios == [] or listaUsuarios == None:
        messagebox.showwarning("Lista vacía", "No hay usuarios registrados")
    else:
        for item in userTable.get_children():
            userTable.delete(item)
        for usuario in listaUsuarios:
            userTable.insert("", END, text=usuario[0], values=usuario[1:])

def selectUpdate():
    usuarioBD = controlador.buscarUsuario(updateId.get())
    if usuarioBD == [] or usuarioBD == None:
        messagebox.showwarning("Usuario Inexistente", "El usuario no fue encontrado")
    else:
        entryNombre.delete(0, END)
        entryNombre.insert(0, usuarioBD[1])
        entryCorreo.delete(0, END)
        entryCorreo.insert(0, usuarioBD[2])

def ejecutarUpdate():
    usuarioBD = controlador.buscarUsuario(updateId.get())
    if usuarioBD == [] or usuarioBD == None:
        messagebox.showwarning("Usuario Inexistente", "El usuario no fue encontrado")
    else:
        controlador.editarUsuario(updateNombre.get(), updateCorreo.get(), updateId.get())
        messagebox.showinfo("Usuario Actualizado", "El usuario fue actualizado exitosamente")
        
def selectDelete():
    usuarioBD = controlador.buscarUsuario(deleteId.get())
    if usuarioBD == [] or usuarioBD == None:
        messagebox.showwarning("Usuario Inexistente", "El usuario no fue encontrado")
    else:
        infoDelete.delete("1.0", END)
        infoDelete.insert(END, usuarioBD)

def ejecutarDelete():
    usuarioBD = controlador.buscarUsuario(deleteId.get())
    if usuarioBD == [] or usuarioBD == None:
        messagebox.showwarning("Usuario Inexistente", "El usuario no fue encontrado")
    else:
        controlador.eliminarUsuario(deleteId.get())
        messagebox.showinfo("Usuario Eliminado", "El usuario fue eliminado exitosamente")

def generarPDF():
    if title == "":
        messagebox.showerror("Titulo Vacio", "El título está vacio")
    else:
        pdf.add_page()
        pdf.chapter_body()
        pdf.output(title.get()+".pdf")
        rutaPDF = "C:/Users/zebaz/Documents/GitHub/FPOO/"+title.get()+".pdf"
        messagebox.showinfo("Archivo Creado", "PDF disponible en carpeta")
        os.system(f"start {rutaPDF}")

# Creación de la ventana
ventana = Tk()
ventana.title("Crud Usuarios")
ventana.geometry("700x300")

# Preparación del notebook para las pestañas
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

# Definir las pestañas del notebook
page1 = ttk.Frame(panel)
page2 = ttk.Frame(panel)
page3 = ttk.Frame(panel)
page4 = ttk.Frame(panel)
page5 = ttk.Frame(panel)
page6 = ttk.Frame(panel)

# Agregamos las pestañas
panel.add(page1, text="Crear Usuario")
panel.add(page2, text="Buscar Usuario")
panel.add(page3, text="Consultar Usuarios")
panel.add(page4, text="Editar Usuario")
panel.add(page5, text="Borrar Usuario")
panel.add(page6, text="Reportes en PDF")

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

# Pestaña 3: Consultar Usuarios
Label(page3, text="Lista de Usuarios", fg="blue", font=("Modern", 18)).pack()

Button(page3, text="Actualizar Lista", command=listaUsuarios).pack(pady=(2,10))

userTable = ttk.Treeview(page3, columns=("#1", "#2", "#3"))
userTable.column("#0", width=80)
userTable.column("#1", width=120, anchor=CENTER)
userTable.column("#2", width=120, anchor=CENTER)
userTable.column("#3", width=110, anchor=CENTER)

userTable.heading("#0", text="ID", anchor=CENTER)
userTable.heading("#1", text="Nombre", anchor=CENTER)
userTable.heading("#2", text="Correo", anchor=CENTER)
userTable.heading("#3", text="Contraseña", anchor=CENTER)
userTable.pack()

# userTable = ttk.Treeview(root, column=("column1", "column2", "column3", "column4"), show='headings')
# userTable.heading("#1", text="ID")
# userTable.heading("#2", text="Nombre")
# userTable.heading("#3", text="Correo")
# userTable.heading("#4", text="Contraseña")
# userTable.pack()

# Pestaña 4: Editar Usuario
Label(page4, text="Editar Usuarios", fg="blue", font=("Modern", 18)).pack()

updateId = tk.StringVar()
Label(page4, text="ID: ").pack()
Entry(page4, textvariable=updateId).pack()

Button(page4, text="Buscar Usuario", command=selectUpdate).pack(pady=(10,10))

updateNombre = tk.StringVar()
Label(page4, text="Nombre: ").pack()
entryNombre = Entry(page4, textvariable=updateNombre)
entryNombre.pack()

updateCorreo = tk.StringVar()
Label(page4, text="Correo: ").pack()
entryCorreo = Entry(page4, textvariable=updateCorreo)
entryCorreo.pack()

Button(page4, text="Guardar Cambios", command=ejecutarUpdate).pack(pady=(10,0))

# Pestaña 5: Eliminar Usuario
Label(page5, text="Eliminar Usuario", fg="blue", font=("Modern", 18)).pack()

deleteId = tk.StringVar()
Label(page5, text="ID: ").pack()
Entry(page5, textvariable=deleteId).pack()

Button(page5, text="Buscar Usuario", command=selectDelete).pack(pady=(10,10))

Label(page5, text="Registrado:", fg="blue", font=("Modern", 16)).pack()
infoDelete = Text(page5, height=5, width=52)
infoDelete.pack()

Button(page5, text="Eliminar Usuario", command=ejecutarDelete).pack(pady=(10,10))

# Pestaña 6: Reportes en PDF
Label(page6, text="Generar Reporte en PDF", fg="green", font=("Modern", 18)).pack()

title = tk.StringVar()
Label(page6, text="Título del Reporte:").pack()
Entry(page6, textvariable=title).pack()

Button(page6, text="Generar Reporte", command=generarPDF).pack(pady=(10,10))

ventana.mainloop()