#Ejercicio 7
base = int(input("Introduce la base del arbol:"))
i = 1

while i <= base:
    espacios = base - i
    asteriscos = 2 * i - 1
    print(" " * espacios + "*" * asteriscos)
    i += 1