from tkinter import *
from tkinter import messagebox
from cuenta import *

class View:
    def createView(self):
        listaCuentas = []
        window = Tk()
        window.title("Administrador de Cuentas")
        window.geometry("450x350")
        
        # Funciones
        def crearCuenta():
            if numero != "" and titular != "" and edad != "" and saldo != "":
                cuenta = Cuenta(numero.get(), titular.get(), edad.get(), saldo.get())
                listaCuentas.append(cuenta)
                print(messagebox.showinfo('Crear Usuario', 'El usuario fue ingresado exitosamente'))
            else:
                print(messagebox.showerror('Crear Usuario', 'El usuario no fue agregado, completa toda la información'))
        
        def ingresarEfectivo():
            cuentaEncontrada = False
            for cuenta in listaCuentas:
                if cuenta.getNumero() == numCuenta.get():
                    cuenta.ingresarEfectivo(efectivo.get())
                    print(messagebox.showinfo('Ingresar Efectivo', 'Saldo agregado exitosamente\n El saldo actual es: ' + cuenta.mostrarSaldo()))
                    cuentaEncontrada = True
            if cuentaEncontrada == False:
                print(messagebox.showerror('Ingresar Efectivo', 'No se encontró la cuenta especificada'))
                
        
        def retirarEfectivo():
            cuentaEncontrada = False
            for cuenta in listaCuentas:
                if cuenta.getNumero() == numCuenta.get() and cuenta.getSaldo() >= int(efectivo.get()):
                    cuenta.retirarEfectivo(efectivo.get())
                    print(messagebox.showinfo('Retirar Efectivo', 'Saldo retirado exitosamente\n El saldo actual es: $' + cuenta.mostrarSaldo()))
                    cuentaEncontrada = True
            if cuentaEncontrada == False:
                print(messagebox.showerror('Ingresar Efectivo', 'No se encontró la cuenta especificada o no cuenta con saldo disponible'))
        
        def mostrarInformacion():
            cuentaEncontrada = False
            for cuenta in listaCuentas:
                if cuenta.getNumero() == numCuenta.get():
                    datos = cuenta.mostrarDatos()
                    print(messagebox.showinfo('Mostrar Datos', datos))
                    cuentaEncontrada = True
            if cuentaEncontrada == False:
                print(messagebox.showerror('Mostrar Datos', 'No se encontró la cuenta especificada'))
        
        def mostrarSaldo():
            cuentaEncontrada = False
            for cuenta in listaCuentas:
                if cuenta.getNumero() == numCuenta.get():
                    saldo = cuenta.mostrarSaldo()
                    print(messagebox.showinfo('Mostrar Saldo', 'El saldo actual de la cuenta: "' + cuenta.getNumero() + '" es: $' + saldo))
                    cuentaEncontrada = True
            if cuentaEncontrada == False:
                print(messagebox.showerror('Mostrar Saldo', 'No se encontró la cuenta especificada'))
        
        def depositarCuentas():
            origenEncontrado = False
            destinoEncontrado = False
            for cuenta in listaCuentas:
                if cuenta.getNumero() == cuentaOrigen.get() and cuenta.getSaldo() >= int(deposito.get()):
                    origenEncontrado = True
            for cuenta in listaCuentas:
                if cuenta.getNumero() == cuentaDestino.get():
                    destinoEncontrado = True
            if origenEncontrado == True and destinoEncontrado == True:
                for cuenta in listaCuentas:
                    if cuenta.getNumero() == cuentaOrigen.get():
                        cuenta.retirarEfectivo(deposito.get())
                for cuenta in listaCuentas:
                    if cuenta.getNumero() == cuentaDestino.get():
                        cuenta.ingresarEfectivo(deposito.get())
                print(messagebox.showinfo('Transferencia de Efectivo', 'Transferencia realizada correctamente'))
            elif origenEncontrado == False:
                print(messagebox.showerror('Transferencia de Efectivo', 'No se encontró la cuenta de origen o no cuenta con el saldo necesario'))
            elif destinoEncontrado == False:
                print(messagebox.showerror('Transferencia de Efectivo', 'No se encontró la cuenta de destino'))
            else:
                print(messagebox.showerror('Transferencia de Efectivo', 'No se encontró la cuenta de origen y destino'))
        
        
        # Interfaz
        titles = Frame(window, bg="lightblue")
        titles.pack(expand = True, fill="both")
        
        labelCrear = Label(titles, text="Crear Usuario", font=("Lexend", 16, "bold"))
        labelCrear.grid(column=1, row=0, pady=(0,10), padx=(5,5))
        
        labelConsultar = Label(titles, text="Consultar", font=("Lexend", 16, "bold"))
        labelConsultar.grid(column=2, row=0, pady=(0,10), padx=(10,5))
        
        labelTransferir= Label(titles, text="Transferir", font=("Lexend", 16, "bold"))
        labelTransferir.grid(column=3, row=0, pady=(0,10), padx=(35,0))
        
        seccion = Frame(window, bg="lightblue")
        seccion.pack(expand = True, fill="both")
        
        numero = StringVar()
        labelNumero = Label(seccion, text="Número: ")
        labelNumero.grid(column=1, row=0, padx = (10, 10))
        inputNumero = Entry(seccion, textvariable=numero)
        inputNumero.grid(column=1, row=1, padx = (10, 10))
        
        titular = StringVar()
        labelTitular = Label(seccion, text="Titular: ")
        labelTitular.grid(column=1, row=2, padx = (10, 10), pady=(10,0))
        inputTitular = Entry(seccion, textvariable=titular)
        inputTitular.grid(column=1, row=3, padx = (10, 10))
        
        edad = StringVar()
        labelEdad = Label(seccion, text="Edad: ")
        labelEdad.grid(column=1, row=4, padx = (10, 10))
        inputEdad = Entry(seccion, textvariable=edad)
        inputEdad.grid(column=1, row=5, padx = (10, 10))
        
        saldo = StringVar()
        labelSaldo = Label(seccion, text="Saldo: ")
        labelSaldo.grid(column=1, row=6, padx = (10, 10))
        inputSaldo = Entry(seccion, textvariable=saldo)
        inputSaldo.grid(column=1, row=7, padx = (10, 10))
        
        numCuenta = StringVar()
        labelCuenta = Label(seccion, text="No. Cuenta: ")
        labelCuenta.grid(column=2, row=0, padx = (10, 10))
        inputCuenta = Entry(seccion, textvariable=numCuenta)
        inputCuenta.grid(column=2, row=1, padx = (10, 10))
        
        efectivo = StringVar()
        labelEfectivo = Label(seccion, text="Efectivo: ")
        labelEfectivo.grid(column=2, row=2, padx = (10, 10), pady=(10,0))
        inputEfectivo = Entry(seccion, textvariable=efectivo)
        inputEfectivo.grid(column=2, row=3, padx = (10, 10))
        
        cuentaOrigen = StringVar()
        labelOrigen = Label(seccion, text="No. Cuenta Origen: ")
        labelOrigen.grid(column=3, row=0, padx = (10, 10))
        inputOrigen = Entry(seccion, textvariable=cuentaOrigen)
        inputOrigen.grid(column=3, row=1, padx = (10, 10))
        
        cuentaDestino = StringVar()
        labelDestino = Label(seccion, text="No. Cuenta Destino: ")
        labelDestino.grid(column=3, row=2, padx = (10, 10), pady=(10,0))
        inputDestino = Entry(seccion, textvariable=cuentaDestino)
        inputDestino.grid(column=3, row=3, padx = (10, 10))
        
        deposito = StringVar()
        labelEfectivo = Label(seccion, text="Efectivo: ")
        labelEfectivo.grid(column=3, row=4, padx = (10, 10))
        inputEfectivo = Entry(seccion, textvariable=deposito)
        inputEfectivo.grid(column=3, row=5, padx = (10, 10))
        
        # Botones
        btnCrearCuenta = Button(seccion, text = "Generar", command = crearCuenta)
        btnCrearCuenta.grid(column=1, row=8, pady = (0, 10))
        
        btnMostrarInformacion = Button(seccion, text = "Mostrar Información", command = mostrarInformacion)
        btnMostrarInformacion.grid(column=2, row=4, pady = (10, 10))
        
        btnIngresarEfectivo = Button(seccion, text = "Ingresar Efectivo", command = ingresarEfectivo)
        btnIngresarEfectivo.grid(column=2, row=5, pady = (0, 10))
        
        btnRetirarEfectivo = Button(seccion, text = "Retirar Efectivo", command = retirarEfectivo)
        btnRetirarEfectivo.grid(column=2, row=6, pady = (0, 10))
        
        btnMostrarSaldo = Button(seccion, text = "Mostrar Saldo", command = mostrarSaldo)
        btnMostrarSaldo.grid(column=2, row=7, pady = (0, 10))
        
        btnTransferencia = Button(seccion, text = "Realizar Transferencia", command = depositarCuentas)
        btnTransferencia.grid(column=3, row=6, pady = (0, 10))
        
        window.mainloop()

view = View()
view.createView()