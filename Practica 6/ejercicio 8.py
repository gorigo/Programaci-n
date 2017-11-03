# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio8: Escribe un programa que permita crear una lista de palabras y
que, a continuación, ordene la lista por orden alfabético. """

print "Dime cuántas palabras tiene la lista:"
numero=int(raw_input())
lista=[]
for i in range(0,numero):
    palabra=raw_input("Escribe una palabra:")
    lista.append(palabra)
print "La lista creada es:", lista
lista.sort()
print lista