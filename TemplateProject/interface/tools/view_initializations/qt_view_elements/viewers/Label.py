from PySide6.QtWidgets import QPushButton, QLabel

from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerLabel(QtViewerObjects):
    className = "ViewerLabels"
    objectName = "QLabel"

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initLabels()

    def initLabels(self):
        self.initObject(QLabel, self.objectName)
        self.setObjectArray(self.className)

    def newLabel(self, label):
        self.newObjectToArray(self.className, label)
        return self.lastObject
