class Personaje:
    # Constructor
    def __init__(self, nombre, especie, altura):
        self.__nombre = nombre
        self.__especie = especie
        self.__altura = altura
    
    # GET
    def getNombre(self):
        return self.__nombre
    def getEspecie(self):
        return self.__especie
    def getAltura(self):
        return self.__altura
        
    # SET
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setEspecie(self, especie):
        self.__especie = especie
    def setAltura(self, altura):
        self.__altura = altura
    
    # Métodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje: " + self.__nombre + " está corriendo")
        else:
            print("El personaje: " + self.__nombre + " está muerto")
    
    def lanzarGranada(self):
        print(self.__nombre + " pegó una granada")
        
    def __pensar(self):
        print(self.__nombre + " está pensando")
    
    #Atributos
    # especie = "Humano"
    # nombre = "John"
    # altura = 2.18