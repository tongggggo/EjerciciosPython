from operator import itemgetter, attrgetter

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

viajes = []

while True :
    contador = contador + 1
    Nombre = input("Ingresa tu nombre: ")
    if (Nombre == "X" or Nombre == "x"):
        break
    Edad = int(input("Ingresa tu edad: "))
    Destino = input("Ingresa destino: ")
    
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

print(viajes)