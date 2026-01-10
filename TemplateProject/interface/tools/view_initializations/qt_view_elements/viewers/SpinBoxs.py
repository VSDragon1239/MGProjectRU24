from PySide6.QtWidgets import QSpinBox


from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerSpinBox(QtViewerObjects):
    className = 'SpinBox'

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initWidgets()

    def initWidgets(self):
        self.initObject(QSpinBox, 'QSpinBox')
        self.setObjectArray(self.className)

    def newSpinBox(self, spinBox):
        self.newObjectToArray(self.className, spinBox)
        return self.lastObject
