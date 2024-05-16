from PyQt5 import QtWidgets

class SecondTab(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupGridLayout()
        self.setupGrid()
        self.setupGroupBox()
        self.placeGroupBox()
        self.setupInputs()

    def setupGrid(self):

        self.gridWidget = QtWidgets.QWidget()
        self.setLayout(self.grid2)
    
    def setupGridLayout(self):

        self.grid2 = QtWidgets.QGridLayout()
        self.setLayout(self.grid2)

    def setupGroupBox(self):

        self.itemGroup = QtWidgets.QGroupBox()
        self.itemGroup.setTitle("Item")

        self.tableGroup = QtWidgets.QGroupBox()
        self.tableGroup.setTitle("Table")

        self.searchGroup = QtWidgets.QGroupBox()
        self.searchGroup.setTitle("Search")

        self.changeGroup = QtWidgets.QGroupBox()
        self.changeGroup.setTitle("Update/Delete")


    def placeGroupBox(self):

        self.grid2.addWidget(self.itemGroup, 0, 0, 2, 3)
        self.grid2.addWidget(self.tableGroup, 2, 0, 4, 3)
        self.grid2.addWidget(self.searchGroup, 6, 0, 1, 2)
        self.grid2.addWidget(self.changeGroup, 6, 2)


    def setupInputs(self):

        #ItemGroup

        self.bookID = QtWidgets.QLabel()
        self.bookID.setText("Book Id")

        self.bookIDField = QtWidgets.QLineEdit()
        self.bookIDField.setObjectName("bookIdField")

        self.itemGroupLayout = QtWidgets.QFormLayout()

        self.itemGroupLayout.addRow(self.bookID, self.bookIDField)

        #TableGroup

        #SearchGroup

        #ChangeGroup
