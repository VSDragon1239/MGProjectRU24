from MGProjectRU25.Project.interface.viewmodels.main_vm import MainViewModel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.ButtonsConnector import \
    buttonConnectToStackWidget, ButtonsConnecting


class MainWindowUiViewButtonsConnect(ButtonsConnecting):
    def __init__(self, View, ViewModel: MainViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel
        self.count_project = 0

    def stack_button_window_view(self):
        conn_func = buttonConnectToStackWidget
        conn_func_hide = self.view.switch_view_console_down
        widget_0 = self.ViewerStackWidgets.getObjectByIndex(2)
        widget_1 = self.ViewerStackWidgets.getObjectByIndex(6)
        widget_1.hide()


        self.setButtonClick(btn_index=1, conn_func=conn_func, widget=widget_0, typeFunc='2', data_text='Профиль',
                            listID=1, Page=0)
        self.setButtonClick(btn_index=2, conn_func=conn_func, widget=widget_0, typeFunc='2', data_text='Проектная Файловая Система',
                            listID=1, Page=1)
        self.setButtonClick(btn_index=3, conn_func=conn_func, widget=widget_0, typeFunc='2', data_text='Инструментальные Хранилища',
                            listID=1, Page=2)
        self.setButtonClick(btn_index=4, conn_func=conn_func, widget=widget_0, typeFunc='2', data_text='Устройства',
                            listID=1, Page=3)
        self.setButtonClick(btn_index=5, conn_func=conn_func, widget=widget_0, typeFunc='2', data_text='Система',
                            listID=1, Page=4)

        self.setButtonClick(btn_index=58, conn_func=conn_func, widget=widget_1, typeFunc='2', data_text='Системный помощник',
                            listID=1, Page=3)
        self.setButtonClick(btn_index=59, conn_func=conn_func, widget=widget_1, typeFunc='2', data_text='Управление музыкой',
                            listID=1, Page=1)
        self.setButtonClick(btn_index=60, conn_func=conn_func, widget=widget_1, typeFunc='2', data_text='New Консоль (cmd)',
                            listID=1, Page=0)
        self.setButtonClick(btn_index=61, conn_func=conn_func, widget=widget_1, typeFunc='2', data_text='Отчёт приложения (логи)',
                            listID=1, Page=2)
        self.setButtonClick(btn_index=62, conn_func=conn_func, widget=widget_1, typeFunc='2',
                            data_text='Отчёт системы (логи)',
                            listID=1, Page=4)
        self.setButtonClick(btn_index=63, conn_func=conn_func, widget=widget_1, typeFunc='2',
                            data_text='---',
                            listID=1, Page=0)
        self.setButtonClick(btn_index=64, conn_func=conn_func_hide, widget=widget_1, typeFunc='7',
                            data_text='Изменить видимость')

    def button_create_global_project(self):
        conn_func = self.view.dialog_create_global_project

        self.setButtonClick(btn_index=25, conn_func=conn_func, typeFunc='1', data_text='Создать новый ГП')

    def button_create_project(self):
        conn_func = self.view.dialog_create_project

        self.setButtonClick(btn_index=52, conn_func=conn_func, typeFunc='1', data_text='Создать новый проект')

    def button_create_sub_dir_to_project(self):
        conn_func = self.view.dialog_create_sub_dir_project

        self.setButtonClick(btn_index=55, conn_func=conn_func, typeFunc='1', data_text='Добавить директорию')

    def button_open_folder_sub_dir(self):
        conn_func = self.viewModel.open_folder_sub_dir

        self.setButtonClick(btn_index=54, conn_func=conn_func, typeFunc='1', data_text='Открыть директорию')

    def button_create_application(self):
        conn_func = self.view.dialog_create_application

        self.setButtonClick(btn_index=57, conn_func=conn_func, typeFunc='1', data_text='Добавить инструмент')

    def button_open_folder_installing_application(self):
        conn_func = self.viewModel.open_folder_installing_apps

        self.setButtonClick(btn_index=20, conn_func=conn_func, typeFunc='1', data_text='Открыть директорию')

    def button_hider(self):
        def add_hide_button(index):
            return self.ViewerButtons.getObjectByIndex(index)
        buttons = [
            add_hide_button(1),
            add_hide_button(4),
            add_hide_button(5),
            add_hide_button(53),
            add_hide_button(56),
            add_hide_button(54),
            add_hide_button(20),
        ]

        for btn in buttons:
            btn.hide()

