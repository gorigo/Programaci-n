"""Sergio Rigo Garc�a - DAW1 - PR�CTICA 5 - EJERCICIO 10: Escriu un programa que et demani els noms i notes d'alumnes. Si escrius una nota fora de
l'interval de 0 a 10, el programa entendr� que no vols introduir m�s notes d'aquest alumne. Si no
escrius el nom, el programa entendr� que no vols introduir m�s alumnes. Nota: La llista en la que
es guarden els noms i notes �s [ [nom1, nota1, nota2, etc], [nom2, nota1, nota2, etc], [nom3,
nota1, nota2, etc], etc] 
"""
lista=[]
print "Introduce el nombre del alumno:"
alumno=raw_input()
if alumno=="":
    print "No has introducido ning�n alumno."
else:
    while alumno!="":
        print "Introduce nota del alumno:"
        nota=float(raw_input())
        lista.append([alumno])
        if nota<=10 and nota>=0:
            lista[-1]+=[nota]
        while nota <=10 and nota>=0:
            print "Introduce nota del alumno:"
            nota=float(raw_input())
            if nota<=10 and nota>=0:
                lista[-1]+=[nota]
        if nota >10 or nota <0:
            print "Introduce nombre del alumno:"
            alumno=raw_input()
    if alumno=="":
        print "Los alumnos y sus respectivas notas son:"
        for i in lista:
            print i
            
        
