# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio9: Escribe un programa que permita crear una lista de palabras y que
, a continuación, cree una segunda lista con las palabras de la primera, pero sin palabras repetidas (el orden de las
palabras en la segunda lista no es importante)."""

print "Dime cuántas palabras tiene la lista:"
numero=int(raw_input())
lista=[]
lista_ambas=[]
lista_primera=[]
for i in range(0,numero):
    palabra=raw_input("Escribe una palabra:")
    lista_ambas.append(palabra)
    if palabra in lista:
        lista_ambas.remove(palabra)
        lista.append(palabra)
    else:
        lista.append(palabra)
print "La lista de palabras es:", lista
print "La lista de palabras sin repetir es", lista_ambas