# -*- coding: utf-8 -*-

"""
	Autor: Diego Misael Blanco Murillo.
	Fecha: 06/SEP/17
"""
class Edad():

	def __init__(self):
		self.resultado = ''

	def obtener_resultado(self):
		return self.resultado

	def calcularEdad(self, edad):
		try:
			if type(edad) == str:
	   			self.resultado = 'No se permiten letras'
	   		elif type(edad) == float:
	   			self.resultado = 'No se permiten decimales'
			elif edad < 0:
				self.resultado = "No existes"
			elif edad >= 0 and edad < 13:
				self.resultado = "Eres niño"
			elif edad >= 13 and edad < 18:
				self.resultado = "Eres adolescente"
			elif edad >= 18 and edad < 65:
				self.resultado = "Eres adulto"
			elif edad >= 65 and edad < 120:
				self.resultado = "Eres adulto mayor"		
			else:
				self.resultado = "Eres Chabelo"
		except:
			self.resultado = "Datos incorrectos"