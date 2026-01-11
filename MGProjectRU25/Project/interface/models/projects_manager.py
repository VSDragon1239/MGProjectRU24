from random import randint


class TemplateUiFrModel:
    def __init__(self, template_structure):
        self.template_structure = template_structure
        self.global_projects_data = []
        self.projects_data = {}
        self.app_data = None

    def get_global_projects_data(self):
        return self.global_projects_data

    def set_global_projects_data(self, data):
        self.global_projects_data = data

    def add_global_projects_data(self, data):
        self.global_projects_data.append(data)

    def get_projects_data(self):
        return self.projects_data

    def set_projects_data(self, data: dict):
        self.projects_data = data

    def add_template_project_data(self, name):
        return {
                "Name": f"{name}",
                "Path": "to/file/path3",
                "GlobalProject": 2,
                "LinkApp": [randint(1, 100)],
            }

    def get_app_data(self):
        return self.app_data

    def set_app_data(self, data):
        self.app_data = data
