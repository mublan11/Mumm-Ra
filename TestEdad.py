# -*- coding: utf-8 -*-

import unittest
from edad import Edad
"""
    Autor: Diego Misael Blanco Murillo.
    Fecha: 06/SEP/17
"""
class EdadTest(unittest.TestCase):
    
    def setUp(self):
        self.edad = Edad()
        self.datosIncorrectos = 'Datos incorrectos'

    def test_no_existes(self):
        self.edad.calcularEdad(-1)
        self.assertEquals(self.edad.obtener_resultado(), 'No existes')
    
    def test_eres_ninio(self):
        self.edad.calcularEdad(0)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres niño')
    
    def test_eres_ninio_2(self):
        self.edad.calcularEdad(11)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres niño')
    
    def test_eres_adolescente(self):
        self.edad.calcularEdad(13)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres adolescente')
    
    def test_eres_adolescente_2(self):
        self.edad.calcularEdad(17)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres adolescente')

    def test_eres_adulto(self):
        self.edad.calcularEdad(19)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres adulto')

    def test_eres_adulto_2(self):
        self.edad.calcularEdad(64)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres adulto')

    def test_eres_adulto_mayor(self):
        self.edad.calcularEdad(66)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres adulto mayor')

    def test_eres_adulto_mayor_2(self):
        self.edad.calcularEdad(119)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres adulto mayor')

    def test_eres_chabelo(self):
        self.edad.calcularEdad(314)
        self.assertEquals(self.edad.obtener_resultado(), 'Eres Chabelo')

    def test_eres_chabelo(self):
        self.edad.calcularEdad('V')
        self.assertEquals(self.edad.obtener_resultado(), 'No se permiten letras')

    def test_eres_chabelo(self):
        self.edad.calcularEdad(11.11)
        self.assertEquals(self.edad.obtener_resultado(), 'No se permiten decimales')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()