from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

class Movie(object):
    def setupUi(self, window):
        # definimos el nombre e icono de la App
        window.setWindowTitle("Metro")

        # definimos los tamaños de la ventana principal
        window.resize(500, 600)
        window.setMinimumSize(QtCore.QSize(500, 600))
        window.setMaximumSize(QtCore.QSize(500, 600))
        window.setObjectName("window")

        # definimos el Widget de la ventana
        self.central_widget = QtWidgets.QWidget(window)
        self.central_widget.setObjectName("central_widget")
        window.setCentralWidget(self.central_widget)

        self.labelMovie = QtWidgets.QLabel(self.central_widget)
        self.labelMovie.setGeometry(QtCore.QRect(100, 100, 100, 100))
        self.labelMovie.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.labelMovie.setScaledContents(True)
        movie = QtGui.QMovie(".\\images\\carga.gif")
        self.labelMovie.setMovie(movie)
        # movie.start()


    pass

if __name__ == "__main__":
    import sys
    nombres = ["Luis", "Lian", "Luisa", "Alberto", "Elisa", "Elma"]
    nombres.sort()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Movie()
    ui.setupUi(mainWindow)
    mainWindow.show()
    ui.labelMovie.movie().start()
    
    sys.exit(app.exec_())