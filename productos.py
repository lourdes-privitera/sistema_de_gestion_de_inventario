from inputs import (
    pedir_informacion_producto,
    ingresar_nombre,
    ingresar_categoria,
    ingresar_precio,
    ingresar_stock_disponible,
    ingresar_stock_minimo,
    ingresar_proveedor
)

from output import(
    mostrar_producto
)
from utilidades import(
    buscar_producto
)

def registrar_producto(inventario:dict) -> dict:
    """Registra un nuevo producto en el inventario.

    Solicita la información del producto y la incorpora al
    inventario utilizando el código como clave.

    Args:
        inventario (dict): Inventario actual.

    Returns:
        dict: Inventario actualizado.
    """

    codigo, informacion_producto = pedir_informacion_producto(inventario)

    inventario[codigo] = informacion_producto #desenpaqueto

    return inventario

def listar_productos(inventario:dict) -> None:
    """Muestra todos los productos registrados.

    Args:
        inventario (dict): Diccionario con todos los productos.
    """

    print("\n========== INVENTARIO ==========\n")

    for codigo, producto in inventario.items():

        mostrar_producto(codigo, producto)

        print("--------------------------------")

def buscar_productos_por_categoria(inventario:dict, categoria:str) -> dict:
    """Busca todos los productos pertenecientes a una categoría.

    Args:
        inventario (dict): Inventario de productos.
        categoria (str): Categoría buscada.

    Returns:
        dict: Productos encontrados dentro de la categoría.
    """

    productos_encontrados = {}

    for codigo, producto in inventario.items():

        if producto["categoria"] == categoria:
            productos_encontrados[codigo] = producto #lo agregamos 

    return productos_encontrados

def modificar_producto(inventario:dict) -> None:
    """Modifica los datos de un producto existente.

    Solicita el código del producto, verifica que exista
    y permite actualizar todos sus datos.

    Args:
        inventario (dict): Diccionario que contiene los productos.
    """

    codigo = input("Ingrese el código del producto: ")

    producto = buscar_producto(inventario, codigo)

    if producto != None:

        producto.update({
            "nombre": ingresar_nombre(),
            "categoria": ingresar_categoria(),
            "precio": ingresar_precio(),
            "stock_disponible": ingresar_stock_disponible(),
            "stock_minimo": ingresar_stock_minimo(),
            "proveedor": ingresar_proveedor()
        })

        print("Producto modificado correctamente.")

    else:
        print("Producto inexistente.")

def eliminar_producto(inventario:dict) -> None:
    """Elimina un producto del inventario.

    Solicita el código del producto y, si existe,
    pide confirmación antes de eliminarlo.

    Args:
        inventario (dict): Diccionario que contiene los productos.
    """

    codigo = input("Ingrese el código del producto: ")

    if codigo in inventario:

        confirmar = input("¿Eliminar producto? (s/n): ")

        if confirmar == "s" or confirmar == "S" :

            inventario.pop(codigo)

            print("Producto eliminado.")

    else:

        print("Producto inexistente.")
