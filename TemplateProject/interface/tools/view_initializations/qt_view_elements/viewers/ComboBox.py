from PySide6.QtWidgets import QComboBox


from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerComboBox(QtViewerObjects):
    className = "ViewerComboBox"
    objectName = "QComboBox"

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initButtons()

    def initButtons(self):
        self.initObject(QComboBox, self.objectName)
        self.setObjectArray(self.className)

    def newObject(self, object):
        self.newObjectToArray(self.className, object)
        return self.lastObject
