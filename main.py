from PyQt5 import QtWidgets
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
import sys

from vtkCamera import CustomInteractorStyle
from menubar import MenuBar

class MainWindow(QtWidgets.QMainWindow):

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    VTK_WINDOW_WIDTH = 400
    VTK_WINDOW_HEIGHT = 300
    STL_FILE = "Moon.stl"

    def __init__(self, parent=None):

        QtWidgets.QMainWindow.__init__(self, parent)

        self.setupUi()
        self.setupVTK()
        self.show()

    def setupUi(self):

        # Groupboxes
        self.grid1 = QtWidgets.QGridLayout()

        self.inspectFrame = QtWidgets.QGroupBox()
        self.inspectFrame.setTitle("Inspect")

        self.statsFrame = QtWidgets.QGroupBox()
        self.statsFrame.setTitle("Stats")

        self.treeView = QtWidgets.QGroupBox()
        self.treeView.setTitle("Table")


        # Input fields
        self.bookNameField = QtWidgets.QLineEdit()
        self.bookNameField.setObjectName("statFieldOne")

        self.bookAuthorField = QtWidgets.QLineEdit()
        self.bookAuthorField.setObjectName("statFieldTwo")

        self.bookPrintDateField = QtWidgets.QLineEdit()
        self.bookPrintDateField.setObjectName("statFieldThree")

        self.bookCategoryField = QtWidgets.QLineEdit()
        self.bookCategoryField.setObjectName("statFieldFour")

        self.bookPublisherField = QtWidgets.QLineEdit()
        self.bookPublisherField.setObjectName("statFieldFive")

        self.bookLanguageField = QtWidgets.QLineEdit()
        self.bookLanguageField.setObjectName("statFieldSix")

        self.bookCoverTypeField = QtWidgets.QLineEdit()
        self.bookCoverTypeField.setObjectName("statFieldSeven")

        # Labels
        self.bookName = QtWidgets.QLabel()
        self.bookName.setText("Book Name")

        self.bookAuthor =  QtWidgets.QLabel()
        self.bookAuthor.setText("Book Author")

        self.bookPrintDate = QtWidgets.QLabel()
        self.bookPrintDate.setText("Book Print Date")

        self.bookCategory = QtWidgets.QLabel()
        self.bookCategory.setText("Book Category")

        self.bookPublisher = QtWidgets.QLabel()
        self.bookPublisher.setText("Book Publisher")

        self.bookLanguage = QtWidgets.QLabel()
        self.bookLanguage.setText("Book Language")

        self.bookCoverType = QtWidgets.QLabel()
        self.bookCoverType.setText("Book Cover Type")



        self.vtkWidget = QVTKRenderWindowInteractor(self.inspectFrame)
        self.vtkWidget.setFixedSize(self.VTK_WINDOW_WIDTH, self.VTK_WINDOW_HEIGHT)


        self.inspectLayout = QtWidgets.QVBoxLayout()
        self.inspectLayout.addWidget(self.vtkWidget)
        self.inspectFrame.setLayout(self.inspectLayout)


        self.grid1.addWidget(self.inspectFrame, 0, 0)
        self.grid1.addWidget(self.statsFrame, 0, 1)
        self.grid1.addWidget(self.treeView, 1, 0)


        # Placing
        self.statsFormLayout = QtWidgets.QFormLayout()

        self.statsFormLayout.addRow(self.bookName, self.bookNameField)
        self.statsFrame.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookAuthor, self.bookAuthorField)
        self.statsFrame.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookPrintDate, self.bookPrintDateField)
        self.statsFrame.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookCategory, self.bookCategoryField)
        self.statsFrame.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookPublisher, self.bookPublisherField)
        self.statsFrame.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookLanguage, self.bookLanguageField)
        self.statsFrame.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookCoverType, self.bookCoverTypeField)
        self.statsFrame.setLayout(self.statsFormLayout)


        # Central widget section
        widget = QtWidgets.QWidget()
        widget.setLayout(self.grid1)
        self.setCentralWidget(widget)

        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        # Menubar
        self.menuBar = MenuBar(self)



    def setupVTK(self):
        self.renderer = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)
        self.renderWindowInteractor = self.vtkWidget.GetRenderWindow().GetInteractor()

        reader = vtk.vtkSTLReader()
        try:
            reader.SetFileName(self.STL_FILE)
        except IOError:
            print(f"Error: Could not read file {self.STL_FILE}")
            return

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.renderer.AddActor(actor)

        style = vtk.vtkInteractorStyleTrackballCamera()
        self.renderWindowInteractor.SetInteractorStyle(style)

        self.renderer.SetBackground(0.5, 0.5, 0.5)
        self.renderer.ResetCamera()

        style = CustomInteractorStyle(self.renderer)
        self.renderWindowInteractor.SetInteractorStyle(style)

        self.renderWindowInteractor.Initialize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())