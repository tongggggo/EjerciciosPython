import csv
from collections import Counter

ciudades = []
with open('synergy_logistics_database.csv') as archivo_csv:
    lector = csv.reader(archivo_csv, delimiter=',')
    contlineas = 0

    for x in lector:
        if contlineas == 0:
            contlineas += 1
        else:
            aux = str(x[2]),str(x[3])
            ciudades.append(aux)
            contlineas += 1
   
    res = Counter(ciudades)
    print(res)