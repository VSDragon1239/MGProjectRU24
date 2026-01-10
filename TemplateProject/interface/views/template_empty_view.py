from PySide6.QtWidgets import QMainWindow

from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel


class TemplateEmptyView(QMainWindow):
    viewModel = None

    def __init__(self):
        super().__init__()
        self.initViewModels()

    def initViewModels(self):
        self.viewModel = TemplateViewModel(self)
