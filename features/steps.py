# -*- coding: utf-8 -*-

"""
    Autor: Diego Misael Blanco Murillo.
    Fecha: 01/OCT/17
"""

from lettuce import step, world
from edad import Edad

#Mumm-Ra
@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, edad):
    world.edad = Edad()
    world.edad.calcularEdad(int(edad))

@step(u'obtengo el resultado de "([^"]*)"')
def obtengo_el_resultado_de_group1(step, esperado):
    obtenido = world.edad.obtener_resultado()
    assert str(esperado) == obtenido, 'El resultado esperado es '+esperado+' y el obtenido es '+str(obtenido)