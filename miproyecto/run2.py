"""
	file: run.py
	autor: @royerjmasache
"""
from misvariables import*
# Uso de condicional simple
nota = input("Ingrese la primera nota del estudiante: ")
nota2 = input("Ingrese la segunda nota del estudiante: ")
nota = int(nota)
nota2 = int(nota2)
if nota >= 18:
	print("%s con: %d" % (mensaje, nota))
else:
	print("%s con: %d" % (mensaje2, nota))

if nota2 >= 18:
	print("%s con: %d" % (mensaje, nota))
else:
	print("%s con: %d" % (mensaje2, nota))
