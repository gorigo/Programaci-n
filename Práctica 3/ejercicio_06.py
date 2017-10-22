"""Sergio Rigo García - DAW1 - PRÁCTICA 3 - Ejercicio 6 -
Escribe un programa que pida una cantidad de segundos y que escriba cuántos minutos
son. """

print "Introduce segundos"
s=float(raw_input())
m=s/60
a=int(m)
b=abs(m) - abs(int(m))
sec=b*60
print int(s) , "segundos son" , int(a) , "minutos y" , int(sec) , "segundos"
