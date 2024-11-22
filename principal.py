#menu principal
#TODO: armar con tkinter una interfaz grafica
#TODO: archivo main y un menu que contenga cada parte del menu - o varios menues
from funciones import *
from funciones_prestamos_devo import *
from funciones_json import * 
from funciones_libros import * 
from funciones_socios import *
ruta_libros = 'libros.json'
ruta_socios = 'socios.json'
ruta_prestamos = 'prestamos.json'
ruta_devoluciones = 'devoluciones.json'

existe_archivo(ruta_libros)
existe_archivo(ruta_socios)
existe_archivo(ruta_prestamos)
existe_archivo(ruta_devoluciones)

print(" ")
print("¡Bienvenido al menú principal!")
print(" ")
print("¿Qué queres hacer?")

while True:
    opcion_usuario = int(input(" 1: Ir al menú de libros \n 2: Ir al menú de socios \n 3: Ir al menú de préstamos y devoluciones \n 4: Salir \n Opción elegida: "))
    match opcion_usuario:
        case 1:
            #mostrar codigo 1
            while True:
            #mostrar menu del registro de libros.
                menu('registro de libros')

                print("     1. Registrar un libro")
                print(" ")
                print("     2. Editar un libro ya registrado")
                print(" ")
                print("     3. Eliminar un libro")
                print(" ")
                print("     4. Buscar un libro")
                print(" ")
                print("     5. Recomendaciones")
                print(" ")
                print("     6. Volver al menú principal")
                print(" ")

                opcion = int(input("Introduzca el número de la opción que quiere realizar: "))
                match opcion:
                    case 1:
                        #registrar un libro.
                        registrar_libro(ruta_libros)
        
                    case 2:
                        #editar un libro.
                        if verificar_json_vacio(ruta_libros):
                            print("No hay ningún libro registrado")
                        else:
                            mostrar_libros(ruta_libros)
                            id_libro=int(input("Por favor ingrese el ID del libro:  "))
                            print("Ingrese la informacion modificada a continuacion:")
                            titulo_editado = input("Titulo: ")
                            autor_editado = input("Autor: ")
                            editorial_editado=input("Editorial: ")
                            anio_editado = int(input("Año de publicación: "))
                            genero_editado = input("Género: ")
                            cantidad_editada = int(input("Cantidad disponible: "))
                            editar_libro(ruta_libros, id_libro, titulo_editado, autor_editado,editorial_editado, anio_editado, genero_editado, cantidad_editada)
                            
                    case 3:
                        #eliminar un libro
                        if verificar_json_vacio(ruta_libros):
                            print("No hay ningún libro registrado")
                        else:
                            mostrar_libros(ruta_libros)
                            id_libro=int(input("Ingrese el ID del libro que desea eliminar:"))
                            eliminar_libro(ruta_libros, id_libro)
                            mensaje()
                    
                    case 4:
                        #buscar libro por titulo, genero, autor o editorial.
                        titulo = input("Ingrese el título del libro, si no lo sabe, ingrese '0': ")
                        genero = input("Ingrese el genero del libro o libros, si no lo sabe, ingrese '0': ")
                        autor = input("Ingrese el autor del libro o libros, si no lo sabe, ingrese '0': ")
                        editorial = input("Ingrese la editorial del libro o libros, si no lo sabe, ingrese '0': ")
                        busqueda_libros(ruta_libros, titulo, genero, autor, editorial)

                    case 5:
                        # recomendar libro pidiendo genero en base a los libros de nuestro json
                        genero = input("¿Qué tipo de género te gustaria que te recomendemos?")
                        recomendar_libros(ruta_libros, genero)
                    case 6:
                        print("¡Volviste al menú principal!")
                        break
                    case _:

                        print("Debes ingresar una opción de las mencionadas.")
        case 2:
            #mostrar codigo 2
            while True:
                print(" ")
                print("¡Bienvenido al menú de registro de socios!")
                print(" ")
                print("     1. Registrar socio")
                print(" ")
                print("     2. Editar datos del socio")
                print(" ")
                print("     3. Eliminar socio")
                print(" ")
                print("     4. Volver al menú principal")
                print(" ")
   
                opcion=int(input("Introduzca el numero de la opcion que quiere realizar: "))
    
                match opcion:
                    case 1:
                        nombre = input("Ingrese el nombre del socio: ")
                        apellido = input("Ingrese el apellido del socio: ")
                        fecha_nacimiento = input("Ingrese la fecha de nacimiento del socio en formato (DD/MM/AAAA)): ")
                        direccion = input("Ingrese la dirección del socio: ")
                        correo = input("Ingrese el correo electrónico del socio: ")
                        telefono=input("Ingrese el telefono del socio: ")
                        agregar_socio(ruta_socios,nombre,apellido,fecha_nacimiento,direccion,correo,telefono)
                        
                    case 2:
                        #editar un socio
                        if verificar_json_vacio(ruta_socios):
                            print("No hay ningún socio registrado")
                        else:
                            mostrar_socios(ruta_socios)
                            id_socio=int(input("Por favor ingrese su ID:  "))
                            print("Ingrese la informacion modificada a continuacion:")
                            nombre2 = input("Nombre: ")
                            apellido2 = input("Apellido: ")
                            fecha_nacimiento2=input("Fecha de nacimiento: ")
                            direccion2 = input("Dirección: ")
                            correo2 = input("Correo electrónico: ")
                            telefono2 = input("Teléfono: ")
                            editar_socio(ruta_socios, id_socio, nombre2, apellido2,fecha_nacimiento2, direccion2, correo2, telefono2)
                              
                    case 3:
                        #eliminar un socio
                        if verificar_json_vacio(ruta_libros):
                            print("No hay ningún libro registrado")
                        else:
                            mostrar_socios(ruta_socios)
                            id_socio=int(input("Ingrese el ID del socio que desea eliminar: "))
                            eliminar_socio(ruta_socios, id_socio)
                            mensaje()
                    case 4:
                        print("¡Volviste al menú principal!")
                        break
        case 3:
            #mostrar codigo 3

            while True:
                menu('Prestamos y Devoluciones')

                print("     1. Registrar un préstamo")
                print(" ")
                print("     2. Conocer la fecha de un préstamo")
                print(" ")
                print("     3. Registrar una devolución")
                print(" ")
                print("     4. Conocer la fecha límite de una devolución")        
                print(" ")        
                print("     5. Conocer la fecha de una devolución realizada")
                print(" ")
                print("     6. Conocer el estado de un préstamo")
                print(" ")
                print("     7. Generar reportes de prestamos y devoluciones por ID de socio")
                print(" ")
                print("     8. Generar reportes de prestamos y devoluciones por ID del libro")
                print(" ")
                print("     9. Generar reportes de prestamos y devoluciones por rango de fechas")
                print(" ")
                print("     10. Volver al menú principal")
                print(" ")
                
            #mostrar menu de Préstamos y devoluciones.

                opcion = int(input("Introduzca el número de la opción que quiere realizar: "))
                match opcion:
                    case 1:
                        #registrar un nuevo prestamo.
                        registrar_prestamo(ruta_prestamos)
                    
                    case 2:
                        #mostrar fecha de un prestamo x
                        if verificar_json_vacio(ruta_prestamos):
                            print("No hay ningún préstamo registrado")
                        else:
                            mostrar_prestamos(ruta_prestamos)
                            id_prestamo=int(input("Por favor ingrese el ID del préstamo:  "))
                            mostrar_fecha_prestamo(ruta_prestamos, id_prestamo)
        
                    case 3:
                        #registrar una devolucion de un prestamo hecho.
                        if verificar_json_vacio(ruta_prestamos):
                            print("No hay ningún préstamo registrado")
                        else:
                            mostrar_prestamos(ruta_prestamos)
                            id_prestamo=int(input("Por favor ingrese el ID del préstamo:  "))
                            fecha_devolucion = input("Ingrese la fecha de la devolución con el siguiente formato (dd/mm/aaaa): ")
                            registrar_devolucion(ruta_prestamos, ruta_devoluciones, id_prestamo, fecha_devolucion) 
                            print("¡Se ha registrado correctamente la devolución!")
        
                    case 4:
                        #mostrar fecha límite de una devolucion 
                        if verificar_json_vacio(ruta_prestamos):
                            print("No hay ningún préstamo registrado")
                        else:
                            mostrar_prestamos(ruta_prestamos)
                            id_prestamo=int(input("Por favor ingrese el ID del préstamo:  "))
                            mostrar_fecha_devolucion(ruta_prestamos, id_prestamo)
                            
                    case 5:
                            #mostrar fecha de una devolucion realizada
                        if verificar_json_vacio(ruta_devoluciones):
                            print("No hay ninguna devolución registrada")
                        else:
                            mostrar_prestamos(ruta_devoluciones)
                            id_prestamo=int(input("Por favor ingrese el ID del préstamo:  "))
                            mostrar_fecha_devolucion(ruta_devoluciones, id_prestamo)
            
                    case 6:
                        #mostrar el estado de un préstamo
                        id_prestamo=int(input("Por favor ingrese el ID del préstamo:  "))
                        mostrar_estado(ruta_prestamos, ruta_devoluciones, id_prestamo)
                        
                    case 7:
                        #Generar reportes de prestamos y devoluciones por ID de socio 
                        mostrar_socios(ruta_socios)
                        ingreso_id=str(input("Por favor ingrese su ID de socio:  "))
                        id_socio_prestamo(ruta_prestamos, ruta_devoluciones, ingreso_id)
                        
                    case 8:
                        #Generar reportes de prestamos y devoluciones por ID del libro
                        mostrar_libros(ruta_libros)
                        ingreso_id=int(input("Por favor ingrese el ID del libro:  "))
                        id_libro_prestamo(ruta_prestamos, ruta_devoluciones, ingreso_id)

                    case 9:
                        #Generar reportes de prestamos y devoluciones por rango de fechas
                        inicio_fecha=input("Por favor ingrese la fecha desde:  ")
                        fin_fecha=input("Hasta:  ")
                        registro_fecha(ruta_prestamos, ruta_devoluciones, inicio_fecha, fin_fecha)
                    
                    case 10:
                        print("¡Volviste al menú principal!")
                        break
                    case _:
                        print("Debes ingresar una opción de las mencionadas: ")
        case 4:
            print("Gracias por ser parte de nuestra biblioteca, que tenga un excelente dia.")
            break