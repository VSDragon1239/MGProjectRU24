# rthook_vosk.py
import sys, os

# Выполнится перед импортом любого другого кода
if getattr(sys, "frozen", False):
    # sys._MEIPASS — это папка, куда PyInstaller распаковал все ваши собранные файлы
    os.add_dll_directory(sys._MEIPASS)
