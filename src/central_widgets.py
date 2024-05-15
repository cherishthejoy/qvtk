from PyQt5 import QtWidgets, QtCore
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
import os

from camera_style import CustomInteractorStyle

class CentralWidget(QtWidgets.QWidget):
    
    VTK_WINDOW_WIDTH = 300
    VTK_WINDOW_HEIGHT = 300
    OBJ_FILE = "assets/The-King-In-Yellow/the_king_in_yellow.obj"
    MTL_FILE = "assets/The-King-In-Yellow/the_king_in_yellow.mtl"

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupGrids()
        self.setupTabs()
        self.setupGroupBoxes()
        self.placeVTK()
        self.placeGroupBoxes()
        self.setupInputFields()
        self.setupLabels()
        self.placeFormLayoutItems()
        self.setupVTK()


    def setupTabs(self):

        self.PlaceholderLabel1 = QtWidgets.QLabel("This is the 2nd tab!")

        self.gridWidget = QtWidgets.QWidget()
        self.gridWidget.setLayout(self.grid1)

        self.gridWrapperLayout = QtWidgets.QVBoxLayout(self)

        self.tabWidget = QtWidgets.QTabWidget(self)

        self.gridWrapperLayout.addWidget(self.tabWidget)
        self.tabWidget.addTab(self.gridWidget, "Inventory")
        

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
        # self.vtkFormLayout.setFormAlignment(QtCore.Qt.AlignCenter)

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

        self.bookISBNField = QtWidgets.QLineEdit()
        self.bookISBNField.setObjectName("bookISBNField")

        self.bookPriceField = QtWidgets.QLineEdit()
        self.bookPriceField.setObjectName("bookPriceField")

        self.stockField = QtWidgets.QLineEdit()
        self.stockField.setObjectName("stockField")

        self.addButton  = QtWidgets.QPushButton('Add', self)



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

        self.bookNameField = QtWidgets.QLineEdit()
        self.bookNameField.setObjectName("statsFieldOne")

        self.bookAuthorField = QtWidgets.QLineEdit()
        self.bookAuthorField.setObjectName("statFieldTwo")

        self.bookLanguageField = QtWidgets.QLineEdit()
        self.bookLanguageField.setObjectName("statFieldThree")

        self.bookPublisherField = QtWidgets.QLineEdit()
        self.bookPublisherField.setObjectName("statFieldFour")

        self.bookPageCountField = QtWidgets.QLineEdit()
        self.bookPageCountField.setObjectName("statFieldFive")

        self.bookPrintDateField = QtWidgets.QLineEdit()
        self.bookPrintDateField.setObjectName("statFieldSix")

        self.bookCategoryField = QtWidgets.QLineEdit()
        self.bookCategoryField.setObjectName("statFieldSeven")

        self.bookCoverTypeField = QtWidgets.QLineEdit()
        self.bookCoverTypeField.setObjectName("statFieldEight")

        self.bookLicenseField = QtWidgets.QLineEdit()
        self.bookLicenseField.setObjectName("statFieldNine") 

        self.bookDimensionField = QtWidgets.QLineEdit()
        self.bookDimensionField.setObjectName("statFieldTen")


    def setupLabels(self):

        self.bookName = QtWidgets.QLabel()
        self.bookName.setText("Book Name")

        self.bookAuthor =  QtWidgets.QLabel()
        self.bookAuthor.setText("Book Author")

        self.bookLanguage = QtWidgets.QLabel()
        self.bookLanguage.setText("Book Language")

        self.bookPublisher = QtWidgets.QLabel()
        self.bookPublisher.setText("Book Publisher")

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

        self.statsFormLayout.addRow(self.bookName, self.bookNameField)

        self.statsFormLayout.addRow(self.bookAuthor, self.bookAuthorField)

        self.statsFormLayout.addRow(self.bookLanguage, self.bookLanguageField)

        self.statsFormLayout.addRow(self.bookPublisher, self.bookPublisherField)

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


        #Synopsis

        self.synopsisGroupLayout = QtWidgets.QVBoxLayout()

        self.synopsisLabel = QtWidgets.QTextEdit()
        self.synopsisLabel.setText("The king in yellow is a book of short" 
                                 "stories by the American writer Robert W. Chambers," 
                                 "first published by F. Tennyson Neely in 1895.")
        

        self.synopsisLabel.setReadOnly(True)
        self.synopsisGroupLayout.addWidget(self.synopsisLabel)
        self.synopsisGroup.setLayout(self.synopsisGroupLayout)









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
