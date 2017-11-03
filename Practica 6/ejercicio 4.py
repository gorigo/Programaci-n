# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio4:
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y elimine esa palabra de la lista.
"""
print "Dime cuántas palabras tiene la lista:"
numero=int(raw_input())
lista=[]
for i in range(0,numero):
    palabra=raw_input("Escribe una palabra:")
    lista.append(palabra)
print "La lista creada es:", lista
palabra=raw_input("Escribe la palabra que quieres eliminar:")
posicion=lista.index(palabra)
lista.remove(palabra)
print "La lista ahora es:", lista