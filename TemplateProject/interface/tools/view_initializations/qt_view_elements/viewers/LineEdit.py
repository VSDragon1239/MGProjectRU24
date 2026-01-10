from PySide6.QtWidgets import QLineEdit


from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerLineEdit(QtViewerObjects):
    className = "ViewerLineEdit"
    objectName = "QLineEdit"

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initButtons()

    def initButtons(self):
        self.initObject(QLineEdit, self.objectName)
        self.setObjectArray(self.className)

    def newObject(self, object):
        self.newObjectToArray(self.className, object)
        return self.lastObject
