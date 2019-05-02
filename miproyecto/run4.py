"""
	file: run4.py
	autor: @royerjmasache
"""
"""
	Se desea obtener el costo de una carrera universitaria. El valor promedio de cada ciclo es de 1200 $.
	El valor promedio del seguro educativo por ciclo es de 100 dólares si la edad del estudiante es menor o igual a 20, caso contrario será de 150 dólares.
	Si el estudiante tiene una modalidad a distancia el número de ciclos a seguir es de 10 caso contrario deberá seguir 8 ciclos.
	Obtener la proyección del costo de la carrera del estudiante.
"""
# Ingreso de datos y declaración de variables
modalidad = input("Ingrese el tipo de modalidad del estudiante:\n1. Modalidad Presencial\n2. Modalidad a Distancia\n")
modalidad = int(modalidad)
edad = input("Ingrese la edad del estudiante: ")
edad = int(edad)
costo = 1200
# Estructura condicional anidada
if (modalidad == 1) and (edad <= 20):
	# Operaciones
	costo = costo * 8
	seguro = 100 * 8
	# Cálculo del precio de la carrera
	costo = costo + seguro
else:
	if (modalidad == 1) and (edad > 20):
		# Operaciones
		costo = costo * 8
		seguro = 150 * 8
		# Cálculo del precio de la carrera
		costo = costo + seguro
	else:
		if (modalidad == 2) and (edad <= 20):
			# Operaciones
			costo = costo * 10
			seguro = 100 * 10
			# Cálculo del precio de la carrera
			costo = costo + seguro
		else:
			if (modalidad == 2) and (edad > 20):
				# Operaciones
				costo = costo * 10
				seguro = 150 * 10
				# Cálculo del precio de la carrera
				costo = costo + seguro
# Presentación de datos
print("El costo de la carrera es de: %d" % costo)