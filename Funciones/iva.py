#Ejercicio 1
def calcularIVA(cantidad, porcentaje = 21):
    resultado = cantidad*(float(porcentaje)/100)
    return resultado

cantidad = float(input("Ingresa una cantidad: "))
porcentaje = input("Ingresa un porcentaje (opcional): ")

if porcentaje != "":
    iva = calcularIVA(cantidad, porcentaje)
    total = cantidad + iva
    print(total)
else:
    iva = calcularIVA(cantidad)
    total = cantidad + iva
    print(total)