"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 4 - Exercici 11(opcional) -
Exercici 12(opcional)
Escriu un programa que demani un nombre i escrigui si �s primer o no."""

print "Escribe un n�mero:"
numero=int(raw_input())

for i in range(1,20):
    if numero/i>numero and numero%i<>0:
        print numero, "no es un n�mero primo"
    else:
        print numero, "es un n�mero primo"

    
