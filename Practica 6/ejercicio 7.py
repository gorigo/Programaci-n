# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio7:
Escribe un programa que permita crear dos listas de palabras y que, a continuación, escriba las
siguientes listas (en las que no debe haber repeticiones):
• Lista de palabras que aparecen en las dos listas
• Lista de palabras que aparecen en la primera lista, pero no en la segunda
• Lista de palabras que aparecen en la segunda lista, pero no en la primera
• Lista de palabras que aparecen en ambas listas
"""
print "Dime cuántas palabras tiene la lista:"
numero=int(raw_input())
lista=[]
lista_ambas=[]
lista_primera=[]
for i in range(0,numero):
    palabra=raw_input("Escribe una palabra:")
    lista.append(palabra)
    lista_ambas.append(palabra)
    lista_primera.append(palabra)
print "La lista creada es:", lista
print "Dime cuántas palabras tiene la segunda lista:"
numero2=int(raw_input())
lista2=[]
lista_repetida=[]
lista_segunda=[]
for i in range(0,numero2):
    palabra=raw_input("Escribe una palabra:")
    lista2.append(palabra)
    if palabra in lista:
        lista_repetida.append(palabra)
        lista_primera.remove(palabra)
    else:
        lista_segunda.append(palabra)
        lista_ambas.append(palabra)
print "La segunda lista de palabras es:", lista2
print "Las palabras que aparecen en las dos listas son:", lista_repetida
print "Las palabras que aparecen sólo en la primera lista son:", lista_primera
print "Las palabras que aparecen sólo en la segunda lista son:", lista_segunda
print "La lista de todas las palabras es:", lista_ambas