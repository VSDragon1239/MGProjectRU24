import os

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QIcon

from MGProjectRU25.App.StructureManager import StructureManager
from MGProjectRU25.Project.interface.interface import main_ui_interface
from MGProjectRU25.Project.interface.models.main_model import MainModel

from MGProjectRU25.Project.project_settings import PROJECT_ROOT, BASE_DIR, JURA, icon_path

import sys


if __name__ == '__main__':
    import ctypes

    try:
        myappid = 'vsdragon.mgproject.mgsd.version'  # Любая уникальная строка
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception as e:
        print(f"Error setting AppID: {e}")
    print(PROJECT_ROOT, BASE_DIR)

    main_structure = StructureManager()
    model = MainModel(main_structure)
    app = QApplication(sys.argv)
    app_icon = QIcon(icon_path)
    app.setWindowIcon(app_icon)
    QFontDatabase.addApplicationFont(JURA.replace('\\', '/'))
    GUI = main_ui_interface(model)
    GUI.setWindowIcon(app_icon)
    sys.exit(app.exec())
