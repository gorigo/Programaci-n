"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 4 - EJERCICIO 04 - Escriu un programa que demani un nombre i calculi el seu factorial"""

print "Inserta un n�mero"
num=int(raw_input())

aux=1
for i in range(num,0,-1):
    aux=aux*i
print "El factorial de", num, "es:", aux
