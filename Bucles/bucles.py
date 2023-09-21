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

print("\nEjercicio 6")
numero = int(input("Introduce un numero: "))
paso=1
texto = "*"
while(paso<=numero):
    print(texto)
    texto=texto+"*"
    paso+=1

print("\nEjercicio 7")
num2=0
for num1 in range(11):
    print("Tabla del {}".format(num1))
    for num2 in range(11):
        print("{} x {} = {}".format(num1, num2, num1*num2))

print("\nEjercicio 8")
numero = int(input("Introduce un numero entero: "))
paso = 1
cambiante = 1
texto = ""
while(paso<=numero):
    texto= str(cambiante)+ " "+ texto
    print(texto)
    cambiante += 2
    paso+=1

print("\nEjercicio 9")
contrasenia = "contraseña"
con = input("Introduce la contraseña: ")
while(con.lower()!=contrasenia):
    con = input("Vuelve a introducir la contraseña: ")
print("Contraseña correcta")

print("\nEjercicio 10")
numero = int(input("Introduce un numero entero: "))
#Funcion para comprobar si un numero es primo
def is_prime(num):
    for i in range(2, num):
        if(num%i)==0:
            return False
        return True
    
if(is_prime(numero)):
    print("El numero es primo")
else:
    print("El numero no es primo")

print("\nEjercicio 11")
palabra = input("Introduce una palabra: ")
#Mi solucion
paso = len(palabra)
while(paso>=0):
    print(palabra[paso-1:paso])
    paso-=1

#Otra solucion
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])

print("\nEjercicio 12")
frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
cantidad = 0
while(len(letra)>1):
    letra = input("Introduce una sola letra: ")
for i in range(len(frase)):
    if(frase[i].lower == letra.lower):
        cantidad+=1
print("La letra {} se repite {} veces en la frase".format(letra, cantidad))
'''

print("\nEjercicio 13")
escrito = input()
while(escrito!="salir"):
    print(escrito)
    escrito = input()