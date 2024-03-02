from PyQt5 import QtWidgets
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
import os

from camera_style import CustomInteractorStyle

class CentralWidget(QtWidgets.QWidget):
    
    VTK_WINDOW_WIDTH = 400
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

        self.listGroup = QtWidgets.QGroupBox()
        self.listGroup.setTitle("Table")


    def placeVTK(self):

        self.vtkWidget = QVTKRenderWindowInteractor(self.inspectGroup)
        self.vtkWidget.setFixedSize(self.VTK_WINDOW_WIDTH, self.VTK_WINDOW_HEIGHT)

        self.inspectVertLayout = QtWidgets.QVBoxLayout()
        self.inspectVertLayout.addWidget(self.vtkWidget)
        self.inspectGroup.setLayout(self.inspectVertLayout)


    def placeGroupBoxes(self):

        self.grid1.addWidget(self.inspectGroup, 0, 0)
        self.grid1.addWidget(self.statsGroup, 0, 1)
        self.grid1.addWidget(self.listGroup, 1, 0, 1, 2)


    def setupInputFields(self):

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


    def setupLabels(self):

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

        
    def placeFormLayoutItems(self):

        self.statsFormLayout = QtWidgets.QFormLayout()

        self.statsFormLayout.addRow(self.bookName, self.bookNameField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookAuthor, self.bookAuthorField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookPrintDate, self.bookPrintDateField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookCategory, self.bookCategoryField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookPublisher, self.bookPublisherField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookLanguage, self.bookLanguageField)
        self.statsGroup.setLayout(self.statsFormLayout)

        self.statsFormLayout.addRow(self.bookCoverType, self.bookCoverTypeField)
        self.statsGroup.setLayout(self.statsFormLayout)
        

    def setupVTK(self):

        importer = vtk.vtkOBJImporter()
        importer.SetFileName(self.OBJ_FILE)
        importer.SetFileNameMTL(self.MTL_FILE)
        
        obj_dir = os.path.dirname(self.OBJ_FILE)

        importer.SetTexturePath(obj_dir)

        self.renderer = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)

        importer.SetRenderWindow(self.vtkWidget.GetRenderWindow())
        importer.Update()


        self.textActor = vtk.vtkTextActor()
        self.textActor.SetInput("The King in Yellow")
        self.textActor.GetTextProperty().SetFontSize(10)
        self.textActor.GetTextProperty().SetColor(0, 0, 0)

        self.renderer.AddActor(self.textActor)

        # Shader, if it works ----------------------------------------------

        self.placeHolderActor = vtk.vtkActor()
        self.shaderProperty = self.placeHolderActor.GetShaderProperty()

        self.shaderProperty.SetFragmentShaderCode(

        "//VTK::System::Dec\n"
        "#version 330\n"
        "#ifdef GL_ES\n"
        "precision mediump float;\n"
        "#endif\n"
        "precision mediump float;\n"
        "uniform float u_time;\n"
        "uniform vec2 u_resolution;\n"
        "uniform sampler2D u_tex0;\n"
        "out vec4 FragColor;\n"
        "//VTK::Normal::Dec\n"
        "vec2 curveEffect(vec2 uv){\n" 
            "uv = (uv - 0.5) s* 2.0;\n"
            "uv *= 1.0;\t// Change this if you want to config distance\n"
            "uv.x *= 1.0 + pow((abs(uv.y) / 5.0), 2.0);\n"
            "uv.y *= 1.0 + pow((abs(uv.x) / 5.0), 2.0);\n"
            "uv  = (uv / 2.0) + 0.5;\n"
            "uv =  uv * 0.92 + 0.04;\n"
            "return uv;\n"
        "}\n"
        "void main(){\n"
            "vec2 fragCoord = gl_FragCoord.xy;\n" 
            "vec4 finalColor;\n" 
            "vec2 uv = curveEffect(fragCoord.xy / u_resolution.xy);\n" 
            "vec3 color;\n"
            "float sinComponent1 = sin(0.3 * u_time + uv.y * 21.0);\n" 
            "float sinComponent2 = sin(0.7 * u_time + uv.y * 29.0);\n" 
            "float sinComponent3 = sin(0.3 + 0.33 * u_time + uv.y * 31.0);\n"
            "float x = sinComponent1 * sinComponent2 * sinComponent3 * 0.002;\n" 
            "color.r = texture(u_tex0, vec2(x + uv.x + 0.001, uv.y + 0.001)).x + 0.05;\n" 
            "color.g = texture(u_tex0, vec2(x + uv.x + 0.000, uv.y - 0.002)).y + 0.05;\n" 
            "color.b = texture(u_tex0, vec2(x + uv.x - 0.002, uv.y + 0.000)).z + 0.05;\n" 
            "color.r += 0.08 * texture(u_tex0, 0.75 * vec2(x + 0.025, -0.027) + vec2(uv.x + 0.001, uv.y + 0.001)).x;\n" \
            "color.g += 0.05 * texture(u_tex0, 0.75 * vec2(x + -0.022, -0.02) + vec2(uv.x + 0.000, uv.y - 0.002)).y;\n" \
            "color.b += 0.08 * texture(u_tex0, 0.75 * vec2(x + -0.02, -0.018) + vec2(uv.x - 0.002, uv.y + 0.000)).z;\n" \
            "color = clamp(color * 0.6 + 0.4 * color * color * 1.0, 0.0, 1.0);\n"
            "float vignette = (1.0 * 16.0 * uv.x * uv.y * (1.0 - uv.x) * (1.0 - uv.y));\n"
            "color *= vec3(pow(vignette, 0.3));\n" 
            "color *= vec3(0.95, 1.05, 0.95);\n"
            "color = mix(color, color * color, 0.3) * 3.8;\n"
            "float scanlineEffect = clamp(0.35 + 0.20 * sin(3.5 * u_time + uv.y * u_resolution.y * 1.5), 0.0, 1.0);\n"
            "float scanlinePower = pow(scanlineEffect, 1.7);\n"
            "color = color * vec3(0.4 + 0.7 * scanlinePower) ;\n"
            "color *= 1.0 + 0.01 * sin(200.0 * u_time);\n"
            "if(uv.x < 0.0 || uv.x > 1.0){\n"
                "color *= 0.0;\n"
            "}\n"
            "if(uv.y < 0.0 || uv.y > 1.0){\n"
                "color *= 0.0;\n" 
            "}\n" 
            "color *= 1.0 - 0.65 * vec3(clamp((mod(fragCoord.x, 2.0) -1.0) * 2.0, 0.0, 1.0));\n"
            "finalColor = vec4(color, 2.0);\n"
            "FragColor = finalColor;\n"
        "}\n"
        )
        
        # ------------------------------------------------------------------------

        self.renderWindowInteractor = self.vtkWidget.GetRenderWindow().GetInteractor()
        style = vtk.vtkInteractorStyleTrackballCamera()

        self.renderer.SetBackground(0.5, 0.5, 0.5)
        self.renderer.ResetCamera()

        style = CustomInteractorStyle(self.renderer)
        self.renderWindowInteractor.SetInteractorStyle(style)

        self.renderWindowInteractor.Initialize()
