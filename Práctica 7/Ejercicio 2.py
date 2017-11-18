# coding=utf-8
"""Sergio Rigo García - DAW 1 - Práctica 7 - Ejercicio 2:Escribe un programa que lea el nombre y los dos apellidos de
una persona (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y
devolver una única cadena. La cadena final la imprimirá el programa por pantalla. """

def nombre_completo(nombre):
    return nombre+" "+apellido+" "+apellido2


nombre=raw_input("Escribe tu nombre:")
apellido=raw_input("Escribe tu primer apellido:")
apellido2=raw_input("Escribe tu segundo apellido:")

print (nombre_completo(nombre))
