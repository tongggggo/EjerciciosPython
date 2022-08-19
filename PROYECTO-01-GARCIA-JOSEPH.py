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
"""    
Synergy logistics está considerando la posibilidad de enfocar sus esfuerzos en las
10 rutas más demandadas. Acorde a los flujos tanto de importación como de
exportación, indica:

● ¿Cuáles son esas 10 rutas?
    Corea del sur - Vietnam (497)
    Países bajos - Belgica (437)
    Estados Unidos - Países bajos (385)
    China - Mexico (351)
    China - Japon (343)
    Alemania - China (328)
    Japon - Francia (299)
    Corea del sur - Japon (294)
    Australia - Singapore (273)
    Japon - Canadá (273)
● ¿Le conviene implementar esa estrategia? ¿Por qué? 
    Creo que sí, aunque existen algunos riesgos; como por ejemplo el que las rutas menos utilizadas empiezen a funcionar aún peor
    y que los cambios en sus rutas más utilizadas no sean lo suficientemente grandes como para compensarlo
