"""Lea de un archivo (miarchivo.txt) números, maneje a través de excepciones la posibilidad
de que no exista el archivo y también que los datos leídos no sean números."""


try:
    file = open('miarchivo.txt','r')
    control = []
    try:
        for linea in file:
            control.append(int(linea))
        print('Se pudo leer el archivo correctamente y se genero la siguiente lista: \n',  control)
        file.close()
    except (TypeError, ValueError):
        print('La linea {} no es un numero'.format(linea))
        file.close()
except OSError:
    print('El archivo no existe.')