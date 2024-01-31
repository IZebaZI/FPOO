#Ejercicio 3
for tabla in range(1,11):
    print(f"Tabla del {tabla}")
    for operacion in range(1,11):
        resultado = tabla*operacion
        print(f"{operacion} x {tabla} = {resultado}")
    print("")