# coding=utf-8
"""Sergio Rigo García - DAW 1 - Práctica 7 - Ejercicio 4: Escribe un programa que pida una frase, y le pase como
parámetro a una función dicha frase. La función debe sustituir todos los espacios en blanco de una frase por un
asterisco, y devolver el resultado para que el programa principal la imprima por pantalla. """

def funcion_1(frase=raw_input("Escribe una frase:")):
    return frase.replace(" ", "*")
print funcion_1()