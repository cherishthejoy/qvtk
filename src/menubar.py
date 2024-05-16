from PyQt5 import QtWidgets
from membership import PopupWindow

class MenuBar:
    def __init__(self, window):
        self.window = window
        self.menubar = window.menuBar()

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuEdit = QtWidgets.QMenu(self.menubar)

        self.menuFile.setTitle("File")
        self.menuEdit.setTitle("Edit")

        self.actionNew = QtWidgets.QAction("New", self.menubar)
        self.actionSave = QtWidgets.QAction("Save", self.menubar)
        self.actionAddMember = QtWidgets.QAction("Register Member", self.menubar)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionAddMember)

        self.actionCopy = QtWidgets.QAction("Copy", self.menubar)
        self.actionPaste = QtWidgets.QAction("Paste", self.menubar)

        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)

        self.menubar.addMenu(self.menuFile)
        self.menubar.addMenu(self.menuEdit)


        #Popup

        self.actionAddMember.triggered.connect(self.open_popup)

    def open_popup(self):
        
        self.popup = PopupWindow(self.window)
        self.popup.show()

