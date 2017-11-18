# coding=utf-8
"""Sergio Rigo García - DAW 1 - Práctica 7 - Ejercicio 5: Escribe un programa que te pida una frase y una vocal, y pase
estos datos como parámetro a una función que se encargará de cambiar todas las vocales de la frase por la vocal
seleccionada. Devolverá la función la frase modificada, y el programa principal la imprimirá"""


vocales=["a","e","i","o","u"]


frase=raw_input("Escribe una frase:")
vocal=raw_input("Escribe una vocal:")

def cambiarfrase(frase,v):
    for i in frase:
        if i in vocales:
            f2=frase.replace(i,v)
    return f2
print cambiarfrase(frase,vocal)