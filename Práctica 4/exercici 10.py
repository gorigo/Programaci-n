"""Sergio Rigo García - DAW1 - PRÁCTICA 4 - EJERCICIO 10(Opcional) -
Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:
Alçada del triangle: 5
 *
 ***
 *****
 *******
*********"""


print "Dame la altura del triángulo:"
altura=int(raw_input())
triangulo="*"
espacio=" "
variable=altura*2
variable_2=altura-2
for i in range(0,variable,+1):
    if i==variable-1:
        print i*triangulo
    else:
        if i%2<>0:
            print variable_2*espacio,
            print i*triangulo
            variable_2+=-1
        
