"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 3 - Ejercicio 5 -
Escribe un programa que pida una temperatura en grados Fahrenheit y que escriba esa
temperatura en grados Celsius. La relaci�n entre grados Celsius (C) y grados Fahrenheit (F) es la
siguiente:
F - 32 = 1,8 * C """

print "Introduce �F"
F=float(raw_input())
C=(F-32)/1.8
print F , "�F son" , C , "�C"
