#!/usr/bin/env python3

print("Ejercicios de condicionales")

'''
print("\nEjercicio 1")
edad = input("Introduce tu edad: ")
if (edad>=18):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

print("\nEjercicio 2")
correcto = "CONTRASEÑA"
contrasenia = input("Introduce la contraseña: ")
if(correcto.lower() == contrasenia.lower()):
    print("Las contraseñas son la misma")
else:
    print("Las contraseñas son diferentes")

print("\nEjercicio 3")
numeroUno = int(input("Introduce un numero: "))
numeroDos = int(input("Introduce otro numero: "))
if(numeroDos==0):
    print("Error al dividir por 0")
else:
    print("{uno}/{dos} = {resultado}".format(uno=numeroUno, dos=numeroDos, resultado=(numeroUno/numeroDos)))

print("\nEjercicio 4")
numero = int(input("Introduce un numero: "))
if(numero%2):
    print("El numero {numero} es impar".format(numero=numero))
else:
    print("El numero {numero} es par".format(numero=numero))

print("\nEjercicio 5")
edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos: "))
if(edad>16 and ingresos>=1000):
    print("Tienes que tributar")
else:
    print("No tienes que tributar")

print("\nEjercicio 6")
#No he sabido hacer la parte del nombre
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M o H): ")

#Primera opcion
if(sexo=="M"):
    if(nombre.lower() < "m"):
        grupo = "A"
    else:
        grupo = "B"
else:
    if(nombre.lower() > "n"):
        grupo = "A"
    else:
        grupo = "B"

#Segunda opcion
if((sexo=="M" and nombre.lower() < "m") or (sexo=="H" and nombre.lower() > "n")):
    grupo = "A"
else:
    grupo = "B"

print("Tu grupo es: ", grupo)

print("\nEjercicio 7")
renta = float(input("Introduzca su renta anual: "))
if(renta<10000):
    tipo=5
elif(10000<=renta<20000):
    tipo=15
elif(20000<=renta<35000):
    tipo=20
elif(35000<=renta<60000):
    tipo=30
else:
    tipo=45

print("Tienes que pagar: {total}€".format(total=(renta*(tipo/100))))

print("\nEjercicio 8")
puntuacion = float(input("Introduce la puntuacion obtenida: "))
if(puntuacion==0.0):
    print("Rendimiento inaceptable, dinero obtenido: {total}€".format(total=round((2400*0.0), 2)))
elif(puntuacion==0.4):
    print("Rendimiento aceptable, dinero obtenido: {total}€".format(total=round((2400*0.4), 2)))
elif(puntuacion>=0.6):
    print("Rendimiento meritorio, dinero obtenido: {total}€".format(total=round((24000*0.6), 2)))
else:
    print("Puntuacion no valida")

print("\nEjercicio 9")
edad = int(input("Introduce tu edad: "))
if(edad<4):
    print("No tiene que pagar")
elif(4<edad<18):
    print("Tiene que pagar 5€")
else:
    print("Tiene que pagar 10€")
'''

print("\nEjercicio 10")
print("Seleccione uno de los siguientes ingredientes: \n-Pimiento\n-Tofu\n-Peperoni\n-Jamón\n-Salmón")
ingrediente = input()
if(ingrediente.lower()=="pimiento" or ingrediente.lower()=="tofu"):
    print("Su pizza es vegetariana y contiene los siguientes ingredientes: mozzarela, tomate y {ingr}".format(ingr=ingrediente))
elif(ingrediente.lower()=="peperoni" or ingrediente.lower()=="jamon" or ingrediente.lower()=="jamon" or ingrediente.lower()=="salmón" or ingrediente.lower()=="salmon"):
    print("Su pizza es no vegetariana y contiene los siguientes ingredientes: mozzarela, tomate y {ingr}".format(ingr=ingrediente))
else:
    print("No tenemos ese ingrediente")