"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 7: Escriu un programa que demani un nombre (l�mit) i despr�s et demani nombres fins a qu� la suma
dels nombres introduits superi un nombre inicial. El programa termina escribint la llista de
nombres.  """
lista=[]
print "Introduce un n�mero l�mite:"
n_limite=int(raw_input())
print "Introduce otro n�mero:"
valor=int(raw_input())
if valor>=n_limite:
    lista.append(valor)
    print "El l�mite a superar es", n_limite, ". La lista creada es", lista
else:
    lista.append(valor)
    aux=valor
    while aux<n_limite:
        print "Escribe otro n�mero:"
        valor=int(raw_input())
        lista.append(valor)
        aux=aux+valor
        if aux>=n_limite:
            print "El l�mite a superar es", n_limite, ". La lista creada es", lista
