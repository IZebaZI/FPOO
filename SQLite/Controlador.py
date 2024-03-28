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
            messagebox.showwarning("Cuidado", "Inputs vacios")
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
    
    def buscarUsuario(self, id):
        conexion = self.conexion()
        if(id==""):
            messagebox.showwarning("Cuidado", "Inputs vacios")
            conexion.close()
        else:
            try:
                cursor = conexion.cursor()
                sqlSelect = "select * from tbUsuarios where id = ?"
                cursor.execute(sqlSelect, id)
                usuario = cursor.fetchone()
                conexion.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la búsqueda")
                
    def listaUsuarios(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "select * from tbUsuarios"
            cursor.execute(sqlSelect)
            listaUsuarios = cursor.fetchall()
            conexion.close()
            return listaUsuarios
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la consulta")
    
    def editarUsuario(self, nombre, correo, id):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            datos = (nombre, correo, id)
            sqlSelect = "update tbUsuarios set nombre = ?, correo = ? where id = ?"
            cursor.execute(sqlSelect, datos)
            conexion.commit()
            conexion.close()
        except sqlite3.OperationalError:
                print("No se pudo ejecutar la búsqueda")
                
    def eliminarUsuario(self, id):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "delete from tbUsuarios where id = ?"
            cursor.execute(sqlSelect, id)
            conexion.commit()
            conexion.close()
        except sqlite3.OperationalError:
                print("No se pudo ejecutar la edición")