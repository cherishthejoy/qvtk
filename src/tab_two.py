from PyQt5 import QtWidgets, QtCore
from database import connect_db, insert_data
import datetime

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

        self.tableWidget.itemSelectionChanged.connect(self.update_line_edits)

    
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

        labels = ["Title", "Author", "Language", 
                "ISBN", "Publisher", "Published Date",
                "Page Count", "Print Date", "Category",
                "Cover Type", "License", "Dimension",
                "Price", "Stock"]
        
        objects = ["bookTitleField", "bookAuthorField", "bookLanguageField", 
                "bookISBNField", "bookPublisherField", "bookPublishedDateField",
                "bookPageCountField", "bookPrintDateField", "bookCategoryField",
                "bookCoverTypeField", "bookLicenseField", "bookDimensionField",
                "bookPriceField", "stockField"]
        
        categoryList = ["None", "Adventure", "Action", "Horror", "Sci-fi", "Romance", "Literature"]
        languageList = ["None", "English", "Mongolian", "Chinese", "German"]
        CoverList = ["None", "Hardcover", "Paperback"]
        LicenseList = ["None", "Copyright", "Public Domain", "CC", "Open Access", "Proprietary"]

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
                field.addItems(CoverList)
            elif object_name == "bookLicenseField":
                field = QtWidgets.QComboBox()
                field.addItems(LicenseList)
            elif object_name in ["bookPublishedDateField", "bookPrintDateField"]:
                field = QtWidgets.QDateEdit()
                field.setDisplayFormat("MM/dd/yyyy")
                field.setCalendarPopup(True)
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

        self.synopsisBox = QtWidgets.QTextEdit()
        self.horizontalLayout.addWidget(self.synopsisBox)

        self.itemGroup.setLayout(self.horizontalLayout)


        #Table Group

        self.tableWidget = QtWidgets.QTableWidget(20, 15)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["Title", "Author", "Language", "ISBN",
                                                    "Publisher", "Published Date", "Page Count", "Print Date",
                                                    "Category", "Cover Type", "License",
                                                    "Dimension", "Price", "Stock", "Synopsis"])


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

        data = tuple(
            field.currentText() if isinstance(field, QtWidgets.QComboBox) 
            else field.toPlainText() if isinstance(field, QtWidgets.QTextEdit)
            else field.dateTime().toString("MM/dd/yyyy") if isinstance(field, QtWidgets.QDateTimeEdit)
            else field.text()
            for _, (_, field) in self.fields.items()
        )

        synopsis = self.synopsisBox.toPlainText()
        data += (synopsis,)

        connection = connect_db()
        cursor = connection.cursor()
        insert_data(cursor, data)
        connection.commit()
        connection.close()

        self.display_records()
        self.tabOne.display_records()

        # Clear

        for _, (_, field) in self.fields.items():
            if isinstance(field, QtWidgets.QLineEdit) or isinstance(field, QtWidgets.QTextEdit):
                field.clear()
            elif isinstance(field, QtWidgets.QComboBox):
                field.setCurrentIndex(0)
            elif isinstance(field, QtWidgets.QDateEdit):
                field.setDate(QtCore.QDate.currentDate())
        self.synopsisBox.clear()

    def button_clearance(self):
        self.insertButton.clicked.connect(self.add_record)
        self.deleteButton.clicked.connect(self.deleted_selected_row)


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
                if column_number in [5, 7]:
                    data = datetime.datetime.strptime(data, '%m/%d/%Y').strftime('%m/%d/%Y')
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def deleted_selected_row(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()

            rowid_item = self.tableWidget.item(row, 3)
            if rowid_item is not None:
                rowid = rowid_item.text()

                connection = connect_db()
                cursor = connection.cursor()
                cursor.execute('DELETE FROM book_info WHERE ISBN = ?', (rowid,))
                connection.commit()
                connection.close()

                self.tableWidget.removeRow(row)
                self.tabOne.display_records()


    def update_line_edits(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()

            published_date_str = self.tableWidget.item(row, 5).text()
            print_date_str = self.tableWidget.item(row, 7).text()

            published_date = QtCore.QDate.fromString(published_date_str, 'MM/dd/yyyy')
            print_date = QtCore.QDate.fromString(print_date_str, 'MM/dd/yyyy')
            
            self.fields['Title'][1].setText(self.tableWidget.item(row, 0).text())
            self.fields['Author'][1].setText(self.tableWidget.item(row, 1).text())
            self.fields['Language'][1].setCurrentText(self.tableWidget.item(row, 2).text())
            self.fields['ISBN'][1].setText(self.tableWidget.item(row, 3).text())
            self.fields['Publisher'][1].setText(self.tableWidget.item(row, 4).text())
            self.fields['Published Date'][1].setDate(published_date)
            self.fields['Page Count'][1].setText(self.tableWidget.item(row, 6).text())
            self.fields['Print Date'][1].setDate(print_date)
            self.fields['Category'][1].setCurrentText(self.tableWidget.item(row, 8).text())
            self.fields['Cover Type'][1].setCurrentText(self.tableWidget.item(row, 9).text())
            self.fields['License'][1].setCurrentText(self.tableWidget.item(row, 10).text())
            self.fields['Dimension'][1].setText(self.tableWidget.item(row, 11).text())
            self.fields['Price'][1].setText(self.tableWidget.item(row, 12).text())
            self.fields['Stock'][1].setText(self.tableWidget.item(row, 13).text())
            self.synopsisBox.setText(self.tableWidget.item(row, 14).text())