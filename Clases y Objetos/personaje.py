class Personaje:
    # Atributos
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    #Métodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje: " + self.nombre + " está corriendo")
        else:
            print("El personaje: " + self.nombre + " está muerto")
    
    def lanzarGranada(self):
        print(self.nombre + " pegó una granada")