"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 4 - Exercici 11(opcional) -
Exercici 11(opcional)
Escriu un programa que demani un nombre i retorni els seus divisors."""

print "Introduce un n�mero:"
numero=int(raw_input())
variable=numero
print "Los divisores de", numero, "son:",
for i in range(numero,0,-1):
    if numero%i==0:
        print i,
