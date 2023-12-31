print("Programacino funcional")
from math import sin, cos, tan, exp, log

'''
print("\nEjercicio 1")
def descuento(price, discount):
    #Función que aplica un descuento a una cantidad.
    #Parámetros:
    #    price: Es un valor real con el precio al que aplicar el descuento.
    #    discount: Es el porcentaje a descontar.
    #Devuelve:
    #    El precio final tras aplicar el descuento.
    return price - price * discount / 100
def Iva(price, percentage):
    #Función que aplica un IVA a una cantidad.
    #Parámetros:
    #    price: Es un valor real con el precio al que aplicar el IVA.
    #    percentage: Es el porcentaje del IVA a aplicar.
    #Devuelve:
    #    El precio final tras aplicar el IVA.
    return price + price * percentage / 100
def cesta(basket, function):
    #Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.
    #Parámetros:
    #    basket: Es un diccionario formado por pares precio:descuento.
    #    function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    #Devuelve:
    #    El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total
print('El precio de la compra tras aplicar los descuentos es: ', cesta({1000:20, 500:10, 100:1}, descuento))

print("\nEjercicio 2")
def calcular(value, funct):
    funciones = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = funciones[funct](value)
    print(result)

valor = int(input("Introduce un valor: \n"))
funcion = input("Escoge una funcion: sin, cos, tan, exp, log \n")
calcular(valor, funcion)

print("\nEjercicio 3")
def aplicar(funcion, lista):
    lis = []
    for i in lista:
        lis.append(funcion(i))
    return lis
def cuadrado(n):
    return n*n

print(aplicar(cuadrado, [1, 2, 3, 4]))

print("\nEjercicio 4")
def aplicar(lista):
    lis = []
    for i in lista:
        if pares(i):
            lis.append(i)
    return lis
def pares(n):
    return n % 2 == 0

print(aplicar(pares, [1, 2, 3, 4]))
'''

print("\nEjercicio 5")
