"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 4 - EJERCICIO 3 - Escriu un programa que demani 2 nombres i escrigui la suma de sencers des del primer nombre
fins al segon.
"""

print "Introduce un n�mero"
num=int(raw_input())
print "Introduce un n�mero mayor que", num
num_2=int(raw_input())
aux=0
for i in range(num,num_2+1):
    aux=aux+i
print "La suma entre", num, "y", num_2, "es igual a", aux
        
