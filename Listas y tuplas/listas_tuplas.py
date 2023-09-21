#!/usr/bin/env python3

print("Ejercicios de listas y tuplas")

'''
print("\nEjercicio 1")
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
print(asignaturas)

print("\nEjercicio 2")
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
for i in asignaturas:
    print("Yo estudio "+i)

print("\nEjercicio 3")
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for i in asignaturas:
    nota = float(input("¿Qué nota has sacado en {}? ".format(i)))
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En {} has sacado {}".format(asignaturas[i], notas[i]))

print("\nEjercicio 4")
numeros = []
for i in range(8):
    numero = int(input("Introduce el numero ganador de la loteria"))
    numeros.append(numero)
numeros.sort()
print(numeros)

print("\nEjercicio 5")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()
print(numeros)
'''

print("\nEjercicio 6")
#Guardar las asignaturas que se hayan aprobado para poder borrarlo luego
'''
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for i in asignaturas:
    nota = float(input("¿Qué nota has sacado en {}? ".format(i)))
    notas.append(nota)
for i in range(len(asignaturas)):
    if(notas[i]>5):
        print(i)
print("Las asignaturas que tienes que repetir son: ")
for i in asignaturas:
    print(i)
'''