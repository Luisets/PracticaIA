import io
import folium
import csv
import pandas as pd


def gen(trayecto, estaciones):

    m3 = folium.Map(location=[
                    37.99000470552127, 23.744516330538477], tiles='cartodbpositron', zoom_start=12)

    folium.Marker(location=trayecto[0], tooltip="Origen: {}".format(estaciones[0]),
                  icon=folium.Icon(color='darkpurple', prefix='fa', icon='subway')).add_to(m3)
    folium.Marker(location=trayecto[-1], tooltip="Destino: {}".format(estaciones[-1]),
                  icon=folium.Icon(color='darkpurple', prefix='fa', icon='subway')).add_to(m3)

    # creamos los grupos
    f1 = folium.FeatureGroup("Linea 1")
    f2 = folium.FeatureGroup("Linea 2")
    f3 = folium.FeatureGroup("Linea 3")
    f4 = folium.FeatureGroup("Trayecto")

    vectorVerde = pd.read_csv(
        "Recursos/MetroVerdeGraf.csv", sep=',', comment='#', header=None).values
    folium.vector_layers.PolyLine(
        vectorVerde, color='green', weight=5).add_to(f1)

    vectorRojo = pd.read_csv("Recursos/MetroRojoGraf.csv",
                             sep=',', comment='#', header=None).values
    folium.vector_layers.PolyLine(
        vectorRojo, color='red', weight=5).add_to(f2)

    vectorAzul = pd.read_csv("Recursos/MetroAzulGraf.csv",
                             sep=',', comment='#', header=None).values
    folium.vector_layers.PolyLine(
        vectorAzul, color='blue', weight=5).add_to(f3)

    folium.vector_layers.PolyLine(
        trayecto, color='orange', weight=6.5).add_to(f4)

    for i in range(1, len(trayecto)-1):
        # folium.CircleMarker(location=trayecto[i], radius=5, tooltip=estaciones[i],
        #                 color='black', fill=True, fill_color='black').add_to(m3)
        folium.Marker(location=trayecto[i], tooltip=estaciones[i], icon=folium.Icon(
            color='blue', prefix='fa', icon='meter')).add_to(m3)
    f1.add_to(m3)
    f2.add_to(m3)
    f3.add_to(m3)
    f4.add_to(m3)

    folium.LayerControl().add_to(m3)
    data = io.BytesIO()
    m3.save(data, close_file=False)

    return data
