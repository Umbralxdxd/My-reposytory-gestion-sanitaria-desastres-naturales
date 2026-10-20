#Verificar si está asegurado el paciente
print("1. Consulta del paciente")
dni = input("Ingrese DNI del paciente: ")

#Leer el archivo TXT
with open("Asegurados.txt", "r") as archivo:
    asegurados = archivo.read().splitlines()

#Verificar si el DNI está registrado
encontrado = False

for asegurado in asegurados:
    datos = asegurado.split(";")

    if datos[0] == dni:
        encontrado = True
        print("El paciente ya está registrado")
        print("Nombre: ", datos[1])
        print("Edad: ", datos[2])
        print("Dirección: ", datos[3])
        print("Celular: ", datos[4])
        print("Celular familiar: ", datos[5])
#Si el DNI no fue encontrado, se registra
if encontrado == False:
    print("El paciente no está asegurado")
    print("Procederemos a registrar sus datos")
    nombre = input("Ingrese el nombre completo: ")
    edad = input("Ingrese su edad: ")
    direccion = input("Ingrese su direccion: ")
    celular = input("Ingrese el numero de celular: ")
    celular2 = input("Ingrese el numero de un familiar: ")

#Guardar los datos del paciente
    with open("SolicitudesN.txt","a") as archivo :
        archivo.write(f"{dni};{nombre};{edad};{direccion};{celular};{celular2}\n")
    print("Paciente registrado correctamente")

#Registrar el motivo de consulta
print("\n2 Motivo de consulta o visita")
motivo = input("Describa el motivo de consulta: ")

#Guardar la atención
with open("Motivos.txt","a") as archivo:
    archivo.write(f"{dni};{motivo}\n")

print("\n Atención registrada correctamente")