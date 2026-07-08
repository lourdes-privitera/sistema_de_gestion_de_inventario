from validaciones import (
    validar_opcion
)
from productos import (
    registrar_producto,
    listar_productos,  
    buscar_productos_por_categoria,
    modificar_producto,
    eliminar_producto  
)
from output import (
    mostrar_menu,
    mostrar_busqueda_producto,
    mostrar_productos_categoria,
    mostrar_estadisticas    
)
from archivos import(
    cargar_inventario,
    guardar_inventario
)

def ejecutar_sistema() -> None:

    inventario = cargar_inventario("inventario.json")

    programa_activo = True  

    while programa_activo:

        mostrar_menu()
       
        opcion= input("Seleccionar opcion: ")
        
        while validar_opcion(opcion) == False :
            opcion = input("Reingrese una opcion valida: ")
        opcion = int(opcion)
                   
        if opcion == 1:
            inventario= registrar_producto(inventario)
            guardar_inventario("inventario.json", inventario)                                             
           
        elif opcion == 2:
            listar_productos(inventario)
            
        elif opcion == 3:
            codigo = input("Ingrese el código del producto que busca: ")
            mostrar_busqueda_producto(codigo,inventario)

        elif opcion == 4:
            categoria = input("Ingrese categoria buscada : ")
            productos = buscar_productos_por_categoria(inventario, categoria)
            mostrar_productos_categoria(productos)
                
        elif opcion == 5:
            modificar_producto(inventario)
            guardar_inventario("inventario.json", inventario)

        elif opcion == 6:
            eliminar_producto(inventario)
            guardar_inventario("inventario.json", inventario)

        elif opcion == 7:
            mostrar_estadisticas(inventario)

        elif opcion == 8:
            print("SALIENDO...")
            programa_activo = False 
            
        if programa_activo:
            input("\nPresione Enter para continuar...")