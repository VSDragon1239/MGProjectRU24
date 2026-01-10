import threading
import sounddevice as sd

# from RecognizingRU24.App.manager_server import runserver

from RecognizingRU24.App.manager_audio import audio_callback, keyword_listener, command_recorder, \
    keyword_detected_s
from RecognizingRU24.Project.settings import (PROJECT_ROOT, BASE_DIR,
                                              SAMPLERATE, BLOCKSIZE, DTYPE, CHANNELS)

if __name__ == '__main__':
    print(PROJECT_ROOT, BASE_DIR)

    # rs = input("run server?")
    # if rs == 'y' or rs == 'Y' or rs == 'Yes' or rs == 'yes' or rs == 'YES':
    #     runserver()

    with sd.RawInputStream(samplerate=SAMPLERATE, blocksize=BLOCKSIZE, dtype=DTYPE,
                           channels=CHANNELS, callback=audio_callback):
        print("Прослушивание... Говорите, и не забудьте командное слово!")
        # Запуск потоков для обнаружения ключевого слова и записи команды
        threading.Thread(target=keyword_listener, daemon=True).start()
        threading.Thread(target=command_recorder, daemon=True).start()
        keyword_detected_s.set()
        input("Нажмите Enter для завершения...\n")
