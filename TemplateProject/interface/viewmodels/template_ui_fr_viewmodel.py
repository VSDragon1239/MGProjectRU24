from random import randint

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QListWidgetItem


from TemplateProject.interface.models.template_ui_fr_model import TemplateUiFrModel


class TemplateUiFRViewModel(QObject):
    Model = None
    selected_project = None
    active_app = None

    global_projects = ["GVR", "GRR", "MGVSD"]
    project_data = {
        "Projects": [
            {
                "Name": "1",
                "Path": "to/file/path1",
                "GlobalProject": global_projects[0],
                "LinkApp": ["Blender", "UE5"],
            },
            {
                "Name": "2",
                "Path": "to/file/path2",
                "GlobalProject": global_projects[1],
                "LinkApp": [],
            },
            {
                "Name": "3",
                "Path": "to/file/path3",
                "GlobalProject": global_projects[2],
                "LinkApp": ["PyCharm"],
            }
        ]
    }
    apps = ['Blender', 'UE5', 'PyCharm', '4', '5', '6', '7', '8', '9']

    def __init__(self, View, model):
        super().__init__()
        self.view = View
        self.Model = model

    def get_apps_data(self):
        return self.apps

    def get_projects_data(self):
        project_count = len(self.project_data["Projects"])
        return [project_count, self.project_data]

    def new_project(self, name):
        return

    def select_project(self, item: QListWidgetItem):
        """Выбирает проект."""
        for project in self.project_data["Projects"]:
            if project["Name"] == item.text():
                self.selected_project = project
        print(self.selected_project)

    def get_selected_project(self):
        return self.selected_project
