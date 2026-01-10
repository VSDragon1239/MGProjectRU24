from PySide6.QtWidgets import QMainWindow

from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainButtonsConnection import MainButtonsConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainSpinBoxsConnection import MainSpinBoxsConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainWidgetsConnection import MainWidgetsConnect

from TemplateProject.interface.views.ui_files.template_view import Ui_QMainViewWindow as compileUI

print("ViewPrint", compileUI)


class TemplateView(QMainWindow, compileUI):
    viewModel = None
    buttonConnect = None
    widgetConnect = None
    spinBoxConnect = None
    updateConnect = None
    scrollData = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initViewModels()
        self.buttonsConnection()
        self.widgetConnections()
        self.spinBoxConnections()
        self.updateDataConnections()

    def initViewModels(self):
        self.viewModel = TemplateViewModel(self)

    def buttonsConnection(self):
        print('== Инициализирован buttonsConnection')
        self.buttonConnect = MainButtonsConnect(self, self.viewModel)
        self.buttonConnect.mainButtonsConnect()

    def widgetConnections(self):
        print('== Инициализирован widgetConnections')
        self.widgetConnect = MainWidgetsConnect(self, self.viewModel)

    def spinBoxConnections(self):
        print('== Инициализирован spinBoxConnections')
        self.spinBoxConnect = MainSpinBoxsConnect(self, self.viewModel)
        self.spinBoxConnect.mainSpinBoxConnect()

    def updateDataConnections(self):
        print('== Инициализирован updateDataConnections')
        pass
        # self.updateConnect = MainUpdateConnect(self, self.viewModel)
        # self.viewModel.dataChanged.connect(lambda data: self.updateConnect.mainUpdateConnect(data))
        # self.updateConnect.checkIPConnect()
        # self.viewModel.dataChanged1.connect(lambda data: self.updateConnect.checkIpUpdateConnect(data))
        # self.updateConnect.subNetConnect()
        # self.viewModel.dataChanged2.connect(lambda data: self.updateConnect.subNetUpdateConnect(data))
