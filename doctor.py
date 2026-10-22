#Usuario del doctor
print("Interfaz del doctor")
usuario = input("Ingrese su usuario: ")
contra = input("Ingrese su contraseña: ")

if usuario == "JcarlosB" and contra == "1234":
    print("\n Acceso correcto")
    print("Bienvenido doctor Juan Carlos")
    print("1. Ver solicitudes de atención")
    print("2. Cerrar sesión")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("Abriendo solicitudes: ")
        with open("Motivos.txt","r") as archivo:
            solicitudes = archivo.readlines()
#Buscar la primera solicitud pendiente
        posicion = -1
        for i in range(len(solicitudes)):
            datos = solicitudes[i].strip().split(";")
            if len(datos) >= 3:
                if "ATENDIDO" not in datos[2]:
                    posicion = i
                    break
#Verificar si quedan solicitudes
        datos = solicitudes[posicion].strip().split(";")        
        print("Turno: ", datos[0])
        print("DNI: ", datos[1])
        print("Motivo de consulta: ", datos[2])
        respuesta = input("Presione enter una vez culminado de atender")
        with open("Recetas.txt","w") as archivo:
            archivo.write(f"{datos[1]};{respuesta}")
            print("Receta guardada correctamente.")
#Marcar la solicitud como atendida
        datos[2] = datos[2] + "ATENDIDO"
        solicitudes[posicion] = ";".join(datos) + "\n"
#Actualizar el archivo completo
        with open("Motivos.txt","w") as archivo:
            archivo.writelines(solicitudes)
        print("Solicitud marcada como ATENDIDO")
        
    elif opcion == "2":
        print("Sesión cerrada.")

else:
    print("\n Usuario o contraseña incorrecta")
    print("Acceso denegado")