from PyQt5 import QtWidgets

class MenuBar:
    def __init__(self, window):
        self.menubar = window.menuBar()

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuEdit = QtWidgets.QMenu(self.menubar)

        self.menuFile.setTitle("File")
        self.menuEdit.setTitle("Edit")

        self.actionNew = QtWidgets.QAction("New", self.menubar)
        self.actionSave = QtWidgets.QAction("Save", self.menubar)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)

        self.actionCopy = QtWidgets.QAction("Copy", self.menubar)
        self.actionPaste = QtWidgets.QAction("Paste", self.menubar)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)

        self.menubar.addMenu(self.menuFile)
        self.menubar.addMenu(self.menuEdit)

