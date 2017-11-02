"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 5: Escriu un programa que te demani dos nombres
cada vegada més grans i els guardi en una llista.Per a terminar d'escriure els nombres, escriu un
nombre que no sigui major a l'anterior. El programa termina escribint la llista de nombres. """

lista=[]
print "Introduce un número:"
numero=int(raw_input())
lista.append(numero)
aux=numero
print "Introduce un número mayor que", numero,"o uno menor para mostrar la lista:"
numero=int(raw_input())
if numero<=aux:
    print "El número que has escrito es", lista
else:
    while numero>aux:
        lista.append(numero)
        aux=numero
        print "Escribe un número mayor que", numero,"o uno menor para mostrar la lista:"
        numero=int(raw_input())
        if numero<=aux:
            print "Los números que has escrito son", lista,
