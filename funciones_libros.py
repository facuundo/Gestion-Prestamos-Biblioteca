from funciones_json import *
from funciones import obtener_siguiente_id

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