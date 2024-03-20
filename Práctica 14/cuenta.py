class Cuenta:
    def __init__(self, numero, titular, edad, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__edad = edad
        self.__saldo = saldo
    
    def getNumero(self):
        return self.__numero
    
    def getSaldo(self):
        return int(self.__saldo)
    
    def mostrarSaldo(self):
        return str(self.__saldo)
    
    def ingresarEfectivo(self, efectivo):
        self.__saldo = int(self.__saldo) + int(efectivo)
        return str(self.__saldo)
    
    def retirarEfectivo(self, efectivo):
        self.__saldo = int(self.__saldo) - int(efectivo)
        return str(self.__saldo)
    
    def mostrarDatos(self):
        datos = "No. Cuenta: "+self.__numero+"\nTitular: "+self.__titular+"\nEdad: "+self.__edad+"\nSaldo: "+str(self.__saldo)
        return datos