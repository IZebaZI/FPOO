class Personaje:
    # Atributos
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    #Métodos del personaje
    def correr(self, estado):
        if(estado):
            print("El personaje:" + self.nombre + " está corriendo")
        else:
            print("El personaje:" + self.nombre + " está muerto")
    
    def lanzarGranada(self):
        print(self.nombre + " pegó una granada")
    
    def recargarArma(self, municion):
        cargador = 25
        cargador = cargador + municion
        print("Arma recargada, capacidad: " + str(cargador) + " balas")

#Crear objeto
spartan = Personaje()

#Llamar atributos
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#Utilizar métodos
# spartan.correr()
# spartan.lanzarGranada()
# spartan.recargarArma()