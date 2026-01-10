from playsound import playsound

from RecognizingRU24.App.manager_commands import CommandManager
from RecognizingRU24.Project.settings import AUDIO_DIR, AUDIO_FILES, SYSTEM_VOICE_DIR, SYSTEM_VOICE


def play_audio(file_path_id: int):
    file_path = AUDIO_DIR + AUDIO_FILES[file_path_id]
    print(file_path)
    try:
        playsound(file_path)
    except Exception as e:
        print(f"Ошибка при воспроизведении: {e}")
        return -1


def play_sys_voice(file_path_id: int):
    file_path = SYSTEM_VOICE_DIR + SYSTEM_VOICE[file_path_id]
    try:
        playsound(file_path)
    except Exception as e:
        print(f"Ошибка при воспроизведении: {e}")


COMMANDS = CommandManager()


# # Функция, вызываемая для команды "джарвис"
# def magic_spell():
#     play_audio(1)
#     print("Magic spell activated! Executing special command...")
#
#
# # Функция, вызываемая для команды "приветствую"
# def play_sound():
#     play_audio(1)
#     print("Sound triggered! Playing greeting sound...")
#
#
# def command_list():
#     print(COMMANDS.keys())



# # Здесь добавляем команды и соответствующие функции
# COMMANDS = {
#     "активация": lambda: lessen_command('1'),
#
#     "сумеречная": twilight,
#     "твайлайт": twilight,
#
#     # "меня": get_me,
#     # "мою": get_me,
#
#     "список команд": command_list,
#     "Новая команда": func_1,
#     "Проверка": get_me,
#
#
#     "Компьютер": open_my_pc_explorer,
#     "Мой компьютер": open_my_pc_explorer,
#     "пк": open_my_pc_explorer,
#     "Мой пк": open_my_pc_explorer,
#     "Проводник": open_my_pc_explorer,
#     "Диски": open_my_pc_explorer,
#     "Место": open_my_pc_explorer,
#     "Объём занимаемой памяти места на диске дисках": open_my_pc_explorer,
#     "Объём": open_my_pc_explorer,
# }



