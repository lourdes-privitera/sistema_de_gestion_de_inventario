#(pertenece a productos.py) esta aca solo para evitar una importación circular entre productos.py y output.py 

def obtener_estado(stock:int,stock_minimo:int)-> str:
    """Determina el estado del stock de un producto.

    Args:
        stock (int): Cantidad disponible.
        stock_minimo (int): Stock mínimo permitido.

    Returns:
        str: Estado del producto.
    """

    if stock == 0:
        estado = "Sin Stock"
    elif stock <= stock_minimo:
       estado = "Stock Bajo"
    else : #stock > stock_minimo
       estado = "Stock Normal"

    return estado

#(pertenece a productos.py) esta aca solo para evitar una importación circular entre productos.py y output.py 

def buscar_producto(inventario:dict, codigo:str) -> dict:
    """Busca un producto por su código(clave).

    Args:
        inventario (dict): Inventario de productos.
        codigo (str): Código del producto a buscar.

    Returns:
        dict: Diccionario con la información del producto si existe.
        None: Si el código no se encuentra registrado.
    """

    producto = None

    if codigo in inventario:
        producto = inventario[codigo]

    return producto

