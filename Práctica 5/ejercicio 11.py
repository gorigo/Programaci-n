"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 11:Escriu un programa per a jugar a endivinar un nombre (l'ordinador “pensa” el nombre i l'usuari l'ha
d'endevinar). El programa comença demanant entre què nombres està el nombre a endevinar,
s'”inventa” un nombre a l'atzar i després l'usuari va probant valors i el programa va decidint si són
massa grans o petits.
"""
import random
import time

random.seed(time.time())


v_minimo=int(raw_input("Introduce el valor mínimo:"))
v_maximo=int(raw_input("Introduce el valor máximo:"))
v_secreto=random.randint(v_minimo,v_maximo)

print "Adivina el número entre", v_minimo, "y", v_maximo,
numero=int(raw_input("Introduce un numero:"))
while numero<v_secreto:
    print "El número que has introducido es inferior, inténtalo de nuevo."
    numero=int(raw_input("Introduce un número:"))
while numero>v_secreto:
    print "El número que has introducido es superior, inténtalo de nuevo."
    numero=int(raw_input("Introduce un número:"))
if numero==v_secreto:
    print "¡Correcto!"
