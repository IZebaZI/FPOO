import statistics

elementos = int(input("Ingresa la cantidad de elementos: "))
lista = []

for i in range(0 , elementos):
    dato = int(input("Ingresa un valor entero: "))
    lista.append(dato)

tupla = tuple(lista)
print(f"La tupla ingresada es: {tupla}")

def sumaValores(lista):
    suma = 0
    for valor in lista:
        suma += valor
    return suma

def numeroMayor(lista):
    lista.sort()
    mayor = lista[elementos-1]
    return mayor

def numeroMenor(lista):
    lista.sort()
    menor = lista[0]
    return menor

def promedioLista(lista):
    suma = 0
    for valor in lista:
        suma += valor
        promedio = suma/elementos
    return promedio

def modaLista(lista):
    moda = statistics.mode(lista)
    return moda

def rangoLista(lista):
    lista.sort()
    rango = lista[elementos-1] - lista[0]
    return rango

while True:
    print("\n------------------------------------------------------")
    print("1. Sumatoria de números en la lista\n2. Número mayor de la lista\n3. Número menor de la lista\n4. Promedio\n5. Moda\n6. Rango\n7. Salir")
    print("------------------------------------------------------")
    option = int(input("Seleccione una opción: "))
    if option == 7:
        break
    
    match option:
        case 1:
            suma = sumaValores(lista)
            print(f"\nLa suma de los valores en la lista {tupla} es: {suma}")
        case 2:
            mayor = numeroMayor(lista)
            print(f"El elemento mayor de la lista {tupla} es: {mayor}")
        case 3:
            menor = numeroMenor(lista)
            print(f"El elemento menor de la lista {tupla} es: {menor}")
        case 4:
            media = promedioLista(lista)
            print(f"\nEl promedio de la lista {tupla} es: {media}")
        case 5:
            moda = modaLista(lista)
            print(f"\nLa moda de la lista {tupla} es: {moda}")
        case 6:
            rango = rangoLista(lista)
            print(f"\nEl rango de la lista {tupla} es: {rango}")
