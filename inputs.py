from validaciones import(
    validar_longitud_minima,
    validar_numero
)

def cargar_codigo (inventario:dict) -> str:
    """Solicita el código del producto y verifica que no exista previamente.

    Args:
        inventario (dict): Diccionario que contiene todos los productos
        registrados utilizando el código como clave.

    Returns:
        str: Código válido y no repetido.
    """

    codigo = input("Ingrese el código del producto: ")

    while codigo in inventario or validar_longitud_minima(codigo,1) == False:

        if validar_longitud_minima(codigo,1) == False:
            print("ERROR. El código no puede estar vacío.")
        else:
            print("ERROR. Ese código ya existe.")

        codigo = input("Reingrese código del producto: ")

    return codigo

def pedir_cadena(mensaje:str) -> str:
    """Solicita un texto y repite el ingreso hasta obtener un valor válido.
        -No puede estar vacío
        
    Args:
        mensaje (str): Mensaje mostrado al usuario para solicitar el dato.

    Returns:
        str: Texto validado ingresado por el usuario.
    """

    nombre = input(mensaje)

    while validar_longitud_minima(nombre,1) == False:
        print("INVALIDO")
        print("NO PUEDE ESTAR VACIO")
        nombre = input(mensaje)

    return nombre

def ingresar_nombre() -> str:
    """Solicita y valida el nombre del producto.

    Returns:
        str: Nombre del producto.
    """
    return pedir_cadena("Ingresar nombre del producto: ")

def ingresar_categoria() -> str:
    """Solicita y valida la categoria del producto.

    Returns:
        str: Categoria del producto.
    """
    return pedir_cadena("Ingresar categoria del producto: ")

def ingresar_proveedor() -> str:
    """Solicita y valida el proveedor del producto.

    Returns:
        str: Proovedor del producto.
    """
    return pedir_cadena("Ingresar provedoor del producto: ")

def pedir_numero(mensaje:str, minimo:float) -> float:
    """Solicita un número y repite el ingreso hasta obtener un valor válido.
        - Que el ingreso no esté vacío.
        - Que contenga solo caracteres numéricos.
        - Que se encuentre dentro del rango indicado(que no sea negativo).

    Args:
        mensaje (str): Texto que se mostrará al usuario para solicitar el dato.
        minimo (float): Valor mínimo permitido.

    Returns:
        int: Número validado dentro del rango especificado.
    """

    numero = input(mensaje)
    ingreso_valido = False

    while ingreso_valido == False:

        ingreso_valido = True

        if validar_longitud_minima(numero,1) == False:
            print("ERROR: NO PUEDE ESTAR VACÍO")
            ingreso_valido = False

        if ingreso_valido and validar_numero(numero,minimo) == False:
            ingreso_valido = False

        if ingreso_valido == False:
            numero = input("Reingrese un número válido: ")

    return float(numero)

def ingresar_precio() -> float:
    """Solicita el precio y lo valida.

    Returns:
        float: Precio del producto mayor a 0.
    """
    return pedir_numero("Ingrese el precio del producto: ", 1)

def ingresar_stock_disponible() -> int:
    """Solicita el precio y lo valida.

    Returns:
        float: Precio del producto mayor a 0.
    """
    return int(pedir_numero("Ingrese el Stock disponible del producto: ", 0))

def ingresar_stock_minimo() -> int:
    """Solicita el precio y lo valida.

    Returns:
        float: Precio del producto mayor a 0.
    """
    return int(pedir_numero("Ingrese el Stock mínimo del producto: ", 0))

def pedir_informacion_producto(inventario:dict) -> tuple:
    """Solicita todos los datos necesarios para registrar un producto.

    Primero obtiene un código único y luego solicita el resto de la
    información necesaria para construir el producto.

    Args:
        inventario (dict): Inventario actual utilizado para validar que
        el código no exista.

    Returns: tuple: Una tupla formada por:
            - codigo (str): Código único del producto.
            - informacion_producto (dict): Diccionario con los datos del producto.
    """

    codigo = cargar_codigo(inventario) #Pide el código / Verifica que no exista /Devuelve un código válido.

    informacion_producto = { #diccionario del producto
        "nombre": ingresar_nombre(),
        "categoria" : ingresar_categoria(),
        "precio" : ingresar_precio(),
        "stock_disponible" : ingresar_stock_disponible(),
        "stock_minimo" :ingresar_stock_minimo(),
        "proveedor" : ingresar_proveedor()      
    }

    return codigo, informacion_producto        