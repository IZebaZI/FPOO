#Ejercicio 6
print("Escriba la bitácora:")
operacion = " "
cantidad = 0

while operacion != "":
    operacion = input("")
    for i in operacion:
        if i in "Dd":
            valor = operacion[1:]
            cantidad += int(valor)
        elif i in "Rr":
            valor = operacion[1:]
            cantidad -= int(valor)
        else:
            cantidad += 0

print(f"El total es: {cantidad}")
