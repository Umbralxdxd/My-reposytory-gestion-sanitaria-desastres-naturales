#Verificar si está asegurado el paciente
print("1. Consulta del paciente")
dni = input("Ingrese DNI del paciente: ")

#Leer el archivo TXT
with open("Asegurados.txt", "r") as archivo :
    asegurados = archivo.read()

#Verificar si el DNI está registrado
if dni in asegurados:
    print("El paciente está asegurado. Aprieta cualquier tecla para continuar")
else:
    print("El paciente no está asegurado")
    print("Procederemos a registrar sus datos")
    nombre = input("Ingrese el nombre completo: ")
    edad = input("Ingrese su edad: ")
    direccion = input("Ingrese su direccion: ")
    celular = input("Ingrese el numero de celular: ")

#Guardar los datos del paciente
with open("Asegurados.txt","a") as archivo :
    archivo.write(f"{dni};{nombre};{edad};{direccion};{celular}\n")
print("Paciente registrado correctamente")