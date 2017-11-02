"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 7: Escriu un programa que demani un nombre (límit) i després et demani nombres fins a què la suma
dels nombres introduits superi un nombre inicial. El programa termina escribint la llista de
nombres.  """
lista=[]
print "Introduce un número límite:"
n_limite=int(raw_input())
print "Introduce otro número:"
valor=int(raw_input())
if valor>=n_limite:
    lista.append(valor)
    print "El límite a superar es", n_limite, ". La lista creada es", lista
else:
    lista.append(valor)
    aux=valor
    while aux<n_limite:
        print "Escribe otro número:"
        valor=int(raw_input())
        lista.append(valor)
        aux=aux+valor
        if aux>=n_limite:
            print "El límite a superar es", n_limite, ". La lista creada es", lista
