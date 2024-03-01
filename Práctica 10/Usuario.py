class Usuario:
    def __init__(self, id, nombre, apellidoP, apellidoM, correo, password):
        self.__id = id
        self.__nombre = nombre
        self.__apellidoP = apellidoP
        self.__apellidoM = apellidoM
        self.__correo = correo
        self.__password = password
    
    # GET
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getapellidoP(self):
        return self.__apellidoP
    def getapellidoM(self):
        return self.__apellidoM
    def getCorreo(self):
        return self.__correo
    def __validatePassword(self, password):
        if(self.__password == password):
            return True
        else:
            return False
    
    # SET
    def setNombre(self, nombre, apellidoP, apellidoM):
        self.__nombre = nombre
        self.__apellidoP = apellidoP
        self.__apellidoM = apellidoM
    def setCorreo(self, correo):
        self.__correo = correo
    def setPassword(self, password):
        self.__password = password
    
    # METHODS
    def changePassword(self, correo, password):
        if(self.__correo == correo ):
            self.__password = password
            return True
        else:
            return False
    
    def printInfo(self):
        print(f"ID: {self.__id}\nNombre: {self.__nombre}\nApellido Paterno: {self.__apellidoP}\nApellido Materno: {self.__apellidoM}\nCorreo: {self.__correo}\nContraseña: {self.__password}")
    
    def borrarUsuario(self):
        self.__id = None
        self.__nombre = None
        self.__apellidoP = None
        self.__apellidoM = None
        self.__correo = None
        self.__password = None