from PySide6.QtWidgets import QPushButton

from MGProjectRU25.Project.project_settings import IMAGES_DIRS
from TemplateProject.interface.tools.view_initializations.qt_view_elements.creates.CreateElements import createQPushButton
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Buttons import ViewerButtons
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.ListWidget import ViewerListWidget
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.StackWidgets import ViewerStackWidgets
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.TextEdit import ViewerTextEdit
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Widgets import ViewerWidgets
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.SpinBoxs import ViewerSpinBox


def buttonConnectToStackWidget(stackWindget, idGui, page):
    if idGui == 1:
        setStackWidgetCurrentIndex(stackWindget, page)
    elif idGui == 2:
        setStackWidgetCurrentIndex(stackWindget, page)
    elif idGui == 4:
        setStackWidgetCurrentIndex(stackWindget, page)


def setStackWidgetCurrentIndex(stackWindget, page):
    stackWindget.setCurrentIndex(page)


class ButtonsConnecting:
    view = None
    viewModel = None
    ViewerButtons = None
    ViewerStackWidgets = None
    ViewerTextEdit = None
    ViewerListWidget = None
    ViewerWidget = None
    ViewerSpinBox = None

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
        self.ViewerSpinBox = ViewerSpinBox(self.view, self.viewModel)
        self.ViewerWidget = ViewerWidgets(self.view, self.viewModel)

    def setButtonClick(self, btn_index, conn_func, typeFunc,
                       listID=None, Page=None, widget=None, data_text=None,
                       id=None):
        btn = self.ViewerButtons.objectsArray[f'QPushButton{btn_index}']
        print(btn)
        if data_text:
            btn.setText(data_text)
        if typeFunc == 'Normal' or typeFunc == '1':
            btn.clicked.connect(lambda: conn_func())
        elif typeFunc == 'Stack Widget' or typeFunc == '2':
            btn.clicked.connect(lambda: conn_func(widget, listID, Page))
        elif typeFunc == 'Checked Data' or typeFunc == '3':
            # btn.clicked.connect(lambda checked, data=dataArray: conn_func(data))
            pass
        elif typeFunc == 'PrintConsole' or typeFunc == '4':
            btn.clicked.connect(lambda: print(data_text))
        elif typeFunc == 'OpenFileByVersion' or typeFunc == '5':
            btn.clicked.connect(lambda: conn_func(id, widget))
        elif typeFunc == 'blockButton' or typeFunc == '6':
            btn.clicked.connect(lambda: btn.setEnabled(False))
        elif typeFunc == 'LoadData' or typeFunc == '7':
            btn.clicked.connect(lambda: conn_func(widget))

    def createButton(self, widget, context, name):
        """Возвращает индекс созданной кнопки"""
        btn = createQPushButton(widget, context)
        btn.setObjectName(name)
        return self.ViewerButtons.newButton(btn)

    def deleteButtons(self, widget):
        """Удаляет все QPushButton внутри указанного виджета вместе с их индексами."""
        to_remove = []  # Список для хранения кнопок, которые нужно удалить

        # Находим все кнопки внутри указанного виджета
        for child in widget.children():
            if isinstance(child, QPushButton):
                to_remove.append(child)  # Добавляем кнопку в список для удаления

        # Удаляем кнопки и их индексы из objectsArray
        for btn in to_remove:
            btn_name = btn.objectName()  # Имя кнопки, например, "QPushButton5"
            btn.deleteLater()  # Удаляем кнопку из памяти и интерфейса

            # Находим и удаляем соответствующий индекс из objectsArray
            key_to_remove = None
            for key, value in self.ViewerButtons.objectsArray.items():
                if value == btn:
                    key_to_remove = key
                    break

            if key_to_remove:
                del self.ViewerButtons.objectsArray[key_to_remove]
                print(f"Удалена кнопка: {btn_name}, индекс: {key_to_remove}")
        self.ViewerButtons.lastObject = 3

    def setButtonImage(self, image_dir):
        img_normal = (image_dir + IMAGES_DIRS[3]).replace('\\', '/')
        img_hover = (image_dir + IMAGES_DIRS[10]).replace('\\', '/')
        img_pressed = (image_dir + IMAGES_DIRS[9]).replace('\\', '/')
        style = (f"""
                QWidget {{
                    border: 1px solid rgb(0, 100, 100);
                    border-radius: 3px;  
                    padding: 3px;
                    background-color: rgba(10, 20, 30, 100);
                    font-family: 'Jura', sans-serif;  
                    font-size: 16px;
                    font-weight: bold;
                }}

                QLabel {{
                    border: 1px solid rgb(0, 100, 100);  
                    border-radius: 3px;
                    padding: 3px;
                    color: #2A9DF4;
                }}

                QPushButton {{
                    outline: none;
                    background-image: url({img_normal});
                    background-position: center;
                    background-repeat: no-repeat;
                    background-color: rgba(255, 255, 255, 30);
                    border-radius: 7px;
                    padding: 5px;
                    font-size: 16px;
                }}

                QPushButton:hover {{
                    background-image: url({img_hover});
                }}

                QPushButton:pressed {{
                    background-image: url({img_pressed});
                }}
            """)
        self.view.setStyleSheet(style)

# QWidget {
#     border: 1px solid rgb(0, 100, 100);
#     border-radius: 3px;
#     padding: 3px; /* Отступы внутри layout */
# 	background-color: rgba(10, 20, 30, 100);
# 	font-family: 'Jura', sans-serif;
# 	font-size: 16px;
# 	font-weight: bold;
# }
#
# QLabel {
#     border: 1px solid rgb(0, 100, 100);;; /* Цвет и толщина рамки */
#     border-radius: 3px; /* Радиус скругления углов */
#     padding: 3px; /* Отступы внутри layout */
#     color: #2A9DF4; /* Цвет фона */
# }
#
# QPushButton {
# 	border-radius: 7px; /* Радиус скругления углов */
#     padding: 5px; /* Отступы внутри кнопки */
#     font-size: 16px; /* Размер шрифта */
# }