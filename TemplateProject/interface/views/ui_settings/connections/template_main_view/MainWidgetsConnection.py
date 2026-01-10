from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.WidgetsConnector import WidgetsConnecting


class MainWidgetsConnect(WidgetsConnecting):
    def __init__(self, View, ViewModel: TemplateViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel

    def mainWidgetConnect(self):
        """Связь виджетов и viewModel"""
        widget = self.ViewerWidget.getObjectByIndex(44)
        
        self.viewModel.setAggregateWidget(widget)
