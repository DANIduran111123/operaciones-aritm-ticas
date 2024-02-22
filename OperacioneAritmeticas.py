#input 
X=int (input("digite el valor de x: "))
Y=int (input("digite el valor de y: "))

#procesiing

S= X+Y
R= X-Y
M= X*Y
D= X/Y
DE= X//Y
MOD= X%Y  
P= X**Y

# output 
print("-------------------")
print("La suma de " + str(X) + " + " + str(Y) + " es " + str(S))
print("La resta de " + str(X) + " - " + str(Y) + " es " + str(R))
print("La multiplicacion de " + str(X) + " * " + str(Y) + " es " + str(M))
print("La division de " + str(X) + " / " + str(Y) + " es " + str(D))
print("La division enterda de " + str(X) +  " // " + str(Y) + " es " + str(DE))
print("El modulo  de " + str(X) +  " % " + str(Y) + " es " + str(MOD))
print("La potencia de " + str(X) +  " ** " + str(Y) + " es " + str(P))
print("-------------------")