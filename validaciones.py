def validar_numero(texto: str, valor_minimo:float) -> bool:
    """Valida que una cadena represente un número mayor o igual
    al valor mínimo indicado.

    La función admite números enteros y decimales con un único
    punto decimal.

    Args:
        texto (str): Cadena a validar.
        valor_minimo (float): Límite inferior permitido.

    Returns:
        bool: True si la cadena representa un número válido mayor
        o igual al mínimo indicado. False en caso contrario.
    """
    retorno = False
    es_numero = True
    cantidad_puntos = 0

    for c in texto:

        if c == ".":
            cantidad_puntos += 1

        if not ("0" <= c <= "9") and c != ".":
            es_numero = False

    if cantidad_puntos > 1:
        es_numero = False

    if es_numero:

        numero = float(texto)

        if numero >= valor_minimo:
            retorno = True
        else:
            print(f"ERROR: El número debe ser mayor o igual a {valor_minimo}.")

    else:
        print("ERROR: Debe ingresar un número válido.")

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

def validar_opcion(opcion:str) -> bool:
    """Valida que la opción ingresada por el usuario sea un número 
    dentro del rango permitido para el menú (del 1 al 9).

    Args:
        opcion (str): Cadena de texto que representa la opción ingresada.

    Returns: bool: True si la opción es válida y está dentro del rango [1, 9], 
             False en caso contrario.
    """

    retorno = True

    if validar_numero(opcion,1) == False:
        retorno = False

    elif float(opcion) > 9:
        retorno = False

    return retorno

