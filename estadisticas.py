def cantidad_productos(inventario:dict)->int:
    """Obtiene la cantidad total de productos registrados.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        int: Cantidad de productos.
    """
    return len(inventario)

def valor_total_inventario(inventario:dict)->float:
    """Calcula el valor total del inventario.

    Multiplica el precio por el stock de cada producto y
    acumula el resultado.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        float: Valor económico total del inventario.
    """

    acumulador = 0

    for producto in inventario.values():

        acumulador += producto["precio"] * producto["stock_disponible"]

    return acumulador

def precio_promedio(inventario:dict)->float:
    """Calcula el precio promedio de todos los productos.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        float: Precio promedio.
    """

    acumulador = 0

    for producto in inventario.values():

        acumulador += producto["precio"]
    
    cantidad = cantidad_productos(inventario)

    if cantidad > 0:

        promedio = acumulador / cantidad

    else:

        promedio = 0

    return promedio

def producto_mas_caro(inventario:dict)->dict:
    """Busca el producto con mayor precio comparando todos los valores uno por uno.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        tuple: Código y datos del producto más caro.
    """

    productos = list(inventario.items())

    codigo, producto = productos[0]

    for codigo_actual, producto_actual in inventario.items():

        if producto_actual["precio"] > producto["precio"]:

            codigo = codigo_actual
            producto = producto_actual

    return codigo, producto

def producto_mayor_stock(inventario:dict)->dict:
    """Busca el producto con mayor cantidad de stock comparando todos los valores uno por uno.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        tuple: Código y datos del producto con mayor stock.
    """

    productos = list(inventario.items())

    codigo, producto = productos[0]

    for codigo_actual, producto_actual in inventario.items():

        if producto_actual["stock_disponible"] > producto["stock_disponible"]:

            codigo = codigo_actual
            producto = producto_actual

    return codigo, producto

def cantidad_sin_stock(inventario:dict)->int:
    """Cuenta los productos sin stock disponible.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        int: Cantidad de productos sin stock.
    """

    contador = 0

    for producto in inventario.values():

        if producto["stock_disponible"] == 0:

            contador += 1

    return contador

def cantidad_stock_bajo(inventario:dict)->int:
    """Cuenta los productos cuyo stock es igual o menor
    al stock mínimo.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        int: Cantidad de productos con stock bajo.
    """

    contador = 0

    for producto in inventario.values():

        if (producto["stock_disponible"] > 0 and
            producto["stock_disponible"] <= producto["stock_minimo"]):

            contador += 1

    return contador

def cantidad_por_categoria(inventario:dict)->dict:
    """Cuenta la cantidad de productos de cada categoría.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        dict: Diccionario con categoría y cantidad.
    """

    categorias = {}

    for producto in inventario.values():

        categoria = producto["categoria"]

        if categoria in categorias:

            categorias[categoria] += 1

        else:

            categorias[categoria] = 1

    return categorias

def porcentaje_stock_bajo(inventario:dict)->float:
    """Calcula el porcentaje de productos con stock bajo.

    Args:
        inventario (dict): Inventario completo.

    Returns:
        float: Porcentaje de productos con stock bajo.
    """

    cantidad = cantidad_productos(inventario)

    if cantidad > 0:

        porcentaje = cantidad_stock_bajo(inventario) * 100 / cantidad

    else:

        porcentaje = 0

    return porcentaje
