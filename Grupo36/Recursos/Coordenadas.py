import geopy.distance
import csv
import time
import math

from geopy.distance import Distance, geodesic

'''
"Agios Antonios", 38.0068146517197, 23.699513438319748
"Sepolia", 38.00274401708804, 23.713544775768924
"Attiki", 37.99942401991833, 23.722088458008933
"Larissa Station", 37.992047322901676, 23.721117242121732
"Metaxourgeio", 37.98640562176535, 23.721177252557546
"Omonoia", 37.98432141126678, 23.728683160119683
"Panepistimio", 37.98046794744238, 23.73304020256116
"Syntagma", 37.97514826952336, 23.735661039531127
"Akropoli", 37.96872712680195, 23.72958182888358
"Syngrou-Fix ", 37.964373881635936, 23.726595006295188
"Neos Kosmos", 37.95795485468016, 23.728521581049492
"Agios Ioannis", 37.9568119964683, 23.734739551693238
"Dafni", 37.94940746612561, 23.73722751946073
"Agios Dimitrios", 37.94065699520722, 23.740670034162275

"Egaleo", 37.99198589578065, 23.68182962337508
"Eleonas", 37.98763768487978, 23.69373842661961
"Kerameikos", 37.97862839747796, 23.71145931764796
"Monastiraki", 37.97507429861217, 23.73568502946803
"Syntagma", 37.97514826952336, 23.735661039531127
"Evangelismos", 37.97605111152339, 23.746633806670683
"Megaro Moussikis", 37.97930283226864, 23.752918222391468
"Ambelokipi", 37.98733637503534, 23.75702468438942
"Panormou", 37.99316014356322, 23.763432481727254
"Katehaki", 37.99316859879299, 23.776148834663914
"Ethniki Amyna", 38.00005294321207, 23.785753825148195
"Holargos", 38.00451395697365, 23.794717358988567
"Nomismatokopio", 38.00927969821997, 23.805671500607282
"Aghia Paraskevi", 38.01719809064458, 23.81231138320322
"Halandri", 38.02151256644872, 23.821217071683567
"Pallini", 38.005727986847674, 23.869621156102774
"Paiania-Kantza", 37.98422733553239, 23.870009588264278
"Koropi", 37.91284422686963, 23.895732263120998
"Airport", 37.9366384061094, 23.944515869823036

"Piraeus", 37.94882818948211, 23.643107297519066
"Faliro", 37.94514793440661, 23.665289470189098
"Moschato", 37.955819334153745, 23.679414986506075
"Kallithea", 37.96231313642352, 23.697238536182965
"Tavros", 37.96366583365432, 23.703149261814215
"Petralona", 37.968614930241806, 23.709207373622185
"Thissio", 37.976781355635346, 23.717910887149436
"Monastiraki", 37.97507429861217, 23.73568502946803
"Omonoia", 37.98432141126678, 23.728683160119683
"Victoria", 37.99313700048735, 23.730292125925665
"Attiki", 37.99942401991833, 23.722088458008933
"Aghios Nikolaos", 38.00687087029947, 23.727714846662487
"Kato Patissia", 38.011635901892774, 23.72863348083961
"Aghios Eleftherios", 38.020079500918186, 23.731848700512863
"Ano Patissia", 38.023778295025075, 23.735880483877715
"Perissos", 38.03216353675219, 23.74403617556809
"Pefkakia", 38.046872106096686, 23.7831463570412
"Nea lonia", 38.033189128190564, 23.744659173575943
"Iraklio", 38.046976145596, 23.766220873964393
"Irini", 38.04371205956952, 23.78266248337522
"Neratziotissa", 38.04518572663135, 23.79306986913043
"Maroussi", 38.05641852222853, 23.805012183685186
"KAT", 38.06595559355917, 23.80414992917583
"Kifissia", 38.073760082370846, 23.808561906380156

'''

lineaRoja = ["Agios Antonios", "Sepolia", "Attiki", "Larissa Station", "Metaxourgeio", "Omonoia", "Panepistimio",
             "Syntagma", "Akropoli", "Syngrou-Fix ", "Neos Kosmos", "agios ioannis", "Dafni", "Agios Dimitrios"]

lineaAzul = ["Egaleo", "Eleonas", "Kerameikos", "Evangelismos", "Megaro Moussikis", "Ambelokipi", "Panormou", "Katehaki",
             "Ethniki Amyna", "Holargos", "Nomismatokopio", "Aghia Paraskevi", "Halandri", "Pallini", "Paiania - Kantza", "Koropi", "Airport"]
lineaVerde = ["Piraeus", "Faliro", "Moschato", "Kallithea", "Tavros", "Petralona", "Thissio", "Monastiraki", "Omonia", "Victoria", "Attiki", "Aghios Nikolaos",
              "Kato Patissia", "Aghios Eleftherios", "Ano Patissia", "Perissos", "Pefkakia", "Nea lonia", "Iraklio", "Irini", "Neratziotissa", "Maroussi", "KAT", "Kifissia"]

# with open('distancias.csv', 'w') as distancias_file:
#     distancias_writer = csv.writer(distancias_file, delimiter=',')
#     with open('coordenadas.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         for row in csv_reader:
#             distancias = []
#             with open('coordenadas.csv') as csv_file2:
#                 csv_reader2 = csv.reader(csv_file2, delimiter=',')
#                 for row2 in csv_reader2:            
#                     distance = geodesic((row[1], row[2]), (row2[1], row2[2])).km
#                     distancias.append(distance)
#                 distancias_writer.writerow(distancias)

# with open('DistanciaEnLineaRoja.csv', 'w') as metro:
#     distancias_writer = csv.writer(metro, delimiter=',')
#     with open('MetroRojo.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         cont = 0
#         prev = None
#         distancias = []
#         for station in csv_reader:
#             if cont > 0:
#                 distance = geodesic((station[1], station[2]), (prev[1], prev[2])).km
#                 distancias_writer.writerow([prev[0], station[0], distance])
#             prev = station
#             cont += 1
#             # print(station)
    
# with open('DistanciaEnLineaAzul.csv', 'w') as metro:
#     distancias_writer = csv.writer(metro, delimiter=',')
#     with open('MetroAzul.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         cont = 0
#         prev = None
#         distancias = []
#         for station in csv_reader:
#             if cont > 0:
#                 distance = geodesic((station[1], station[2]), (prev[1], prev[2])).km
#                 distancias_writer.writerow([prev[0], station[0], distance])
#             prev = station
#             cont += 1
#             # print(station)

# with open('DistanciaEnLineaVerde.csv', 'w') as metro:
#     distancias_writer = csv.writer(metro, delimiter=',')
#     with open('MetroVerde.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         cont = 0
#         prev = None
#         distancias = []
#         for station in csv_reader:
#             if cont > 0:
#                 distance = geodesic((station[1], station[2]), (prev[1], prev[2])).km
#                 distancias_writer.writerow([prev[0], station[0], distance])
#             prev = station
#             cont += 1
#             # print(station)

