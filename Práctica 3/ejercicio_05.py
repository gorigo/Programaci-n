"""Sergio Rigo García - DAW1 - PRÁCTICA 3 - Ejercicio 5 -
Escribe un programa que pida una temperatura en grados Fahrenheit y que escriba esa
temperatura en grados Celsius. La relación entre grados Celsius (C) y grados Fahrenheit (F) es la
siguiente:
F - 32 = 1,8 * C """

print "Introduce ºF"
F=float(raw_input())
C=(F-32)/1.8
print F , "ºF son" , C , "ºC"
