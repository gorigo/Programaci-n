# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio6:
Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una
segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear
una lista distinta)
"""
print "Dime cuántas palabras tiene la lista:"
numero=int(raw_input())
lista=[]
for i in range(0,numero):
    palabra=raw_input("Escribe una palabra:")
    lista.append(palabra)
print "La lista creada es:", lista
lista2=lista[:]
lista2.reverse()
print"La lista inversa es:", lista2