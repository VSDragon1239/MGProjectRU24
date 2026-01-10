from PySide6.scripts.project_lib import project_data

from MGProjectRU25.App.Data import PROJECTS, PROJECTS_VISUAL
from MGProjectRU25.App.SystemManager import SystemManager
from MGProjectRU25.Project.project_settings import PROJECT_ROOT
from TemplateProject.core.services.file_service import FileService


class ProjectManager(SystemManager):
    projects_file = FileService(str(PROJECT_ROOT), "ProjectFile", "json")
    projects_file_visualize = FileService(str(PROJECT_ROOT), "ProjectFileView", "json")
    project_data_cache = None
    project_view_data_cache = None

    def __init__(self):
        super().__init__()
        self._init_projects_file()
        self._init_projects_file_visualize()
        self._back_default()

    def _init_projects_file(self):
        self.project_data_cache = self.projects_file.read_file()[1]
        if self.project_data_cache == {}:
            self.projects_file.write_file(PROJECTS)
            self.project_data_cache = self.projects_file.read_file()

    def _init_projects_file_visualize(self):
        self.project_view_data_cache = self.projects_file_visualize.read_file()[1]
        if self.project_view_data_cache == {}:
            if PROJECTS_VISUAL["GlobalProjectsData"] != self.project_data_cache["StructureData"]["GlobalProjectsData"]:
                self.import_project_data_into_projects_file_visualize()
                self.projects_file_visualize.write_file(self.project_view_data_cache)
            else:
                if self.project_view_data_cache == {}:
                    self.projects_file_visualize.write_file(PROJECTS_VISUAL)
                    self.project_view_data_cache = self.projects_file_visualize.read_file()

    def import_project_data_into_projects_file_visualize(self):
        self.project_view_data_cache = self.project_data_cache["StructureData"]

    def _back_default(self):
        back_projects = self.structure["MGProjectRU25"]["StructureData"]["GlobalProjectsData"]
        if back_projects != [] and self.project_data_cache == PROJECTS:
            self.project_data_cache["StructureData"]["GlobalProjectsData"] = back_projects
            self.structure["MGProjectRU25"]["StructureData"]["GlobalProjectsData"] = []
            self.safe_projects()
            self.safe_structure_data()

    def pashalochka(self):
        data1 = "Не"
        Operator2 = "^"
        data2 = ["Лутшая Потрушка", "лп"]
        IlonMaxYablochkinSkazal = data1 + Operator2 + data2[1]
        print(IlonMaxYablochkinSkazal)

    def find_index_gp_by_ru_name(self, ru_name):
        for i, item in enumerate(self.project_view_data_cache["GlobalProjectsData"]):
            if item["GlobalProjectRuName"] == ru_name:
                return i
        return -1

    def find_index_project_by_ru_name(self, gp_index, ru_name):
        for i, item in enumerate(self.project_view_data_cache["GlobalProjectsData"][gp_index]["Projects"]):
            if item["ProjectRuName"] == ru_name:
                return i
        return -1

    def get_data_projects(self) -> list:
        return self.project_view_data_cache["GlobalProjectsData"]

    def move_global_project_visual(self, forward, selected_global_project):
        """
        :param forward: 'up' or 'down'
        :param selected_global_project: "Виртуализация Реальности" (GlobalProjectRuName)
        :return:
        """
        # print("move_global_project_visual" + "TEST")
        data = self.project_view_data_cache["GlobalProjectsData"]
        index = self.find_index_gp_by_ru_name(selected_global_project)

        if index <= 0 and forward == "up":
            return
        if forward == "up":
            data[index - 1], data[index] = data[index], data[index - 1]
            print('move_global_project_visual.forward-up')
        elif forward == "down":
            data[index + 1], data[index] = data[index], data[index + 1]
            print('move_global_project_visual.forward-down')
        self.safe_projects_visual()

    def move_project_visual(self, forward, selected_global_project, selected_project):
        """
        :param forward: 'up' or 'down'
        :param selected_global_project: "Виртуализация Реальности" (GlobalProjectRuName)
        :param selected_project: "Learn - Компьютерная графика" (ProjectRuName)
        :return: None
        """
        print("move_project_visual" + "TEST")
        gp_index = self.find_index_gp_by_ru_name(selected_global_project)

        data_p = self.project_view_data_cache["GlobalProjectsData"][gp_index]["Projects"]
        index = self.find_index_project_by_ru_name(gp_index, selected_project)
        print("move_project_visual.data = " + f"{data_p}")
        print("move_project_visual.forward = " + f"{forward}")
        if index <= 0 and forward == "up":
            return
        if forward == "up":
            print("move_global_project_visual.forward-up")
            data_p[index - 1], data_p[index] = data_p[index], data_p[index - 1]
        elif forward == "down":
            print("move_global_project_visual.forward-down")
            data_p[index + 1], data_p[index] = data_p[index], data_p[index + 1]
        self.safe_projects_visual()


    def safe_projects(self):
        if self.project_data_cache != self.projects_file.read_file():
            self.projects_file.write_file(self.project_data_cache)

    def safe_projects_visual(self):
        if self.project_view_data_cache != self.projects_file_visualize.read_file():
            self.projects_file_visualize.write_file(self.project_view_data_cache)

    # === Создание Глобального Проекта ===
    def __create_data_global_project(self, global_project_data: list):
        """
        Вызывается из функции create_new_global_project(), для словаря данных из списка
        :param global_project_data: Получаем список,
            где [0] = GlobalProjectEnName
                [1] = GlobalProjectSlugName
                [2] = GlobalProjectRuName
        :return: dict
        """
        self.last_global_project_id = len(self.get_data_projects()) + 1
        return {
            "id_GlobalProject": self.last_global_project_id,
            "GlobalProjectEnName": global_project_data[0],
            "GlobalProjectSlugName": global_project_data[1],
            "GlobalProjectRuName": global_project_data[2],
            "Projects": []
        }

    def __append_new_global_project(self, global_project_data: dict):
        """
        Вызывается из функции create_new_global_project()
        :param global_project_data: получает сформированный словарь из функции __create_data_global_project(data: list)
        :return: None ( Сохраняет данные функцией safe_data() )
        """
        self.project_data_cache["StructureData"]["GlobalProjectsData"].append(global_project_data)
        self.safe_projects()

    def create_new_global_project(self, global_project_data: list):
        """
        :param global_project_data: [GlobalProjectEnName, SlugName, RuName]
        :return: None
        """
        data = self.__create_data_global_project(global_project_data)
        self.__append_new_global_project(data)

    def rename_global_project(self, global_project_name: str, new_global_project_names: list):
        gp = self.get_global_project_by_name(global_project_name)
        if gp is None:
            raise TypeError("Проект не найден")
        gp["GlobalProjectEnName"], gp["GlobalProjectSlugName"], gp["GlobalProjectRuName"] = new_global_project_names
        self.safe_projects()

    # === Добавление Проекта в Глобальный проект ===
    def __create_data_project(self, global_project_name: str, project_data: list):
        for global_project in self.get_data_projects():
            if (
                    global_project["GlobalProjectEnName"] == global_project_name or
                    global_project["GlobalProjectSlugName"] == global_project_name or
                    global_project["GlobalProjectRuName"] == global_project_name
            ):
                global_project_id = global_project["id_GlobalProject"]
                if global_project["Projects"]:
                    last_project_id = global_project["Projects"][-1]["id_Project"] + 1
                else:
                    last_project_id = 1
                for project in global_project["Projects"]:
                    if project["ProjectEnName"] == project_data[0] or project["ProjectSlugName"] == project_data[1] or \
                            project["ProjectRuName"] == project_data[2]:
                        raise ValueError("Проект с таким названием уже существует...")
                new_project = {
                    "id_Project": last_project_id,
                    "ProjectEnName": project_data[0],
                    "ProjectSlugName": project_data[1],
                    "ProjectRuName": project_data[2],
                }
                return global_project_id, new_project
        raise ValueError("Указанный Глобальный проект - не найден")

    def __append_new_project(self, global_project_id: int, project_data: dict):
        self.project_data_cache["StructureData"]["GlobalProjectsData"][global_project_id - 1]["Projects"].append(project_data)
        self.safe_projects()

    def create_project(self, global_project_name: str, project_data: list):
        """
        :param global_project_name: "Name"
        :param project_data: [ "ProjectEnName", "ProjectSlugName", "ProjectRuName" ]
        :return:
        """
        try:
            data = self.__create_data_project(global_project_name, project_data)
        except ValueError:
            return -1
        select_global_project_id = data[0]
        project = data[1]
        self.__append_new_project(select_global_project_id, project)

    def rename_project(self, global_project_name, project_name: str, new_name: list):
        print("rename_project.new_name = " + f"{new_name}")
        gp_project = self.get_project_filter_projects_name_filter_gp_name(global_project_name, project_name)
        gp_project["ProjectEnName"], gp_project["ProjectSlugName"], gp_project["ProjectRuName"] = new_name
        self.safe_projects()

    def get_global_projects(self):
        return self.get_data_projects()

    def get_global_project_by_name(self, global_project_name):
        for gp_i in self.get_data_projects():
            if (
                    gp_i["GlobalProjectEnName"] == global_project_name or
                    gp_i["GlobalProjectSlugName"] == global_project_name or
                    gp_i["GlobalProjectRuName"] == global_project_name
            ):
                return gp_i

    def __get_projects_filter_gp_id(self, global_project_name: str, project_data="id_Project", return_mod=0):
        """
        :param global_project_id:
        :param project_data: "id_Project", "ProjectEnName", "ProjectSlugName", "ProjectRuName"
        :param return_mod: 0: возвращает данные проектов, 1: Возвращает только ids проектов
        :return:
        """
        gp_index = self.find_index_gp_by_ru_name(global_project_name)
        if return_mod == 0:
            print(f'__get_projects_filter_gp_id.get_data_projects = {self.get_data_projects()[gp_index]["Projects"]}')
            print(f'__get_projects_filter_gp_id.global_project_name and gp_index = {global_project_name}, {gp_index}')
            return self.get_data_projects()[gp_index]["Projects"]
        elif return_mod == 1:
            project_ids = []
            for project_i in \
                    self.get_data_projects()[gp_index]["Projects"]:
                project_ids.append(project_i[project_data])
            return project_ids

    def get_projects_filter_gp_name(self, global_project_name, return_mod=0):
        print("get_projects_filter_gp_name.gpn = " + f"{global_project_name}, {self.get_global_project_by_name(global_project_name)['id_GlobalProject']}")
        return self.__get_projects_filter_gp_id(
            self.get_global_project_by_name(global_project_name)["GlobalProjectRuName"], return_mod=return_mod)

    def get_project_filter_projects_name_filter_gp_name(self, global_project_name, project_name, return_mod=0):
        projects = self.__get_projects_filter_gp_id(
            self.get_global_project_by_name(global_project_name)["GlobalProjectRuName"], return_mod=return_mod)
        for project in projects:
            if project["ProjectEnName"] == project_name:
                return project
            elif project["ProjectSlugName"] == project_name:
                return project
            elif project["ProjectRuName"] == project_name:
                return project
            print(f'get_project_filter_projects_name_filter_gp_name.project = {project}')

        raise ValueError("Проект не найден")


