"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 4:Escriu un programa que te demani dos nombres,
de manera que el segon sigui major que el primer. El programa termina escrivint els dos nombre tal
i com es demana. """

print "Escribe un n�mero:"
numero_menor=int(raw_input())
print "Escribe un n�mero mayor que", numero_menor,":"
numero_mayor=int(raw_input())
if numero_mayor>numero_menor:
    print "Los n�meros que has escrito son", numero_menor, "y", numero_mayor,"."
else:
    while numero_mayor<=numero_menor:
        print numero_mayor, "no es mayor que", numero_menor, ". Introduce de nuevo un n�mero:"
        numero_mayor=int(raw_input())
        if numero_mayor>numero_menor:
            print "Los n�meros que has escrito son", numero_menor, "y", numero_mayor,"."
