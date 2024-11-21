#todas las funciones
#TODO: separar en varios archivos de funciones
import json
import os

# **inicio funciones JSON**
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
# **fin funciones JSON**

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

# **inicio funciones libros**
def registrar_libro(ruta_archivo):
#función para registrar un nuevo préstamo
    libros = abrir_archivo(ruta_archivo)
    id_libro = obtener_siguiente_id(ruta_archivo)
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    anio_de_publicacion = int(input("Ingrese el año de publicación: "))
    genero = input("Ingrese el género del libro: ")
    cantidad_disponible = int(input("Ingrese la cantidad disponible de este libro: "))

    libro = {
        'id': id_libro,
        'titulo': titulo,
        'autor': autor,
        'editorial': editorial,
        'anio_de_publicacion': anio_de_publicacion,
        'genero': genero,
        'cantidad_disponible': cantidad_disponible,
    }
    libros.append(libro)
    id_libro += 1

    escribir_archivo(ruta_archivo, libros)
    print(f"El libro {libro['titulo']} se ha registrado con éxito")

def editar_libro(ruta_archivo, id_libro, titulo_editado, autor_editado, editorial_editado, anio_editado, genero_editado, cantidad_editada):
    libros = abrir_archivo(ruta_archivo)
    id_libro = obtener_siguiente_id(ruta_archivo)
    for libro in libros:
        if libro['id'] == id_libro:
            libro['titulo'] = titulo_editado
            libro['autor'] = autor_editado
            libro['editorial'] = editorial_editado
            libro['anio_de_publicacion'] = anio_editado
            libro['genero'] = genero_editado
            libro['cantidad_disponible']=cantidad_editada
            break
    escribir_archivo(ruta_archivo, libros)
    print(f"El libro {libro['titulo']} se ha editado con éxito")

def mostrar_libros(ruta_archivo):
    libros = abrir_archivo(ruta_archivo)
    for libro in libros:
        print(f"ID: {libro['id']}, {libro['titulo']}")

def eliminar_libro(ruta_archivo, id_libro):
    libros = abrir_archivo(ruta_archivo)
    for libro in libros:
        if libro['id'] == id_libro:
            libros.remove(libro)
            break
    escribir_archivo(ruta_archivo, libros)

def mensaje():
    print(" ")
    print("¡Se ha eliminado exitosamente!")
    print(" ")

def busqueda_libros(ruta_archivo, titulo, genero, autor, editorial):
    libros = abrir_archivo(ruta_archivo)
    encontrado = False

    for libro in libros:
        if (titulo != '0' and titulo in libro['titulo']) or (genero != '0' and genero in libro['genero']) or (autor != '0' and autor in libro['autor']) or (editorial !='0' and editorial in libro['editorial']):
            encontrado = True
            print(f"Libro: {libro['titulo']}, Género: {libro['genero']}, Autor: {libro['autor']}, Editorial: {libro['editorial']}, Cantidad disponible: {libro['cantidad_disponible']}")

    if not encontrado:
        print("No se encontraron libros con esos criterios de busqueda.")        

def recomendar_libros(ruta_archivo, genero):
    libros = abrir_archivo(ruta_archivo) 
    recomendados = []

    for libro in libros:
        if genero in libro['genero']:
            recomendados.append(libro)

    if recomendados:
        print(f"Los libros que te recomendados del género {genero} son:")
        for libro in recomendados:
            print(f"Libro:{libro['titulo']}, del Autor:{libro['autor']}, de la editorial {libro['editorial']} .")
    else:
        print(f"Lo siento, no pudimos encontrar libros del genero {genero} ")                    
# **fin funciones libros**


# **inicio funciones socios**
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
# **fin funciones socios**

# **inicio funciones prestamos y devoluciones**
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