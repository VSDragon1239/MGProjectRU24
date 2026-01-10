import importlib.util

from PySide6.QtUiTools import loadUiType

from TemplateProject.interface.views.ui_files.ui_files_list import UITypes, PYUITypes

UIType = UITypes
PYUITypes = PYUITypes


def loadUi(UiType):
    try:
        # '''-----------------------------------'''
        print((UITypes[UiType-1]))
        Gui, QGui = loadUiType(UITypes[UiType-1])
        return Gui, QGui
        # '''-----------------------------------'''
    except Exception as e:
        print('ОШИБКА ЗАГРУЗКИ « .ui » ->   ', e)


def loadPyUi(pyui_path_id):
    """
    Загружает скомпилированный .py UI‑модуль и возвращает класс,
    у которого есть метод setupUi(self, MainWindow).
    """
    try:
        pyui_path = PYUITypes[pyui_path_id]
        module_name = pyui_path.replace("/", ".").rstrip(".py")
        spec = importlib.util.spec_from_file_location(module_name, pyui_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Ищем класс с setupUi
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and hasattr(obj, "setupUi"):
                return obj

        raise ValueError("В модуле не найден класс с setupUi.")
    except Exception as e:
        print(f"Ошибка загрузки UI‑класса из {pyui_path}: {e}")
        return None


