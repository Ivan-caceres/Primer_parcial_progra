from utilidades import es_letra

def validar_contraseña(contraseña: str) -> bool:
    """
    Valida que la contraseña no este vacia, que tenga 8 caracteres como minimo, no inicie con espacio y que tenga al menos una letra.

    Args:
        contraseña(str): contraseña a validar.

    Return:
        bool: True si la contraseña es valida, False si no.
    """
    if len(contraseña) == 0:
        print("🚨Error: La contraseña no puede estar vacía.🚨")
        return False
        
    if len(contraseña) < 8:
        print("🚨Error: La contraseña debe tener al menos 8 caracteres.🚨")
        return False
        
    if contraseña[0] == ' ':
        print("🚨Error: La contraseña no puede comenzar con espacios.🚨")
        return False
        
    tiene_letra = False
    for i in range(len(contraseña)):
        if es_letra(contraseña[i]):
            tiene_letra = True
            
    if not tiene_letra:
        print("🚨Error: La contraseña debe contener al menos una letra.🚨")
        return False
        
    return True