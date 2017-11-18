# coding=utf-8
"""Sergio Rigo García - DAW 1 - Práctica 7 - Ejercicio 8: Escribe un programa que pida una frase, y pase la frase como
parámetro a una función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá
por pantalla el resultado final. """

frase=raw_input("Dime una frase:")

def espacios(frase):
    for i in frase:
        if i==" ":
            return i.replace("")

print espacios()