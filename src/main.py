from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase
import sys
import qdarktheme

from menubar import MenuBar
from central_widgets import CentralWidget


class MainWindow(QtWidgets.QMainWindow):

    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800


    def __init__(self):
         
        super().__init__()

        self.menuBar = MenuBar(self)

        self.centralWidget = CentralWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.setSystemFont()

        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)


    def setSystemFont(self):

        fontId = QFontDatabase.addApplicationFont("fonts/saxMono.ttf")

        if fontId != -1:
            fontFamily = QFontDatabase.applicationFontFamilies(fontId)
            if fontFamily:
                self.FONT = QFont(fontFamily[0], 10)
                self.centralWidget.setFont(self.FONT)



if __name__ == "__main__":

    qdarktheme.enable_hi_dpi()
    
    app = QtWidgets.QApplication(sys.argv)

    qdarktheme.setup_theme("auto")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())