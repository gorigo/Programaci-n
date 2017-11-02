"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 3 -
Escriu un programa que demani notes i les guardi en una llista. Per a terminar d'introduir notes,
escriu una nota que no estigui entre 0 i 10. El programa termina escrivint la llista de notes. 

"""
print "Escribe una nota para crear una lista que contenga esa nota:"
nota=float(raw_input())
lista=[]
if nota>10 or nota<0:
    print "No has introducido ninguna nota válida", lista
else:
    lista.append(nota)
    while nota<=10 or nota>=0:
        print "Escribe otra nota para añadirla a la lista, o escribe un número queno esté entre 0 y 10 para mostrarla:"
        nota=float(raw_input())
        lista.append(nota)
        if nota >10 or nota<0:
            lista.pop()
            print lista
            break
