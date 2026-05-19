def es_letra(caracter: str) -> bool:
    """
    Determina si un caracter es una letra (mayuscula o minuscula), mediante comparacion directa de codigos ASCII.

    Args:
        caracter(str): caracter a procesar.
    
    Return:
        bool: True si el caracter es letra, False si no.
    """
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')


def es_numero(caracter: str) -> bool:
    """
    Determina si un caracter es un digito numerico, mediante comparacion directa de codigos ASCII.

    Args:
        caracter(str): caracter a procesar.

    Return:
        bool: True si el caracter es digito numerico, False si no.
    """
    return '0' <= caracter <= '9'


def es_simbolo(caracter: str) -> bool:
    """
    Determina si un caracter pertenece al grupo de simbolos admitidos:
    ! " # $ % & ' ( ) * + , - . /

    Args:
        caracter(str): caracter a procesar.

    Return:
        bool: True si el caracter es un simbolo admitido, False si no.
    """
    simbolos = '!"#$%&\'()*+,-./'
    for i in range(len(simbolos)):
        if caracter == simbolos[i]:
            return True
    return False

def agregar_a_lista(lista: list, elemento: any) -> None:
    """
    Agrega un elemento al final de una lista.

    Args:
        lista(list): lista a la cual se le agrega el elemento.
        elemento(any): Elemento a agregar.
    
    Return:
        None
    """
    lista += [elemento]

def mostrar_lista(lista: list) -> None:
    """
    Recibe una lista y la muestra por consola
    
    Args:
        lista(list): lista a mostrar
    
    Return:
        None
    """
    for i in range(len(lista)):
        print("-", lista[i], end=" ")
        print("")
