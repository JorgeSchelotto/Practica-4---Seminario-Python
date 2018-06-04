"""Implemente una clase Punto que represente una coordenada (x, y). Debe poseer los siguientes
métodos:
calcularDistancia(): Recibe como parámetro otro punto y retorna la distancia entre
ambos.
esIgual(): Recibe como parámetro otro punto y retorna si ambos puntos son iguales.
sumarX(): Recibe como parámetro un número entero, y lo suma a la coordenada x,
retornando el nuevo punto generado.
sumarY(): Recibe como parámetro un número entero, y lo suma a la coordenada y,
retornando el nuevo punto generado."""


import math

class Punto:
	def __init__(self, puntoX, puntoY):
		self.x=puntoX
		self.y=puntoY
		
	def calcularDistancia(self, otroX , otroY):
		"""Calcula la distancia entre dos punto."""
		distancia = math.sqrt((math.pow(otroX-self.x, 2))+(math.pow(otroY-self.y, 2)))
		return distancia
			
			
	def esIgual(self, otroX , otroY):
		"""Retorna True si dos puntos son iguales"""
		if (otroX == self.x) and (otroY==self.Y):
			return False
		return True
			
	def sumarX(self, valor):
		"""Suma un valor al punto X"""
		self.x = self.x + valor
		return self.x
			
	def sumarY(self, valor):
		"""Suma un valor al punto Y"""
		self.y= self.y + valor

prue = Punto(20,50)

print(prue.calcularDistancia(89, 58))
