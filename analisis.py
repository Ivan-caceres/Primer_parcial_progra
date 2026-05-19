from utilidades import es_letra, es_numero, es_simbolo, agregar_a_lista, mostrar_lista

def evaluar_seguridad(contraseña: str) -> str:
    """
    Analiza y devuelve el nivel de seguridad de la contraseña: Debil, Media o Fuerte.

    Args:
        contraseña(str): contraseña a evaluar.

    Return:
        str: Indicando si es Debil, Media o Fuerte.
    """
    largo = len(contraseña)
    solo_letras = True
    tiene_letras = False
    tiene_numeros = False
    tiene_simbolos = False
    
    for i in range(largo):
        caracter_validar = contraseña[i]
        if es_letra(caracter_validar):
            tiene_letras = True
        elif es_numero(caracter_validar):
            tiene_numeros = True
            solo_letras = False
        elif es_simbolo(caracter_validar):
            tiene_simbolos = True
            solo_letras = False
        else:
            solo_letras = False

    # Criterio Fuerte
    if largo >= 12 and tiene_letras and tiene_numeros and tiene_simbolos:
        return "Fuerte ✅✅✅"
        
    # Criterio Debil
    if 8 <= largo <= 9 and solo_letras:
        return "Debil ❌"
        
    # Criterio Media (por descarte si paso la validacion basica)
    return "Media ✅"


def contar_tipos(contraseña: str) -> None:
    """
    Muestra en consola el conteo detallado de caracteres.

    Args:
        contraseña(str): contraseña a evaluar.

    Return:
        None
    """
    letras = 0
    numeros = 0
    simbolos = 0
    espacios = 0
    
    for i in range(len(contraseña)):
        caracter_validar = contraseña[i]
        if es_letra(caracter_validar):
            letras += 1
        elif es_numero(caracter_validar):
            numeros += 1
        elif es_simbolo(caracter_validar):
            simbolos += 1
        elif caracter_validar == ' ':
            espacios += 1

    print("=="*26)
    print(" ")
    print("TIPOS DE CARACTERES ENCONTRADOS:")
    print(" ")       
    print(f"🔠 Cantidad de letras: {letras}")
    print(f"🔢 Cantidad de numeros: {numeros}")
    print(f"‼❗ Cantidad de simbolos: {simbolos}")
    print(f"⭕ Cantidad de espacios: {espacios}")


def buscar_caracter(contraseña: str, caracter: str) -> None:
    """
    Busca las ocurrencias e indices de un caracter especifico.
    
    Args:
        contraseña(str): contraseña donde se realizara la busqueda del caracter.
        caracter(str): caracter a buscar.
    Return:
        None
    """
    contador = 0
    posiciones = []
    
    for i in range(len(contraseña)):
        if contraseña[i] == caracter:
            contador += 1
            agregar_a_lista(posiciones, i)
    print("=="*26)        
    print(f"El caracter '{caracter}' aparece {contador} vez/veces.")
    if contador > 0:
        print("Posiciones de aparicion (indices): ")
        mostrar_lista(posiciones)


def invertir_contraseña(contraseña: str) -> str:
    """
    Invierte una cadena acumulando caracteres de atras hacia adelante.

    Args:
        contraseña(str): contraseña a invertir.
    
    Return:
        invertida(str): el resultado de invertir la contraseña
    """
    invertida = ""
    for i in range(len(contraseña)):
        invertida = contraseña[i] + invertida
    return invertida


def es_palindromo(contraseña: str) -> bool:
    """
    Determina si la contraseña es palindromo (se lee igual del derecho y del reves) comparando la cadena original con su inversión manual.

    Args:
        contraseña(str): contraseña a verificar palindromo.
    
    Return:
        bool: True en caso de verificarse el palindromo, False en caso contrario.
    """
    return contraseña == invertir_contraseña(contraseña)


def ordenar_caracteres(contraseña: str, ascendente: bool) -> str:
    """
    Ordena los caracteres según la tabla ASCII implementando el algoritmo Bubble Sort.

    Args:
        contraseña(str): contraseña a ordenar.
        ascendente(bool): indica con True si el orden elegido es ascendente o False si es descendente.
    
    Return:
        resultado(str): contraseña ordenada.
    """
    # Convertimos la string a una lista manualmente
    lista_caracteres = []
    for i in range(len(contraseña)):
        #lista_caracteres = lista_caracteres + [contraseña[i]]
        agregar_a_lista(lista_caracteres, contraseña[i])
    n = len(lista_caracteres)
    
    # Bubble Sort manual
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascendente:
                if lista_caracteres[j] > lista_caracteres[j + 1]:
                    aux = lista_caracteres[j]
                    lista_caracteres[j] = lista_caracteres[j + 1]
                    lista_caracteres[j + 1] = aux
            else:
                if lista_caracteres[j] < lista_caracteres[j + 1]:
                    aux = lista_caracteres[j]
                    lista_caracteres[j] = lista_caracteres[j + 1]
                    lista_caracteres[j + 1] = aux
                    
    # Reconstrucción de la string resultante
    resultado = ""
    for i in range(len(lista_caracteres)):
        resultado = resultado + lista_caracteres[i]
        
    return resultado