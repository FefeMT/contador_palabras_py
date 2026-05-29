#   Paso 1: Solicitar al usuario que ingrese la edad del cliente

edad = input("\nIngrese su edad: ")
while type(edad) is not int:
    try:
        edad = int(edad)
    except ValueError:
        edad = input("\nIngrese su edad en numeros: ")

#   Paso 2: Verificar si la edad es suficiente para entrar

if edad >= 18:
    print("\nPude entrar.\n")
else:
    print("\nNo pude entrar.\n")

#   Paso 3: Informarle al usuario el resultado