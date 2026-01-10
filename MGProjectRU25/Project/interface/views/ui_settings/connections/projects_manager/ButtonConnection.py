from TemplateProject.interface.viewmodels.template_ui_fr_viewmodel import TemplateUiFRViewModel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.ButtonsConnector import \
    buttonConnectToStackWidget, ButtonsConnecting


class TemplateUiFRViewButtonsConnect(ButtonsConnecting):
    def __init__(self, View, ViewModel: TemplateUiFRViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel
        self.count_project = 0

    def template_stack_button_window_view(self):
        conn_func = buttonConnectToStackWidget
        widget = self.ViewerStackWidgets.getObjectByIndex(1)

        self.setButtonClick(btn_index=1, conn_func=conn_func, widget=widget, typeFunc='2', data_text='Главная',
                            listID=1, Page=0)
        self.setButtonClick(btn_index=2, conn_func=conn_func, widget=widget, typeFunc='2', data_text='Документация',
                            listID=1, Page=1)
        self.setButtonClick(btn_index=3, conn_func=conn_func, widget=widget, typeFunc='2', data_text='Заметки',
                            listID=1, Page=2)
        self.setButtonClick(btn_index=4, conn_func=conn_func, widget=widget, typeFunc='2', data_text='Проекты',
                            listID=1, Page=3)

    def template_button_apps_list(self):
        Widget = self.ViewerWidget.getObjectByIndex(199)

        list_index_btn = []
        for list_index in range(2, len(self.viewModel.get_apps_data())+2):
            context = f'Версия {list_index}'
            list_index_btn.append(self.createButton(widget=Widget, context=context, name=f"BTN{list_index-1}_openfile"))
            print("list_index_btn   ", list_index_btn)
        x = 0
        for index_btn in list_index_btn:
            print('index_btn    ', index_btn)
            self.setButtonClick(btn_index=index_btn, conn_func=print, typeFunc='4',
                                data_text=f'{self.viewModel.get_apps_data()[x]}', id=index_btn-2)
            x += 1

    # def template_button_new_project(self):
    #     Widget = self.ViewerWidget.getObjectByIndex(181)
    #
    #     content = self.viewModel.new_project("name")
    #     context = f'Проект номер {self.count_project}'
    #
    #     index_btn = self.createButton(widget=Widget, context=context, name=f"BTN{self.count_project}_project")
    #     self.setButtonClick(btn_index=index_btn, conn_func=print, typeFunc='4',
    #                         data_text=f'{content}')
    #     self.set_count_project()
    #
    # def template_button_project_add(self):
    #     conn_func = self.template_button_new_project
    #
    #     self.setButtonClick(btn_index=40, conn_func=conn_func, typeFunc='1', data_text='Добавить новый проект')
    #
    # def set_count_project(self):
    #     self.count_project = self.count_project + 1
