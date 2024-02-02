#Ejercicio 1
def calcularIVA(cantidad, porcentaje = 21):
    resultado = cantidad*(float(porcentaje)/100)
    print(resultado)

cantidad = float(input("Ingresa una cantidad: "))
porcentaje = input("Ingresa un porcentaje (opcional): ")

if porcentaje != "":
    calcularIVA(cantidad, porcentaje)
else:
    calcularIVA(cantidad)