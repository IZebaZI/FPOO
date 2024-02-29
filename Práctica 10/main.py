from Usuario import *

print("Bienvenido al sistema de registro de usuarios")
print("Por favor, selecciona una opción:")
print("1. Registrar usuario")
print("2. Consultar usuario")
print("3. Editar Usuario")
print("4. Borrar Usuario")
print("5. Salir")
listaUsuarios = []
while True:
    option = int(input("Opción: "))
    if option == 5:
        break
    match option:
        case 1:
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            apellidoP = input("Apellido Paterno: ")
            apellidoM = input("Apellido Materno: ")
            correo = input("Correo: ")
            password = input("Contraseña: ")
            usuario = Usuario(id, nombre, apellidoP, apellidoM, correo, password)
            listaUsuarios.append(usuario)
            print("Usuario registrado")
        
        case 2:
            if not listaUsuarios:
                print("No hay usuarios registrados")
            else:
                id = int(input("ID: "))
                for usuario in listaUsuarios:
                    if usuario.getId() == id:
                        usuario.printInfo()
            
        case 3:
            if not listaUsuarios:
                print("No hay usuarios registrados")
            else:
                id = int(input("ID: "))
                for usuario in listaUsuarios:
                    if usuario.getId() == id:
                        print("Seleccione el atributo a modificar:")
                        print("1. Nombre")
                        print("2. Correo")
                        print("3. Contraseña")
                        print("4. Salir")
                        
                        while True:
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
                                    print("Se ha actualizado la información del usuario")
                                
                                case 2:
                                    print("Ingresa los datos del usuario:")
                                    correo = input("Correo: ")
                                    usuario.setCorreo(correo)
                                    print("Se ha actualizado la información del usuario")
                                
                                case 3:
                                    print("Ingresa los datos del usuario:")
                                    password = input("Contraseña: ")
                                    usuario.setPassword(password)
                                    print("Se ha actualizado la información del usuario")
        
        case 4:
            id = int(input("ID: "))
            for usuario in listaUsuarios:
                if usuario.getId() == id:
                    usuario.borrarUsuario()
                    print("Se ha eliminado la información del usuario:")