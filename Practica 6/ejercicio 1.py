# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio1: Escribe un programa que permita crear una lista de palabras.
Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
Por último, el programa tiene que escribir la lista.
"""

print "Dime cuántas palabras tiene la lista:"
numero=int(raw_input())
lista=[]
for i in range(0,numero):
    palabra=raw_input("Escribe una palabra:")
    lista.append(palabra)
print "La lista creada es:", lista
