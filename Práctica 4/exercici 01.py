"""Sergio Rigo Garc�a - DAW1 - Pr�ctica 4 - Ejercicio 1
Escriu un programa que escrigui els seg�ents nombres (la separaci� entre nombre �s per a
facilitar-te sabre quants de nombres s'ha d'escriure en cada bucle) i en el que la funci� range que
utilitzis tengui un �nic argument (per exemple, per a la primera llista range(10))"""

for i in range(10): print i+1,
print '\n'
for i in range(10): i=i+1; print i*2,
print '\n'
for i in range(10): i=i+10; print i*2,
print '\n'
for i in range(6): i=i+2.5; print int(i*4),
print '\n'
aux=45
for i in range(9): aux+=-5; print aux,
