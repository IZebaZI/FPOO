import random

contador = 0
lista = []
repetidos = []
revisados = []

for i in range(0,30):
    numero = random.randint(10,21)
    lista.append(numero)
print(f"La lista generada es:\n{lista}")

while True:
    print("\n------------------------------------------------------")
    print("1. Contar números repetidos\n2. Eliminar números repetidos\n3. Reemplazar números repetidos con 0\n4. Salir")
    print("------------------------------------------------------")
    option = int(input("Seleccione una opción: "))
    if option == 4:
        break
    
    match option:
        case 1:
            contador = 0
            for i in lista:
                if i not in revisados:
                    revisados.append(i)
                else:
                    repetidos.append(i)
                    contador += 1
            print(f"Existen un total de {contador} numeros repetidos, los cuales son: {repetidos}")
            repetidos = []
            revisados = []
            
        case 2:
            repetidosEliminados = list(set(lista))
            print(f"La lista sin números repetidos es: {repetidosEliminados}")
            
        case 3:
            repetidosCero = lista
            contador = 0
            for i in repetidosCero:
                if i not in revisados:
                    revisados.append(i)
                    contador += 1
                else:
                    repetidosCero[contador] = 0
                    contador += 1
            revisados = []
            print(f"La lista con los números repetidos convertidos en cero es: {repetidosCero}")