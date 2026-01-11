import logging
from random import randint

from PySide6.QtCore import QObject, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QListWidgetItem, QSizePolicy

from MGProjectRU25.Project.interface.models.main_model import MainModel
from MGProjectRU25.Project.interface.tools.global_project_item import GlobalProjectItemWidget
from MGProjectRU25.Project.interface.tools.icon_manager import IconManager
from MGProjectRU25.Project.interface.tools.icon_with_random_hue import cached_random_icon
from MGProjectRU25.Project.interface.tools.project_item import ProjectItemWidget
from MGProjectRU25.Project.project_settings import IMAGES_DIRS, IMAGES_DIR, GEN_IMAGES
from MGProjectRU25.Project.variable_settings import random_titles, d_space


class MainViewModel(QObject):
    Model = None
    selected_gp = None
    selected_project = None
    selected_project_dir = None
    selected_sub_dir = None
    active_app = None

    all_global_projects = None
    all_projects_by_gp = None
    all_sub_dirs_of_select_project = None

    widget_list_gp = None
    widget_list_project = None
    widget_list_sub_dirs_of_select_project = None
    widget_list_apps = None

    def __init__(self, view, model):
        super().__init__()
        self.project_items_by_id = {}
        self.iconManager = IconManager()
        self.iconManager.icon_ready.connect(self.on_icon_ready)
        self.logger = logging.getLogger(__name__)
        self.view = view  # MainUiView
        self.model: MainModel = model
        self._set_data()
        # self.view.setWindowIcon(QIcon(IMAGES_DIR + IMAGES_DIRS[11]))

        # x1 = randint(1, 70)
        # x2 = randint(80, 200)
        # print(f"Тестируем случайность: {x1, x2, x1<x2}")
        if not randint(1, 70) <= randint(70, 200):
            self.view.setWindowTitle(
                'MGPRU2425' + d_space + self.model.dir_manager("get_main_drive", "None")[:3] + d_space + str(
                    randint(99999, 999999)))
        else:
            self.view.setWindowTitle(
                'MGPRU2425' + d_space
                + self.model.dir_manager("get_main_drive", "None")[:3] + d_space
                + random_titles[randint(0, 100)] + d_space
                # + str(randint(9999999999999, 999999999999999))
            )

    def _set_data(self, *args, **kwargs):
        for arg in args:
            match arg:
                case "":
                    pass
                case "":
                    pass
                case "":
                    pass
                case "":
                    pass
                case _:
                    pass
        for key, value in kwargs.items():
            match key:
                case "":
                    pass
                case "":
                    pass
                case "":
                    pass
                case "":
                    pass
                case _:
                    pass

        self.all_global_projects = self.model.model_manager("all_global_projects")

    def _get_data(self, *args, **kwargs):
        """
        :param args: QListWidgetItem -> text()
                kwargs: type_data: str [global_project, all_projects, project]
        :return:
        """
        type_data, item = self.manager_args_kwargs(*args, **kwargs)

        if type_data == "global_project" or type_data == "all_projects":
            # print(f'_get_data.item[0] = {item[0]}')
            return self.model.model_manager(type_data, global_project_name=item[0])
        elif type_data == "project":
            return self.model.model_manager(type_data, global_project_name=self.selected_gp["GlobalProjectSlugName"],
                                            project_name=item[0])
        else:
            raise TypeError("Тип данных дан не верно!")

    def get_all_global_projects(self):
        return self.all_global_projects

    def get_global_project(self, item: QListWidgetItem):
        self.selected_gp = self._get_data(item, type_data="global_project")
        self.__get_all_projects_by_global_project(item)
        self.list_projects()
        return self.selected_gp

    def move_global_project_up(self, select_global_project: str):
        self.model.model_manager(type_data="move_global_project_up", global_project_name=select_global_project)
        self.list_global_projects()

    def move_global_project_down(self, select_global_project: str):
        self.model.model_manager(type_data="move_global_project_down", global_project_name=select_global_project)
        self.list_global_projects()

    def move_project_up(self, selected_project):
        self.model.model_manager(type_data="move_project_up", global_project_name=self.selected_gp["GlobalProjectRuName"], project_name=selected_project)
        self.list_projects()

    def move_project_down(self, selected_project):
        self.model.model_manager(type_data="move_project_down", global_project_name=self.selected_gp["GlobalProjectRuName"], project_name=selected_project)
        self.list_projects()

    def __get_all_projects_by_global_project(self, item: QListWidgetItem):
        # print(f'__get_all_projects_by_global_project.item = {item.text()}')
        self.all_projects_by_gp = self._get_data(item, type_data="all_projects")

    def get_all_projects(self):
        return self.all_projects_by_gp

    def get_project(self, item: QListWidgetItem, widget_label_name):
        # print(f'get_project.item = {item.text()}, widget_label_name = {widget_label_name}')
        self.selected_project = self._get_data(item, type_data="project")
        widget_label_name(str(self.selected_project["ProjectRuName"]))
        self.set_project_path()
        self.get_sub_dirs_of_select_project()
        self.list_sub_dirs_of_select_project()
        return self.selected_project

    def set_project_path(self):
        self.selected_project_dir = self.model.model_manager("get_project_path", self.selected_gp["id_GlobalProject"],
                                                             self.selected_project["id_Project"])

    def get_sub_dirs_of_select_project(self):
        if self.selected_project_dir:
            self.all_sub_dirs_of_select_project = self.model.dir_manager("get_sub_dirs_of_select_project",
                                                                         self.selected_project_dir)

    def select_sub_dir(self, item: QListWidgetItem):
        for sub_dir in self.all_sub_dirs_of_select_project:
            if sub_dir == item.text():
                self.selected_sub_dir = sub_dir

    def create_sub_dir_select_project(self, sub_dir_name):
        self.model.dir_manager("create_sub_dir_select_project", self.selected_project_dir, sub_dir_name)
        self.get_sub_dirs_of_select_project()
        self.list_sub_dirs_of_select_project()

    def create_global_project(self, ru_gp_name):
        self.model.model_manager("create_global_project", global_project_name=ru_gp_name)
        self.list_global_projects()

    def rename_global_project(self, select_gp_name, new_name):
        self.model.model_manager("rename_global_project", global_project_name=select_gp_name, new_name=new_name)
        self.list_global_projects()

    def delete_global_project(self, select_gp_name):
        self.model.model_manager("delete_global_project", global_project_name=select_gp_name)
        self.list_global_projects()

    def delete_project(self, select_gpp_name):
        self.model.model_manager("delete_project", global_project_name=self.selected_gp["GlobalProjectRuName"], project_name=select_gpp_name)
        self.list_projects()

    def create_project(self, ru_gp_name, ru_project_name):
        if self.model.model_manager("create_project", global_project_name=ru_gp_name,
                                    project_name=ru_project_name) == -1:
            return False
        else:
            self.list_projects()
            return True

    def rename_project(self, select_project_name, new_name):
        self.model.model_manager("rename_project", global_project_name=self.selected_gp["GlobalProjectSlugName"],
                                 project_name=select_project_name, new_name=new_name)
        self.list_projects()

    def list_global_projects(self):
        self.widget_list_gp.clear()
        for gp_project in self.get_all_global_projects():
            if gp_project["GlobalProjectSlugName"] == "virtualizatsiya-realnosti":
                icon = QIcon(IMAGES_DIR + IMAGES_DIRS[7])
            elif gp_project["GlobalProjectSlugName"] == "GRR":
                icon = QIcon(IMAGES_DIR + IMAGES_DIRS[8])
            elif gp_project["GlobalProjectSlugName"] == "programmnaya-globalizatsiya":
                icon = QIcon(IMAGES_DIR + IMAGES_DIRS[6])
            else:
                icon = QIcon(IMAGES_DIR + IMAGES_DIRS[5])
            item = QListWidgetItem(icon, f"{gp_project['GlobalProjectRuName']}")
            widget_item = GlobalProjectItemWidget(
                project=gp_project,
                viewModel=self
            )
            item.setSizeHint(widget_item.sizeHint())
            self.widget_list_gp.addItem(item)
            self.widget_list_gp.setItemWidget(item, widget_item)
            # self.widget_list_gp.addItem(item)
            self.widget_list_gp.setIconSize(QSize(48, 48))

    def list_projects(self):
        self.widget_list_project.setUpdatesEnabled(False)  # временно отключаем перерисовку
        self.widget_list_project.clear()
        self.project_items_by_id.clear()

        # Рисуем иконку
        slug = self.selected_gp.get("GlobalProjectSlugName")
        if slug == "virtualizatsiya-realnosti":
            icon_path = IMAGES_DIR + IMAGES_DIRS[7]
        elif slug == "GRR":
            icon_path = IMAGES_DIR + IMAGES_DIRS[8]
        elif slug == "programmnaya-globalizatsiya":
            icon_path = IMAGES_DIR + IMAGES_DIRS[6]
        else:
            icon_path = IMAGES_DIR + IMAGES_DIRS[5]

        placeholder_icon = QIcon(
            QPixmap(icon_path)
        )

        for project in self.get_all_projects():
            # print("list_projects - TEST " + f"{project}")
            # icon = cached_random_icon(
            #     icon_path,
            #     key=str(project["id_Project"]) + project["ProjectRuName"] + project["ProjectSlugName"] + str(len(project["ProjectEnName"]) / 2)
            # )

            widget_item = ProjectItemWidget(
                project=project,
                viewModel=self
            )

            item = QListWidgetItem(placeholder_icon, f"{project['ProjectRuName']}")
            item.setSizeHint(widget_item.sizeHint())
            self.widget_list_project.addItem(item)
            self.widget_list_project.setItemWidget(item, widget_item)
            self.widget_list_project.setIconSize(QSize(32, 32))


            key = project["id_Project"]
            self.project_items_by_id[key] = item

            # 👇 ЗАПРОС В ФОН
            if GEN_IMAGES:
                self.iconManager.request_icon(icon_path, key)

        self.widget_list_project.setUpdatesEnabled(True)

    def on_icon_ready(self, key, icon):
        item = self.project_items_by_id.get(key)
        if item:
            item.setIcon(icon)

    def list_sub_dirs_of_select_project(self):
        self.widget_list_sub_dirs_of_select_project.clear()
        for sub_dir in self.all_sub_dirs_of_select_project:
            self.widget_list_sub_dirs_of_select_project.addItem(sub_dir)

    def init_widget_list_gp(self, widget):
        self.widget_list_gp = widget
        self.list_global_projects()

    def init_widget_list_project(self, widget):
        self.widget_list_project = widget

    def init_widget_list_sub_dirs_of_select_project(self, widget):
        self.widget_list_sub_dirs_of_select_project = widget

    def init_widget_list_apps(self, widget):
        self.widget_list_apps = widget
        self.list_apps()

    def init_widget_list_tools_applications_path(self, widget):
        self.widget_list_tools_applications_path = widget
        self.list_tools_applications_path()

    def open_folder_sub_dir(self):
        self.model.dir_manager("open_folder_sub_dir", self.selected_sub_dir)

    def open_folder_installing_apps(self):
        pass_data = None
        self.model.dir_manager("open_folder_installing_apps", pass_data)

    def open_folder_tools_sub_dir(self, sub_dir_name):
        pass_data = None
        self.model.dir_manager("open_folder_tools_sub_dir", pass_data, sub_dir_name=sub_dir_name)

    def create_app(self, exe_app_path, path_icon):
        # print("create_app")
        self.model.dir_manager("create_app", "project_name", exe_app_path=exe_app_path, icon_path=path_icon)
        self.list_apps()

    def list_apps(self):
        self.widget_list_apps.clear()
        print("list_apps", self.get_all_apps_data())
        for app_name, icon_dir in self.get_all_apps_data():
            icon = QIcon(icon_dir)
            item = QListWidgetItem(icon, f"{app_name}")
            self.widget_list_apps.addItem(item)

    def list_tools_applications_path(self):
        self.widget_list_tools_applications_path.clear()
        for tool_dir_name in self.get_tools_applications_path():
            print(tool_dir_name)
            item = QListWidgetItem(f"{tool_dir_name}")
            self.widget_list_tools_applications_path.addItem(item)

    def open_app(self, item: QListWidgetItem):
        self.model.dir_manager("open_app", "", exe_app_path=item.text())

    def get_all_apps_data(self) -> list[tuple[str, str | None]]:
        data = self.model.dir_manager("get_apps_data", "")

        # 1) Разделяем на исполняемые иконки
        exes = [p for p in data if p.lower().endswith((".exe", ".lnk"))]
        icons = [p for p in data if p.lower().endswith((".icon", ".png", ".jpg"))]

        pairs: list[tuple[str, str | None]] = []
        for exe in exes:
            #  имя файла, без пути
            fname = exe.replace("\\", "/").split("/")[-1]
            #  базовое имя — всё до первого "."
            base = fname.split(".", 1)[0]

            # ищем иконку с тем же base
            match = None
            for ic in icons:
                ic_name = ic.replace("\\", "/").split("/")[-1]
                if ic_name.split(".", 1)[0] == base:
                    match = ic
                    break

            pairs.append((exe, match))

        return pairs

    @staticmethod
    def manager_args_kwargs(*args, **kwargs):
        type_data = None
        item = []

        for arg in args:
            match arg:
                case QListWidgetItem():
                    item.append(arg.text())
        for key, value in kwargs.items():
            match key:
                case "type_data":
                    type_data = value
                case "":
                    pass

        if type_data is None:
            raise TypeError

        if item is None:
            raise TypeError

        return type_data, item

    def get_tools_applications_path(self):
        return self.model.dir_manager("get_all_installs_applications_path", "")
