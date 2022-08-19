
from ast import Break, Continue
from operator import itemgetter

promedioedadbjx = 0
promedioedadgdl = 0
promedioedadjal = 0

contador = 0
contadorbjx = 0
contadorgdl = 0
contadorjal = 0

contbjx = 0
contgdl = 0
contjal = 0

datosusuario = ()
datosusuarioP = ()
datosusuariolistapreferentes = {}
datosusuariolistanopreferentes = {}
diccionariotodos = {}
diccionariopref = {}

viajes = []

while True :

    print("========================")
    print("1.- Añadir clientes")
    print("2.- Listar todos los clientes")
    print("3.- Listar clientes preferentes")
    print("4.- Salir")
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
        break
    
    contador += 1
    ID = input("Ingrese el ID del suario: ")
    Nombre = input("Ingresa tu nombre: ")
    Edad = int(input("Ingresa tu edad: "))
    Destino = input("Ingresa destino: ")
    ClienteP = input("¿EL usuario es un cliene preferente? ")
    if (ClienteP == "Si" or ClienteP == "si"):
        ClienteP = True
    elif (ClienteP == "No" or ClienteP == "no"):
        ClienteP = False
    datosusuariolistanopreferentes[Nombre] = ID , Edad , Destino , ClienteP
    diccionariotodos[Nombre] = ID
    if (ClienteP == True) :
            datosusuariolistapreferentes[Nombre] = ID , Edad, Destino, ClienteP 
            diccionariopref[Nombre] = ID
    if Destino == "BJX" :
        contbjx += 1
        promedioedadbjx = promedioedadbjx + Edad
    elif Destino == "GDL" :
        contgdl += 1
        promedioedadgdl =  promedioedadgdl + Edad
    elif Destino == "JAL" :
        contjal += 1
        promedioedadjal = promedioedadjal + Edad

if contbjx > 0:
    promedioedadbjx = promedioedadbjx / contbjx
if contgdl > 0:
    promedioedadgdl = promedioedadgdl / contgdl
if contjal > 0:
    promedioedadjal = promedioedadjal / contjal

informacionBJX = ("BJX" , contbjx, promedioedadbjx)
informacionGDL = ("GDL" , contgdl, promedioedadgdl)
informacionJAL = ("JAL" , contjal, promedioedadjal)

if contbjx > 0:
    viajes.append(informacionBJX)
if contgdl > 0:
    viajes.append(informacionGDL)
if contjal > 0:
    viajes.append(informacionJAL)

viajes = sorted(viajes, key=itemgetter(1), reverse=True)

# Al momento de imprimir viajes solo se mostrará un arreglo
# en vez de mostrar los dos que pide el ejercicio
# este arreglo contiene la información en el siguiente orden
# "Destino" , "Número de pasajeros" , "Promedio de la edad"
# Me pareció más optimo que separarlo en dos arreglos
# Y crear otas 3 variables más para separar los detalles y el
# promedio de edad, saludos cordiales

Opt3 = input("¿Desea mostrar la información de los viajes?")
if (Opt3 == "Si" or Opt3 == "si") :
    print(viajes)
else :
    print("Programa finalizado")