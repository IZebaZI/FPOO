from Usuario import *

print("Bienvenido al sistema de registro de usuarios")
listaUsuarios = []
while True:
    print("Por favor, selecciona una opción:")
    print("1. Registrar usuario")
    print("2. Consultar usuario")
    print("3. Editar Usuario")
    print("4. Borrar Usuario")
    print("5. Salir")
    print("------------------------------------")
    option = int(input("Opción: "))
    print("------------------------------------")
    if option == 5:
        print("Gracias por utilizar el sistema, vuelva pronto!")
        break
    match option:
        case 1:
            print("La opcion seleccionada es: Registrar usuario")
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            apellidoP = input("Apellido Paterno: ")
            apellidoM = input("Apellido Materno: ")
            correo = input("Correo: ")
            password = input("Contraseña: ")
            usuario = Usuario(id, nombre, apellidoP, apellidoM, correo, password)
            listaUsuarios.append(usuario)
            print("------------------------------------")
            print("Usuario registrado exitosamente con los datos:")
            usuario.printInfo()
            usuario = None
            print("------------------------------------")
        
        case 2:
            print("La opcion seleccionada es: Consultar usuario")
            if not listaUsuarios:
                print("No hay usuarios registrados")
                print("------------------------------------")
            else:
                id = int(input("ID: "))
                usuarioEncontrado = False
                for usuario in listaUsuarios:
                    if usuario.getId() == id:
                        print("------------------------------------")
                        print("Información del usuario:")
                        usuario.printInfo()
                        usuarioEncontrado = True
                        print("------------------------------------")
                if usuarioEncontrado == False:
                    print("No se encontró el usuario, verifica el ID ingresado")
                    print("------------------------------------")
            
        case 3:
            print("La opcion seleccionada es: Editar Usuario")
            if not listaUsuarios:
                print("No hay usuarios registrados")
            else:
                id = int(input("ID: "))
                usuarioEncontrado = False
                for usuario in listaUsuarios:
                    if usuario.getId() == id:
                        usuarioEncontrado = True
                        print("------------------------------------")
                        print("Información del usuario:")
                        usuario.printInfo()
                        while True:
                            print("------------------------------------")
                            print("Seleccione el atributo a modificar:")
                            print("1. Nombre")
                            print("2. Correo")
                            print("3. Contraseña")
                            print("4. Salir")
                            print("------------------------------------")
                            select = int(input("Opción: "))
                            if select == 4:
                                break
                            match select:
                                case 1:
                                    print("Ingresa los datos del usuario:")
                                    nombre = input("Nombre: ")
                                    apellidoP = input("Apellido Paterno: ")
                                    apellidoM = input("Apellido Materno: ")
                                    usuario.setNombre(nombre, apellidoP, apellidoM)
                                    print("------------------------------------")
                                    print("Se ha actualizado la información del usuario:")
                                    usuario.printInfo()
                                    print("------------------------------------")
                                
                                case 2:
                                    print("Ingresa los datos del usuario:")
                                    correo = input("Correo: ")
                                    usuario.setCorreo(correo)
                                    print("------------------------------------")
                                    print("Se ha actualizado la información del usuario:")
                                    usuario.printInfo()
                                    print("------------------------------------")
                                
                                case 3:
                                    print("Ingresa el correo registrado:")
                                    correo = input("Correo: ")
                                    print("Ingresa la nueva contraseña:")
                                    password = input("Contraseña: ")
                                    estado = usuario.changePassword(correo, password)
                                    if estado == True:
                                        print("------------------------------------")
                                        print("Se ha actualizado la información del usuario")
                                        usuario.printInfo()
                                    else:
                                        print("------------------------------------")
                                        print("El correo ingresado no coincide con el registrado")
                                    print("------------------------------------")
                if usuarioEncontrado == False:
                    print("No se encontró el usuario, verifica el ID ingresado")
                    print("------------------------------------")
        
        case 4:
            id = int(input("ID: "))
            usuarioEncontrado = False
            for usuario in listaUsuarios:
                if usuario.getId() == id:
                    usuario.borrarUsuario()
                    print("Se ha eliminado la información del usuario")
                    usuarioEncontrado = True
                    print("------------------------------------")
            if usuarioEncontrado == False:
                print("No se encontró el usuario, verifica el ID ingresado")
                print("------------------------------------")