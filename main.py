from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
import sys

from menuBar import MenuBar
from centralWidgets import CentralWidget


class MainWindow(QtWidgets.QMainWindow):

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    FONT = QFont("Times", 10)

    def __init__(self):
         
        super().__init__()

        self.menuBar = MenuBar(self)

        self.centralWidget = CentralWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setFont(self.FONT)

        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())