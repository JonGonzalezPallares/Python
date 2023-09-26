#!/usr/bin/env python3

print("Ejercicios de funciones")

'''
print("\nEjercicio 1")
def saludo():
    print("¡Hola mundo!")
    return

saludo()

print("\nEjercicio 2")
def saludo(nombre):
    print("¡Hola {}!".format(nombre))
    return

saludo("Jon")

print("\nEjercicio 3")
def factorial(num):
    factor = 1
    for i in range(num):
        factor *= i+1
    return factor

print(factorial(3))

print("\nEjercicio 4")
#Valor por defecto de iva=21, si no se le pasa nada
def calculo(cantidad, iva=21):
    cal = (cantidad*iva)/100
    final = cal+cantidad
    return final

print("Sin iva ",23)
print("Con iva ", calculo(23, 2))

print("\nEjercicio 5")
import math
def circuloArea (radio):
    area = math.pi*(radio**2)
    return area

def cilindroVol (radio, altura):
    volumen = circuloArea(radio)*altura
    return volumen

print(cilindroVol(3, 5))

print("\nEjercicio 6")
def media(numerosLis):
    cal = sum(numerosLis)/len(numerosLis)
    return(cal)

numeros = [1, 2, 3]
print(media(numeros))

print("\nEjercicio 7")
def cuadrados(numerosLis):
    cuadradosLis = []
    for i in numerosLis:
        cuadradosLis.append(i**2)
    return cuadradosLis

numeros = [0, 1, 2, 3]
print(cuadrados(numeros))

print("\nEjercicio 8")
import math
def calculos(numerosLis):
    final = {}
    media = sum(numerosLis)/len(numerosLis)
    #Lista de los numeros que hemos pasado, de manera cuadrado
    cuadrados = []
    for i in numerosLis:
        cuadrados.append(i**2)
    varianza = (sum(cuadrados)/len(numerosLis))-(media**2)
    desviacion = round(math.sqrt(varianza), 2)
    
    final["media"]=media
    final["varianza"]=varianza
    final["desviacion"]=desviacion

    return final

numeros = [0, 1, 2, 3]
print(calculos(numeros))
'''

print("\nEjercicio 9")