#!/usr/bin/env python3

'''
import sys

#Para recoguer y mostrar el dato pasado por consola, en este caso si no le pasamos nada da error
param1 = sys.argv[1]
print(param1)

nombre = "Jon"
apellido = "Gonzalez"
print("Ejemplo de Strings:")
print(nombre)
print(apellido+"\n")
print("Hello {} {}!\nFormat por defecto\n".format(nombre, apellido))
print("Hello {1} {0}!\nFormat con orden especificado\n".format(nombre, apellido))

print("\nEjemplo de booleanos:")
print("¿10 es mayor que 9?",10 < 9)
a = 200
b = 30
if a<b:
    print("{} es menor que {}".format(a, b))
else:
    print("{} es mayor que {}".format(a, b))

print("\nEjemplos del bool true:")
print(bool(a))
print(bool(15))
print(bool())

print("\nEjemplos del bool falso:")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print("\nOperadores aritmeticos:")
print("+ suma, - resta, * multiplicacion, / division, % modulo (devuelve el resto de la division), ** exponentes, // 'floor divisor' (redondea el resultado al numero entero más bajo y cercano)")

print("\nOperadores de identificación")
x = 2
y = "s"
print("x is y, devuelve TRUE si las dos variables son el mismo objeto:")
print(x is y)

print("x is not y, devuelve TRUE si las dos variables NO son el mismo objeto:")
print(x is not y)
'''

print("\nPruebas con bits: https://www.w3schools.com/python/python_operators.asp")

print("\nProbando texto con numeros")
print("Repeticiones del texto"*2)
par = "23"
var = int(par)
print(var+3)