# if __name__ == "__main__":
#     PROJECT_MANAGER = ProjectManager()
#     PROJECT_MANAGER.pashalochka()
# PROJECT_MANAGER.create_new_global_project(["Global Reversion Virtualization", "GRV", "Глобальная Реверсия Виртуализации"])
# PROJECT_MANAGER.create_new_global_project(["Global Reversion Reality", "GRR", "Глобальная Реверсия Реальности"])
# PROJECT_MANAGER.create_new_global_project(["Global Reversion Program", "GRP", "Глобальная Реверсия Программ"])
# PROJECT_MANAGER.create_project("GRV", ["EquestriaVirtualReality", "EquusVR", "ЭквестрияVR"])
# PROJECT_MANAGER.create_project("GRV", ["EquestriaRDaP", "EquusRDP", "Робо Дракон и Пони"])
# PROJECT_MANAGER.create_project("GRV", ["VoxPlayProject", "VPP", "Проект Игры 'VoxPlay'"])
# PROJECT_MANAGER.create_project("GRR", ["Fanfics", "FFB", "Фанфики"])
# PROJECT_MANAGER.create_project("GRR", ["Memories", "MMS", "Воспоминания"])
# PROJECT_MANAGER.create_project("GRR", ["ReversTerraria", "RST", "Реверсия Террарии"])
# PROJECT_MANAGER.create_project("GRP", ["MGProject24", "MGP", "Главный Глобальный Проект"])
# PROJECT_MANAGER.create_project("GRP", ["MGSD", "MGSDsl", "Глваный проект"])
# PROJECT_MANAGER.create_project("GRP", ["TestProject", "TPP", "Тестовый Проект"])
# # PROJECT_MANAGER.create_project("GRV", ["EquestriaVirtualReality", "EquusVR", "ЭквестрияVR"])
# # PROJECT_MANAGER.print_structure_data()
