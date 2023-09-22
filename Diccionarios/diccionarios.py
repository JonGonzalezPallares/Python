#!/usr/bin/env python3

print("Ejercicios de diccionarios")

'''
print("\nEjercicio 1")
divisasDic = {"Euro": "€", "Dolar":"$", "Yen":"¥"}
divisa = input("Introduce una divisa: ")
print(divisasDic.get(divisa, "No existe esa divisa"))

print("\nEjercicio 2")
persona = {"Nombre": "", "Edad": "", "Direccion": "", "Telefono": ""}
persona["Nombre"]=input("Introduce tu nombre: ")
persona["Edad"]=int(input("Introduce tu edad: "))
persona["Direccion"]=input("Introduce tu direccion: ")
persona["Telefono"]=int(input("Introduce tu telefono: "))
print(persona['Nombre'], 'tiene', persona['Edad'], 'años, vive en', persona['Direccion'], 'y su número de teléfono es', persona['elefono'])

print("\nEjercicio 3")
frutas = {"Platano":1.35, "Manzana": 0.8, "Pera": 0.84, "Naranja": 0.7}
fruta = input("Introduce una fruta: ")
kilos = float(input("Introduce cuantos kilos: "))
precio = frutas.get(fruta, "No existe esa fruta")
precioFinal = precio*kilos
print(kilos,"kg de ",fruta," cuestan: ",str(precioFinal))

print("\nEjercicio 4")
meses = {"01":"Enero", "02":"Febrero", "03":"Marzo", "04":"Abril", "05":"Mayo", "06":"Junio", "07":"Julio", "08":"Agosto", "09":"Septiembre", "10":"Octubre", "11":"Noviembre", "12":"Diciembre"}
fecha = input("Introduce una fecha (formato= dd/mm/aaaa): ")
fechaSep = fecha.split("/")
fechaSep[1]=meses.get(fechaSep[1], "No existe ese mes")
print(fechaSep[0]+" de ",fechaSep[1]," de "+fechaSep[2])

print("\nEjercicio 5")
asignaturas = {"Matematicas": 6, "Fisica": 4, "Quimica": 5}
creditos = 0
for asignatura in asignaturas:
    creditos+=asignaturas[asignatura]
    print(asignatura," tiene ",asignaturas[asignatura]," creditos.")
print("El numero total de creditos es de = ", creditos)

print("\nEjercicio 6")
persona = {}
continuar=True
while continuar:
    clave = input("¿Que quieres introducir? ")
    valor = input("Introduce el valor: ")
    persona[clave] = valor
    print(persona)
    confirmacion = input("¿Quieres continuar?")
    if(confirmacion=="si"):
        continuar=True
    else:
        continuar=False

print("\nEjercicio 7")
cesta = {}
continuar=True
while continuar:
    clave = input("¿Que articulo a comprado? ")
    valor = float(input("Cuanto es su precio: "))
    cesta[clave] = valor
    confirmacion = input("¿A terminado?")
    if(confirmacion=="no"):
        continuar=True
    else:
        continuar=False
print(cesta)
print("Lista de la compra\n")
suma = 0
for producto in cesta:
    suma += cesta[producto]
    print(producto, "-----", cesta[producto], "\n")
print("Total -----", suma)
'''

print("\nEjercicio 8")
combinacion = input("Introduce una palabra en castellano y su traduccion en ingles (formato= castellano:ingles): ")
combinacion = combinacion.split(":")
print(combinacion)
