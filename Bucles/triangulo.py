#Ejercicio 4
numero = int(input("Introduce un numero entero y positivo:"))

if numero % 2 == 0:
    inicio = int(0)
else:
    inicio = int(1)

for i in range(inicio, numero + 1, 2):
    for j in range(i, -1, -2):
        print(j, end=" ")
    print("")