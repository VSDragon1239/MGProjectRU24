from PySide6.QtWidgets import QStackedWidget


from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerStackWidgets(QtViewerObjects):
    className = 'ViewerStackWidgets'

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initStackWidgets()

    def initStackWidgets(self):
        self.initObject(QStackedWidget, 'QStackedWidget')
        self.setObjectArray(self.className)
