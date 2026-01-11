import os

from PySide6.QtCore import QFileSystemWatcher, QTimer, QFile
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader

# from MGProjectRU25.Project.interface.models.reco_model import RecognizingModel
from MGProjectRU25.Project.interface.viewmodels.main_vm import MainViewModel
from MGProjectRU25.Project.interface.views.add_application_view import AddApplicationView
# from MGProjectRU25.Project.interface.views.ai_calibration_view import AICalibrationUiView
from MGProjectRU25.Project.interface.views.create_global_project_view import GlobalProjectDialogView
from MGProjectRU25.Project.interface.views.create_project_view import ProjectDialogView
from MGProjectRU25.Project.interface.views.create_sub_dir_project_view import SubDirProjectDialogView
# from MGProjectRU25.Project.interface.views.run_voice_detector_view import RunVoiceDetectorDialogView
from MGProjectRU25.Project.interface.views.ui_settings.connections.main_window.ButtonConnection import \
    MainWindowUiViewButtonsConnect
from MGProjectRU25.Project.interface.views.ui_settings.connections.main_window.WidgetListConnection import \
    MainWindowUiViewWidgetListConnect
from MGProjectRU25.Project.interface.views.ui_settings.connections.projects_manager.LabelConnection import \
    MainWindowUiLabelConnect
from MGProjectRU25.Project.project_settings import RESOURCES_DIR, IMAGES_DIRS, IMAGES_DIR
from TemplateProject.interface.viewmodels.template_ui_fr_viewmodel import TemplateUiFRViewModel
from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainButtonsConnection import \
    MainButtonsConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainSpinBoxsConnection import \
    MainSpinBoxsConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainUpdateConnection import \
    MainUpdateConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainWidgetsConnection import \
    MainWidgetsConnect

from TemplateProject.interface.views.ui_settings.connections.template_ui_fire_reset_view.TemplateUiFRViewButtonConnection import \
    TemplateUiFRViewButtonsConnect
from TemplateProject.interface.views.ui_settings.connections.template_ui_fire_reset_view.TemplateUiFRViewListWidgetsConnection import \
    TemplateUiFRViewWidgetListConnect
from MGProjectRU25.Project.interface.views.ui_files.main_window import Ui_QMW1


# if not compileUI:
#     ui, QUi = loadUi(2)
#     QUi: QMainWindow
#     ui: QUi


# class MainUiView(ui, QUi):
class MainUiView(QMainWindow, Ui_QMW1):
    model = None
    viewModel = None
    buttonConnect = None
    widgetListConnect = None
    labelConnect = None

    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(IMAGES_DIR + IMAGES_DIRS[11]))

        self.AICalibrationUiView = None
        self.ProjectManagerView = None
        self.set_model(model)
        self.buttonsConnection()
        self.labelConnection()
        self.widgetConnections()
        # self.dialog_run_voice_detector()

    def set_model(self, model):
        self.model = model
        self.load_vm()

    def load_vm(self):
        self.viewModel = MainViewModel(self, self.model)

    def buttonsConnection(self):
        print("== Инициализированы connections кнопок ==")
        self.buttonConnect = MainWindowUiViewButtonsConnect(self, self.viewModel)
        self.buttonConnect.stack_button_window_view()
        self.buttonConnect.setButtonImage(IMAGES_DIR)
        self.buttonConnect.button_create_global_project()
        self.buttonConnect.button_create_project()
        self.buttonConnect.button_create_sub_dir_to_project()
        self.buttonConnect.button_open_folder_sub_dir()
        self.buttonConnect.button_create_application()
        self.buttonConnect.button_open_folder_installing_application()
        self.buttonConnect.button_hider()

    def widgetConnections(self):
        print("== Инициализированы connections виджетов ==")
        self.widgetListConnect = MainWindowUiViewWidgetListConnect(self, self.viewModel)
        self.widgetListConnect.list_widget_global_projects_list()
        self.widgetListConnect.list_widget_projects_list(self.labelConnect.set_project_name)
        self.widgetListConnect.list_widget_sub_dirs_to_project_list()
        self.widgetListConnect.list_widget_apps_list()
        self.widgetListConnect.list_widget_tools_list()
        # self.widgetListConnect.widget_hider()

    def labelConnection(self):
        self.labelConnect = MainWindowUiLabelConnect(self, self.viewModel)
        self.labelConnect.set_image_label(IMAGES_DIR + IMAGES_DIRS[0], [100, 100])
        # self.labelConnect.set_background_image(RESOURCES_DIR+IMAGES_DIRS[1])
        # self.labelConnect.set_background_image_gif(RESOURCES_DIR+IMAGES_DIRS[2])
        self.labelConnect.set_background_image_gif(IMAGES_DIR + IMAGES_DIRS[4])
        self.labelConnect.set_username_label("username")

    def dialog_create_global_project(self):
        gp_name = GlobalProjectDialogView(self).get_name()
        print(f"dialog_create_global_project.gp_name{gp_name}")

        if gp_name:
            return self.viewModel.create_global_project(gp_name)
        else:
            print("Создание проекта отменено")

    def dialog_create_project(self):
        global result_gp_c
        print('dialog_create_project    ', self.viewModel.selected_gp)
        if self.viewModel.selected_gp:
            gp_name = self.viewModel.selected_gp["GlobalProjectSlugName"]
        else:
            print('ГП не выбран')
            return None
        if gp_name:
            project_name = ProjectDialogView(self).get_name()
            print('dialog_create_project    ', project_name)
            if project_name:
                while not self.viewModel.create_project(gp_name, project_name):
                    try:
                        result_gp_c = self.viewModel.create_project(gp_name, project_name)
                    except AttributeError as e:
                        print('dialog_create_project, except', e)
                        QMessageBox.warning(
                            None,
                            "Проект уже существует",
                            f"Проект с именем '{project_name}' уже существует.\nВыберите другое имя.",
                            QMessageBox.Ok
                        )
                        continue
                    if not result_gp_c:
                        QMessageBox.warning(
                            None,
                            "Проект уже существует",
                            f"Проект с именем '{project_name}' уже существует.\nВыберите другое имя.",
                            QMessageBox.Ok
                        )
                        project_name = ProjectDialogView(self).get_name()
                        continue
                    break
                try:
                    return result_gp_c
                except NameError:
                    return None
        else:
            print("Создание проекта отменено")

    def dialog_create_sub_dir_project(self):
        print('dialog_create_project    ', self.viewModel.selected_gp)
        if self.viewModel.selected_gp and self.viewModel.selected_project:
            sub_dir_name = SubDirProjectDialogView(self).get_name()
            if sub_dir_name:
                return self.viewModel.create_sub_dir_select_project(sub_dir_name)
            else:
                print("Создание проекта отменено")
        else:
            print('ГП и Проект не выбраны')
            return None

    # def ai_calibration_start(self):
    #     self.AICalibrationUiView = AICalibrationUiView(self, RecognizingModel())
    #     self.AICalibrationUiView.show()
    #
    # def dialog_run_voice_detector(self):
    #     if_run = RunVoiceDetectorDialogView(self).get_result()
    #     if if_run:
    #         self.ai_calibration_start()

    def dialog_create_application(self):
        exe_app_path, path_icon = AddApplicationView(self).get_paths()
        print('dialog_create_application', path_icon, exe_app_path)
        if exe_app_path and path_icon:
            self.viewModel.create_app(exe_app_path, path_icon)

    @staticmethod
    def switch_view_console_down(stack_widget):
        if stack_widget.isVisible():
            stack_widget.setVisible(False)
        else:
            stack_widget.setVisible(True)

