import json
import os 

def cargar_inventario(nombre_archivo:str) -> dict:
    """Carga el inventario desde un archivo JSON.

    Si el archivo no existe, devuelve un diccionario vacío.

    Args:
        nombre_archivo (str): Nombre del archivo.

    Returns:
        dict: Inventario cargado.
    """

    if os.path.exists(nombre_archivo): #para no usar try/except que esta prohibido

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            inventario = json.load(archivo)

    else:

        inventario = {}

    return inventario

def guardar_inventario(nombre_archivo:str, inventario:dict) -> None:
    """Guarda el inventario en un archivo JSON.

    Args:
        nombre_archivo (str): Nombre del archivo.
        inventario (dict): Inventario a guardar.
    """

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:

        json.dump(inventario, archivo, indent=4)

