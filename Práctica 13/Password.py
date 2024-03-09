import string
import random

class Password:
    def __init__(self):
        self.__password = []
        
    def generarPassword(self, upper, specials, longitud):
        if upper == True and specials == True:
            characters = string.ascii_letters + string.digits + string.punctuation
            self.__password = ''.join(random.choice(characters) for i in range(longitud))
            return self.__password
        
        elif upper == False and specials == True:
            characters = string.ascii_lowercase + string.digits + string.punctuation
            self.__password = ''.join(random.choice(characters) for i in range(longitud))
            return self.__password
        
        elif upper == True and specials == False:
            characters = string.ascii_letters
            self.__password = ''.join(random.choice(characters) for i in range(longitud))
            return self.__password
        
        else:
            characters = string.ascii_lowercase
            self.__password = ''.join(random.choice(characters) for i in range(longitud))
            return self.__password
        
    def comprobarFortaleza(self, upper, specials, longitud):
        if not self.__password:
            return False
        if upper == True and specials == True and longitud >= 8:
            return "Fuerte, la contraseña es segura"
        elif upper == False and specials == True and longitud >= 8:
            return "Media, la contraseña es segura pero es recomendable agregar mayúsculas"
        elif upper == True and specials == False and longitud >= 8:
            return "Media, la contraseña es segura pero es recomendable agregar carácteres especiales"
        elif upper == False and specials == False and longitud >= 8:
            return "Baja, agregue mayúsculas y/o carácteres especiales"
        elif longitud < 8:
            return "Muy Débil, seleccione más opciones o asegurese de que la longitud sea mayor o igual a 8"
        else:
            return "Error al generar la contraseña, intente de nuevo"
