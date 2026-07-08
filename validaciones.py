def validar_entero(texto: str, valor_minimo:int) -> bool:
    """Valida que una cadena represente un número entero mayor o igual
    al valor mínimo indicado.

    Args:
        texto (str): Cadena a validar.
        valor_minimo (int): Límite inferior permitido.
        
    Returns:
        bool: True si el texto es un entero dentro del rango, False en caso contrario.
    """
    retorno = False
    es_entero = True
        
    for c in texto: # Validar que todos los caracteres sean dígitos numericos
        if not ("0" <= c <= "9"):
            es_entero = False
   
    if es_entero:  # Si es entero, validamos el rango numérico
        numero = int(texto)

        if valor_minimo <= numero :
            retorno = True
        else:
            print(f"NO SE ADMITEN NEGATIVOS.")

    else:
        print("SE DEBE INGRESAR UN NUMERO ENTERO")

    return retorno

def validar_longitud_minima(cadena:str,minimo:int) -> bool:
    """Valida que una cadena tenga una longitud minima determinada.

    Args:
        cadena (str): Cadena a validar.
        minimo (int): Cantidad mínima de caracteres requerida.

    Returns:
        bool: True si la longitud de la cadena es mayor o igual al mínimo indicado,
        False en caso contrario.
    """

    retorno = False

    if len(cadena) >= minimo :
        retorno = True

    return retorno

