from PyQt5 import QtWidgets
from database import connect_db, insert_data
from tab_one import FirstTab

class SecondTab(QtWidgets.QWidget):

    def __init__(self, tabOne, parent = None):
        super().__init__(parent)
        self.setupGridLayout()
        self.setupGroupBox()
        self.placeGroupBox()
        self.setupInputs()
        self.button_clearance()
        self.display_records()

        self.tabOne = tabOne

    
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

        #Item Group

        labels = ["Book Title", "Book Publisher", "Book ISBN", 
                "Book Published Date", "Book Language",
                "Book Author", "Book Category", "Book Price",
                "Book Dimension", "Book Print Date", "Stock",
                "Book Cover Type", "Book Page Count"]
        
        objects = ["bookTitleField", "bookPublisherField", "bookISBNField", 
                "bookPublishedDateField", "bookLanguageField",
                "bookAuthorField", "bookCategoryField", "bookPriceField",
                "bookDimensionField", "bookPrintDateField", "stockField",
                "bookCoverTypeField", "bookPageCountField"]
        
        categoryList = ["None", "Adventure", "Action", "Horror", "Sci-fi", "Romance", "Literature"]
        languageList = ["None", "English", "Mongolian", "Chinese", "German"]
        bookCoverList = ["None", "Hardcover", "Paperback"]

        self.fields = {}

        for label_text, object_name in zip(labels, objects):
            label = QtWidgets.QLabel()
            label.setText(label_text)

            if object_name == "bookCategoryField":
                field = QtWidgets.QComboBox()
                field.addItems(categoryList)
            elif object_name == "bookLanguageField":
                field = QtWidgets.QComboBox()
                field.addItems(languageList)
            elif object_name == "bookCoverTypeField":
                field = QtWidgets.QComboBox()
                field.addItems(bookCoverList)
            elif object_name in ["bookPublishedDateField", "bookPrintDateField"]:
                field = QtWidgets.QDateEdit()
            else:
                field = QtWidgets.QLineEdit()

            field.setObjectName(object_name)

            self.fields[label_text] = (label, field)

        self.formLayouts = [QtWidgets.QFormLayout() for _ in range(3)]

        for i, (label_text, (label, field)) in enumerate(self.fields.items()):
            self.formLayouts[i % 3].addRow(label, field)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        for formLayout in self.formLayouts:
            self.horizontalLayout.addLayout(formLayout)


        self.insertButton = QtWidgets.QPushButton('Insert', self)
        self.insertButton.setMaximumWidth(100)
        self.insertButtonLayout = QtWidgets.QHBoxLayout()
        self.insertButtonLayout.addStretch(1)
        self.insertButtonLayout.addWidget(self.insertButton)
        self.formLayouts[2].addRow(self.insertButtonLayout)

        self.itemGroup.setLayout(self.horizontalLayout)


        #Table Group

        self.tableWidget = QtWidgets.QTableWidget(20, 13)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["Title", "Author", "Language", "ISBN",
                                                    "Publisher", "Page Count", "Print Date",
                                                    "Category", "Cover Type", "License",
                                                    "Dimension", "Price", "Stock"])


        self.tableGroupLayout = QtWidgets.QVBoxLayout()
        self.tableGroupLayout.addWidget(self.tableWidget)

        self.tableGroup.setLayout(self.tableGroupLayout)

        #Search Group

        self.searchBar = QtWidgets.QLabel()
        self.searchBar.setText("Search")

        self.searchBarField = QtWidgets.QLineEdit()
        self.searchBarField.setObjectName("searchField")

        self.categoryBar = QtWidgets.QLabel()
        self.categoryBar.setText("Filter/Category")

        self.categoryBarField = QtWidgets.QLineEdit()
        self.categoryBarField.setObjectName("categoryField")


        self.searchBarLayout = QtWidgets.QHBoxLayout()

        self.searchBarLayout.addWidget(self.searchBar)
        self.searchBarLayout.addWidget(self.searchBarField)

        self.searchBarLayout.addWidget(self.categoryBar)
        self.searchBarLayout.addWidget(self.categoryBarField)

        self.searchButton = QtWidgets.QPushButton('Search', self)
        self.searchBarLayout.addWidget(self.searchButton)

        self.resetButton = QtWidgets.QPushButton('Reset', self)
        self.searchBarLayout.addWidget(self.resetButton)
    
        self.searchGroup.setLayout(self.searchBarLayout)

        #Change Group

        self.changeButtonsLayout = QtWidgets.QHBoxLayout()

        self.updateButton = QtWidgets.QPushButton('Update', self)
        self.changeButtonsLayout.addWidget(self.updateButton)

        self.deleteButton = QtWidgets.QPushButton('Delete', self)
        self.changeButtonsLayout.addWidget(self.deleteButton)

        self.changeGroup.setLayout(self.changeButtonsLayout)


    def add_record(self):

        data = tuple(field.currentText() if isinstance(field, QtWidgets.QComboBox) else field.text()
        for _, (_, field) in self.fields.items())

        connection = connect_db()
        cursor = connection.cursor()
        insert_data(cursor, data)
        connection.commit()
        connection.close()

        self.display_records()
        self.tabOne.display_records()

        # Clear

        for _, (_, field) in self.fields.items():
            field.clear()

    def button_clearance(self):
        self.insertButton.clicked.connect(self.add_record)


    def display_records(self):

        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM book_info')
        records = cursor.fetchall()
        connection.close()

        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(records):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))