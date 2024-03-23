from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    def conexion(self):
        try:
            conexion = sqlite3.connect("C:/Users/zebaz/Documents/GitHub/FPOO/SQLite/database.db")
            print('Conectado')
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def encriptarPass(self, password):
        passFlat = password
        passFlat = passFlat.encode()
        # salt es parte de la codificación que añade un nivel extra de seguridad
        salt = bcrypt.gensalt()
        # hashpw nos ayuda a encriptar la contraseña
        passHash = bcrypt.hashpw(passFlat, salt)
        return passHash
    
    def insertUsuario(self, nombre, correo, password):
        conexion = self.conexion()
        if(nombre=="" or correo=="" or password==""):
            messagebox.showwarning("Cuidado", "Inputs Vacios")
            conexion.close()
        else:
            cursor = conexion.cursor()
            encriptedPass = self.encriptarPass(password)
            datos = (nombre, correo, encriptedPass)
            sqlInsert = "insert into tbusuarios (nombre, correo, password) values (?,?,?)"
            cursor.execute(sqlInsert, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito", "El usuario se guardo exitosamente")
