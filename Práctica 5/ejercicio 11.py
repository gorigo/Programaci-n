"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 11:Escriu un programa per a jugar a endivinar un nombre (l'ordinador �pensa� el nombre i l'usuari l'ha
d'endevinar). El programa comen�a demanant entre qu� nombres est� el nombre a endevinar,
s'�inventa� un nombre a l'atzar i despr�s l'usuari va probant valors i el programa va decidint si s�n
massa grans o petits.
"""
import random
import time

random.seed(time.time())


v_minimo=int(raw_input("Introduce el valor m�nimo:"))
v_maximo=int(raw_input("Introduce el valor m�ximo:"))
v_secreto=random.randint(v_minimo,v_maximo)

print "Adivina el n�mero entre", v_minimo, "y", v_maximo,
numero=int(raw_input("Introduce un numero:"))
while numero<v_secreto:
    print "El n�mero que has introducido es inferior, int�ntalo de nuevo."
    numero=int(raw_input("Introduce un n�mero:"))
while numero>v_secreto:
    print "El n�mero que has introducido es superior, int�ntalo de nuevo."
    numero=int(raw_input("Introduce un n�mero:"))
if numero==v_secreto:
    print "�Correcto!"
