from PyQt5 import QtWidgets, QtCore
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
import os
from database import connect_db

from camera_style import CustomInteractorStyle

class FirstTab(QtWidgets.QWidget):
    
    VTK_WINDOW_WIDTH = 300
    VTK_WINDOW_HEIGHT = 300
    OBJ_FILE = "assets/The-King-In-Yellow/the_king_in_yellow.obj"
    MTL_FILE = "assets/The-King-In-Yellow/the_king_in_yellow.mtl"

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupGrids()
        self.setupGroupBoxes()
        self.placeVTK()
        self.placeGroupBoxes()
        self.setupInputFields()
        self.setupLabels()
        self.placeFormLayoutItems()
        self.setupVTK()
        self.display_records()

        self.tableWidget.itemSelectionChanged.connect(self.update_line_edits)


    def setupGrids(self):

        self.grid1 = QtWidgets.QGridLayout()
        self.setLayout(self.grid1)
        

    def setupGroupBoxes(self):

        self.inspectGroup = QtWidgets.QGroupBox()
        self.inspectGroup.setTitle("Inspect")

        self.statsGroup = QtWidgets.QGroupBox()
        self.statsGroup.setTitle("Stats")

        self.synopsisGroup = QtWidgets.QGroupBox()
        self.synopsisGroup.setTitle("Synopsys")

        self.searchGroup = QtWidgets.QGroupBox()
        self.searchGroup.setTitle("Search")

        self.tableGroup = QtWidgets.QGroupBox()
        self.tableGroup.setTitle("Table")


    def placeVTK(self):

        self.vtkWindow = QVTKRenderWindowInteractor(self.inspectGroup)
        self.vtkWindow.setFixedSize(self.VTK_WINDOW_WIDTH, self.VTK_WINDOW_HEIGHT)

        self.inspectHorizontalLayout = QtWidgets.QHBoxLayout()
        self.inspectHorizontalLayout.addWidget(self.vtkWindow)

        self.vtkFormLayout = QtWidgets.QFormLayout()
        self.inspectHorizontalLayout.addLayout(self.vtkFormLayout)

        self.inspectGroup.setLayout(self.inspectHorizontalLayout)


        self.bookID = QtWidgets.QLabel()
        self.bookID.setText("Book Id")

        self.bookISBN = QtWidgets.QLabel()
        self.bookISBN.setText("Book ISBN")

        self.bookPrice =  QtWidgets.QLabel()
        self.bookPrice.setText("Book Price")

        self.bookStock = QtWidgets.QLabel()
        self.bookStock.setText("Stock")

        self.bookIDField = QtWidgets.QLineEdit()
        self.bookIDField.setObjectName("bookIdField")
        self.bookIDField.setReadOnly(True)

        self.bookISBNField = QtWidgets.QLineEdit()
        self.bookISBNField.setObjectName("bookISBNField")
        self.bookISBNField.setReadOnly(True)

        self.bookPriceField = QtWidgets.QLineEdit()
        self.bookPriceField.setObjectName("bookPriceField")
        self.bookPriceField.setReadOnly(True)

        self.stockField = QtWidgets.QLineEdit()
        self.stockField.setObjectName("stockField")
        self.stockField.setReadOnly(True)

        self.addButton = QtWidgets.QPushButton('Add', self)



        self.vtkFormLayout.addRow(self.bookID, self.bookIDField)
        self.vtkFormLayout.addRow(self.bookISBN, self.bookISBNField)
        self.vtkFormLayout.addRow(self.bookPrice, self.bookPriceField)
        self.vtkFormLayout.addRow(self.bookStock, self.stockField)
        self.vtkFormLayout.addWidget(self.addButton)


    def placeGroupBoxes(self):

        self.grid1.addWidget(self.inspectGroup, 0, 0, 2, 1)
        self.grid1.addWidget(self.searchGroup, 0, 1)
        self.grid1.addWidget(self.synopsisGroup, 2, 0, 2, 1)
        self.grid1.addWidget(self.statsGroup, 1, 1, 3, 1)
        self.grid1.addWidget(self.tableGroup, 4, 0, 2, 2)


    def setupInputFields(self):

        self.bookTitleField = QtWidgets.QLineEdit()
        self.bookTitleField.setObjectName("statsFieldOne")
        self.bookTitleField.setReadOnly(True)

        self.bookAuthorField = QtWidgets.QLineEdit()
        self.bookAuthorField.setObjectName("statFieldTwo")
        self.bookAuthorField.setReadOnly(True)

        self.bookLanguageField = QtWidgets.QLineEdit()
        self.bookLanguageField.setObjectName("statFieldThree")
        self.bookLanguageField.setReadOnly(True)

        self.bookPublisherField = QtWidgets.QLineEdit()
        self.bookPublisherField.setObjectName("statFieldFour")
        self.bookPublisherField.setReadOnly(True)

        self.bookPublishedDateField = QtWidgets.QLineEdit()
        self.bookPublishedDateField.setObjectName("statFieldEleven")
        self.bookPublishedDateField.setReadOnly(True)

        self.bookPageCountField = QtWidgets.QLineEdit()
        self.bookPageCountField.setObjectName("statFieldFive")
        self.bookPageCountField.setReadOnly(True)

        self.bookPrintDateField = QtWidgets.QLineEdit()
        self.bookPrintDateField.setObjectName("statFieldSix")
        self.bookPrintDateField.setReadOnly(True)

        self.bookCategoryField = QtWidgets.QLineEdit()
        self.bookCategoryField.setObjectName("statFieldSeven")
        self.bookCategoryField.setReadOnly(True)

        self.bookCoverTypeField = QtWidgets.QLineEdit()
        self.bookCoverTypeField.setObjectName("statFieldEight")
        self.bookCoverTypeField.setReadOnly(True)

        self.bookLicenseField = QtWidgets.QLineEdit()
        self.bookLicenseField.setObjectName("statFieldNine") 
        self.bookLicenseField.setReadOnly(True)

        self.bookDimensionField = QtWidgets.QLineEdit()
        self.bookDimensionField.setObjectName("statFieldTen")
        self.bookDimensionField.setReadOnly(True)


    def setupLabels(self):

        self.bookTitle = QtWidgets.QLabel()
        self.bookTitle.setText("Book Title")

        self.bookAuthor =  QtWidgets.QLabel()
        self.bookAuthor.setText("Book Author")

        self.bookLanguage = QtWidgets.QLabel()
        self.bookLanguage.setText("Book Language")

        self.bookPublisher = QtWidgets.QLabel()
        self.bookPublisher.setText("Book Publisher")

        self.bookPublishedDate = QtWidgets.QLabel()
        self.bookPublishedDate.setText("Book Published Date")

        self.bookPageCount = QtWidgets.QLabel()
        self.bookPageCount.setText("Book Page Count")

        self.bookPrintDate = QtWidgets.QLabel()
        self.bookPrintDate.setText("Book Print Date")

        self.bookCategory = QtWidgets.QLabel()
        self.bookCategory.setText("Book Category")

        self.bookCoverType = QtWidgets.QLabel()
        self.bookCoverType.setText("Book Cover Type")

        self.bookLicense = QtWidgets.QLabel()
        self.bookLicense.setText("Book License")

        self.bookDimension = QtWidgets.QLabel()
        self.bookDimension.setText("Dimension")

        
    def placeFormLayoutItems(self):

        #Stats Group

        self.statsFormLayout = QtWidgets.QFormLayout()

        self.statsFormLayout.addRow(self.bookTitle, self.bookTitleField)
        self.statsFormLayout.addRow(self.bookAuthor, self.bookAuthorField)
        self.statsFormLayout.addRow(self.bookLanguage, self.bookLanguageField)
        self.statsFormLayout.addRow(self.bookPublisher, self.bookPublisherField)
        self.statsFormLayout.addRow(self.bookPublishedDate, self.bookPublishedDateField)
        self.statsFormLayout.addRow(self.bookPageCount, self.bookPageCountField)
        self.statsFormLayout.addRow(self.bookPrintDate, self.bookPrintDateField)
        self.statsFormLayout.addRow(self.bookCategory, self.bookCategoryField)
        self.statsFormLayout.addRow(self.bookCoverType, self.bookCoverTypeField)
        self.statsFormLayout.addRow(self.bookLicense, self.bookLicenseField)
        self.statsFormLayout.addRow(self.bookDimension, self.bookDimensionField)
        self.statsGroup.setLayout(self.statsFormLayout)


        #SearchGroup

        self.searchBar = QtWidgets.QLabel()
        self.searchBar.setText("Search")

        self.searchBarField = QtWidgets.QLineEdit()
        self.searchBarField.setObjectName("searchField")

        self.categoryBar = QtWidgets.QLabel()
        self.categoryBar.setText("Filter/Category")

        self.categoryBarField = QtWidgets.QLineEdit()
        self.categoryBarField.setObjectName("categoryField")


        self.searchBarLayout = QtWidgets.QHBoxLayout()
        self.searchBarLayout.setAlignment(QtCore.Qt.AlignTop)

        self.searchBarLayout.addWidget(self.searchBar)
        self.searchBarLayout.addWidget(self.searchBarField)

        self.searchBarLayout.addWidget(self.categoryBar)
        self.searchBarLayout.addWidget(self.categoryBarField)

        self.keywordCheck = QtWidgets.QCheckBox()
        self.keywordCheck.setText("Keyword/Prompt")
        self.searchBarLayout.addWidget(self.keywordCheck)

        self.searchGroupLayout = QtWidgets.QVBoxLayout()
        self.searchGroupLayout.addLayout(self.searchBarLayout)

        self.searchButton  = QtWidgets.QPushButton('Search', self)
        self.searchGroupLayout.addWidget(self.searchButton)
    
        self.searchGroup.setLayout(self.searchGroupLayout)


        #SynopsisGroup

        self.synopsisGroupLayout = QtWidgets.QVBoxLayout()

        self.synopsisLabel = QtWidgets.QTextEdit()        

        self.synopsisLabel.setReadOnly(True)
        self.synopsisGroupLayout.addWidget(self.synopsisLabel)
        self.synopsisGroup.setLayout(self.synopsisGroupLayout)


        #TableGroup

        self.tableWidget = QtWidgets.QTableWidget(10, 15)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["Title", "Author", "Language", "ISBN",
                                                    "Publisher", "Published Date", "Page Count", "Print Date",
                                                    "Category", "Cover Type", "License",
                                                    "Dimension", "Price", "Stock", "Synopsis"])


        self.tableGroupLayout = QtWidgets.QVBoxLayout()
        self.tableGroupLayout.addWidget(self.tableWidget)

        self.tableGroup.setLayout(self.tableGroupLayout)


    def setupVTK(self):

        importer = vtk.vtkOBJImporter()
        importer.SetFileName(self.OBJ_FILE)
        importer.SetFileNameMTL(self.MTL_FILE)
        
        obj_dir = os.path.dirname(self.OBJ_FILE)

        importer.SetTexturePath(obj_dir)

        self.renderer = vtk.vtkRenderer()
        self.vtkWindow.GetRenderWindow().AddRenderer(self.renderer)

        importer.SetRenderWindow(self.vtkWindow.GetRenderWindow())
        importer.Update()


        self.textActor = vtk.vtkTextActor()
        self.textActor.SetInput("The King in Yellow")
        self.textActor.GetTextProperty().SetFontSize(10)
        self.textActor.GetTextProperty().SetColor(1, 1, 1)

        self.renderer.AddActor(self.textActor)

        self.renderWindowInteractor = self.vtkWindow.GetRenderWindow().GetInteractor()
        style = vtk.vtkInteractorStyleTrackballCamera()

        self.renderer.SetBackground(0.2, 0.2, 0.2)
        self.renderer.ResetCamera()

        style = CustomInteractorStyle(self.renderer)
        self.renderWindowInteractor.SetInteractorStyle(style)

        self.renderWindowInteractor.Initialize()

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
        
        self.tableWidget.hideColumn(self.tableWidget.columnCount() - 1)
        

    def update_line_edits(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()

            self.bookTitleField.setText(self.tableWidget.item(row, 0).text())
            self.bookAuthorField.setText(self.tableWidget.item(row, 1).text())
            self.bookLanguageField.setText(self.tableWidget.item(row, 2).text())
            self.bookISBNField.setText(self.tableWidget.item(row, 3).text())
            self.bookPublisherField.setText(self.tableWidget.item(row, 4).text())
            self.bookPublishedDateField.setText(self.tableWidget.item(row, 5).text())
            self.bookPageCountField.setText(self.tableWidget.item(row, 6).text())
            self.bookPrintDateField.setText(self.tableWidget.item(row, 7).text())
            self.bookCategoryField.setText(self.tableWidget.item(row, 8).text())
            self.bookCoverTypeField.setText(self.tableWidget.item(row, 9).text())
            self.bookLicenseField.setText(self.tableWidget.item(row, 10).text())
            self.bookDimensionField.setText(self.tableWidget.item(row, 11).text())
            self.bookPriceField.setText(self.tableWidget.item(row, 12).text())
            self.stockField.setText(self.tableWidget.item(row, 13).text())
            self.synopsisLabel.setText(self.tableWidget.item(row, 14).text())