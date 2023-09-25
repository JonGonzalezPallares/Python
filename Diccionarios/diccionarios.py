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

print("\nEjercicio 8")
diccionario = {}
continuar=True
while continuar:
    combinacion = input("Introduce una palabra en castellano y su traduccion en ingles (formato= castellano:ingles): ")
    combinacion = combinacion.split(":")
    diccionario[combinacion[0]]=combinacion[1]
    prueba = input("¿Continuar añadiendo?")
    if(prueba.lower()=="si"):
        continuar=True
    else:
        continuar=False
frase = input("Introduce una frase: ")
frase = frase.split(" ")
traducido = ""
paso=0
for palabra in frase:
    if(palabra in diccionario):
        traducido += diccionario[palabra]+" "
    else:
        traducido += palabra+" "
    paso+=1
print(traducido)

print("\nEjercicio 9")
facturasG = {
    0 : 76.48,
    1 : 97.22,
    2 : 6.09,
    3 : 80.83,
    4 : 52.04
}
eleccion = int(input("Selecciona una opción\n1. Añadir factura\n2. Pagar factura\n3. Terminar factura\n"))
cobrada = 0
pendiente = 0
for factura in facturasG:
    pendiente += facturasG[factura]
pendiente = round(pendiente, 2)
if(eleccion==1):
    nuevaNum = input("Introduce un numero de factura: ")
    nuevaCos = round(float(input("Introduce el coste: ")), 2)
    facturasG[nuevaNum]=nuevaCos
elif(eleccion==2):
    pago = int(input("Introduce un numero de factura para pagar: "))
    if(pago in facturasG):
        pendiente -= round(facturasG[pago], 2)
        cobrada += round(facturasG[pago], 2)
        facturasG.pop(pago)
    else:
        print("El numero de factura ", pago, " no existe")
elif(eleccion==3):
    print("Acciones acabadas, que tenga un buen dia")
print("Cantidad cobrada: {}\nCantidad pendiente: {}".format(cobrada, pendiente))

print("\nEjercicio 10")
baseDatos = {
    1: {
        "Nombre": "Jon",
        "Direccion": "Gaztain",
        "Telefono": 122334456,
        "Correo": "jon@gmail.com",
        "Preferente": True
    },
    2: {
        "Nombre": "Usuario",
        "Direccion": "Calle 1",
        "Telefono": 000000000,
        "Correo": "usuario@usuario.com",
        "Preferente": False
    }
}

cambiado = False
opcion=""
while opcion!=6:
    if(opcion==1):
        print("\nIntroduzca los datos del nuevo usuario:\n")
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        while True:
            telefono = input("Telefono: ")
            if(telefono.isnumeric()):
                telefono = int(telefono)
                break
            else:
                print("Vuelve a introducir el telefono")
        correo = input("Correo: ")
        while cambiado!=True:
            preferente = input("Preferente: ")
            if(preferente.lower()=="true"):
                preferente = True
                preferente = bool(preferente)
                cambiado=True
            elif(preferente.lower()=="false"):
                preferente = False
                preferente = bool(preferente)
                cambiado=True
            else:
                print("\nSolo se acepta True o False")

    elif(opcion==2):
        nif = int(input("Introduce el NIF del cliente a borrar: "))
        if(nif in baseDatos):
            baseDatos.pop(nif)
        else:
            print("\nEl cliente con NIF ",nif," no existe")

    elif(opcion==3):
        nifBus = int(input("Introduce el NIF del cliente a buscar: "))
        if(nifBus in baseDatos):
            print("\n",baseDatos[nifBus])
        else:
            print("\nEl usuario con NIF ", nifBus, " no existe")
    
    elif(opcion==4):
        print("\nTodos los clientes disponibles:")
        for cliente in baseDatos:
            print("\n",baseDatos[cliente])

    elif(opcion==5):
        print("\nTodos los clientes PREFERENTES:")
        for cliente in baseDatos:
            if(baseDatos[cliente]["Preferente"]==True):
                print("\n"+baseDatos[cliente])

    opcion = int(input("\n\nSeleccione una opcion:\n1. Añadir cliente\n2. Eliminar cliente\n3. Mostrar cliente\n4. Listar todos los clientes\n5. Listar clientes preferentes\n6. Terminar\n"))
'''