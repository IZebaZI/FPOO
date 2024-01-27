#Ejercicio 3
edad = int(input("Ingresa tu edad: "))

if edad < 4:
    print("¡Puedes entrar gratis!")
elif edad >= 4 and edad <= 18:
    print("Debes pagar $110 para entrar")
else:
    print("Debes pagar $190 para entrar")