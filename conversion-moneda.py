#Paso 1: Definir el valor del Euro y Dolar en respecto al Peso

tipo_cambio_eur_pes = 23.70
tipo_cambio_usd_pes = 20.75

# Paso 2: Solicitar al usuario el tipo de conversión (Euro a Peso o Dolar a Peso)

moneda = input("Ingrese la moneda origen para convertir (EUR/USD): ")
while moneda != "EUR" and moneda != "USD":
    moneda = input("Ingrese la moneda origen para convertir (EUR/USD): ")
    moneda = moneda.upper()

# Paso 3: Solicitar monto a convertir

monto = input("Ingrese el monto a convertir: ")
while type(monto) is not float:
    try:
        monto = float(monto)
    except ValueError:
        monto = input("Ingrese el monto a convertir de forma numerica: ")

# Paso 4: Realizar la conversiòn
    
if moneda == "EUR":
    total = monto * tipo_cambio_eur_pes
else:
    total = monto * tipo_cambio_usd_pes

# Paso 5: Mostrar el resultado
    
print(f"\n${monto} " + moneda + f" = ${total} Pesos.\n")