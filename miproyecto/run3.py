"""
	file: run.py
	autor: @royerjmasache
"""
from misvariables import*
# Uso de condicional anidada
nota = input("Ingrese la nota del estudiante: ")
nota = int(nota)
# Estructura condicional anidada
if nota >= 18:
	print("%s de manera %s con: %d" % (mensaje, "Sobresaliente", nota))
else:
	if (nota >= 16) and (nota <18):
		print(print("%s de manera %s con: %d" % (mensaje, "Muy buena", nota)))
	else:
		if (nota >= 13) and (nota < 16):
			print("%s de manera %s con: %d" % (mensaje, "Buena", nota))
		else:
			print("%s de manera %s con: %d" % (mensaje2, "Insuficiente", nota))

