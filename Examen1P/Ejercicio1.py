palabra1 = str(input("Ingresa una palabra: "))
palabra2 = str(input("Ingresa otra palabra: "))

longitud1 = len(palabra1)
longitud2 = len(palabra2)

if longitud1 > longitud2:
    diferencia = int(longitud1) - int(longitud2)
    print(f"La primer palabra '{palabra1}' es más larga por: {diferencia} letras")
elif longitud2 > longitud1:
    diferencia = int(longitud2) - int(longitud1)
    print(f"La segunda palabra '{palabra2}' es más larga por: {diferencia} letras")
else:
    print(f"Ambas palabras tienen la misma longitud")