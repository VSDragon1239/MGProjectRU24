import sys

from PySide6.QtWidgets import QApplication
from TemplateProject.interface.tools.view_initializations.initialization_view import initMainView
from TemplateProject.interface.views.template_view import TemplateView
from TemplateProject.interface.views.template_empty_view import TemplateEmptyView
from TemplateProject.interface.views.template_ui_view import TemplateUiView
from TemplateProject.interface.views.template_ui_fire_reset_view import TemplateUiFireResetView


def template_ui_interface(model):
    print("Создаём главное окно...")
    # GUI = initMainView(TemplateView, is_maximize=True)
    # GUI = initMainView(TemplateEmptyView, is_maximize=True)
    # GUI = initMainView(TemplateUiView, is_maximize=True)
    GUI = initMainView(TemplateUiFireResetView, is_maximize=True)
    GUI.set_template_model(model)
    print("Главное окно создано:", GUI)
    return GUI
