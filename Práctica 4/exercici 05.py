"""Sergio Rigo García - DAW1 - PRACTICA 4 - EJERCICIO 05 - Escriu un programa que demani l'amplada i alçada d'un rectangle i ho dibuixi de la següent manera: Amplada del rectangle: 5
Alçada del rectangle: 3
*****
*****
*****"""

print "Escribe la anchura que quieres que tenga el rectángulo:"
ancho=int(raw_input())
print "Escribe la altura que quieres que tenga el rectángulo:"
altura=int(raw_input())
aux="*"
for i in range(altura):
    print aux*ancho
    
