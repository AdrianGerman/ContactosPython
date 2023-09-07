import os
# Carpeta de contactos
CARPETA = 'contactos/datos/'
EXTENSION = '.txt'


class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    # Revisa si la carpeta existo o no
    crear_directorio()

    # Muestra el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la acción
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

    # Ejecutar las operaciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no valida, intente de nuevo')


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto:\r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w', encoding='utf-8') as archivo:
            # Resto de los campos
            telefono_contacto = input('Agrega el teléfono:\r\n')
            categoria_contacto = input('Categoría del contacto:\r\n')
            # Instanciar la clase
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)
            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')
            # Mostrar mensaje de exito
            print('\r\n --- Contacto creado correctamente --- \r\n')
    else:
        print('\r\n--- Ese contacto ya existe ---\r\n')
    # Se reinicia la app
    app()


def editar_contacto():
    print("Escribe el nombre del contacto a editar")
    nombre_anterior = input('Nombre del contacto que desea editar:\r\n')

    # Revisar si el archivo existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w', encoding='utf-8') as archivo:
            # Resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre:\r\n')
            telefono_contacto = input('Agrega el nuevo teléfono:\r\n')
            categoria_contacto = input('Agrega la nueva categoría:\r\n')

            # Instanciar
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

        # Si esta en esta parte idendada del codigo, lo de arriba se cierra.

        # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION,
                  CARPETA + nombre_contacto + EXTENSION)

        # Mostrar mensaje de exito
        print('\r\n --- Contacto editado correctamente --- \r\n')

    else:
        print('Ese contacto no existe')

    # Reiniciar la aplicación
    app()


def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo, encoding='utf-8') as contacto:
            for linea in contacto:
                # Imprime contenidos
                print(linea.rstrip())
            # Imprime el separador entre contactos3

            print('\r\n')
    # Reiniciar la app
    app()


def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION, encoding='utf-8') as contacto:
            print('\r\n --- Información del contacto --- \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('\r\nEl archivo no existe\r\n')

    # Reiniciar la app
    app()


def eliminar_contacto():
    nombre = input('Seleccione el contacto que deseas eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n --- Eliminado correctamente --- \r\n')
    except IOError:
        print('\r\nEl archivo no existe\r\n')

    # Reiniciar la app
    app()


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


def mostrar_menu():
    print('Seleccione lo que desee hacer')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contacto')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')


def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crea la carpeta
        os.makedirs(CARPETA)


app()
