from random import randint

from PySide6.QtWidgets import QLabel, QSizePolicy

from MGProjectRU25.Project.interface.viewmodels.main_vm import MainViewModel
from MGProjectRU25.Project.variable_settings import random_titles
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.LabelConnector import \
    LabelsConnecting


class MainWindowUiLabelConnect(LabelsConnecting):
    def __init__(self, View, ViewModel: MainViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel
        self.count_project = 0

    def set_image_label(self, image_dir: str, image_size: list):
        self.setLabelImage(1, image_dir, image_size)

    def set_background_image(self, image_dir: str):
        self.setBackgroundImage(image_dir)

    def set_background_image_gif(self, image_dir: str):
        self.setBackgroundGif(image_dir)

    def set_project_name(self, project_name: str):
        select_label: QLabel = self.ViewerLabel.getObjectByIndex(22)
        select_label.setText(project_name)
        select_label.setWordWrap(True)
        select_label.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        select_label.setMinimumWidth(300)

    def set_username_label(self, username: str):
        username = random_titles[randint(0, 100)]
        select_label: QLabel = self.ViewerLabel.getObjectByIndex(2)
        # select_label.setFont(QFont('Jura', 8))
        select_label.setText(username)
        select_label.setStyleSheet("font: 16pt;")
        select_label.setWordWrap(True)

