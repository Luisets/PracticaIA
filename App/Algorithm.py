import csv


class Graph:
    def __init__(self, graph_dict=None):
        self.graph_dict = graph_dict or {}

    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        self.graph_dict.setdefault(B, {})[A] = distance

    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)


class Node:

    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes

    def __lt__(self, other):
        return self.f < other.f


class Coordenada:
    def __init__(self, name, longitud, latitud):
        self.name = name
        self.longitud = longitud
        self.latitud = latitud


def Calcular(inicio: str, final: str, hora):
    grafo = Graph(None)
    with open('Recursos/DistanciaEnLineaRoja.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            grafo.connect(row[0], row[1], row[2])
            # print(row[0],row[1],row[2])

    with open('Recursos/DistanciaEnLineaAzul.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            grafo.connect(row[0], row[1], row[2])
            # print(row[0],row[1],row[2])

    with open('Recursos/DistanciaEnLineaVerde.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            grafo.connect(row[0], row[1], row[2])
            # print(row[0],row[1],row[2])
    # print(len(grafo.graph_dict))

    distancias = []
    with open('Recursos/distancias.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            distancias.append(row)

    path = Algoritmo(grafo, inicio, final, distancias, hora)
    coord = []
    for i in path:
        with open('Recursos/coordenadas.csv') as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if row[0] == i:
                    coord.append(row[1])
                    coord.append(row[2])
    # print(path)
    # print(coord)
    result = []
    j = 0
    for i in path:
        result.append(Coordenada(i, coord[j], coord[j+1]))
        j = j+2
    # print(result)
    return result

def Algoritmo(grafo, inicio: str, final: str, distancias, minuto):

    toGetIndex = ["Agios Antonios", "Sepolia", "Attiki", "Larissa Station", "Metaxourgeio", "Omonoia", "Panepistimio",
                  "Syntagma", "Akropoli", "Syngrou-Fix ", "Neos Kosmos", "Agios Ioannis", "Dafni", "Agios Dimitrios",
                  "Egaleo", "Eleonas", "Kerameikos", "Monastiraki", "Evangelismos", "Megaro Moussikis",
                  "Ambelokipi", "Panormou", "Katehaki", "Ethniki Amyna", "Holargos", "Nomismatokopio", "Aghia Paraskevi",
                  "Halandri", "Pallini", "Paiania-Kantza", "Koropi", "Airport",
                  "Piraeus", "Faliro", "Moschato", "Kallithea", "Tavros", "Petralona", "Thissio",
                  "Victoria", "Aghios Nikolaos", "Kato Patissia", "Aghios Eleftherios", "Ano Patissia", "Perissos", "Pefkakia",
                  "Nea lonia", "Iraklio", "Irini", "Neratziotissa", "Maroussi", "KAT", "Kifissia"]
    open = []
    closed = []
    end_index = toGetIndex.index(final)
    tiempo_extra_trasbordo = 0

    if (minuto <= 360):
        tiempo_extra_trasbordo = 3
    elif (minuto <= 1230):
        tiempo_extra_trasbordo = 1.5
    elif (minuto <= 1320):
        tiempo_extra_trasbordo = 2.1
    else:
        tiempo_extra_trasbordo = 3

    ini_node = Node(inicio, None)
    end_node = Node(final, None)

    open.append(ini_node)

    while len(open) > 0:
        open.sort()

        act_node = open.pop(0)

        closed.append(act_node)

        # if del final
        if act_node == end_node:
            path = []
            while act_node != ini_node:
                path.append(act_node.name)
                act_node = act_node.parent
            path.append(ini_node.name)

            return path[::-1]

        vecinos = grafo.get(act_node.name)

        for k, i in vecinos.items():
            peso_transbordo = 0.0

            vecino = Node(k, act_node)
            if(vecino in closed):
                continue

            if (act_node != ini_node):
                # Monastiraki
                if((act_node.parent.name == "Kerameikos" or act_node.parent.name == "Syntagma") and (vecino.name == "Omonia" or vecino.name == "Thissio")):
                    peso_transbordo = 0.45 + tiempo_extra_trasbordo
                if((act_node.parent.name == "Omonia" or act_node.parent.name == "Thissio") and (vecino.name == "Syntagma" or vecino.name == "Kerameikos")):
                    peso_transbordo = 0.45 + tiempo_extra_trasbordo
                # Omonia
                if((act_node.parent.name == "Monastiraki" or act_node.parent.name == "Victoria") and (vecino.name == "Panepistimio" or vecino.name == "Metaxourgeio")):
                    peso_transbordo = 0.60 + tiempo_extra_trasbordo
                if((act_node.parent.name == "Metaxourgeio" or act_node.parent.name == "Panepistimio") and (vecino.name == "Victoria" or vecino.name == "Monastiraki")):
                    peso_transbordo = 0.60 + tiempo_extra_trasbordo

                # Attiki
                if((act_node.parent.name == "Aghios Nikolaos" or act_node.parent.name == "Victoria") and (vecino.name == "Sepolia" or vecino.name == "Larissa Station")):
                    peso_transbordo = 0.2 + tiempo_extra_trasbordo
                if((act_node.parent.name == "Sepolia" or act_node.parent.name == "Larissa Station") and (vecino.name == "Aghios Nikolaos" or vecino.name == "Victoria")):
                    peso_transbordo = 0.2 + tiempo_extra_trasbordo

                # Syntagma
                if((act_node.parent.name == "Panepistimio" or act_node.parent.name == "Akropoli") and (vecino.name == "Evangelismos" or vecino.name == "Monastiraki")):
                    peso_transbordo = 0.52 + tiempo_extra_trasbordo
                if((act_node.parent.name == "Evangelismos" or act_node.parent.name == "Monastiraki") and (vecino.name == "Panepistimio" or vecino.name == "Akropoli")):
                    peso_transbordo = 0.52 + tiempo_extra_trasbordo

            vecino.g = act_node.g + \
                float(grafo.get(act_node.name, vecino.name)) + peso_transbordo
            vecino.h = float(distancias[end_index]
                             [toGetIndex.index(act_node.name)])
            vecino.f = vecino.g + vecino.h

            if(add_to_open(open, vecino) == True):
                open.append(vecino)
    return None


def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True


if __name__ == "__main__":
    obj = Calcular("Metaxourgeio", "Attiki", 0)
    for x in obj:
        print("estacion: {}, longitud: {}, latitud: {}\n".format(x.name, x.longitud, x.latitud))
