playlist = {}  # Diccionario vacio
playlist['canciones'] = []  # lista vacio de canciones


# Funcion principal
def app():
    # Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Cómo deseas nombrar la playlist?\r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            # Si ya se proporciono el nombre del playlist
            agregar_playlist = False
            # Mandar a llamar la funcion del nombre, para que se ejecute en cuanto termine esta.
            agregar_canciones()


def agregar_canciones():
    agregar_cancion = True

    while agregar_cancion:
        # Pregunta al usuario que canción desea agregagr
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)
        if cancion == 'X':
            # Dejar de agregar canciones
            agregar_cancion = False
            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            # Agregar las canciones a la playlist
            playlist['canciones'].append(cancion)


def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'\r\nPlaylist:\r\n{nombre_playlist}\r\n')
    print('Canciones:\r')
    for cancion in playlist['canciones']:
        print(cancion)


app()
