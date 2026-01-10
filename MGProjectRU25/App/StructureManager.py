import os
from pathlib import Path

from MGProjectRU25.App.Data import get_main_modules
from MGProjectRU25.App.ProjectManager import ProjectManager
from MGProjectRU25.App.SystemManager import SystemManager
from TemplateProject.core.services.directory_service import DirectoryService
from TemplateProject.core.services.file_service import FileService


class StructureManager(ProjectManager):
    MAIN_DRIVE = None
    AllGlobalProjectsPath = []
    MODULES_NAME = ["GMSStorageFilesModule", "GMSControlDataModule", "GMSServerFilesModule"]
    DSProjectService = None
    DSIApplicationService = None
    DSApplicationService = None

    def __init__(self):
        super().__init__()
        self.set_drive()
        self._init_installs_applications_path()
        self._init_applications_path()

    def set_drive(self):
        self.MAIN_DRIVE = self.get_main_drive()
        if self.MAIN_DRIVE is None:
            self.set_main_drive()
            self.MAIN_DRIVE = self.get_main_drive()

    @staticmethod
    def __get_gms_module(module_name):
        if module_name == "GMSStorageFilesModule":
            return get_main_modules()["Modules"][0]
        elif module_name == "GMSControlDataModule":
            return get_main_modules()["Modules"][1]
        elif module_name == "GMSServerFilesModule":
            return get_main_modules()["Modules"][2]

    def __get_gms_global_project_path(self, module_name):
        return self.__get_gms_module(module_name)["Directory"] + '/' + \
            self.__get_gms_module(module_name)["SubDirectories"][0]["Directory"]

    def __get_gms_applications_path(self, module_name):
        return self.__get_gms_module(module_name)["Directory"] + '/' + \
            self.__get_gms_module(module_name)["SubDirectories"][3]["Directory"]

    def get_all_installs_applications_path(self):
        return self.MAIN_DRIVE + self.__get_gms_applications_path("GMSStorageFilesModule")

    def _init_installs_applications_path(self):
        self.DSIApplicationService = DirectoryService(self.get_all_installs_applications_path(), starry_dir=True)

    def _init_applications_path(self):
        self.DSApplicationService = DirectoryService(self.get_installing_applications_to_path() + '/systemApps',
                                                     starry_dir=True)
        if not self.DSApplicationService.directory_exists(""):
            self.DSApplicationService.create_directory("")

    def get_installing_applications_to_path(self):
        return self.DSIApplicationService.base_directory

    def get_tools_applications_to_path(self):
        return self.DSApplicationService1.base_directory

    def get_tools_applications_paths(self):
        self.DSApplicationService1 = DirectoryService(self.get_installing_applications_to_path(),
                                                      starry_dir=True)
        return self.DSApplicationService1.get_directories()

    def get_applications_path(self):
        return self.DSApplicationService.base_directory

    def get_all_global_projects_path(self, module_name, global_project_id=None):
        path = self.MAIN_DRIVE + self.__get_gms_global_project_path(module_name) + '/'
        if global_project_id is None:
            return path
        else:
            return path + str(global_project_id) + '/'

    def get_all_projects_to_gp_path(self, module_name, global_project_id, project_id=None):
        # print(f'get_all_projects_to_gp_path.global_project_id = {global_project_id}')
        gp_path = self.get_all_global_projects_path(module_name, global_project_id)
        if project_id is None:
            return gp_path
        else:
            return gp_path + str(project_id) + '/'

    def get_sub_dirs_to_path(self, project_path):
        self.DSProjectService = DirectoryService(project_path, starry_dir=True)
        if self.DSProjectService is None:
            raise TypeError("Вероятно зацикливание...")
        return self.DSProjectService.get_directories()

    def create_subdir_to_project(self, project_path, sub_dir_name):
        if self.DSProjectService:
            self.DSProjectService.create_directory(sub_dir_name)
            return self.DSProjectService.get_directories()
        else:
            self.get_sub_dirs_to_path(project_path)
        self.create_subdir_to_project(project_path, sub_dir_name)

    def open_folder_sub_dir(self, sub_dir_name):
        if self.DSProjectService:
            self.DSProjectService.openFolder(sub_dir_name)

    def open_folder_installing_apps(self):
        if self.get_installing_applications_to_path():
            self.DSIApplicationService.openFolder("")
        else:
            raise TypeError("Что-то пошло не так...")

    def open_folder_tools_sub_dir(self, sub_dir_name):
        if self.get_tools_applications_to_path():
            self.DSApplicationService1.openFolder(sub_dir_name)
        else:
            raise TypeError("Что-то пошло не так...")

    def create_app(self, exe_app_path, icon_path):
        work_app_path = str(Path(exe_app_path).parent)
        print("create_app")
        file_name_id = 1
        while True:
            if not self.DSApplicationService.search_files(str(file_name_id)):
                self.DSApplicationService.create_shortcut(exe_app_path, self.get_applications_path(),
                                                          shortcut_name=str(file_name_id) + '.exe',
                                                          working_directory=work_app_path, source_mode=True)
                self.DSApplicationService.copy_file(icon_path, self.get_applications_path(),
                                                    new_name=str(file_name_id) + '.png',
                                                    source_mode=True)
                return file_name_id
            else:
                file_name_id += 1

    def get_apps_data(self):
        return self.DSApplicationService.list_files()

    def open_app(self, app_name):
        self.DSApplicationService.open_file(app_name)

