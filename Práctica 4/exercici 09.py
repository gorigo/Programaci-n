"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 4 - Ejercicio 09 - Escriu un programa que demani l'amplada i l'al�ada d'un rectangle i ho dibuixi de la seg�ent
manera:
Amplada del rectangle: 5
Al�ada del rectangle: 4
*****
* *
* *
*****"""

print "Dame el ancho del rect�ngulo:"
ancho=int(raw_input())
print "Dame la altura del rect�ngulo:"
altura=int(raw_input())
forma="*"
espacio=" "
aux=ancho-2
for i in range(altura+1):
    if i==0 or i==altura:
        print ancho*forma
    else:
        print forma,
        print espacio*(aux-2),
        print forma
        
