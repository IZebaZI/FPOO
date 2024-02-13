import statistics

elementos = int(input("Ingresa un la cantidad de elementos: "))
lista = []

for i in range(0 , elementos):
    dato = int(input("Ingresa un valor entero: "))
    lista.append(dato)

tupla = tuple(lista)
print(f"La tupla ingresada es: {tupla}")
while True:
    print("\n------------------------------------------------------")
    print("1. Sumatoria de números en la lista\n2. Número mayor de la lista\n3. Número menor de la lista\n4. Promedio\n5. Moda\n6. Rango\n7. Salir")
    print("------------------------------------------------------")
    option = int(input("Seleccione una opción: "))
    if option == 7:
        break
    
    match option:
        case 1:
            suma = 0
            for valor in lista:
                suma += valor
            print(f"\nEl valor de la suma es: {suma}")
        case 2:
            lista.sort()
            print(f"El elemento mayor de la lista {tupla} es: {lista[elementos-1]}")
        case 3:
            lista.sort()
            print(f"El elemento mayor de la lista {tupla} es: {lista[0]}")
        case 4:
            suma = 0
            for valor in lista:
                suma += valor
                promedio = suma/elementos
            print(f"\nEl promedio de la lista {tupla} es: {promedio}")
        case 5:
            moda = statistics.mode(lista)
            print(f"\nLa moda de la lista {tupla} es: {moda}")
        case 6:
            lista.sort
            rango = lista[elementos-1] - lista[0]
            print(f"\nEl rango de la lista {tupla} es: {rango}")