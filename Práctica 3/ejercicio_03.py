"""Sergio Rigo García - DAW1 - PRÁCTICA 3 - Ejercicio 3 -
Escribe un programa que pida una distancia en pies y pulgadas y que escriba esa distancia en
centímetros. Recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm. """

print "Escribe una cantidad de pies"
pies=float(raw_input())
print "Escribe una cantidad de pulgadas"
pulg=float(raw_input())
cm=((pies*12)+pulg)*2.54
print pies , "y" , pulg , "es igual a" , cm , "cm"
