import vtk

class CustomInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, renderer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renderer = renderer
        self.AddObserver("MouseWheelForwardEvent", self.mouseWheelForwardEvent)
        self.AddObserver("MouseWheelBackwardEvent", self.mouseWheelBackwardEvent)
    
    def mouseWheelForwardEvent(self, obj, event):
        camera = self.renderer.GetActiveCamera()
        if camera.GetDistance() > 1:
            self.OnMouseWheelForward()

    def mouseWheelBackwardEvent(self, obj, event):
        camera = self.renderer.GetActiveCamera()
        if camera.GetDistance() < 10:
            self.OnMouseWheelBackward()
