#Ejercicio 4
nombre = str(input("Ingresa tu nombre: "))
nombreUpper = nombre.upper()
nombreReplace = len(nombre.replace(" ",""))

print("El nombre:",nombreUpper,"tiene",nombreReplace,"letras")