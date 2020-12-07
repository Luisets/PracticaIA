from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QWidget
from PySide2 import QtWebEngineWidgets
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from App.Worker import Worker
import App.Algorithm as Algorithm
import time
import App.Mapa as mapa
import io


class Gui_MainWindow(object):

    # definimos la ubicacion del icono
    icon_Path = "App/images/logo.ico"
    logo_Path = "App/images/logo.png"
    load_Path = "App/images/carga.gif"

    def setupUi(self, window):
        # definimos el nombre e icono de la App
        window.setWindowTitle("Metro")
        window.setWindowIcon(QtGui.QIcon(self.icon_Path))

        # definimos los tamaños de la ventana principal
        window.resize(500, 600)
        window.setMinimumSize(QtCore.QSize(500, 600))
        window.setMaximumSize(QtCore.QSize(500, 600))
        window.setStyleSheet("background-color: white")
        window.setObjectName("window")

        # definimos el Widget de la ventana
        self.central_widget = QtWidgets.QWidget(window)
        self.central_widget.setObjectName("central_widget")

        # definimos el frame de la pantalla inicial
        self.frame_principal = QtWidgets.QFrame(self.central_widget)
        self.frame_principal.setGeometry(QtCore.QRect(0, 0, 500, 600))
        self.frame_principal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_principal.setObjectName("frame_principal")
        # definimos central_windget como widget principal de la ventana
        window.setCentralWidget(self.central_widget)

        # definimos el logo principal
        self.label_logo = QtWidgets.QLabel(self.frame_principal)
        self.label_logo.setGeometry(QtCore.QRect(175, 25, 150, 150))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")

        # definimos la paleca de color para error los label de error
        # # solo definimos la activa
        error_palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        error_palette.setBrush(QtGui.QPalette.Active,
                               QtGui.QPalette.WindowText, brush)
        error_palette.setBrush(QtGui.QPalette.Inactive,
                               QtGui.QPalette.WindowText, brush)

        # definimos el font a usar en los label
        arialFont_label = QtGui.QFont()
        arialFont_label.setFamily("Arial")
        arialFont_label.setPointSize(15)
        arialFont_label.setBold(True)
        arialFont_label.setWeight(75)
        arialFont_label.setStrikeOut(False)

        # definimos el font a usar en los intro
        arialFont_intro = QtGui.QFont()
        arialFont_intro.setFamily("Arial")
        arialFont_intro.setPointSize(15)
        arialFont_intro.setBold(False)
        arialFont_intro.setWeight(1)
        arialFont_intro.setStrikeOut(False)

        # definimos el label Inicio
        self.label_inicio = QtWidgets.QLabel(self.frame_principal)
        self.label_inicio.setGeometry(QtCore.QRect(100, 240, 80, 35))
        self.label_inicio.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_inicio.setFont(arialFont_label)
        self.label_inicio.setObjectName("label_inicio")

        # definimos la caja de texto para el inicio
        self.intro_inicio = QtWidgets.QLineEdit(self.frame_principal)
        self.intro_inicio.setGeometry(QtCore.QRect(190, 240, 175, 35))
        self.intro_inicio.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.intro_inicio.setFont(arialFont_intro)
        self.intro_inicio.setStyleSheet("border : none;")
        self.intro_inicio.setObjectName("intro_inicio")

        # definimos la linea para resaltar la introduccion del inicio
        self.line_inicio = QtWidgets.QFrame(self.frame_principal)
        self.line_inicio.setGeometry(QtCore.QRect(190, 276, 175, 2))
        self.line_inicio.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_inicio.setLineWidth(2)

        # definimos el label de Inicio invalido
        self.label_invalid_inicio = QtWidgets.QLabel(self.frame_principal)
        self.label_invalid_inicio.setGeometry(QtCore.QRect(190, 275, 111, 21))
        self.label_invalid_inicio.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_invalid_inicio.setPalette(error_palette)
        self.label_invalid_inicio.setStyleSheet(
            "background-color: transparent")
        self.label_invalid_inicio.setObjectName("label_invalid_inicio")
        # # lo escondemos mientras no sea necesario
        self.label_invalid_inicio.hide()

        # definimos el label destino
        self.label_destino = QtWidgets.QLabel(self.frame_principal)
        self.label_destino.setGeometry(QtCore.QRect(100, 330, 80, 35))
        self.label_destino.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_destino.setFont(arialFont_label)
        self.label_destino.setObjectName("label_destino")

        # definimos la caja de texto para el destino
        self.intro_destino = QtWidgets.QLineEdit(self.frame_principal)
        self.intro_destino.setGeometry(QtCore.QRect(190, 330, 175, 35))
        self.intro_destino.setFont(arialFont_intro)
        self.intro_destino.setStyleSheet("border : none;")
        self.intro_destino.setText("")
        self.intro_destino.setObjectName("intro_destino")

        # definimos la linea para resaltar la introduccion del destino
        self.line_destino = QtWidgets.QFrame(self.frame_principal)
        self.line_destino.setGeometry(QtCore.QRect(190, 366, 175, 2))
        self.line_destino.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_destino.setLineWidth(2)

        # definimos el label de Destino invalido
        self.label_invalid_destino = QtWidgets.QLabel(self.frame_principal)
        self.label_invalid_destino.setGeometry(QtCore.QRect(190, 365, 111, 21))
        self.label_invalid_destino.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_invalid_destino.setPalette(error_palette)
        self.label_invalid_destino.setStyleSheet(
            "background-color: transparent")
        self.label_invalid_destino.setObjectName("label_invalid_destino")
        # # lo escondemos mientras no sea necesario
        self.label_invalid_destino.hide()

        # definimos el boton para el algoritmo
        self.button_calcular = QtWidgets.QPushButton(self.frame_principal)
        self.button_calcular.setGeometry(QtCore.QRect(200, 430, 100, 30))
        self.button_calcular.setFont(arialFont_intro)
        self.button_calcular.setStyleSheet("background-color: #A0A0A0A0")
        # # definimos la accion al presionar el boton
        self.button_calcular.clicked.connect(self.calcularAction)
        self.button_calcular.setObjectName("button_calcular")

        # # # # # # Frame de carga # # # # # #
        # definimos el segundo frame 2 "pantalla de carga"
        self.frame_carga = QtWidgets.QFrame(self.central_widget)
        self.frame_carga.setGeometry(QtCore.QRect(125, 120, 250, 250))
        self.frame_carga.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_carga.setObjectName("frame_solucion")
        # # iniciamos el frame oculto
        self.frame_carga.hide()

        # font para el mensaje en pantalla de carga
        arialFont_WaitingLabel = QtGui.QFont()
        arialFont_WaitingLabel.setFamily("Arial")
        arialFont_WaitingLabel.setPointSize(12)
        arialFont_WaitingLabel.setBold(True)
        arialFont_WaitingLabel.setWeight(75)

        # definimos el label para el gif de carga
        self.label_cargaMovie = QtWidgets.QLabel(self.frame_carga)
        self.label_cargaMovie.setGeometry(QtCore.QRect(75, 40, 100, 100))
        self.label_cargaMovie.setScaledContents(True)

        # definimos el label para el mensaje de carga
        self.label_carga = QtWidgets.QLabel(self.frame_carga)
        self.label_carga.setGeometry(QtCore.QRect(75, 150, 100, 25))
        self.label_carga.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_carga.setFont(arialFont_WaitingLabel)

        # # # # # # Frame de solucion # # # # # #
        # definimos el segundo frame 3 "pantalla de solucion"
        self.frame_solucion = QtWidgets.QFrame(self.central_widget)
        self.frame_solucion.setGeometry(QtCore.QRect(0, 0, 500, 600))
        self.frame_solucion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_solucion.setObjectName("frame_solucion")
        # # iniciamos el frame oculto
        self.frame_solucion.hide()

        '''
        Resto de elementos para la Ventana de solucion
        '''
        # definimos el widgetBrowser
        self.browser = QtWebEngineWidgets.QWebEngineView(self.frame_solucion)
        self.browser.setGeometry(QtCore.QRect(0, 0, 500, 500))

        # definimos un boton para volver a la pagina principal
        self.button_volver_frame1 = QtWidgets.QPushButton(self.frame_solucion)
        self.button_volver_frame1.setGeometry(QtCore.QRect(200, 530, 100, 30))
        # # definimos la accion del button
        self.button_volver_frame1.clicked.connect(self.volver_framePrincipal)
        self.button_volver_frame1.setObjectName("button_volver_frame1")

        # definimos al madre ne nuestra Gui a la window a la que esta asociada
        QtCore.QMetaObject.connectSlotsByName(window)

        # rellenamos todos los componentes
        self.fillTexts()

        # pool de treads
        self.poolThread = QtCore.QThreadPool()

    def fillTexts(self):
        # # # # # # Definimos los textos para el frame principal
        # definimos le contenido del logo
        image = QtGui.QImage(self.logo_Path)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.label_logo.setPixmap(pixmap)
        # definimos el contenido del resto de labels y el button
        self.label_inicio.setText("Inicio:")
        self.label_destino.setText("Destino:")
        self.button_calcular.setText("Calcular")
        self.label_invalid_inicio.setText("La estación no existe")
        self.label_invalid_destino.setText("La estación no existe")

        # # # # # # Definimos los textos del frame de carga
        load_movie = QtGui.QMovie(self.load_Path)
        self.label_cargaMovie.setMovie(load_movie)
        self.label_carga.setText("Procesando")

        # # # # # # Definimos los textos del frame solucion
        self.button_volver_frame1.setText("Volver")
        # self.browser.setHtml("<p>Hola</p>")

    def setCompleter(self, names):
        # definimos un completer con los nombres especificados
        self.names = names
        completer = QtWidgets.QCompleter(names)
        # hacemos que no sea case sensible
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.intro_inicio.setCompleter(completer)
        self.intro_destino.setCompleter(completer)

    def calcularAction(self):
        # comprobamos si el inicio es una estacion de valida
        if self.intro_inicio.text() not in self.names:
            self.label_invalid_inicio.show()
        else:
            self.label_invalid_inicio.hide()

        # comprobamos si el destino es una estacion de valida
        if self.intro_destino.text() not in self.names:
            self.label_invalid_destino.show()
        else:
            self.label_invalid_destino.hide()
        # si destino y origen son validos, se lanza un tread en el que se lanza el algoritmo
        if self.intro_inicio.text() in self.names and self.intro_destino.text() in self.names:
            # if True:
            self.frame_principal.hide()
            self.label_cargaMovie.movie().start()
            self.frame_carga.show()
            # Lanzamos el algoritmo
            worker = Worker(self.doAlgorithm)
            worker.signals.result.connect(self.algorithmDone)
            self.poolThread.start(worker)

    def volver_framePrincipal(self):
        self.intro_inicio.clear()
        self.intro_destino.clear()
        self.frame_solucion.hide()
        self.frame_principal.show()

        # realiza las operaciones para el frame de soluciones
    def algorithmDone(self, data):
        self.browser.setHtml(data.getvalue().decode())
        self.frame_carga.hide()
        self.frame_solucion.show()
         

    def doAlgorithm(self):
        solution = Algorithm.Calcular(
            self.intro_inicio.text(), self.intro_destino.text(), 500)
        trayecto = []
        for x in solution:
            trayecto.append([float(x.longitud), float(x.latitud)])
        data = mapa.gen(trayecto, solution[0].name, solution[-1].name)
        return data
