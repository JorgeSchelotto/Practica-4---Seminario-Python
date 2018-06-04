"""Modelice las clases Puntaje y Jugador. La clase Puntaje tendrá como atributos nivel, puntos
y tiempo. La clase Jugador tendrá como información su nombre y una lista de Puntajes,
con los siguientes métodos:
nivelMaximo(): Retorna el nivel máximo alcanzado por el jugador.
cantidadTotalPuntajes(): Retorna la cantidad de puntajes almacenados del jugador.
puntajeMaximo(): Recibe como parámetro un nivel y retorna el máximo puntaje del
jugador para ese nivel.
menorTiempo(): Recibe como parámetro un nivel y retorna el menor tiempo de juego
del jugador para ese nivel."""




class Puntaje:
    def __init__(self, nivel, puntos, tiempo):
        self.nivel= nivel
        self.puntos = puntos
        self.tiempo = tiempo

class Jugador:
    def __init__(sel, nombre, puntajes):
        sel.nombre = nombre
        self.listPuntajes = puntajes

    def nivelMaximo(self):
        max = -1
        for puntajes in self.listPuntajes:
            if puntajes.nivel < max:
                max = puntajes.nivel
        return max

    def cantidadTotalPuntajes(self):
        return len(self.listPuntajes)

    def puntajeMAximo(self, nivel):
        for puntaje in self.listPuntajes:
            if puntaje.nivel == nivel:
                max = -1
                if max < puntaje.puntos:
                    max = puntaje.puntos
        return max

    def menorTiempo(self, nivel):
        for puntaje in self.listPuntajes:
            if puntaje.nivel == nivel:
                min = 9999
                if min < puntaje.tiempo:
                    min = puntaje.tiempo
        return min