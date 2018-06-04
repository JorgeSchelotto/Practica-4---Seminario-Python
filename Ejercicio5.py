"""Defina dos funciones que recibe una cantidad variable de argumentos:
+ La función sumar, puede llegar a recibir hasta 30 números como parámetros (*args) y debe devolver la suma total de los mismos.
+ La otra función que debe definirse, recibe parámetros con nombre(**kwargs),
se deberá imprimir los datos que reciba(usar excepciones para determinar qué campos faltan como parámetros). De antemano
no se sabe cuáles de los tres posibles parámetros se
reciben:
    nombre
    apellido
    sexo"""

def sumar(*args):
    try:
        if len(args) <= 30:
            try:
                total = 0
                for num in args:
                    total =  total + int(num)
                print('La suma total es: ', total)
            except ValueError:
                print('El argumento {} no es un numero y no puede ser sumado'.format(num))
        else:
            raise IndexError
    except IndexError:
        print('Se ingresaron mas de 30 argumentos')



def imprimeDatos(**kwargs):
    #print(kwargs)
    try:
        for key, value in kwargs.items():
            if value != '':
                print(key + ': ' + value)
            else:
                raise ValueError
    except ValueError:
        print('Falta el valor de la clave: ', key)





sumar(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

imprimeDatos( Apellido = 'Cucatrap' , Sexo = 'Veneno')