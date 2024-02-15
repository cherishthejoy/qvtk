import sys
from PyQt5 import QtWidgets
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.frame = QtWidgets.QFrame()

        self.vl = QtWidgets.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vtkWidget.setFixedSize(400, 300)  # Set the fixed size for the VTK widget

        self.vl.addWidget(self.vtkWidget)

        self.renderer = vtk.vtkRenderer()
        
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # Create a reader for your stl file
        reader = vtk.vtkSTLReader()
        reader.SetFileName("Moon.stl")  # replace with your file

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.renderer.AddActor(actor)

        # Set the camera to trackball style
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.iren.SetInteractorStyle(style)

        # Set the background color of the rendered color
        self.renderer.SetBackground(0.5, 0.5, 0.5)

        self.renderer.ResetCamera()

        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)

        # Set the window size
        self.resize(1024, 768)

        self.show()
        self.iren.Initialize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())