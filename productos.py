from inputs import (
    pedir_informacion_producto
)

from output import(
    mostrar_producto
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










# buscar_producto()
# modificar_producto()
# eliminar_producto()