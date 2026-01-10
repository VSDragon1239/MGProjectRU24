import os

from PySide6.QtCore import QFileSystemWatcher, QTimer, QFile
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader

from TemplateProject.interface.viewmodels.template_ui_fr_viewmodel import TemplateUiFRViewModel
from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainButtonsConnection import MainButtonsConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainSpinBoxsConnection import MainSpinBoxsConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainUpdateConnection import MainUpdateConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainWidgetsConnection import MainWidgetsConnect

from TemplateProject.interface.views.ui_settings.connections.template_ui_fire_reset_view.TemplateUiFRViewButtonConnection import \
    TemplateUiFRViewButtonsConnect
from TemplateProject.interface.views.ui_settings.connections.template_ui_fire_reset_view.TemplateUiFRViewListWidgetsConnection import \
    TemplateUiFRViewWidgetListConnect
from TemplateProject.interface.tools.ui_initializations.initialization_ui import loadUi, loadPyUi

# ui, QUi = loadUi(0)
# QUi: QMainWindow
# ui: QUi

compileUI = loadPyUi(0)


class ProjectsManagerUiView(QMainWindow, compileUI):
    model = None
    viewModel = None
    buttonConnect = None
    widgetListConnect = None

    def __init__(self, model):
        super().__init__()
        self.setupUi(self)
        self.set_model(model)
        self.buttonsConnection()
        self.widgetConnections()

    def set_model(self, model):
        self.model = model
        self.initViewModels()

    def initViewModels(self):
        # Создаём ViewModel, передавая ему сам загруженный виджет (чтобы он мог им управлять)
        self.viewModel = TemplateUiFRViewModel(self, self.model)

    def buttonsConnection(self):
        print("== Инициализированы connections кнопок ==")
        self.buttonConnect = TemplateUiFRViewButtonsConnect(self, self.viewModel)
        self.buttonConnect.template_stack_button_window_view()
        self.buttonConnect.template_button_apps_list()

    def widgetConnections(self):
        print("== Инициализированы connections виджетов ==")
        self.widgetListConnect = TemplateUiFRViewWidgetListConnect(self, self.viewModel)
        self.widgetListConnect.template_list_widget_project_list()
