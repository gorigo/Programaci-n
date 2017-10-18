print "Introduce precio del producto"
p=float(raw_input())
iva=(p*16)/100
pfinal=p+iva
print "El precio con IVA es" , pfinal , "€"
