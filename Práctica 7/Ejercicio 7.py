# coding=utf-8
"""Sergio Rigo García - DAW 1 - Práctica 7 - Ejercicio 7: Escribe un programa que lea una frase, y la pase como
parámetro a un procedimiento. El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá
por pantalla."""



def change(frase=raw_input("Escribe una frase:")):
    a=frase.count("a");
    e=frase.count("e");
    i=frase.count("i");
    o=frase.count("o");
    u=frase.count("u");
    print "La vocal 'a' aparece", a, "veces.";
    print "La vocal 'e' aparece", e, "veces.";
    print "La vocal 'i' aparece", i, "veces.";
    print "La vocal 'o' aparece", o, "veces.";
    print "La vocal 'u' aparece", u, "veces.";
change()