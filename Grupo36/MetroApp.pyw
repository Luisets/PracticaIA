import random
import sys
from PySide2 import QtWidgets
from App.Gui import AppGui


def main():
    nombres = ["Agios Antonios", "Sepolia", "Attiki", "Larissa Station", "Metaxourgeio", "Omonoia", "Panepistimio",
               "Syntagma", "Akropoli", "Syngrou-Fix ", "Neos Kosmos", "Agios Ioannis", "Dafni", "Agios Dimitrios",
               "Egaleo", "Eleonas", "Kerameikos", "Monastiraki", "Evangelismos", "Megaro Moussikis",
               "Ambelokipi", "Panormou", "Katehaki", "Ethniki Amyna", "Holargos", "Nomismatokopio", "Aghia Paraskevi",
               "Halandri", "Pallini", "Paiania-Kantza", "Koropi", "Airport",
               "Piraeus", "Faliro", "Moschato", "Kallithea", "Tavros", "Petralona", "Thissio",
               "Victoria", "Aghios Nikolaos", "Kato Patissia", "Aghios Eleftherios", "Ano Patissia", "Perissos", "Pefkakia",
               "Nea lonia", "Iraklio", "Irini", "Neratziotissa", "Maroussi", "KAT", "Kifissia"]
    nombres.sort()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = AppGui()
    ui.setupUi(mainWindow)
    ui.setCompleter(nombres)
    mainWindow.show()
    sys.exit(app.exec_())
    pass


if __name__ == "__main__":
    main()
