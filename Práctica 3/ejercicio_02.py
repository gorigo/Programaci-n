"""Sergio Rigo García - DAW1 - PRÁCTICA 3 - Ejercicio 2 -
Escribe un programa que pida el peso y la altura de una persona y que calcule su índice de masa
corporal (imc). El imc se calcula con la fórmula imc = peso / altura2"""

print "Introduce tu peso(kg)"
p=float(raw_input())
print "Introduce tu altura(m)"
a=float(raw_input())
imc=p/a**2

print "Si pesas" , p , "kg y tu altura es de" , a , "m, entonces tu imc es de" , imc
