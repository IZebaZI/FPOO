import random

class Usuario:
    def __init__(self, nombre, apellidoP, apellidoM, nacimiento, carrera):
        self.__nombre = nombre
        self.__apellidoP = apellidoP
        self.__apellidoM = apellidoM
        self.__nacimiento = nacimiento
        self.__carrera = carrera
        self.__matricula = ""
    
    def generarMatricula(self):
        letrasCarrera = str(self.__carrera[0:3])
        numerosActual = "24"
        numerosNacimiento = str(self.__nacimiento[2:4])
        letrasNombre = str(self.__nombre[0])
        letrasApeP = str(self.__apellidoP[0:3])
        letrasApeM = str(self.__apellidoM[0:3])
        numeros = ""
        for i in range(0,3):
            numero = random.randint(0,9)
            numeros = numeros+str(numero)
        self.__matricula = str(letrasCarrera+numerosActual+numerosNacimiento+letrasNombre+letrasApeP+letrasApeM+numeros).upper()
        return self.__matricula