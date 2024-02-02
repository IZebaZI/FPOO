def decimalBinario(numero):
    resultado = ""
    while numero >= 1:
        if numero % 2 == 0:
            resultado = resultado + "0"
            numero = numero/2
        else:
            resultado = resultado + "1"
            numero = (numero - 1)/2
    resultado = resultado[::-1]
    return resultado

def binarioDecimal(numero):
    numero = numero[::-1]
    contador = int(0)
    resultado = int(0)
    for i in numero:
        if i =="1":
            resultado = resultado + 2**contador
        else:
            resultado = resultado + 0
        contador += 1
    return resultado

option = input("1. Decimal a Binario \n2. Binario a Decimal\nEscoge una opción: ")

if option == "1":
    numero = int(input("Introduce el número entero: "))
    print(decimalBinario(numero))
else:
    numero = input("Introduce el número binario: ")
    print(binarioDecimal(numero))