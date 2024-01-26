#Ejercicio 5
pesoPayasos = 112
pesoMunecas = 75

cantidadPayasos = int(input("Ingresa la cantidad de payasos vendidos: "))
cantidadMunecas = int(input("Ingresa la cantidad de muñecas vendidas: "))

pesoPaquete = (cantidadPayasos*pesoPayasos) + (cantidadMunecas*pesoMunecas)
pesoKilos = pesoPaquete/1000

print("El paquete tiene un peso total de:", pesoPaquete, "gramos o ", pesoKilos, "kilogramos")