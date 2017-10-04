Feature: Calcular la Edad biologica
	Como usuario de la Edad biologica
	deseo introducir mi edad
	para obtener mi edad biologica

	Scenario: Menor de 0
		Dado que ingreso la edad "-1"
		cuando realizo la operacion entonces
		obtengo el resultado de "No existes"

	Scenario: Menor de 13
		Dado que ingreso la edad "12"
		cuando realizo la operacion entonces
		obtengo el resultado de "Eres ninio"

	Scenario: Menor de 18
		Dado que ingreso la edad "17"
		cuando realizo la operacion entonces
		obtengo el resultado de "Eres adolescente"

	Scenario: Menor de 65
		Dado que ingreso la edad "64"
		cuando realizo la operacion entonces
		obtengo el resultado de "Eres adulto"

	Scenario: Menor de 120
		Dado que ingreso la edad "119"
		cuando realizo la operacion entonces
		obtengo el resultado de "Eres adulto mayor"

	Scenario: Mayor de 120
		Dado que ingreso la edad "666"
		cuando realizo la operacion entonces
		obtengo el resultado de "Eres Mumm-Ra"