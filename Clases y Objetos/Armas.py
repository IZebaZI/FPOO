class Armas:
    def seleccionarArma(self, nombre):
        seleccion = int(input("Selecciona un arma:\n 1. Rifle de asalto\n 2. Espada de Energía\n 3. Rifle M392\n"))
        if(seleccion == 1):
            print("Rifle de asalto asignado a " + nombre)
            print("Municiones 7.62 * 52mm, sin mira")
            
        if(seleccion == 2):
            print("Espada de energía asignada a " + nombre)
            print("Arma creada por los Sangheili")
            
        if(seleccion == 3):
            print("Rifle M392 asignada a " + nombre)
            print("Municiones 7.62 * 52mm, con mira")
            
    def recargarArma(self, municion):
        cargador = 25
        cargador = cargador + municion
        print("Arma recargada, capacidad: " + str(cargador) + "%")

