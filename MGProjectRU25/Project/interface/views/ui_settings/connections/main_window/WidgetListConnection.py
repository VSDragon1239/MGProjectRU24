from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QMenu, QInputDialog, QListView, QListWidget, QAbstractItemView

from MGProjectRU25.Project.interface.tools.QDelegator3000 import IconOnlyDelegate
from MGProjectRU25.Project.interface.tools.global_project_item import GlobalProjectItemWidget
from MGProjectRU25.Project.interface.viewmodels.main_vm import MainViewModel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.WidgetsConnector import \
    WidgetsConnecting


class MainWindowUiViewWidgetListConnect(WidgetsConnecting):
    def __init__(self, View, ViewModel: MainViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel

    def _setup_context_menu(self, widget, rename_callback=None, delete_callback=None):
        widget.setContextMenuPolicy(Qt.CustomContextMenu)
        widget.customContextMenuRequested.connect(
            lambda pos: self._show_context_menu(widget, pos, rename_callback, delete_callback)
        )

    @staticmethod
    def _show_context_menu(widget, pos, rename_callback, delete_callback):
        item = widget.itemAt(pos)
        if not item:
            return

        menu = QMenu(widget)
        rename_action = menu.addAction("Переименовать")
        delete_action = menu.addAction("Удалить")
        action = menu.exec(widget.viewport().mapToGlobal(pos))

        if action == rename_action and rename_callback:
            new_name, ok = QInputDialog.getText(widget, "Переименование", "Новое имя:", text=item.text())
            if ok and new_name:
                rename_callback(item, new_name)
        elif action == delete_action and delete_callback:
            delete_callback(item)

    def list_widget_global_projects_list(self):
        widget = self.ViewerListWidget.getObjectByIndex(2)
        self.viewModel.init_widget_list_gp(widget)

        list_func = self.viewModel.get_global_project

        widget.itemClicked.connect(
            lambda item: list_func(item=item))

        self._setup_context_menu(
            widget,
            rename_callback=lambda item, new_name: self.viewModel.rename_global_project(item.text(), new_name),
            delete_callback=lambda item: self.viewModel.delete_global_project(item)
        )

    def list_widget_projects_list(self, widget_label_set_name):
        widget = self.ViewerListWidget.getObjectByIndex(3)
        self.viewModel.init_widget_list_project(widget)

        list_func = lambda item: self.viewModel.get_project(item, widget_label_set_name)

        widget.itemClicked.connect(
            lambda item: list_func(item=item))

        self._setup_context_menu(
            widget,
            rename_callback=lambda item, new_name: self.viewModel.rename_project(item.text(), new_name),
            delete_callback=lambda item: self.viewModel.delete_global_project(item)
        )

    def list_widget_tools_list(self):
        widget = self.ViewerListWidget.getObjectByIndex(1)
        widget.setViewMode(QListWidget.ListMode)
        widget.setFlow(QListWidget.TopToBottom)
        widget.setWrapping(False)
        widget.setResizeMode(QListWidget.Adjust)
        widget.setMovement(QListWidget.Static)
        widget.setStyleSheet("""
                                QListWidget {
                                    font-size: 32px;
                                    background-color: rgba(0, 0, 0, 0);
                                    padding: 0;
                                }
                            """)
        self.viewModel.init_widget_list_tools_applications_path(widget)

        list_func = self.viewModel.open_folder_tools_sub_dir

        widget.itemDoubleClicked.connect(
            lambda item: list_func(sub_dir_name=item.text()))

    def list_widget_sub_dirs_to_project_list(self):
        widget = self.ViewerListWidget.getObjectByIndex(4)
        self.viewModel.init_widget_list_sub_dirs_of_select_project(widget)

        list_func = self.viewModel.select_sub_dir
        d_list_func = self.viewModel.open_folder_sub_dir

        widget.itemClicked.connect(
            lambda item: list_func(item=item))

        widget.itemDoubleClicked.connect(lambda item: d_list_func())
        # widget.itemActivated.connect(lambda item: d_list_func())

    def list_widget_apps_list(self):
        widget = self.ViewerListWidget.getObjectByIndex(5)
        widget.setViewMode(QListWidget.IconMode)
        widget.setIconSize(QSize(72, 64))
        widget.setGridSize(QSize(72, 64))
        widget.setUniformItemSizes(True)
        widget.setWrapping(True)
        widget.setResizeMode(QListWidget.Adjust)
        widget.setSpacing(10)
        widget.setItemDelegate(IconOnlyDelegate(widget))

        # === включаем drag’n’drop внутри виджета ===
        # widget.setDragEnabled(True)  # можно тащить
        # widget.setAcceptDrops(True)  # можно сбрасывать
        # widget.setDropIndicatorShown(True)  # подсказка разрешённой зоны
        # widget.setDragDropMode(QAbstractItemView.InternalMove)  # перемещение внутри
        # widget.setDefaultDropAction(Qt.MoveAction)  # при сбросе — Move
        #
        # # === фиксируем, чтобы иконки «прилипали» к ячейкам сетки ===
        # widget.setMovement(QListView.Snap)  # Snap = сетка; Free = куда хочешь
        #
        # # === даём каждому элементу возможность быть перетаскиваемым и принимать сброс ===
        # for i in range(widget.count()):
        #     item = widget.item(i)
        #     item.setFlags(
        #         item.flags()
        #         | Qt.ItemIsSelectable
        #         | Qt.ItemIsEnabled
        #         | Qt.ItemIsDragEnabled
        #         | Qt.ItemIsDropEnabled
        #     )

        self.viewModel.init_widget_list_apps(widget)

        list_func = self.viewModel.open_app

        # widget.itemClicked.connect(lambda item: list_func(item=item))
        widget.itemDoubleClicked.connect(lambda item: list_func(item=item))
        # widget.itemActivated.connect(lambda item: list_func(item=item))

    def widget_hider(self):
        def add_hide_widget(index):
            return self.ViewerWidget.getObjectByIndex(index)

        buttons = [
            add_hide_widget(190),
            add_hide_widget(138),
            add_hide_widget(72),
        ]

        for btn in buttons:
            btn.hide()
