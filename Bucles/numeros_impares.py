numero = int(input("Ingresa un número entero positivo: "))
i = 1

while i <= numero:
    if i % 2 != 0:
        print(i, end=",")
    i += 1