"""Sergio Rigo García - DAW1 - PRÁCTICA 5 - EJERCICIO 9: Escriu un programa que et demani noms de persones i els seus números de telèfon. Per a
terminar de escriure nombres i numeros s'ha de pulsar Intro quan et demani el nom. El programa
termina escribint noms i números de telèfon. Nota: La llista en la que es guarden els noms i
números de telèfon és [ [nom1, telef1], [nom2, telef2], [nom3, telef3], etc] .  
"""

lista=[]
print "Introduce el nombre:"
nombre=raw_input()
if nombre !="":
    print "Introduce número de teléfono:"
    numero=int(raw_input())
    lista.append([nombre,numero])
if nombre=="":
    print "No has introducido ningún dato"
lista.append([nombre,numero])
while nombre!="":
    print "Introduce el nombre:"
    nombre=raw_input()
    if nombre !="":
        print "Introduce número de teléfono:"
        numero=int(raw_input())
        lista.append([nombre,numero])
    if nombre=="":
        print "Los nombres y sus números de teléfono son:"
        for i in lista:
            print i
    
        
