"""Sergio Rigo García - DAW1 - PRÁCTICA 3 - Ejercicio 4 -
Escribe un programa que pida una temperatura en grados Celsius y que escriba esa temperatura
en grados Fahrenheit. La relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente:
F - 32 = 1,8 * C"""

print "Introduce ºC"
C=float(raw_input())
F=C*1.8+32

print C , "ºC son" , F , "ºF"
