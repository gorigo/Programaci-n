"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 1:
Escriu un programa que te demani paraules i les guardi en una llista. Per a terminar d'introduir
paraules, simplement pitja Enter. El programa termina escribint la llista de paraules. 
"""
print "Escribe una palabra para crear una lista que contenga la palabra"
palabra=str(raw_input())
lista=[palabra]
while palabra<>"":
    print "Escribe una palabra para añadirla a la lista, o aprieta enter para mostrar la lista"
    palabra=str(raw_input())
    lista.append(palabra)
    if palabra=="":
        lista.remove("")
        print lista
