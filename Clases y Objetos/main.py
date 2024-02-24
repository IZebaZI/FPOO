from Personaje import *
from Armas import *

#Crear objeto
spartan = Personaje()
arma = Armas()

#Llamar atributos
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#Utilizar métodos
spartan.correr(False)
spartan.lanzarGranada()

#Utilizar métodos de Armas
arma.seleccionarArma(spartan.nombre)
arma.recargarArma(65)
