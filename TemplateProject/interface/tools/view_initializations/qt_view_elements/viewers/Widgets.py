from PySide6.QtWidgets import QWidget


from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerWidgets(QtViewerObjects):
    className = 'ViewerWidgets'

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initWidgets()

    def initWidgets(self):
        self.initObject(QWidget, 'QWidget')
        self.setObjectArray(self.className)

    def newWidget(self, btn):
        self.newObjectToArray(self.className, btn)
        return self.lastObject
