from PyQt5 import QtWidgets

class ThirdTab(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupGridsTwo()
        self.setupTabTwo()
        

    def setupTabTwo(self):

        self.gridWidget = QtWidgets.QWidget()
        self.gridWidget.setLayout(self.grid2)

        self.gridWrapperLayout = QtWidgets.QVBoxLayout(self)

        self.tabWidget = QtWidgets.QTabWidget(self)

        self.gridWrapperLayout.addWidget(self.tabWidget)
    
    def setupGridsTwo(self):

        self.grid2 = QtWidgets.QGridLayout()
        self.setLayout(self.grid2)