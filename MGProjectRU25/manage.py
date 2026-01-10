import os

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QIcon

from MGProjectRU25.App.StructureManager import StructureManager
from MGProjectRU25.Project.interface.interface import main_ui_interface
from MGProjectRU25.Project.interface.models.main_model import MainModel

from MGProjectRU25.Project.project_settings import PROJECT_ROOT, BASE_DIR, JURA, IMAGES_DIR, IMAGES_DIRS

import sys


if __name__ == '__main__':
    print(PROJECT_ROOT, BASE_DIR)

    main_structure = StructureManager()
    model = MainModel(main_structure)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(IMAGES_DIR + IMAGES_DIRS[11]))
    QFontDatabase.addApplicationFont(JURA.replace('\\', '/'))
    GUI = main_ui_interface(model)
    sys.exit(app.exec())
