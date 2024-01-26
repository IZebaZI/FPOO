#Ejercicio 2
nombre = str(input("Ingresa tu nombre: "))
apellidoP = str(input("Ingresa tu apellido paterno: "))
apellidoM = str(input("Ingresa tu apellido materno: "))

nombreCompleto = nombre + apellidoP + apellidoM
completoLower = nombreCompleto.lower()
completoUpper = nombreCompleto.upper()

paternoUpper = apellidoP.upper()
maternoUpper = apellidoM.upper()

print(completoLower)
print(completoUpper)
print(nombre[0],paternoUpper,maternoUpper)