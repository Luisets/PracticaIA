# Practica IA

Implementacion de una red de metro, para calcular el mejor trayecto entre dos estaciones utilizando un algoritmo A*

## **Requisitos:**
1. Tener Python instalado(versión 3.8 o superior).
2. Tener instaladas las siguientes librerías:
    *   pandas
    *   PySide2
    *   folium
    *   csv

## **Ejecución:**
Ejecutar el archivo MetroApp.pyw

## **Estructura:**
*   App
    *   Algorithm.py
    *   AppGui.py
    *   Mapa.py
    *   Worker.py
    *   WorkerSignal.py
*   images
    * carga.gif
    * logo.ico
    * logo.png
*   Recursos
    * coordenadas.csv
    * DistanciaEnLineaAzul.csv
    * DistanciaEnLineaRoja.csv
    * DistanciaEnLineaVerde.csv
    * distancias.csv
    * HorasPunta.csv
    * MetroAzul.csv
    * MetroAzulGraf.csv
    * MetroRojo.csv
    * MetroRojoGraf.csv
    * MetroVerde.csv
    * MetroVerdeGraf.csv
    * Transbordos.cs
*   MetroApp.pyw
*   README.md

## Contenido

* MetroApp.pyw
    > Punto de inicio de la aplicación.

* Algorithm.py
    > Realiza el algoritmo A* recibiendo dos estaciones de tren distintas y la hora del día.

* Gui.py
    > Se encarga de dibujar la Ventana de la aplicación y llamar al algoritmo para graficar su solución.

* Mapa.py
    > Se encarga de generar el mapa y graficar las lineas del metro, junto con el trayecto resultante.

* Worker.py y WorkerSignal.py
    > Clases para controlar las señales de fin y resultado de un thread.