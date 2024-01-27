#Ejercicio 1
password = input("Introduce una contraseña: ")

confirm = input("Introduce nuevamente la contraseña: ")
if confirm == password:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden, intenta nuevamente")