# if __name__ == "__main__":
# STRUCTURE_MANAGER: SystemManager and ProjectManager = StructureManager()
#
#     print(STRUCTURE_MANAGER.get_all_global_projects_path("GMSStorageFilesModule"))
#
#     # Установка типа диска
#     STRUCTURE_MANAGER.set_type_drive("C:/", 2)
#
#     # Создание глобальных проектов:
#     STRUCTURE_MANAGER.create_new_global_project(["Global Reversion Virtualization", "GRV", "Глобальная Реверсия Виртуализации"])
#     STRUCTURE_MANAGER.create_new_global_project(["Global Reversion Reality", "GRR", "Глобальная Реверсия Реальности"])
#     STRUCTURE_MANAGER.create_new_global_project(["Global Reversion Program", "GRP", "Глобальная Реверсия Программ"])
#
#     # Создание проектов:
#     STRUCTURE_MANAGER.create_project("GRV", ["EquestriaVirtualReality", "EquusVR", "ЭквестрияVR"])
#     STRUCTURE_MANAGER.create_project("GRV", ["EquestriaRDaP", "EquusRDP", "Робо Дракон и Пони"])
#     STRUCTURE_MANAGER.create_project("GRV", ["VoxPlayProject", "VPP", "Проект Игры 'VoxPlay'"])
#     STRUCTURE_MANAGER.create_project("GRR", ["Fanfics", "FFB", "Фанфики"])
#     STRUCTURE_MANAGER.create_project("GRR", ["Memories", "MMS", "Воспоминания"])
#     STRUCTURE_MANAGER.create_project("GRR", ["ReversTerraria", "RST", "Реверсия Террарии"])
#     STRUCTURE_MANAGER.create_project("GRP", ["MGProject24", "MGP", "Главный Глобальный Проект"])
#     STRUCTURE_MANAGER.create_project("GRP", ["MGSD", "MGSDsl", "Глваный проект"])
#     STRUCTURE_MANAGER.create_project("GRP", ["TestProject", "TPP", "Тестовый Проект"])
#
#     # Получение данных (временно) о проектах
#     STRUCTURE_MANAGER.print_projects(1)
#     STRUCTURE_MANAGER.print_global_projects()
#     # Получение данных о проектах
#     print(STRUCTURE_MANAGER.get_global_projects())
#     print(STRUCTURE_MANAGER.get_global_project_by_name("GRV"))
#     print(STRUCTURE_MANAGER.get_projects_filter_gp_id(1, return_mod=1))
#     # print(STRUCTURE_MANAGER.get_projects_filter_gp_id(1, return_mod=0))
