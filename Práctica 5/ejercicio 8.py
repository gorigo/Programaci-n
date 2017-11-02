"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 8: Escriu un programa que et demani primer un nombre i després et demani nombres fins a què la
suma dels nombres introduïts coincideixi amb el nombre inicial. El programa termina escribint la
llista de nombres.  
 """

lista=[]
print "Introduce un número a alcanzar:"
n_limite=int(raw_input())
print "Introduce otro número:"
valor=int(raw_input())
aux=valor
if valor==n_limite:
    lista.append(valor)
    print "El número a alcanzar es", n_limite, ". La lista creada es", lista
while valor>n_limite:
    print "El número", valor, "es demasiado grande."
    print "Introduce otro número"
    valor=int(raw_input())
    aux=valor
    if aux<n_limite:
        lista.append(valor)
        while aux<n_limite:
            print "Escribe otro número:"
            valor=int(raw_input())
            lista.append(valor)
            aux=aux+valor
            if aux>n_limite:
                print "El número", valor, "es demasiado grande."
                aux=aux-valor
                while aux<n_limite:
                    print "Escribe otro número:"
                    valor=int(raw_input())
                    lista.append(valor)
                    aux=aux+valor
            if aux==n_limite:
                print "El límite a alcanzar es", n_limite, ". La lista creada es", lista
if valor<n_limite:
    lista.append(valor)
    while aux<n_limite:
        print "Escribe otro número:"
        valor=int(raw_input())
        lista.append(valor)
        aux=aux+valor
        if aux>n_limite:
            print "El número", valor, "es demasiado grande."
            del lista[-1]
            aux=aux-valor
            while aux<n_limite:
                print "Escribe otro número:"
                valor=int(raw_input())
                lista.append(valor)
                aux=aux+valor
        if aux==n_limite:
            print "El límite a alcanzar es", n_limite, ". La lista creada es", lista
