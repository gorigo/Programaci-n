# coding=utf-8
"""Sergio Rigo García - DAW 1 - Práctica 7 - Ejercicio 6: Escribe un programa que lea el nombre de una persona y un
carácter, le pase estos datos a una función que comprobará si dicho carácter está en su nombre. El resultado de dicha
función lo imprimirá el programa principal por pantalla. """

nombre=raw_input("Dime tu nombre:")
car=raw_input("Escrbe un carácter:")
a="el cáracter está en la cadena"
b="el carácter no está en la cadena"

def encontrar(nombre,car):
    nombre.find(car)
    if car in nombre:
        return a
    else:
        return b

print encontrar(nombre,car)