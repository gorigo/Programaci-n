# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio 05: Escribe un programa que permita crear dos listas de
palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.
"""
print "Dime cuántas palabras tiene la lista:"
numero=int(raw_input())
lista=[]
for i in range(0,numero):
    palabra=raw_input("Escribe una palabra:")
    lista.append(palabra)
print "La lista creada es:", lista
print "Dime cuántas palabras tiene la lista de palabras a eliminar:"
numero2=int(raw_input())
lista2=[]
for i in range(0,numero2):
    palabra=raw_input("Escribe una palabra:")
    lista2.append(palabra)
print "La lista de palabras a eliminar es:", lista2
for i in range (len(lista2)):
    eliminar=lista2.pop()
    if eliminar in lista:
        lista.remove(eliminar)
print "La lista con las palabras eliminadas queda así:", lista