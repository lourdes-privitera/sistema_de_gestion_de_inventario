
def mostrar_menu() -> None:
    print("=========== GESTIÓN DE INVENTARIO ===========")  
    print("")    
    print("1.   Registrar producto")
    print("2.   Listado productos")
    print("3.   Buscar producto")
    print("4.   Buscar producto por categoría ")
    print("5.   Modificar producto ")
    print("6.   Eliminar producto")
    print("7.   Ver estadísticas")
    print("8.   Guardar producto")
    print("9.   Salir")

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

#la reutilizo para todas las opciones que muestran producto
def mostrar_producto(codigo:str, producto:dict) -> None:

    estado = obtener_estado( producto["stock_disponible"],producto["stock_minimo"])

    print(f"Código: {codigo}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoría: {producto['categoria']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock_disponible']}")
    print(f"Stock mínimo: {producto['stock_minimo']}")
    print(f"Proveedor: {producto['proveedor']}")
    print(f"Estado: {estado}")
