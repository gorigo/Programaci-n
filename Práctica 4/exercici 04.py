"""Sergio Rigo García - DAW1 - PRÁCTICA 4 - EJERCICIO 04 - Escriu un programa que demani un nombre i calculi el seu factorial"""

print "Inserta un número"
num=int(raw_input())

aux=1
for i in range(num,0,-1):
    aux=aux*i
print "El factorial de", num, "es:", aux
