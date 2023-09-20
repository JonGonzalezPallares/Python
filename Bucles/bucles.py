#!/usr/bin/env python3

print("Ejercicios de bucles")

'''
print("\nEjercicio 1")
palabra = input("Introduce una palabra: ")

#Opcion 1 -> pone las palabras una detras de otra
print(palabra*10)

#Opcion 2 -> pone las palabras en diferentes lineas
for i in range(10):
    print(palabra)

print("\nEjercicio 2")
edad = int(input("Introduzca su edad: "))

#Opcion 1 -> usando la funcion while
paso=1
while(paso<=edad):
    print(paso)
    paso+=1

#Opcion 2 -> usando la funcion range
for i in range(edad):
    print(i+1)

print("\nEjercicio 3")
numero = int(input("Introduce un numero entero positivo: "))
paso=1
resultado=""
while(paso<=numero):
    if((paso%2)!=0):
        if(resultado==""):
            resultado = str(paso)
        else:
            resultado = resultado+", "+str(paso)
    paso+=1
print(resultado)

print("\nEjercicio 4")
numero = int(input("Introduce un numero entero positivo: "))
paso=numero
resultado=""
while(numero>=0):
    if(paso==numero):
        resultado = str(numero)
    else:
        resultado = resultado+", "+str(numero)
    numero-=1
print(resultado)

print("\nEjercicio 5")
invertir = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interes anual: "))
anios = int(input("Introduce la cantidad de años: "))
final = 0
for i in range(anios):
    if(final==0):
        final = invertir+(invertir*(interes/100))
    else:
        final = final+(final*(interes/100))
    print("Capital obtenido: {final}".format(final=final))
'''