from utilidades import(
    obtener_estado,
    buscar_producto
)
from estadisticas import(
    cantidad_productos,
    valor_total_inventario,
    precio_promedio,
    producto_mas_caro,
    producto_mayor_stock,
    cantidad_sin_stock,
    cantidad_stock_bajo,
    cantidad_por_categoria,
    porcentaje_stock_bajo
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

def mostrar_producto(codigo:str, producto:dict) -> None:
    """Imprime en consola los datos detallados de un producto específico,
    incluyendo el estado de su stock calculado.

    Args:
        codigo (str): Código único del producto.
        producto (dict): Diccionario con las propiedades del producto 
                         (nombre, categoría, precio, etc.).
    """

    estado = obtener_estado( producto["stock_disponible"],producto["stock_minimo"])

    print(f"Código: {codigo}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoría: {producto['categoria']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock_disponible']}")
    print(f"Stock mínimo: {producto['stock_minimo']}")
    print(f"Proveedor: {producto['proveedor']}")
    print(f"Estado: {estado}\n")

def mostrar_busqueda_producto(codigo:str,inventario:dict) -> None:
    """Busca un producto por su código dentro del inventario. Si lo encuentra,
    muestra su información; de lo contrario, advierte que no existe.

    Args:
        codigo (str): Código del producto que se desea buscar.
        inventario (dict): Inventario completo donde se realizará la búsqueda.
    """

    producto = buscar_producto(inventario, codigo)

    if producto != None:
        mostrar_producto(codigo, producto)
    else:
        print("Producto inexistente.")

def mostrar_productos_categoria(productos:dict) -> None:
    """Recorre y muestra todos los productos que pertenecen a una categoría 
    filtrada previamente. Si el diccionario está vacío, informa la situación.

    Args:
        productos (dict): Diccionario filtrado que contiene únicamente los 
                          productos de la categoría seleccionada.
    """

    if len(productos) == 0:

        print("No existen productos registrados en esa categoría.")

    else:

        for codigo, producto in productos.items():

            mostrar_producto(codigo, producto)

            print("------------------------")

def mostrar_estadisticas(inventario:dict) -> None:
    """Consolida, procesa y despliega de forma visual en la consola todo el
    set de métricas, totales, máximos y porcentajes calculados sobre el inventario.

    Args:
        inventario (dict): Inventario completo utilizado para extraer las métricas.
    """

    total_productos = cantidad_productos(inventario)
    total_inventario = valor_total_inventario(inventario)
    promedio = precio_promedio(inventario)
    cod_caro, prod_caro = producto_mas_caro(inventario)
    cod_stock, prod_stock = producto_mayor_stock(inventario)
    sin_stock = cantidad_sin_stock(inventario)
    stock_bajo = cantidad_stock_bajo(inventario)
    categorias = cantidad_por_categoria(inventario)
    porcentaje_bajo_stock = porcentaje_stock_bajo(inventario)

    print("=========== ESTADISTICAS ===========") 

    print(f"cantidad total de productos: {total_productos}\n")  
    print(f"valor total del inventario: {total_inventario}\n")
    print(f"precio promedio de los productos: {promedio}\n")
    print(f"producto más caro:") 
    mostrar_producto(cod_caro, prod_caro)
    print(f"\nproducto con mayor cantidad de stock:")
    mostrar_producto(cod_stock, prod_stock)
    print(f"\ncantidad de productos sin stock:{sin_stock}\n")
    print(f"cantidad de productos con stock bajo:{stock_bajo}") 
    for categoria, cantidad in categorias.items():
        print(f"{categoria}: {cantidad}")
    print(f"\nporcentaje de productos con stock bajo respecto del total:{porcentaje_bajo_stock}\n")
