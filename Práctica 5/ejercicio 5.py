"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 5: Escriu un programa que te demani dos nombres
cada vegada m�s grans i els guardi en una llista.Per a terminar d'escriure els nombres, escriu un
nombre que no sigui major a l'anterior. El programa termina escribint la llista de nombres. """

lista=[]
print "Introduce un n�mero:"
numero=int(raw_input())
lista.append(numero)
aux=numero
print "Introduce un n�mero mayor que", numero,"o uno menor para mostrar la lista:"
numero=int(raw_input())
if numero<=aux:
    print "El n�mero que has escrito es", lista
else:
    while numero>aux:
        lista.append(numero)
        aux=numero
        print "Escribe un n�mero mayor que", numero,"o uno menor para mostrar la lista:"
        numero=int(raw_input())
        if numero<=aux:
            print "Los n�meros que has escrito son", lista,
