#!/usr/bin/env python3

print("Ejercicios de cadenas de caracteres")

'''
print("\nEjercicio 1")
nombre = input("Introduce tu nombre: ")
cantidad = int(input("Introduce la cantidad de veces que se va a repetir: "))
paso = 0
while paso<cantidad:
    print("\n", nombre)
    paso+=1

print("\nEjercicio 2")
nombre = input("Introduce tu nombre completo: ")
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

print("\nEjercicio 3")
nombre = input("Introduce tu nombre: ")
print(nombre, " tiene ", len(nombre) , " caracteres")

print("\nEjercicio 4")
telefono = input("Introduce un numero de telefono (formato: +xx-xxxxxxxxx-xx): ")
#Para cortar una cadena de caracteres
print("El numero de telefono es: ",telefono[4:-3])

print("\nEjerciico 5")
frase = input("Introduce una frase: ")
print(frase[::-1])

print("\nEjercicio 6")
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")
print(frase.replace(vocal, vocal.upper()))

print("\nEjercicio 7")
correo = input("Introduce tu correo: ")
separado = correo.split("@")
separado[1] = "ceu.es"
print(separado[0]+"@"+separado[1])

print("\nEjercicio 8")
precioT = input("Precio de producto: ")
precioD = precioT.split(".")
print("Euros del producto: "+precioD[0]+"\nCentimos del producto: "+precioD[1])

print("\nEjercicio 9")
fecha = input("Introduce tu fecha de nacimiento (formato: dd/mm/aaaa): ")
fechaS = fecha.split("/")
print("Tu dia es: "+fechaS[0]+"\nTu mes es: "+fechaS[1]+"\nTu año es: "+fechaS[2])

print("\nEjercicio 10")
productos = input("Introduce los productos separados por comas: ")
productosS = productos.split(",")
paso = 0
while paso<len(productosS):
    posicion = paso+1
    print("Producto ",posicion,": ",str(productosS[paso]))
    paso += 1
'''

print("\nEjercicio 11")
nombre = input("Introduce el nombre de un producto: ")
precio = float(input("Introduce su precio: "))
unidades = int(input("Introduce el numero de unidades: "))

print("{nombre}: {unidades} unidades x {precio}€ = {total}€".format(nombre=nombre, unidades=unidades, precio=round(precio, 2), total=round((precio*unidades), 2)))
