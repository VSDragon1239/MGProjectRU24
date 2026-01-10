# hook‑vosk.py
from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

# забираем всё, что лежит в папке vosk (JSON, DLL, модели и т.п.)
datas = collect_data_files('vosk')
# кроме того, берём все динамические библиотеки (.dll/.so/.dylib)
binaries = collect_dynamic_libs('vosk')

print('Работает?')
