"""Dada la lista de colores del Ejercicio 1 de la Práctica 2, realice una función que ingrese
coordenadas por teclado y retorne el color asociado al mismo. Maneje con excepciones si
las coordenadas ingresadas no existen en la lista, informándolo y requiriendo que las ingrese
nuevamente."""

import random


def coordenadas():
    coordenadas = [(2, 3), (5, 6), (8, 8), (10, 2), (-5, -8)]
    colores = ['azul', 'amarillo', 'rojo', 'blanco', 'negro']
    dic = {}

    for i in coordenadas:
        dic[i] = []

    for i in dic:
        numRan = random.randrange(len(colores) - 1)
        dic[i] = colores[numRan]

    return dic


def evalua():
    x = int(input('ingrese x: '))
    y = int(input('ingrese y: '))
    coor = (x, y)

    estructura = coordenadas()
    control = False
    while (control != True):
        try:
            print('Entro al bloque Try')
            print('El color asociado a la coordenada {}, {} es el '.format(x,y) + estructura[coor])
            control = True
        except (KeyError):
            print('No existe la coordenada. Ingrese nuevamente:')
            x = int(input('ingrese x: '))
            y = int(input('ingrese y: '))
            coor = (x, y)
            control = False


evalua()