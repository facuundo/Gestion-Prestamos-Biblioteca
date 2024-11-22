from funciones_json import *

#TODO: separar en varios archivos de funciones -> LISTO
#TODO: ACA VA FUNCIONES MENU - HACER FUNCIONES TIME


def menu(nombre):
#función para imprimir cada menu
    print(" ")
    print(f"¡Bienvenido al menú de {nombre}!")
    print(" ")
    print("Elija una opción: ")

def obtener_siguiente_id(ruta_archivo):
    datos = abrir_archivo(ruta_archivo)
    if not datos:
        return 1
    max_id = max(dato['id'] for dato in datos)
    return max_id + 1

