"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 4 - EJERCICIO 2: Escriu un programa que demani dos nombres i escrigui quins nombres son parells i quins s�n
senars (=�impares�) des del primer fins al segon."""

print "Introduce un n�mero"
num=int(raw_input())
print "Introduce un n�mero mayor que el anterior"
num2=int(raw_input())

for i in range(num,num2+1):
    if i%2==0:
        print i, "es un n�mero par"
    else:
        print i, "es un n�mero impar"


    
