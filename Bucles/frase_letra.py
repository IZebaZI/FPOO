#Ejercicio 5
frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")

contador = 0

for i in frase:
    if i.lower() == letra:
        contador += 1
print (f"La letra '{letra}' está {contador} veces en la frase: {frase}")