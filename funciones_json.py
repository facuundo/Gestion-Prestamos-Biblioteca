import json
import os

def crear_archivo(ruta_archivo):
    if os.path.exists(ruta_archivo) == True:
        return True
    archivo = open(ruta_archivo, 'w')
    lista_vacia = []
    #Inicializar el archivo con algo
    lista_string = json.dumps(lista_vacia)
    #Se escribe ese algo
    archivo.write(lista_string)
    archivo.close()
    return ruta_archivo

def abrir_archivo(ruta_archivo):
    if os.path.exists(ruta_archivo) == False:
        return False
    archivo = open(ruta_archivo, 'r', encoding='utf-8')
    contenido = archivo.read()
    #Se convierte el contenido del archivo desde formato JSON a un objeto Python
    obj_json = json.loads(contenido)
    archivo.close()
    return obj_json

def escribir_archivo(ruta_archivo, datos):
    if os.path.exists(ruta_archivo) == False:
        return False

    archivo = open(ruta_archivo, 'w')
    #Se transforman los datos de un tipo objecto (object) a un tipo String
    datos_string = json.dumps(datos, indent=4)
    archivo.write(datos_string)
    archivo.close()
    #retornar true para mostrar que la operacion fue exitosa.
    return True

def existe_archivo(ruta_archivo):
    # funcion que verifica si el archivo existe, si no, lo crea
    existe = abrir_archivo(ruta_archivo)
    if not existe:
        return crear_archivo(ruta_archivo)
    return existe

def verificar_json_vacio(ruta_archivo):
    lista_json = abrir_archivo(ruta_archivo)
    return len(lista_json) < 1