"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 2:Escriu un programa
que te demani nombres i els guardi en una llista. Per a terminar d'introduir
nombres, simplement pitja Enter. El programa termina escrivint la llista de nombres. 

"""
print "Escribe un número para crear una lista que contenga ese número:"
numero=raw_input()
lista=[]
if numero=="":
    print "La lista está vacía", lista
else:
        lista.append (int(numero))
        while numero<>"":
            print "Escribe otro número para añadirlo a la lista, o aprieta enter para mostrar la lista"
            numero=raw_input()
            if numero=="":
                print lista
            else:
                lista.append (int(numero))
        
