from PySide6.QtWidgets import QPushButton

from TemplateProject.interface.tools.view_initializations.qt_view_elements.creates.CreateElements import createQPushButton, createQWidget
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Buttons import ViewerButtons
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.ListWidget import ViewerListWidget
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.StackWidgets import ViewerStackWidgets
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.TextEdit import ViewerTextEdit
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Widgets import ViewerWidgets


class WidgetsConnecting:
    view = None
    viewModel = None
    ViewerButtons = None
    ViewerStackWidgets = None
    ViewerTextEdit = None
    ViewerListWidget = None
    ViewerWidget = None

    def __init__(self, View, ViewModel):
        self.initViewViewModel(View, ViewModel)
        self.initViewers()

    def initViewViewModel(self, View, ViewModel):
        self.view = View
        self.viewModel = ViewModel

    def initViewers(self):
        self.ViewerButtons = ViewerButtons(self.view, self.viewModel)
        self.ViewerStackWidgets = ViewerStackWidgets(self.view, self.viewModel)
        self.ViewerTextEdit = ViewerTextEdit(self.view, self.viewModel)
        self.ViewerListWidget = ViewerListWidget(self.view, self.viewModel)
        self.ViewerWidget = ViewerWidgets(self.view, self.viewModel)

    def createWidget(self, widget, name):
        """Возвращает индекс созданного виджета"""
        cWidget = createQWidget(widget)
        cWidget.setObjectName(name)
        return self.ViewerWidget.newWidget(cWidget)

    def deleteWidget(self, widget):
        """Удаляет весь указанный виджет вместе с его дочерними элементами."""
        # Если виджет содержится в родительском layout, убираем его оттуда
        parent_layout = widget.parentWidget().layout()
        if parent_layout is not None:
            parent_layout.removeWidget(widget)

        # Если нужно удалить сам виджет из массива объектов — сделайте логику аналогично тому,
        # как вы делали с кнопками:
        key_to_remove = None
        for key, value in self.ViewerWidget.objectsArray.items():
            if value == widget:
                key_to_remove = key
                break
        if key_to_remove:
            del self.ViewerWidget.objectsArray[key_to_remove]
            print(f"Удалён виджет: {widget.objectName()}, индекс: {key_to_remove}")

        # Удаляем сам виджет
        widget.setParent(None)  # Отвязываем от родителя
        widget.deleteLater()  # Помечаем на удаление из памяти

        # Если вам нужно что-то записать в lastObject
        # self.ViewerWidget.lastObject = 3

