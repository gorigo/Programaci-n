# coding=utf-8
"""Sergio Rigo García - DAW 1 - Práctica 7 - Ejercicio 3:Escribe un programa que lea una frase, y la pase como parámetro
a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea. """

def funcion_1(frase=raw_input("Escribe una frase:")):
    for i in range(0, len(frase)):
        print frase[i]
funcion_1()