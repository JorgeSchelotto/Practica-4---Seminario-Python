"""Una manera de evitar problemas con la versión de Python para el ingreso de datos por
teclado es deniendo la siguiente función:

def ingresar(texto):
import sys
if sys.version > '3':
    return input(texto)
else:
    return raw_input(texto)

Cómo haría para tener el mismo resultado con manejo de excepciones y sin usar una función
aparte?"""

import sys


try:

	if sys.version > '3':
		print('ingrese el numero: ')
		n = input()
	else:
		raise OSError
except OSError:
	print('ingrese en num para python 2')
	n = raw_input()


