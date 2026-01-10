from TemplateProject.interface.tools.view_initializations.qt_view_elements.creates.CreateElements import createQWidget
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Buttons import ViewerButtons
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.ComboBox import ViewerComboBox
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.LineEdit import ViewerLineEdit
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.ListWidget import ViewerListWidget
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.PlainTextEdit import ViewerPlainTextEdit
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.SpinBoxs import ViewerSpinBox
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.StackWidgets import ViewerStackWidgets
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.TextEdit import ViewerTextEdit
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Widgets import ViewerWidgets


class SpinBoxConnecting:
    view = None
    viewModel = None
    ViewerButtons = None
    ViewerStackWidgets = None
    ViewerTextEdit = None
    ViewerPlainTextEdit = None
    ViewerListWidget = None
    ViewerWidget = None
    ViewerSpinBox = None
    ViewerLineEdit = None
    ViewerComboBox = None

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
        self.ViewerPlainTextEdit = ViewerPlainTextEdit(self.view, self.viewModel)
        self.ViewerListWidget = ViewerListWidget(self.view, self.viewModel)
        self.ViewerSpinBox = ViewerSpinBox(self.view, self.viewModel)
        self.ViewerWidget = ViewerWidgets(self.view, self.viewModel)
        self.ViewerLineEdit = ViewerLineEdit(self.view, self.viewModel)
        self.ViewerComboBox = ViewerComboBox(self.view, self.viewModel)

    def setSpinBoxChange(self, index, conn_func, typeFunc,
                         widget=None, data_text=None,
                         id=None):
        vObject = self.ViewerSpinBox.objectsArray[f'QSpinBox{index}']
        print(vObject)
        if data_text:
            vObject.setText(data_text)
        if typeFunc == 'Normal' or typeFunc == '1':
            vObject.valueChanged.connect(lambda value: conn_func(value))
        elif typeFunc == 'PrintConsole' or typeFunc == '4':
            vObject.valueChanged.connect(lambda: conn_func(data_text))
        elif typeFunc == 'OpenFileByVersion' or typeFunc == '5':
            vObject.valueChanged.connect(lambda: conn_func(id, widget))
        elif typeFunc == 'LoadData' or typeFunc == '7':
            vObject.valueChanged.connect(lambda: conn_func(widget))

    def createSpinBox(self, widget, name):
        """Возвращает индекс созданного виджета"""
        cSpinBox = createQWidget(widget)
        cSpinBox.setObjectName(name)
        return self.ViewerSpinBox.newSpinBox(cSpinBox)

    # def deleteWidget(self, widget):
    #     """Удаляет весь указанный виджет вместе с его дочерними элементами."""
    #     # Если виджет содержится в родительском layout, убираем его оттуда
    #     parent_layout = widget.parentWidget().layout()
    #     if parent_layout is not None:
    #         parent_layout.removeWidget(widget)
    #
    #     # Если нужно удалить сам виджет из массива объектов — сделайте логику аналогично тому,
    #     # как вы делали с кнопками:
    #     key_to_remove = None
    #     for key, value in self.ViewerWidget.objectsArray.items():
    #         if value == widget:
    #             key_to_remove = key
    #             break
    #     if key_to_remove:
    #         del self.ViewerWidget.objectsArray[key_to_remove]
    #         print(f"Удалён виджет: {widget.objectName()}, индекс: {key_to_remove}")
    #
    #     # Удаляем сам виджет
    #     widget.setParent(None)  # Отвязываем от родителя
    #     widget.deleteLater()  # Помечаем на удаление из памяти
    #
    #     # Если вам нужно что-то записать в lastObject
    #     # self.ViewerWidget.lastObject = 3
