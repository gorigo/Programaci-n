"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 4 - EJERCICIO 08 - Escriu un programa que demani l'amplada d'un triangle i ho dibuixi de la seg�ent manera:
Al�ada del triangle: 4
*
**
***
****
***
**
*"""
print "Escribe la altura del tri�ngulo:"
altura=int(raw_input())
forma="*"
for i in range(1,altura+1):
    print forma*i
for i in range(altura-1,0,-1):
    print forma*i
