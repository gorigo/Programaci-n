"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 8: Escriu un programa que et demani primer un nombre i despr�s et demani nombres fins a qu� la
suma dels nombres introdu�ts coincideixi amb el nombre inicial. El programa termina escribint la
llista de nombres.  
 """

lista=[]
print "Introduce un n�mero a alcanzar:"
n_limite=int(raw_input())
print "Introduce otro n�mero:"
valor=int(raw_input())
aux=valor
if valor==n_limite:
    lista.append(valor)
    print "El n�mero a alcanzar es", n_limite, ". La lista creada es", lista
while valor>n_limite:
    print "El n�mero", valor, "es demasiado grande."
    print "Introduce otro n�mero"
    valor=int(raw_input())
    aux=valor
    if aux<n_limite:
        lista.append(valor)
        while aux<n_limite:
            print "Escribe otro n�mero:"
            valor=int(raw_input())
            lista.append(valor)
            aux=aux+valor
            if aux>n_limite:
                print "El n�mero", valor, "es demasiado grande."
                aux=aux-valor
                while aux<n_limite:
                    print "Escribe otro n�mero:"
                    valor=int(raw_input())
                    lista.append(valor)
                    aux=aux+valor
            if aux==n_limite:
                print "El l�mite a alcanzar es", n_limite, ". La lista creada es", lista
if valor<n_limite:
    lista.append(valor)
    while aux<n_limite:
        print "Escribe otro n�mero:"
        valor=int(raw_input())
        lista.append(valor)
        aux=aux+valor
        if aux>n_limite:
            print "El n�mero", valor, "es demasiado grande."
            del lista[-1]
            aux=aux-valor
            while aux<n_limite:
                print "Escribe otro n�mero:"
                valor=int(raw_input())
                lista.append(valor)
                aux=aux+valor
        if aux==n_limite:
            print "El l�mite a alcanzar es", n_limite, ". La lista creada es", lista
