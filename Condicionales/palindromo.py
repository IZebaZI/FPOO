frase = input("Ingresa una cadena de carácteres: ")
fraseinv = frase[::-1]

if frase == fraseinv:
    print("La frase es un palíndromo")
else:
    print("La frase no es un palindromo")