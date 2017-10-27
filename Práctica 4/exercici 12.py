"""Sergio Rigo García - DAW1 - PRÁCTICA 4 - Exercici 11(opcional) -
Exercici 12(opcional)
Escriu un programa que demani un nombre i escrigui si és primer o no."""

print "Escribe un número:"
numero=int(raw_input())

for i in range(1,20):
    if numero/i>numero and numero%i<>0:
        print numero, "no es un número primo"
    else:
        print numero, "es un número primo"

    
