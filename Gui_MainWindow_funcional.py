
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget


class Gui_MainWindow(object):

    # definimos la ubicacion del icono
    icon_Path = ".\\images\\metro_icon.jpg"

    def setupUi(self, window):
        # definimos el nombre e icono de la App
        window.setWindowTitle("Metro")
        window.setWindowIcon(QtGui.QIcon(self.icon_Path))

        # definimos los tamaños de la ventana principal
        window.resize(500, 600)
        window.setMinimumSize(QtCore.QSize(500, 600))
        window.setMaximumSize(QtCore.QSize(500, 600))
        window.setObjectName("window")

        # definimos el Widget de la ventana
        self.central_widget = QtWidgets.QWidget(window)
        self.central_widget.setObjectName("central_widget")

        # definimos central_windget como widget principal de la ventana
        window.setCentralWidget(self.central_widget)

        # definimos el logo principal
        self.label_logo = QtWidgets.QLabel(self.central_widget)
        self.label_logo.setGeometry(QtCore.QRect(175, 25, 150, 150))
        self.label_logo.setObjectName("label_logo")

        # definimos la paleca de color para error los label de error
        # # solo definimos la activa 
        error_palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        error_palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)

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
        self.label_inicio = QtWidgets.QLabel(self.central_widget)
        self.label_inicio.setGeometry(QtCore.QRect(100, 240, 80, 35))
        self.label_inicio.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_inicio.setFont(arialFont_label)
        self.label_inicio.setObjectName("label_inicio")

        # definimos la caja de texto para el inicio
        self.intro_inicio = QtWidgets.QLineEdit(self.central_widget)
        self.intro_inicio.setGeometry(QtCore.QRect(190, 240, 175, 35))
        self.intro_inicio.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.intro_inicio.setFont(arialFont_intro)
        self.intro_inicio.setText("")
        self.intro_inicio.setObjectName("intro_inicio")
        
        # definimos el label de Inicio invalido
        self.label_invalid_inicio = QtWidgets.QLabel(self.central_widget)
        self.label_invalid_inicio.setGeometry(QtCore.QRect(190, 272, 111, 21))
        self.label_invalid_inicio.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_invalid_inicio.setPalette(error_palette)
        self.label_invalid_inicio.setObjectName("label_invalid_inicio")
        # # lo escondemos mientras no sea necesario
        self.label_invalid_inicio.hide()
        # definimos el label destino
        self.label_destino = QtWidgets.QLabel(self.central_widget)
        self.label_destino.setGeometry(QtCore.QRect(100, 330, 80, 35))
        self.label_destino.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_destino.setFont(arialFont_label)
        self.label_destino.setObjectName("label_destino")

        # definimos la caja de texto para el destino
        self.intro_destino = QtWidgets.QLineEdit(self.central_widget)
        self.intro_destino.setGeometry(QtCore.QRect(190, 330, 175, 35))
        self.intro_destino.setFont(arialFont_intro)
        self.intro_destino.setText("")
        self.intro_destino.setObjectName("intro_destino")

        # definimos el label de Destino invalido
        self.label_invalid_destino = QtWidgets.QLabel(self.central_widget)
        self.label_invalid_destino.setGeometry(QtCore.QRect(190, 362, 111, 21))
        self.label_invalid_destino.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_invalid_destino.setPalette(error_palette)
        self.label_invalid_destino.setObjectName("label_invalid_inicio")
        # # lo escondemos mientras no sea necesario
        self.label_invalid_destino.hide()

        # definimos el boton para el algoritmo
        self.button_calcular = QtWidgets.QPushButton(self.central_widget)
        self.button_calcular.setGeometry(QtCore.QRect(200, 430, 100, 30))
        self.button_calcular.setFont(arialFont_intro)
        # definimos la accion al presionar el boton
        self.button_calcular.clicked.connect(self.calcularAction)
        self.button_calcular.setObjectName("button_calcular")
        # rellenamos todos los componentes
        self.fillTexts()

        # definimos al madre ne nuestra Gui a la window a la que esta asociada
        QtCore.QMetaObject.connectSlotsByName(window)

    def fillTexts(self):
        # definimos le contenido del logo
        icon = QtGui.QIcon(self.icon_Path)
        pixmap = icon.pixmap(150, 150, QtGui.QIcon.Active, QtGui.QIcon.On)
        self.label_logo.setPixmap(pixmap)

        #definimos el contenido del resto de labels y el button
        self.label_inicio.setText("Inicio:")
        self.label_destino.setText("Destino:")
        self.button_calcular.setText("Calcular")
        self.label_invalid_inicio.setText("La estación no existe")
        self.label_invalid_destino.setText("La estación no existe")

    def setCompleter(self, names):
        # definimos un completer con los nombres especificados
        self.names = names
        completer = QtWidgets.QCompleter(names)
        # hacemos que no sea case sensible
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.intro_inicio.setCompleter(completer)
        self.intro_destino.setCompleter(completer)
        
    def calcularAction(self):
        if self.intro_inicio.text() not in self.names:
            self.label_invalid_inicio.show()

        if self.intro_destino.text() not in self.names:
            self.label_invalid_destino.show()
            
        if self.intro_inicio.text() in self.names and self.intro_destino.text() in self.names:
            self.label_invalid_inicio.hide()
            self.label_invalid_destino.hide()
            print("estación de inicio:  {}".format(self.intro_inicio.text()))
            print("estación de destino: {}".format(self.intro_destino.text()))
            self.central_widget.setHidden(True)
            import time
            time.sleep(3)
            print("he escondido el widget")
            self.central_widget.setHidden(False)



if __name__ == "__main__":
    import sys
    nombres = ["Luis", "Lian", "Luisa", "Alberto", "Elisa", "Elma"]
    nombres.sort()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Gui_MainWindow()
    ui.setupUi(mainWindow)
    ui.setCompleter(nombres)
    mainWindow.show()
    sys.exit(app.exec_())
