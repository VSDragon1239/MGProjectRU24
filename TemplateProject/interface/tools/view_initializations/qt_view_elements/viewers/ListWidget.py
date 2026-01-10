from PySide6.QtWidgets import QListWidget


from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerListWidget(QtViewerObjects):
    className = 'ViewerListWidget'

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initListWidget()

    def initListWidget(self):
        self.initObject(QListWidget, 'QListWidget')
        self.setObjectArray(self.className)
