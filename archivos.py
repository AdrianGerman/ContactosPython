def app():
    # Crear el archivo
    # w es escritura, y si no existe lo crea
    archivo = open('archivo.txt', 'w')

    # generar numeros en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea ' + str(i) + "\r")

    # Cerrar archivo
    archivo.close()


app()
