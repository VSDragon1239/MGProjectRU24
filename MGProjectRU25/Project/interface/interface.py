from TemplateProject.interface.tools.view_initializations.initialization_view import initMainView
from MGProjectRU25.Project.interface.views.main_view import MainUiView


def main_ui_interface(model):
    print("Создаём главное окно...")
    GUI = initMainView(MainUiView, model, is_maximize=True)
    print("Главное окно создано:", GUI)
    return GUI
