from TemplateProject.interface.viewmodels.template_ui_fr_viewmodel import TemplateUiFRViewModel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.WidgetsConnector import WidgetsConnecting


class TemplateUiFRViewWidgetListConnect(WidgetsConnecting):
    def __init__(self, View, ViewModel: TemplateUiFRViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel

    def template_list_widget_project_list(self):
        widget = self.ViewerListWidget.getObjectByIndex(1)
        list_func = self.viewModel.select_project

        project_data = self.viewModel.get_projects_data()[1]

        for name in project_data["Projects"]:
            widget.addItem(f"{name['Name']}")

        widget.itemClicked.connect(
            lambda item: list_func(item=item))
