"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 9: Escriu un programa que et demani noms de persones i els seus n�meros de tel�fon. Per a
terminar de escriure nombres i numeros s'ha de pulsar Intro quan et demani el nom. El programa
termina escribint noms i n�meros de tel�fon. Nota: La llista en la que es guarden els noms i
n�meros de tel�fon �s [ [nom1, telef1], [nom2, telef2], [nom3, telef3], etc] .  
"""

lista=[]
print "Introduce el nombre:"
nombre=raw_input()
if nombre !="":
    print "Introduce n�mero de tel�fono:"
    numero=int(raw_input())
    lista.append([nombre,numero])
if nombre=="":
    print "No has introducido ning�n dato"
lista.append([nombre,numero])
while nombre!="":
    print "Introduce el nombre:"
    nombre=raw_input()
    if nombre !="":
        print "Introduce n�mero de tel�fono:"
        numero=int(raw_input())
        lista.append([nombre,numero])
    if nombre=="":
        print "Los nombres y sus n�meros de tel�fono son:"
        for i in lista:
            print i
    
        
