"""Sergio Rigo García - DAW1 - PRÁCTICA 4 - Ejercicio 09 - Escriu un programa que demani l'amplada i l'alçada d'un rectangle i ho dibuixi de la següent
manera:
Amplada del rectangle: 5
Alçada del rectangle: 4
*****
* *
* *
*****"""

print "Dame el ancho del rectángulo:"
ancho=int(raw_input())
print "Dame la altura del rectángulo:"
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
        
