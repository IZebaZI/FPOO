from Personaje import *
from Arma import *

# Solicitar datos del Spartan
nombreS = input("Escribe el nombre del Spartan: ")
especieS = input("Escribe la especie del Spartan: ")
alturaS = float(input("Escribe la altura del Spartan: "))

#Solicitar datos del Némesis
nombreN = input("\nEscribe el nómbre del Némesis: ")
especieN = input("Escribe la especie del Némesis: ")
alturaN = float(input("Escribe la altura del Némesis: "))

# Crear objetos
spartan = Personaje(nombreS, especieS, alturaS)
nemesis = Personaje(nombreN, especieN, alturaN)
arma = Arma()

# Atributos del Spartan
print("\n-- El Spartan contiene: --")
print(spartan.getNombre())
print(spartan.getEspecie())
print(spartan.getAltura())

# Atributos del Némesis
print("\n-- El Némesis contiene: --")
print(nemesis.getNombre())
print(nemesis.getEspecie())
print(nemesis.getAltura())

# Métodos del Spartan
print("\n-- Métodos del Spartan: --")
spartan.correr(True)
spartan.lanzarGranada()

# Métodos del Némesis
print("\n-- Métodos del Némesis: --")
nemesis.correr(True)
nemesis.lanzarGranada()

# Métodos de Armas
arma.seleccionarArma(spartan.getNombre())
arma.recargarArma(65)

#Llamar atributos
# print(spartan.nombre)
# print(spartan.especie)
# print(spartan.altura)

#Utilizar métodos
# spartan.correr(False)
# spartan.lanzarGranada()

