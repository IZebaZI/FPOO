#Ejercicio 2
import math

def areaCirculo(radio):
    area = math.pi*(radio**2)
    return area

def volumenCilindro(radio, altura):
    area = areaCirculo(radio)
    volumen = altura * area
    return volumen

radio = float(input("Introduce el radio: "))
resultado = areaCirculo(radio)
print(f"El área del círculo es: {resultado}")

altura = float(input("\nIntroduce la altura del cilindro: "))
resultado = volumenCilindro(radio, altura)
print(f"El volumen del cilindro es: {resultado}")
