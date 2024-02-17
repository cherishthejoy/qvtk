from PyQt5 import QtWidgets
import sys

from menuBar import MenuBar
from centralWidgets import CentralWidget

class MainWindow(QtWidgets.QMainWindow):

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        
        self.centralWidget = CentralWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.menuBar = MenuBar(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())