
class Password:
    def __init__(self, upper, specials, longitud = 8):
        self.__longitud = longitud
        self.__password = []
        self.__upper = upper
        self.__specials = specials
    
    def getLongitud(self):
        return self.__longitud
    def __getPassword(self):
        return self.__password
    
    def generarPassword(self):
        if self.__upper == 1 and self.__specials == 1:
            characters = string.ascii_letters + string.digits + string.punctuation
            self.__password = ''.join(random.choice(characters) for i in range(self.__longitud))
            return self.__password
        
        elif self.__upper == 0 and self.__specials == 1:
            characters = string.ascii_lowercase + string.digits + string.punctuation
            self.__password = ''.join(random.choice(characters) for i in range(self.__longitud))
            return self.__password
        
        elif self.__upper == 1 and self.__specials == 0:
            characters = string.ascii_letters
            self.__password = ''.join(random.choice(characters) for i in range(self.__longitud))
            return self.__password
        
        else:
            characters = string.ascii_lowercase
            self.__password = ''.join(random.choice(characters) for i in range(self.__longitud))
            return self.__password