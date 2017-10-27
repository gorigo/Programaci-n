"""Sergio Rigo García - DAW1 - PRÁCTICA 4 - Ejercicio 07 - Exercici 07
Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:
Alçada del triangle: 4
****
***
**
*"""

print "Escribe la altura del triángulo:"
altura=int(raw_input())
forma="*"
for i in range(altura,0,-1):
    print forma*i
