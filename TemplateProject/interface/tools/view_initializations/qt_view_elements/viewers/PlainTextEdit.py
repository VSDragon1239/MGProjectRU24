from PySide6.QtWidgets import QPlainTextEdit


from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Objects import QtViewerObjects


class ViewerPlainTextEdit(QtViewerObjects):
    className = 'ViewerPlainTextEdit'

    def __init__(self, View, ViewModel):
        super().__init__(View, ViewModel)
        self.initTextEdit()

    def initTextEdit(self):
        self.initObject(QPlainTextEdit, 'QPlainTextEdit')
        self.setObjectArray(self.className)
