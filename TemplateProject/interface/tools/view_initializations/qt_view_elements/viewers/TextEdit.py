from PySide6.QtWidgets import QTextEdit


from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerTextEdit(QtViewerObjects):
    className = 'ViewerTextEdit'

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initTextEdit()

    def initTextEdit(self):
        self.initObject(QTextEdit, 'QTextEdit')
        self.setObjectArray(self.className)
