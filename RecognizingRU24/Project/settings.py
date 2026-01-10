import sys, os
from pathlib import Path

if getattr(sys, 'frozen', False):
    # Упакованный exe: кладём рядом с ним
    BASE_DIR = Path(sys.executable)
else:
    # Запуск из кода — папка проекта
    BASE_DIR = Path(__file__).resolve().parent

# Корневая директория проекта (если нужно выше)
PROJECT_ROOT = BASE_DIR.parent

# Модели
# SMALL_MODEL_PATH = Path(r"C:/(0)MGProjectData/4/1/1/3/2/2/2/RecognizingRU24/Models/vosk-model-small-ru-0.22")

base = getattr(sys, "_MEIPASS", os.path.dirname(__file__))
if getattr(sys, 'frozen', False):
    SMALL_MODEL_PATH = os.path.join(base, "Models", "vosk-model-small-ru-0.22")
else:
    SMALL_MODEL_PATH = "C:/1/1/3/10/PCProjects/MGSD2425/RecognizingRU24/Models/vosk-model-small-ru-0.22"

HIGH_MODEL_PATH = Path(r"C:/(0)MGProjectData/4/1/1/3/2/2/2/RecognizingRU24/Models/vosk-model-ru-0.42")

# Сервер
USE_SERVER = False
FLASK_URL = "http://127.0.0.1:5000/recognize"

# Основные настройки
SAMPLERATE = 16000
BLOCKSIZE = 8000
DTYPE = "int16"
CHANNELS = 1

COMMAND_RECORD_DURATION = 5
# сколько секунд тишины подряд считаем концом команды
SILENCE_THRESHOLD = 1.5
# минимальный уровень громкости (подбирается экспериментально)
SILENCE_LEVEL = 121

if getattr(sys, 'frozen', False):
    AUDIO_DIR = str(PROJECT_ROOT).replace('\\', '/') + '/resources/audio/'
else:
    AUDIO_DIR = str(BASE_DIR).replace('\\', '/') + '/resources/'

AUDIO_FILES = [
    'start_sound.mp3',
    'PinkiePieParty.mp3',
]

SYSTEM_VOICE_DIR = AUDIO_DIR + 'system_voice/'

SYSTEM_VOICE = [
    'mainstream_system_activated.wav',
    'mainstream_twilight_sparkle.wav',
    'mainstream_starry_dragon.wav',
    'mainstream_star_dragon.wav',
    'mainstream_starry_alicorn.wav',
    'mainstream_command_ok.wav',
    'welcome_to_system.wav',
    'pricol_v2.wav',  # Аккуратно, без цензуры!!!
    'pricol_v1.wav',  # Аккуратно, без цензуры!!!
]

COMMAND_CONFIGURATION = {
    "version": 1,
    "types": {
        "SystemWindowsManager": {
            "ApplicableWords": [["Да", "Yes"], ["Нет", "Не", "Not", "No", "Отмена"]],
            "KeyCast": [
                {
                    "phrases": ["открой проводник", "open explorer"],
                    "action": "plugins.win.keycast.open_explorer",
                    "args": {}
                },
                {
                    "phrases": ["нажми win + e", "press win e"],
                    "action": "plugins.win.keycast.press_combo",
                    "args": {"combo": ["win", "e"]}
                }
            ],
            "WinCast": [
                {
                    "phrases": ["сверни все окна", "show desktop"],
                    "action": "plugins.win.wincast.show_desktop",
                    "args": {}
                }
            ]
        },
        "ProjectManager": {
            "Projects": [
                {
                    "phrases": ["запусти проект {name}", "run project {name}"],
                    "action": "plugins.projects.run_project",
                    "args": {"name": "{name}"}
                }
            ]
        }
    }
}
