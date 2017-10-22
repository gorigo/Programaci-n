"""Sergio Rigo García - DAW1 - PRÁCTICA 3 - Ejercicio 07 -
Escribe un programa que pida una cantidad de segundos y que escriba cuántas horas y minutos
son. """

print "Introduce segundos"
s=float(raw_input())
m=s/60
h=m//60
mn=m%60
a=int(mn)
b=abs(mn) - abs(int(mn))
sec=b*60
print int(s) , "segundos son" , int(h) , "horas," , int(a) , "minutos y" ,int(sec) , "segundos"
