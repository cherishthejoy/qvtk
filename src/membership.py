from PyQt5 import QtWidgets, QtCore

class PopupWindow(QtWidgets.QDialog):

    WINDOW_WIDTH = 300
    WINDOW_HEIGHT = 200

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setupGrid()
        self.setupGroupBox()
        self.placeGroupBox()
        self.setupInput()
        self.show()
        self.setWindowTitle("Register")
        self.resize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        

    def setupGrid(self):

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

    def setupGroupBox(self):

        self.membershipGroup = QtWidgets.QGroupBox()
        self.membershipGroup.setTitle("Membership Registry")

    def placeGroupBox(self):

        self.grid.addWidget(self.membershipGroup, 0, 0)

    def setupInput(self):

        self.gridTwo = QtWidgets.QGridLayout()
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignVCenter)

    
        self.phoneNumber = QtWidgets.QLabel()
        self.phoneNumber.setText("Phone Number")
        self.firstName = QtWidgets.QLabel()
        self.firstName.setText("First Name")
        self.membershipId = QtWidgets.QLabel()
        self.membershipId.setText("Membership ID")
        self.discountPerc = QtWidgets.QLabel()
        self.discountPerc.setText("Discount %")
        self.passcode = QtWidgets.QLabel()
        self.passcode.setText("Passcode")
        self.phoneNumberField = QtWidgets.QLineEdit()
        self.phoneNumberField.setObjectName("phoneNumberField")
        self.firstNameField = QtWidgets.QLineEdit()
        self.firstNameField.setObjectName("firstNameField")
        self.membershipIdField = QtWidgets.QLineEdit()
        self.membershipIdField.setObjectName("membershipIdField")
        self.discountField = QtWidgets.QLineEdit()
        self.discountField.setObjectName("discountField")
        self.passcodeField = QtWidgets.QLineEdit()
        self.passcodeField.setObjectName("passcodeField")

        self.formLayout.addRow(self.phoneNumber, self.phoneNumberField)
        self.formLayout.addRow(self.firstName, self.firstNameField)
        self.formLayout.addRow(self.membershipId, self.membershipIdField)
        self.formLayout.addRow(self.discountPerc, self.discountField)
        self.formLayout.addRow(self.passcode, self.passcodeField)

        self.resetButton = QtWidgets.QPushButton('Register', self)

        self.gridTwo.addLayout(self.formLayout, 0, 0)
        self.gridTwo.addWidget(self.resetButton, 1, 0)
        self.gridTwo.setAlignment(self.resetButton, QtCore.Qt.AlignCenter)

        self.membershipGroup.setLayout(self.gridTwo)
    



        