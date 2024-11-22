from funciones_json import *
from funciones import obtener_siguiente_id

def registrar_prestamo(ruta_archivo):
    #función para registrar un nuevo préstamo
    prestamos = abrir_archivo(ruta_archivo)
    id_prestamo = obtener_siguiente_id(ruta_archivo)
    id_socio = input("¿Cual es el id del socio?: ")
    id_libro = int(input("Ingrese el id del libro: "))
    precio = float(input("Ingrese el precio del producto: "))
    fecha_prestamo = input("Ingrese la fecha del préstamo con el siguiente formato (dd/mm/aaaa): ")
    fecha_devolucion = input("Ingrese la fecha límite de la devolución con el siguiente formato (dd/mm/aaaa): ")

    prestamo = {
        'id': id_prestamo,
        'nombre': id_socio,
        'marca': id_libro,
        'precio': precio,
        'fecha': fecha_prestamo,
        'fecha_devolucion': fecha_devolucion,
        'estado': 'en curso',
    }
    prestamos.append(prestamo)
    id_prestamo += 1

    escribir_archivo(ruta_archivo, prestamos)
    print("El préstamo se ha registrado con éxito")

def mostrar_prestamos(ruta_archivo):
    prestamos = abrir_archivo(ruta_archivo)
    for prestamo in prestamos:
        print(f"ID: {prestamo['id']}")


def mostrar_fecha_prestamo(ruta_archivo, id_prestamo):
    prestamos = abrir_archivo(ruta_archivo)
    for p in prestamos:
        if p['id'] == id_prestamo:
            print(f"La fecha del préstamos es: {p['fecha']}")
            break
    
def registrar_devolucion(ruta_prestamos, ruta_devoluciones, id_prestamo, fecha):
    prestamos = abrir_archivo(ruta_prestamos)
    devoluciones = abrir_archivo(ruta_devoluciones)

    for p in prestamos:
        if p['id'] == id_prestamo:
            prestamos.remove(p)
            p['fecha_devolucion'] = fecha
            p['estado'] = 'Devuelto'
            devoluciones.append(p)
            break
    escribir_archivo(ruta_prestamos, prestamos)
    escribir_archivo(ruta_devoluciones, devoluciones)

def mostrar_fecha_devolucion(ruta_archivo, id_prestamo):
    data = abrir_archivo(ruta_archivo)
    for p in data:
        if p['id'] == id_prestamo:
            print(f"La fecha de la devolución es: {p['fecha_devolucion']}")
            break

def mostrar_estado(ruta_prestamos, ruta_devoluciones, id_prestamo):
    prestamos = abrir_archivo(ruta_prestamos)
    devoluciones = abrir_archivo(ruta_devoluciones)

    estado = 'No encontrado'
    for prestam in prestamos:
        if prestam['id'] == id_prestamo:
            estado = prestam['estado']
            print(f"El estado del libro es: {estado}")
            break
    if estado == 'No encontrado':
        for p in devoluciones:
            if p['id'] == id_prestamo:
                estado= p['estado']
                print(f"El estado del libro es: {estado}")
                break

def id_socio_prestamo(ruta_prestamos, ruta_devoluciones, id_socio):
    #funcion que genera reportes de prestamos y devoluciones por id socio
    prestamos = abrir_archivo(ruta_prestamos)
    devoluciones = abrir_archivo(ruta_devoluciones)
    nuevos_registros=[]
    nuevos_registros2=[]

    for prestamo in prestamos:
        if id_socio==prestamo['nombre']:
            nuevos_registros.append("Libro:")
            nuevos_registros.append(prestamo["marca"])
            nuevos_registros.append("Fecha de prestamo:")
            nuevos_registros.append(prestamo["fecha"])
            print(f"El socio {id_socio} tiene los siguientes registros de préstamos: {nuevos_registros}")
            
    for prestamo in devoluciones:
        if id_socio==prestamo['nombre']:
            nuevos_registros2.append("Libro:")
            nuevos_registros2.append(prestamo["marca"])
            nuevos_registros2.append("Fecha de prestamo:")
            nuevos_registros2.append(prestamo["fecha"])
            nuevos_registros2.append("Fecha de devolucion:")
            nuevos_registros2.append(prestamo["fecha_devolucion"])
            print(f"El socio {id_socio} tiene los siguientes registros de devoluciones: {nuevos_registros2}")
            
def id_libro_prestamo(ruta_prestamos, ruta_devoluciones, id_libro):
    #funcion que genera reportes de prestamos y devoluciones por id libro
    prestamos = abrir_archivo(ruta_prestamos)
    devoluciones = abrir_archivo(ruta_devoluciones)
    nuevos_registros=[]
    nuevos_registros2=[]

    for prestamo in prestamos:
        if id_libro==int(prestamo["marca"]):
            nuevos_registros.append("Id socio:")
            nuevos_registros.append(prestamo["nombre"])
            nuevos_registros.append("Fecha de prestamo:")
            nuevos_registros.append(prestamo["fecha"])
            print(f"El libro {id_libro} tiene los siguientes registros de prestamos: ", nuevos_registros)

    for prestamo in devoluciones:
        if id_libro==int(prestamo["marca"]):
            nuevos_registros2.append("Id socio:")
            nuevos_registros2.append(prestamo["marca"])
            nuevos_registros2.append("Fecha de prestamo:")
            nuevos_registros2.append(prestamo["fecha"])
            nuevos_registros2.append("Fecha de devolucion:")
            nuevos_registros2.append(prestamo["fecha_devolucion"])
            print(f"El libro {id_libro} tiene los siguientes registros de devoluciones: ", nuevos_registros2)
    
def registro_fecha(ruta_prestamos, ruta_devoluciones, inicio, fin):
    #funcion que genera reportes de prestamos y devoluciones por rango de fechas
    prestamos = abrir_archivo(ruta_prestamos)
    devoluciones = abrir_archivo(ruta_devoluciones)
    fechas=[]
    for dia in devoluciones:
        fecha_registro = dia["fecha"]
        if inicio <= fecha_registro <= fin:
            fechas.append(dia)
    if fechas:
        print("Prestamos encontrados:")
        for dia in devoluciones:
            print(f"ID: {dia['id']}, Fecha: {dia['fecha']}, Estado: {dia['estado']}")
    else:
        print("No se encontraron registros en ese rango de fechas.")