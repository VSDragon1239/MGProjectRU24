from PySide6.QtWidgets import QPushButton

from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerButtons(QtViewerObjects):
    className = "ViewerButtons"
    objectName = "QPushButton"

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initButtons()

    def initButtons(self):
        self.initObject(QPushButton, self.objectName)
        self.setObjectArray(self.className)

    def newButton(self, btn):
        self.newObjectToArray(self.className, btn)
        return self.lastObject
