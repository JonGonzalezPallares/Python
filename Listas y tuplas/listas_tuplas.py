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

print("\nEjercicio 6")
asignaturas = ["Matematicas",  "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
recuperar = []
for i in asignaturas:
    nota = float(input("¿Qué nota has sacado en {}? ".format(i)))
    notas.append(nota)
for i in range(len(asignaturas)):
    if(notas[i]<5):
        recuperar.append(asignaturas[i])
print("Las asignaturas que tienes que repetir son: ")
for i in recuperar:
    print(i)

print("\nEjercicio 7")
#Para guardar todo el abecedario
import string
abecedario = list(string.ascii_lowercase)
for i in abecedario:
    index = abecedario.index(i)
    if((index%3)==0):
        abecedario.pop(index-1)
print(abecedario)

print("\nEjercicio 8")
palabra = input("Introduce una palabra: ")
revertida = palabra[::-1]
if(palabra==revertida):
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")

print("\nEjercicio 9")
palabra = input("Introduce una palabra: ")
vocales=[0, 0, 0, 0, 0]
for i in range(len(palabra)):
    letra = palabra[i].lower()
    if(letra==("a")):
        vocales[0]+=1
    elif(letra=="e"):
        vocales[1]+=1
    elif(letra=="i"):
        vocales[2]+=1
    elif(letra=="o"):
        vocales[3]+=1
    elif(letra=="u"):
        vocales[4]+=1
print("A aparece: {}\nE aparece: {}\nI aparece: {}\nO aparece: {}\nU aparece: {}".format(vocales[0], vocales[1], vocales[2], vocales[3], vocales[4]))

print("\nEjercicio 10")
precios = [50, 75, 46, 22, 80, 65, 8]
mostrar = [0, 0]
for i in precios:
    if(mostrar[0]==0):
        mostrar[0]=i
    elif(mostrar[1]==0):
        mostrar[1]=i
    elif(mostrar[0]<i):
        mostrar[0]=i
    elif(mostrar[1]>i):
        mostrar[1]=i
print("El numero mas alto es {} y el mas pequeño {}".format(mostrar[0], mostrar[1]))

print("\nEjercicio 11")
vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
producto = 0
for i in vector1:
    paso = (i*vector2[i-1])
    producto += paso
print("El producto escalar de los vectores: [1, 2, 3] y [-1, 0, 2] es : {}".format(producto))

print("\nEjercicio 12")
import numpy as np
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[-1, 0], [0, 1], [1, 1]]
producto = np.matmul(matriz1, matriz2)
print(producto)
'''

print("\nEjercicio 13")
import math
texto = input("Introduce una serie de numeros separados por comas: ")
divisor:int = texto.replace(" ", "").split(",")
total = 0
for i in divisor:
    total += int(i)    
media = total/(len(divisor))
suma = 0
for i in divisor:
    suma += (int(i)-media)**2
desviacion = round(math.sqrt(suma/len(divisor)), 2)
print("La media de los numeros es = {}\nLa desviacion tipica es = {}".format(media, desviacion))