"""Sergio Rigo García - DAW1 - PRÁCTICA 4 - EJERCICIO 13:
Escriu un programa que imprimeixi les taules de multiplicar del 0 al 9
"""
print "Tablas de multiplicar"
aux=0
for i in range (0,11,1):
    print "Tabla del", i
    for aux in range (0,11,1):
        print i*aux
        
    
