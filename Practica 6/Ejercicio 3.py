# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio3: Escribe un programa que permita crear una lista de palabras y
que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
"""
print "Dime cuántas palabras tiene la lista:"
numero=int(raw_input())
lista=[]
for i in range(0,numero):
    palabra=raw_input("Escribe una palabra:")
    lista.append(palabra)
print "La lista creada es:", lista
palabra=raw_input("Escribe la palabra que quieres cambiar:")
cambio=raw_input("Escribe la palabra que quieres poner en su lugar:")
posicion=lista.index(palabra)
lista.remove(palabra)
lista.insert(posicion,cambio)
print "La lista modificada es:", lista