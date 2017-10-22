"""Sergio Rigo García - DAW1 - PRÁCTICA 4 - Ejercicio 08 -
Escribe un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades
son. Recuerda que una gruesa son doce docenas. """

print "Escribe una cantidad(sin decimales)"
numero=int(raw_input())
gruesas=numero//144
docena=numero%144//12
unidades=numero%12
print numero, "unidades son", gruesas, "gruesas", docena, "docenas y", unidades, "unidades."
