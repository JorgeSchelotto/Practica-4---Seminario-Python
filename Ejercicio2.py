""" Dado el archivo utilizado con datos de jugadores del Ejercicio 3 de la Práctica 3, implemente
una función que reciba el nombre del archivo como parámetro y maneje con excepciones el
caso que el archivo no exista, informando dicha situación."""

import json

jugadores = {}
clave = {}

def modifica_datos():
    # leo jugador a buscar
    print()
    nom = input('ingrese el jugador a buscar: ')

    # cargo el diccionario almacenado en el txt. E el bloque try  busco si el
    # jugador existe para actualizar sus datos. Sino existe, lo agrego mediante
    # el bloque except. En finally imprimo el diccionario completo.
    with open('json.txt', 'r+') as f:
        d = json.load(f)
        try:
            print('Los datos del jugador ',nom,' son: ',d[nom])
            print('Actualice los datos del jugador: ', nom)
            nivel = input('Ingrese el nuevo nivel: ')
            puntaje = int(input('Ingrese el nuevo puntaje: '))
            horasJuego = input('Ingrese las nuevas horas de juego: ')
            clave['nivel'] = nivel
            clave['puntaje'] = puntaje
            clave['horas'] = horasJuego
            d[nom] = clave.copy()

        except (KeyError):
            print()
            print('El jugador no existe. Cargue los datos de: ', nom, ', nuevo jugador.')
            nivel = input('Ingrese el nuevo nivel: ')
            puntaje = int(input('Ingrese el nuevo puntaje: '))
            horasJuego = input('Ingrese las nuevas horas de juego: ')
            clave['nivel'] = nivel
            clave['puntaje'] = puntaje
            clave['horas'] = horasJuego
            d[nom] = clave.copy()

        # imprimo versión final del diccionario
        finally:
            print()
            print('Último registro de jugadores: ')
            print(d)

# carga inicial de jugadores y sus datos
nombre = input('Ingrese Nombre del jugador. Ingrese "fin" para cortar la carga: ')
while(nombre != 'fin'):
    nivel = input('Ingrese Nivel del jugador: ')
    puntaje = input('Ingrese puntaje del jugador: ')
    horasJuego = input('Ingrese horas de juego del jugador: ')

    clave['nivel'] = nivel
    clave['puntaje'] = puntaje
    clave['horas'] = horasJuego
    jugadores[nombre] = clave.copy()

    nombre = input('Ingrese Nombre del jugador: ')

# guardo el diccionario de jugadores en archivo de texto plano
file = open('json.txt', 'w')
json.dump(jugadores,file)
file.close()

print()
print('diccionario inicial: ')
print(jugadores)

modifica_datos()
