# coding=utf-8
"""Sergio Rigo García - DAW 1 - Práctica 7 - Ejercicio 1: Escribe un programa que pida un texto por pantalla, este texto
 lo pase como parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.
 """

def mi_funcion(texto=raw_input("Escribe un texto, por favor:")):
    print texto.lower()
    print texto.upper()
mi_funcion()