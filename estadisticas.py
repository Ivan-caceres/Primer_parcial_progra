from utilidades import es_letra, es_numero, es_simbolo

def generar_reporte(contraseña: str) -> None:
    """
    Calcula longitudes, porcentajes y procesa repeticiones de caracteres de forma consecutiva.
    """
    largo = len(contraseña)
    letras = 0
    numeros = 0
    simbolos = 0
    
    for i in range(largo):
        char = contraseña[i]
        if es_letra(char):
            letras += 1
        elif es_numero(char):
            numeros += 1
        elif es_simbolo(char):
            simbolos += 1
            
    porc_letras = (letras / largo) * 100
    porc_numeros = (numeros / largo) * 100
    porc_simbolos = (simbolos / largo) * 100
    
    print("📊📊📊 REPORTE ESTADÍSTICO 📊📊📊")
    print(f"-Longitud total: {largo} caracteres")
    print(f"-Porcentaje de letras: {porc_letras:.2f}%")
    print(f"-Porcentaje de números: {porc_numeros:.2f}%")
    print(f"-Porcentaje de símbolos: {porc_simbolos:.2f}%")
    print("\n🔂Análisis de repeticiones consecutivas🔂:")
    print(" ")
    
    # Algoritmo Run-Length adaptado para cumplir el formato del enunciado
    i = 0
    hubo_repeticiones = False
    while i < largo:
        caracter_actual = contraseña[i]
        cuenta = 1
        
        while i + 1 < largo and contraseña[i + 1] == caracter_actual:
            cuenta += 1
            i += 1
            
        if cuenta > 1:
            repeticiones = cuenta - 1
            print(f"-{repeticiones} repetición/es de '{caracter_actual}'")
            hubo_repeticiones = True
        i += 1
        
    if not hubo_repeticiones:
        print("❌No se encontraron caracteres repetidos consecutivos.❌")