"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 4 - EJERCICIO 06 - Escriu un programa que demani l'al�ada d'un triangle i ho dibuixi de la seg�ent manera:
Al�ada del triangle: 4
*
**
***
****"""

print "Escribe la altura del tri�ngulo:"
altura=int(raw_input())
forma="*"
for i in range(1,altura+1):
    print forma*i
