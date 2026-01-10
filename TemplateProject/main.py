import sys

from PySide6.QtWidgets import QApplication

from TemplateProject.interface.interface import template_ui_interface
from TemplateProject.interface.models.template_ui_fr_model import TemplateUiFrModel

from TemplateProject.template.template_structure import TemplateStructure


if __name__ == '__main__':
    template_structure = TemplateStructure()
    model = TemplateUiFrModel(template_structure)

    app = QApplication(sys.argv)
    GUI = template_ui_interface(model)
    sys.exit(app.exec())
