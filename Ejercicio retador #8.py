
from ast import Break, Continue
from operator import itemgetter

Edad = 0

promedioedadbjx = 0
promedioedadgdl = 0
promedioedadjal = 0

contador = 2
contadorpref = contador

contbjx = 1
contgdl = 0
contjal = 1

datosusuario = ()
datosusuarioP = ()
datosusuariolistapreferentes = {45471:["Luis Perez",45,"BJX", True], 8944411:["Fernanda Garcia",25,"JAL", True], 15223:["Alejandra Ortiz",33,"GDL", True]}
datosusuariolistanopreferentes = {45471:["Luis Perez",45,"BJX", True], 8944411:["Fernanda Garcia",25,"JAL", True], 15223:["Alejandra Ortiz",33,"GDL", True]}
diccionariotodos = {45471:["Luis Perez"], 8944411:["Fernanda Garcia"]}
diccionariopref = {45471:["Luis Perez"], 8944411:["Fernanda Garcia"]}

viajes = []

edadpromediotodos = 70
edadpromediopreferentes = 70

while True :

    print("========================")
    print("1.- Añadir clientes")
    print("2.- Listar todos los clientes")
    print("3.- Listar clientes preferentes")
    print("4.- Eliminar un cliente")
    print("5.- Edad promedio de todos los clientes")
    print("6.- Edad promedio de clientes preferentes")
    print("7.- Salir")
    print("========================")

    Optmain = int(input())

    if (Optmain == 1) :
        Continue
    elif (Optmain == 2) :
        print(diccionariotodos)
        break
    elif (Optmain == 3) : 
        print(diccionariopref)
        break
    elif (Optmain == 4) :
        pinole = int(input("Ingrese la ID que desea eliminar "))
        del(datosusuariolistanopreferentes[pinole])
        del(datosusuariolistapreferentes[pinole])
        del(diccionariotodos[pinole])
        del(diccionariopref[pinole])
        print(diccionariotodos)
             
        break
    elif (Optmain == 5) :
        edadpromediotodos/=contador
        print(edadpromediotodos)
        break
    elif (Optmain == 6) :
        edadpromediopreferentes/=contadorpref
        print(edadpromediopreferentes)
        break
    elif (Optmain == 7) :
        break
    
    contador += 1
    ID = int(input("Ingrese el ID del suario: "))
    Nombre = input("Ingresa tu nombre: ")
    Edad = int(input("Ingresa tu edad: "))
    Destino = input("Ingresa destino: ")
    ClienteP = input("¿EL usuario es un cliene preferente? ")

    if (ClienteP == "Si" or ClienteP == "si"):
        contadorpref=contador
        ClienteP = True
    elif (ClienteP == "No" or ClienteP == "no"):
        ClienteP = False

    edadpromediotodos += Edad
    datosusuariolistanopreferentes[ID] = [Nombre , Edad , Destino , ClienteP]
    diccionariotodos[ID] = [Nombre]

    if (ClienteP == True) :
        edadpromediopreferentes += Edad
        datosusuariolistapreferentes[ID] = [Nombre , Edad, Destino, ClienteP]
        diccionariopref[ID] = [Nombre]
    
    if Destino == "BJX" :
        contbjx += 1
        promedioedadbjx = promedioedadbjx + Edad
    elif Destino == "GDL" :
        contgdl += 1
        promedioedadgdl =  promedioedadgdl + Edad
    elif Destino == "JAL" :
        contjal += 1
        promedioedadjal = promedioedadjal + Edad