from funciones_json import *
from funciones import obtener_siguiente_id

def agregar_socio(ruta_archivo, nombre, apellido, fecha_nacimiento, direccion, correo, telefono):
    socios = abrir_archivo(ruta_archivo)
    id_socio = obtener_siguiente_id(ruta_archivo)
    socio = {
    'id': id_socio,
    'Nombre': nombre,
    'Apellido': apellido,
    'Fecha de Nacimiento': fecha_nacimiento,
    'Dirección': direccion,
    'Correo Electrónico': correo,
    'Telefono' : telefono
    }
    socios.append(socio)
    id_socio += 1

    escribir_archivo(ruta_archivo, socios)
    print(f"El socio {socio['Nombre']} se ha agregado con éxito.")

def editar_socio(ruta_archivo, id_socio, nombre2, apellido2,fecha_nacimiento2, direccion2, correo2,telefono2):
    socios = abrir_archivo(ruta_archivo)
    for socio in socios:
        if socio['id'] == id_socio:
            socio['Nombre'] = nombre2
            socio['Apellido'] = apellido2
            socio['Fecha de Nacimiento'] =fecha_nacimiento2
            socio['Dirección'] = direccion2
            socio['Correo Electrónico'] = correo2
            socio['Telefono']=telefono2
            break
    escribir_archivo(ruta_archivo, socios)
    print(f"El socio {socio['Nombre']} se ha editado con éxito")
    
def mostrar_socios(ruta_archivo):
    socios = abrir_archivo(ruta_archivo)
    for socio in socios:
        print(f"ID: {socio['id']}, {socio['Nombre']}")

def eliminar_socio(ruta_archivo, id_socio):
    socios = abrir_archivo(ruta_archivo)
    for socio in socios:
        if socio['id'] == id_socio:
            socios.remove(socio)
            break
    escribir_archivo(ruta_archivo, socios)
