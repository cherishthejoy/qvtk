import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk

class MainWindow(QtWidgets.QMainWindow):

    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 768
    VTK_WINDOW_WIDTH = 400
    VTK_WINDOW_HEIGHT = 300
    STL_FILE = "Moon.stl"

    def __init__(self, parent=None):

        QtWidgets.QMainWindow.__init__(self, parent)

        self.setupUi()
        self.setupVTK()

        self.show()

    def setupUi(self):
        self.grid1 = QtWidgets.QGridLayout()

        self.inspectFrame = QtWidgets.QGroupBox()
        self.inspectFrame.setTitle("Inspect")

        self.statsFrame = QtWidgets.QGroupBox()
        self.statsFrame.setTitle("Stats")

        self.treeView = QtWidgets.QGroupBox()
        self.treeView.setTitle("Table")

        self.vtkWidget = QVTKRenderWindowInteractor(self.inspectFrame)
        self.vtkWidget.setFixedSize(self.VTK_WINDOW_WIDTH, self.VTK_WINDOW_HEIGHT)


        self.inspectLayout = QtWidgets.QVBoxLayout()
        self.inspectLayout.addWidget(self.vtkWidget)
        self.inspectFrame.setLayout(self.inspectLayout)


        self.grid1.addWidget(self.inspectFrame, 0, 0)
        self.grid1.addWidget(self.statsFrame, 0, 1)
        self.grid1.addWidget(self.treeView, 1, 0)


        widget = QtWidgets.QWidget()
        widget.setLayout(self.grid1)
        self.setCentralWidget(widget)

        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)




        self.menubar = self.menuBar()
       
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        
        self.menuFile.setTitle("File")
        self.menuEdit.setTitle("Edit")
    
        self.actionNew = QtWidgets.QAction("New", self)
        self.actionSave = QtWidgets.QAction("Save", self)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)

        self.actionCopy = QtWidgets.QAction("Copy", self)
        self.actionPaste = QtWidgets.QAction("Paste", self)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)

        self.menubar.addMenu(self.menuFile)
        self.menubar.addMenu(self.menuEdit)

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


class CustomInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, renderer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renderer = renderer
        self.AddObserver("MouseWheelForwardEvent", self.mouseWheelForwardEvent)
        self.AddObserver("MouseWheelBackwardEvent", self.mouseWheelBackwardEvent)
    
    def mouseWheelForwardEvent(self, obj, event):
        camera = self.renderer.GetActiveCamera()
        if camera.GetDistance() > 100:
            self.OnMouseWheelForward()

    def mouseWheelBackwardEvent(self, obj, event):
        camera = self.renderer.GetActiveCamera()
        if camera.GetDistance() < 300:
            self.OnMouseWheelBackward()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())