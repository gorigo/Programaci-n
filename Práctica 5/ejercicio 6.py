"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 6: Escriu un programa que demani primer dos nombres (m�xim i m�nim) i que despr�s te demani 2
nombres situats entre ells. Per a terminar d'escriure nombres, escriu un nombre que no sigui
compr�s entre els dos valors inicials. El programa termina escribint la llista de nombres.  """

lista=[]
print "Introduce un n�mero:"
n_menor=int(raw_input())
print "Introduce un n�mero mayor que", n_menor,":"
n_mayor=int(raw_input())
if n_mayor<=n_menor:
    while n_mayor<=n_menor:
        print n_mayor, "no es mayor que", n_menor, ". Introduce un n�mero v�lido:"
        n_mayor=int(raw_input())
if n_mayor>n_menor:
    print "Introduce un n�mero entre", n_menor, "y", n_mayor, ":"
    numero=int(raw_input())
    while numero>n_menor and numero<n_mayor:
        lista.append(numero)
        print "Introduce un n�mero entre", n_menor, "y", n_mayor, ":"
        numero=int(raw_input())
        if numero<=n_menor or numero>=n_mayor:
            print "Los n�meros situados entre", n_menor, "y", n_mayor, "son:", lista
        
