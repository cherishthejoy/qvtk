from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase
import sys

from menubar import MenuBar
from central_widgets import CentralWidget


class MainWindow(QtWidgets.QMainWindow):

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600


    def __init__(self):
         
        super().__init__()

        self.menuBar = MenuBar(self)

        self.centralWidget = CentralWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.setSystemFont()

        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)


    def setSystemFont(self):

        fontId = QFontDatabase.addApplicationFont("fonts/JuliaMono-Regular.ttf")

        if fontId != -1:
            fontFamily = QFontDatabase.applicationFontFamilies(fontId)
            if fontFamily:
                self.FONT = QFont(fontFamily[0], 10)
                self.centralWidget.setFont(self.FONT)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())