"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 3 - Ejercicio 4 -
Escribe un programa que pida una temperatura en grados Celsius y que escriba esa temperatura
en grados Fahrenheit. La relaci�n entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente:
F - 32 = 1,8 * C"""

print "Introduce �C"
C=float(raw_input())
F=C*1.8+32

print C , "�C son" , F , "�F"
