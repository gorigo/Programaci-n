"""Sergio Rigo Garc�a - DAW1 - PRACTICA 4 - EJERCICIO 05 - Escriu un programa que demani l'amplada i al�ada d'un rectangle i ho dibuixi de la seg�ent manera: Amplada del rectangle: 5
Al�ada del rectangle: 3
*****
*****
*****"""

print "Escribe la anchura que quieres que tenga el rect�ngulo:"
ancho=int(raw_input())
print "Escribe la altura que quieres que tenga el rect�ngulo:"
altura=int(raw_input())
aux="*"
for i in range(altura):
    print aux*ancho
    
