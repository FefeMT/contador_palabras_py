#Paso 1: Definir el valor de la pulgada en relacion a los centimetros

pulgada = 2.54

# Paso 2: Solicitar medidas a convertir

medida = input("\nIngrese la medida a convertir: ")
while type(medida) is not float:
    try:
        medida = float(medida)
    except ValueError:
        medida = input("Ingrese la medida a convertir de forma numerica: ")

# Paso 3: Realizar la conversiòn

resultado = medida/pulgada

# Paso 4: Mostrar el resultado

print("\nLa medida de la pieza en pulgadas es:", resultado, "pulgadas.\n")