# coding=utf-8
"""Sergio Rigo García - DAW1 - Práctica6 - Ejercicio10:
Escribe un programa que pida un número y a continuación escriba la lista de todos los divisores
del número (incluidos el uno y él mismo). """

print "Introduce un número:"
numero=int(raw_input())
variable=numero
lista=[]
print "Los divisores de", numero, "son:",
for i in range(numero,0,-1):
    if numero%i==0:
        lista.append(i)
lista.reverse()
print lista
