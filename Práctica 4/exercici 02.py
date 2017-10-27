"""Sergio Rigo García - DAW1 - PRÁCTICA 4 - EJERCICIO 2: Escriu un programa que demani dos nombres i escrigui quins nombres son parells i quins són
senars (=”impares”) des del primer fins al segon."""

print "Introduce un número"
num=int(raw_input())
print "Introduce un número mayor que el anterior"
num2=int(raw_input())

for i in range(num,num2+1):
    if i%2==0:
        print i, "es un número par"
    else:
        print i, "es un número impar"


    
