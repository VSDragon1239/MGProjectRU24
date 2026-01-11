from PySide6.scripts.pyside_tool import project

from MGProjectRU25.App.StructureManager import StructureManager
from MGProjectRU25.Project.interface.tools.data_transl import transliterate, slugify



class MainModel:
    def __init__(self, structure_data):
        """
            Есть несколько методов. Они имеет несколько типов работы с данными
                :model_manager
                        :get_project_path

                        :all_global_projects
                        :all_projects

                        :global_project
                        :project

                        :create_global_project
                        :rename_global_project

                        :create_project
                        :rename_project

                        :all_apps
                        :app (No Work)

                :dir_manager
                    :get_sub_dirs_of_select_project
                    :create_sub_dir_select_project

                    :open_folder_sub_dir
                    :open_folder_installing_apps

                    :create_app
                    :get_apps_data
                    :open_app

                    :get_main_drive

                :get_names_manager
                    :Просто посылаем русское название проекта, он отдаёт Eng, Slug, и Ru названия для чего либо, к примеру для проекта

            """
        self.structure_data: StructureManager = structure_data

    def model_manager(self, type_data, global_project_name="", project_name="", new_name="", app_name=""):
        match type_data:
            case "all_global_projects":
                return self.structure_data.get_global_projects()
            case "global_project":
                return self.structure_data.get_global_project_by_name(global_project_name)
            case "all_projects":
                return self.structure_data.get_projects_filter_gp_name(global_project_name)
            case "project":
                return self.structure_data.get_project_filter_projects_name_filter_gp_name(global_project_name,
                                                                                           project_name)
            case "get_project_path":
                return self.structure_data.get_all_projects_to_gp_path("GMSStorageFilesModule", global_project_name, project_name)
            case "all_apps":
                pass
            case "app":
                pass

            case "create_global_project":
                return self.structure_data.create_new_global_project(self.get_names_manager(global_project_name))
            case "create_project":
                return self.structure_data.create_project(global_project_name, self.get_names_manager(project_name))

            case "rename_global_project":
                return self.structure_data.rename_global_project(global_project_name, self.get_names_manager(new_name))
            case "rename_project":
                return self.structure_data.rename_project(global_project_name, project_name, self.get_names_manager(new_name))
            case "delete_global_project":
                return self.structure_data.delete_global_project(global_project_name)
            case "delete_project":
                return self.structure_data.delete_project(global_project_name, project_name)

            case "move_global_project_up":
                return self.structure_data.move_global_project_visual("up", global_project_name)
            case "move_global_project_down":
                return self.structure_data.move_global_project_visual("down", global_project_name)
            case "move_project_up":
                return self.structure_data.move_project_visual("up", global_project_name, project_name)
            case "move_project_down":
                return self.structure_data.move_project_visual("down", global_project_name, project_name)
            case _:
                pass

    def dir_manager(self, type_data, project_path, sub_dir_name="", exe_app_path="", icon_path=""):
        match type_data:
            case "get_sub_dirs_of_select_project":
                return self.structure_data.get_sub_dirs_to_path(project_path)
            case "create_sub_dir_select_project":
                return self.structure_data.create_subdir_to_project(project_path, sub_dir_name)
            case "open_folder_sub_dir":
                return self.structure_data.open_folder_sub_dir(project_path)
            case "open_folder_installing_apps":
                return self.structure_data.open_folder_installing_apps()
            case "open_folder_tools_sub_dir":
                return self.structure_data.open_folder_tools_sub_dir(sub_dir_name)
            case "create_app":
                return self.structure_data.create_app(exe_app_path, icon_path)
            case "get_apps_data":
                return self.structure_data.get_apps_data()
            case "open_app":
                return self.structure_data.open_app(exe_app_path)
            case "get_main_drive":
                return self.structure_data.MAIN_DRIVE
            case "get_all_installs_applications_path":
                return self.structure_data.get_tools_applications_paths()

    @staticmethod
    def get_names_manager(ru_name):
        new_name_data = []

        GlobalProjectEnName = transliterate(ru_name)
        SlugName = str(slugify(GlobalProjectEnName))

        new_name_data.append(GlobalProjectEnName)
        new_name_data.append(SlugName)
        new_name_data.append(ru_name)
        return new_name_data
