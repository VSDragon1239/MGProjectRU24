from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.ButtonsConnector import buttonConnectToStackWidget, ButtonsConnecting


class MainButtonsConnect(ButtonsConnecting):
    def __init__(self, View, ViewModel: TemplateViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel

    def mainButtonsConnect(self):
        conn_func = buttonConnectToStackWidget
        widget = self.ViewerStackWidgets.getObjectByIndex(1)

        self.setButtonClick(btn_index=1, conn_func=conn_func, widget=widget, typeFunc='2', data_text='Главная', listID=1, Page=0)
        self.setButtonClick(btn_index=2, conn_func=conn_func, widget=widget, typeFunc='2', data_text='Документация', listID=1, Page=1)
        self.setButtonClick(btn_index=3, conn_func=conn_func, widget=widget, typeFunc='2', data_text='Заметки', listID=1, Page=2)
