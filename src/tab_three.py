from PyQt5 import QtWidgets, QtCore

class ThirdTab(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupGridLayout()
        self.setupGroupBox()
        self.placeGroupBox()
        self.setupInputs()
        

    def setupGridLayout(self):

        self.grid3 = QtWidgets.QGridLayout()
        self.setLayout(self.grid3)

    def setupGroupBox(self):

        self.buyGroup = QtWidgets.QGroupBox()
        self.buyGroup.setTitle("Item")

        self.tableGroup = QtWidgets.QGroupBox()
        self.tableGroup.setTitle("Table")

        self.membershipGroup = QtWidgets.QGroupBox()
        self.membershipGroup.setTitle("Membership")

        self.buttonGroup = QtWidgets.QGroupBox()
        self.buttonGroup.setTitle("Whatitdonigga")

    def placeGroupBox(self):


        # The only reason I'm putting splitter between those two groupboxes is
        # because the table and the membership box proportions are 3:2 regardless.
        # Not a good workaround but will take it.

        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.addWidget(self.tableGroup)
        self.splitter.addWidget(self.membershipGroup)
        
        self.grid3.addWidget(self.buyGroup, 0, 0, 1, 2)
        self.grid3.addWidget(self.splitter, 1, 0, 3, 2)
        self.grid3.addWidget(self.buttonGroup, 4, 0, 1, 2)

    def setupInputs(self):

        #Item Group

        self.bookID = QtWidgets.QLabel()
        self.bookID.setText("Book Id")

        self.bookTitle = QtWidgets.QLabel()
        self.bookTitle.setText("Book ISBN")

        self.bookPrice =  QtWidgets.QLabel()
        self.bookPrice.setText("Book Price")

        self.bookQuantity = QtWidgets.QLabel()
        self.bookQuantity.setText("Stock")

        self.bookIDField = QtWidgets.QLineEdit()
        self.bookIDField.setObjectName("bookIdField")

        self.bookTitleField = QtWidgets.QLineEdit()
        self.bookTitleField.setObjectName("bookISBNField")

        self.bookPriceField = QtWidgets.QLineEdit()
        self.bookPriceField.setObjectName("bookPriceField")

        self.bookQuantityField = QtWidgets.QLineEdit()
        self.bookQuantityField.setObjectName("stockField")

        self.clearButton = QtWidgets.QPushButton('Clear', self)
        self.addButton = QtWidgets.QPushButton('Add', self)

        self.itemGroupLayoutOne = QtWidgets.QFormLayout()
        self.itemGroupLayoutOne.setFormAlignment(QtCore.Qt.AlignVCenter)
        self.itemGroupLayoutTwo = QtWidgets.QFormLayout()
        self.itemGroupLayoutTwo.setFormAlignment(QtCore.Qt.AlignVCenter)

        # self.itemGroupLayoutOne.addRow(self.bookID, self.bookIDField)
        self.itemGroupLayoutOne.addRow(self.bookTitle, self.bookTitleField)
        self.itemGroupLayoutTwo.addRow(self.bookPrice, self.bookPriceField)
        self.itemGroupLayoutTwo.addRow(self.bookQuantity, self.bookQuantityField)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.horizontalLayout.addLayout(self.itemGroupLayoutOne)
        self.horizontalLayout.addLayout(self.itemGroupLayoutTwo)

        self.horizontalLayout.addWidget(self.clearButton)
        self.horizontalLayout.addWidget(self.addButton)

        self.buyGroup.setLayout(self.horizontalLayout)

        #Table Group

        self.tableWidget = QtWidgets.QTableWidget(10, 5)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(["ISBN", "Title", "Quantity", "Price", "Total"])


        self.deleteButton = QtWidgets.QPushButton("Delete")

        self.total = QtWidgets.QLabel()
        self.total.setText("Total:")

        self.totalField = QtWidgets.QLineEdit()
        self.totalField.setObjectName("totalField")

        self.payButton = QtWidgets.QPushButton("Pay")


        self.tableGroupLayout = QtWidgets.QGridLayout()

        self.tableGroupLayout.addWidget(self.tableWidget, 0, 0, 2, 2)
        self.tableGroupLayout.addWidget(self.deleteButton, 3, 0)

        self.tableGroupLayout.addWidget(self.total, 2, 0)
        self.tableGroupLayout.addWidget(self.totalField, 2, 1)
        self.tableGroupLayout.addWidget(self.payButton, 3, 1)

        self.tableGroup.setLayout(self.tableGroupLayout)



        #Membership Group

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


        self.membershipGrid = QtWidgets.QGridLayout()
        self.membershipGroup.setLayout(self.membershipGrid)

        self.memberLayoutTop = QtWidgets.QFormLayout()
        self.memberLayoutTop.setFormAlignment(QtCore.Qt.AlignVCenter)
        self.memberLayoutBottom = QtWidgets.QHBoxLayout()


        self.memberLayoutTop.addRow(self.phoneNumber, self.phoneNumberField)
        self.memberLayoutTop.addRow(self.firstName, self.firstNameField)
        self.memberLayoutTop.addRow(self.membershipId, self.membershipIdField)
        self.memberLayoutTop.addRow(self.discountPerc, self.discountField)
        self.memberLayoutTop.addRow(self.passcode, self.passcodeField)

        self.memberClearButton = QtWidgets.QPushButton("Clear")
        self.applyButton = QtWidgets.QPushButton("Apply Discount")

        self.memberLayoutBottom.addWidget(self.memberClearButton)
        self.memberLayoutBottom.addWidget(self.applyButton)

        self.membershipGrid.addLayout(self.memberLayoutTop, 0, 0, 2, 2)
        self.membershipGrid.addLayout(self.memberLayoutBottom, 2, 0, 1, 2)


        #Button Group

        self.ButtonGroupHLayout = QtWidgets.QHBoxLayout()

        self.clearTable = QtWidgets.QPushButton("Clear")
        self.removeDiscount = QtWidgets.QPushButton("Remove Discount")
        self.printInvoice = QtWidgets.QPushButton("Print Invoice")

        self.ButtonGroupHLayout.addWidget(self.clearTable)
        self.ButtonGroupHLayout.addWidget(self.removeDiscount)
        self.ButtonGroupHLayout.addWidget(self.printInvoice)

        self.buttonGroup.setLayout(self.ButtonGroupHLayout)


