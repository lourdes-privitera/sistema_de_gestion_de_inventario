from utilidades import(
    obtener_estado,
    buscar_producto
)

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


#la reutilizo para todas las opciones que muestran producto (solo imprime 1 producto)
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

def mostrar_busqueda_producto(codigo:str,inventario:dict) -> None:
    """Busca un producto y muestra su información."""

    producto = buscar_producto(inventario, codigo)

    if producto != None:
        mostrar_producto(codigo, producto)
    else:
        print("Producto inexistente.")

def mostrar_productos_categoria(productos:dict) -> None:

    if len(productos) == 0:

        print("No existen productos registrados en esa categoría.")

    else:

        for codigo, producto in productos.items():

            mostrar_producto(codigo, producto)

            print("------------------------")

