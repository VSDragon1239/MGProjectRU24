import os
import sys
from pathlib import Path


GEN_IMAGES = False


if getattr(sys, 'frozen', False):
    # Упакованный exe: кладём рядом с ним
    BASE_DIR = Path(sys.executable)
else:
    # Запуск из кода — папка проекта
    BASE_DIR = Path(__file__).resolve().parent

# Корневая директория проекта (если нужно выше)
PROJECT_ROOT = BASE_DIR.parent  #

UI_DIR = str(BASE_DIR).replace("\\", "/") + '/interface/views/ui_files/'

UIS_DIRS = [
    "projects_manager",
    "main_window",
    "ai_calibration_view",
]

PY_UIS_DIRS = [
    "projects_manager",
    "main_window",
    "ai_calibration_view",
]

if getattr(sys, 'frozen', False):
    RESOURCES_DIR = str(PROJECT_ROOT).replace("\\", "/") + '/resources/'
    BASE_PACKAGE = "resources"
else:
    RESOURCES_DIR = str(BASE_DIR).replace("\\", "/") + '/interface/resources/'
    BASE_PACKAGE = "Project.interface.resources"


IMAGES_DIR = RESOURCES_DIR + 'img/'

APP_ICONS_DIR = RESOURCES_DIR + 'AppDataIcons/'

FONTS_DIR = RESOURCES_DIR + 'fonts/'


IMAGES_DIRS = [
    "img_vsd_1.png",
    "background_image.png",
    "background_image.gif",
    "button_image.png",
    "background_image_1.gif",
    "icon_1.png",
    "icon_2.png",
    "icon_3.png",
    "icon_4.png",
    "button_image_active.png",
    "button_image_hover.png",
    "main_icon.png",
]


JURA = FONTS_DIR + "Jura.ttf"

icon_path = os.path.join(IMAGES_DIR, IMAGES_DIRS[11])


# PLUGINS_PATH = os.path.join(RESOURCES_DIR, "plugins")
# sys.path.insert(0, PLUGINS_PATH)

# BASE_PACKAGE = "plugins"

