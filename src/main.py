from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase
import sys
import sqlite3
import qdarktheme

from menubar import MenuBar
from tab_one import FirstTab
from tab_two import SecondTab
from tab_three import ThirdTab
from database import initialize_db


class MainWindow(QtWidgets.QMainWindow):

    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800

    def __init__(self):
         
        super().__init__()

        self.conn = sqlite3.connect('ishtar.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM book_info")
    
        self.menuBar = MenuBar(self)
        self.tabOne = FirstTab()
        self.tabTwo = SecondTab(self.tabOne)
        self.tabThree = ThirdTab()

        self.tabWidget = QtWidgets.QTabWidget(self)

        self.tabWidget.addTab(self.tabOne, "Information")
        self.tabWidget.addTab(self.tabTwo, "Inventory")
        self.tabWidget.addTab(self.tabThree, "Buy")

        self.setCentralWidget(self.tabWidget)
        self.setSystemFont()
        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.refresh_tables()


    def setSystemFont(self):

        fontId = QFontDatabase.addApplicationFont("fonts/saxMono.ttf")

        if fontId != -1:
            fontFamily = QFontDatabase.applicationFontFamilies(fontId)
            if fontFamily:
                self.FONT = QFont(fontFamily[0], 10)
                self.centralWidget.setFont(self.FONT)


    def refresh_tables(self):
        
        self.cursor.execute("SELECT * FROM book_info")
        data = self.cursor.fetchall()
        



if __name__ == "__main__":

    initialize_db()

    qdarktheme.enable_hi_dpi()
    
    app = QtWidgets.QApplication(sys.argv)

    qdarktheme.setup_theme("auto")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())