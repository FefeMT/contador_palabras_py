#    // Paso 1: Solicitar entrada alusuario

palabra_ingresada = input("\nIngrese una palabra: ")
palabra_ingresada = palabra_ingresada.strip()
#    // Paso 2: Contar cantidad de letras

cantidad_letras = len(palabra_ingresada)

#    // Paso 3: Mostrar el resultado

print(f"\nLa palabra {palabra_ingresada} tiene {cantidad_letras} de letras.\n")