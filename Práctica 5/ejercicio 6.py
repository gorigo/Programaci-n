"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 6: Escriu un programa que demani primer dos nombres (màxim i mínim) i que després te demani 2
nombres situats entre ells. Per a terminar d'escriure nombres, escriu un nombre que no sigui
comprès entre els dos valors inicials. El programa termina escribint la llista de nombres.  """

lista=[]
print "Introduce un número:"
n_menor=int(raw_input())
print "Introduce un número mayor que", n_menor,":"
n_mayor=int(raw_input())
if n_mayor<=n_menor:
    while n_mayor<=n_menor:
        print n_mayor, "no es mayor que", n_menor, ". Introduce un número válido:"
        n_mayor=int(raw_input())
if n_mayor>n_menor:
    print "Introduce un número entre", n_menor, "y", n_mayor, ":"
    numero=int(raw_input())
    while numero>n_menor and numero<n_mayor:
        lista.append(numero)
        print "Introduce un número entre", n_menor, "y", n_mayor, ":"
        numero=int(raw_input())
        if numero<=n_menor or numero>=n_mayor:
            print "Los números situados entre", n_menor, "y", n_mayor, "son:", lista
        
