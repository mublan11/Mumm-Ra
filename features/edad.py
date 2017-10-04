# -*- coding: utf-8 -*-

"""
	Autor: Diego Misael Blanco Murillo.
	Fecha: 01/OCT/17
"""

class Edad():
	def __init__(self):
		self.resultado = ' '
	def obtener_resultado(self):
		return self.resultado
	def calcularEdad(self, edad):		
		if edad < 0:
			self.resultado = "No existes"
		elif edad >= 0 and edad < 13:
			self.resultado = "Eres ninio"
		elif edad >= 13 and edad < 18:
			self.resultado = "Eres adolescente"
		elif edad >= 18 and edad < 65:
			self.resultado = "Eres adulto"
		elif edad >= 65 and edad < 120:
			self.resultado = "Eres adulto mayor"		
		elif edad >=120:
			self.resultado = "Eres Mumm-Ra"