"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 2:Escriu un programa
que te demani nombres i els guardi en una llista. Per a terminar d'introduir
nombres, simplement pitja Enter. El programa termina escrivint la llista de nombres. 

"""
print "Escribe un n�mero para crear una lista que contenga ese n�mero:"
numero=raw_input()
lista=[]
if numero=="":
    print "La lista est� vac�a", lista
else:
        lista.append (int(numero))
        while numero<>"":
            print "Escribe otro n�mero para a�adirlo a la lista, o aprieta enter para mostrar la lista"
            numero=raw_input()
            if numero=="":
                print lista
            else:
                lista.append (int(numero))
        
