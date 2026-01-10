import json
import time
import queue
import audioop
import threading
import requests
import vosk
from rapidfuzz import process, fuzz

# from RecognizingRU24.App.manager_server import runserver
from RecognizingRU24.Project.commands import COMMANDS, play_audio, play_sys_voice
from RecognizingRU24.Project.settings import SMALL_MODEL_PATH, COMMAND_RECORD_DURATION, FLASK_URL, SILENCE_LEVEL, \
    SILENCE_THRESHOLD, USE_SERVER

# Очередь для аудио данных, получаемых из микрофона
audio_queue = queue.Queue()

# Событие, сигнализирующее об обнаружении командного слова
keyword_detected = threading.Event()
keyword_detected_s = threading.Event()


def audio_callback(indata, frames, time_info, status):
    if status:
        print(status, flush=True)
    # Добавляем аудио данные в очередь
    audio_queue.put(bytes(indata))


# def send_to_flask(audio_data):
#     try:
#         response = requests.post(FLASK_URL, data=audio_data)
#         result = response.json()
#         print("Результат распознавания команды на сервере:", result)
#     except Exception as e:
#         print("Ошибка запроса к Flask:", e)


def reco_text(response):
    try:
        raw = response.text
        print("Raw text:", raw)
        data = json.loads(raw)  # преобразуем строку в dict
        if isinstance(data, str):
            # если внутри снова строка, нужно распарсить второй раз
            data = json.loads(data)
            text = data["text"]
            print("Text:", text)
            return text
    except json.JSONDecodeError as e:
        print("Ошибка при парсинге JSON:", e)


def if_error_command_listener(audio_data, player, text_data=None):
    if not text_data:
        rec = vosk.KaldiRecognizer(keyword_model, 16000)
        data = audio_data

        if rec.AcceptWaveform(data):
            result_o = json.loads(rec.Result())
            result = result_o.get("text", "").lower()
            print(str(result))

            if not result:
                print("Результат пустой.")
                return

            COMMANDS.exec_command(result)
        else:
            print('Пустота...')
    else:
        COMMANDS.exec_command(text_data)

        # if "система" in text and not is_triggered:
        #     print("Обнаружено командное слово:", text)
        #     player("audio", 0)
        #     keyword_detected.set()
        #     is_triggered = True
        # else:
        #     # Быстрый отклик с частичным результатом
        #     partial = json.loads(rec.PartialResult())
        #     partial_text = partial.get("partial", "").lower()
        #     if "система" in partial_text and not is_triggered:
        #         print("Обнаружено командное слово (partial):", partial_text)
        #         player("audio", 0)
        #         keyword_detected.set()
        #         is_triggered = True
        #
        # if keyword_detected.is_set():
        #     keyword_detected_s.clear()
        #     rec.Reset()  # сбрасываем состояние распознавания
        #     keyword_detected_s.wait()
        #     is_triggered = False  # готов снова слушать


def send_to_flask(audio_data, player):
    if USE_SERVER:
        try:
            print("Отправка данных на сервер...")
            response = requests.post(FLASK_URL, data=audio_data)
            result = reco_text(response)
            print("Результат распознавания на сервере:", result)

            if not result:
                print("Результат пустой.")
                return

            COMMANDS.exec_command(result)
            # # Попытка найти наиболее похожую команду
            # best_match, score, _ = process.extractOne(result, COMMANDS.keys(), scorer=fuzz.partial_ratio)
            # print(f"Лучшее совпадение: {best_match} ({score}%)")
            #
            # if score >= 64:  # Порог можно подстроить
            #     COMMANDS[best_match]()
            # else:
            #     print("Команда не распознана.")

        except Exception as e:
            print("Ошибка запроса к Flask:", e)
            if_error_command_listener(audio_data, player)
            # rs = input("restart server?")
            # rs = rs.lower()
            # rs = rs.replace(" ", "")
            # if rs == "y" or rs == "yes" or rs == "yeah" or rs == "yup":
            #     runserver()
    else:
        print("Анализ результата...")
        if_error_command_listener(audio_data, player)


print(str(SMALL_MODEL_PATH).replace("\\", "/"))
keyword_model = vosk.Model(SMALL_MODEL_PATH)


def keyword_listener(player):
    player("voice", 6)

    KEYWORDS = ["система", "помощник", "эй пони", "глория"]
    INSTANT_COMMANDS = {
        "открой проводник": lambda: if_error_command_listener(None, player, "открой проводник"),
        "открой мой компьютер": lambda: if_error_command_listener(None, player, "открой мой компьютер"),
        "открой документы": lambda: if_error_command_listener(None, player, "открой документы"),
        "открой загрузки": lambda: if_error_command_listener(None, player, "открой загрузки"),

        "открой рабочий стол": lambda: if_error_command_listener(None, player, "открой рабочий стол"),
        "покажи рабочий стол": lambda: if_error_command_listener(None, player, "открой рабочий стол"),
        "рабочий стол": lambda: if_error_command_listener(None, player, "открой рабочий стол"),
        "стол": lambda: if_error_command_listener(None, player, "открой рабочий стол"),

        "закрой окно": lambda: if_error_command_listener(None, player, "закрой окно"),

        "поменяй": lambda: if_error_command_listener(None, player, "альт таб"),
        "поменять": lambda: if_error_command_listener(None, player, "альт таб"),
        "помене": lambda: if_error_command_listener(None, player, "альт таб"),
        "поминай": lambda: if_error_command_listener(None, player, "альт таб"),
        "фоминой": lambda: if_error_command_listener(None, player, "альт таб"),
        "помимо и": lambda: if_error_command_listener(None, player, "альт таб"),
        "панельной": lambda: if_error_command_listener(None, player, "альт таб"),
        "каменной": lambda: if_error_command_listener(None, player, "альт таб"),
        "альт таб": lambda: if_error_command_listener(None, player, "альт таб"),
        "альта бы": lambda: if_error_command_listener(None, player, "альт таб"),
        "аль табор": lambda: if_error_command_listener(None, player, "альт таб"),
        "альт штаба": lambda: if_error_command_listener(None, player, "альт таб"),
        "ай дабз": lambda: if_error_command_listener(None, player, "альт таб"),
        "альт та бы": lambda: if_error_command_listener(None, player, "альт таб"),
        "альт тобой": lambda: if_error_command_listener(None, player, "альт таб"),
    }

    keyword_detected_s.wait()

    rec = vosk.KaldiRecognizer(keyword_model, 16000)
    is_triggered = False  # <— ключ!
    is_active_command = False
    while True:
        data = audio_queue.get()

        # Если получаем полный результат
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "").lower()
            if any(word in text for word in KEYWORDS) and not is_triggered:
                print("Обнаружено командное слово:", text)
                player("audio", 0)
                keyword_detected.set()
                is_triggered = True
        else:
            # Быстрый отклик с частичным результатом
            partial = json.loads(rec.PartialResult())
            partial_text = partial.get("partial", "").lower()
            if any(word in partial_text for word in KEYWORDS) and not is_triggered:
                print("Обнаружено командное слово (partial):", partial_text)
                player("audio", 0)
                keyword_detected.set()
                is_triggered = True

            # Прямая команда
            for phrase, action in INSTANT_COMMANDS.items():
                if partial_text:
                    print(partial_text)
                if phrase in partial_text:
                    if not is_active_command:
                        print("Выполняется прямая команда:", phrase)
                        player("audio", 1)
                        action()
                        is_active_command = True
                        break
                    else:
                        is_active_command = False
                        break

        if keyword_detected.is_set():
            keyword_detected_s.clear()
            rec.Reset()  # сбрасываем состояние распознавания
            keyword_detected_s.wait()
            is_triggered = False  # готов снова слушать


def command_recorder(player):
    """
    После обнаружения командного слова записывает аудио до тех пор,
    пока речь не закончится (тишина более N секунд), затем отправляет.
    """
    while True:
        keyword_detected.wait()
        print("Командное слово найдено! Начинается запись команды...")

        keyword_detected_s.clear()

        # очищаем очередь от лишних данных
        while not audio_queue.empty():
            try:
                audio_queue.get_nowait()
            except queue.Empty:
                break

        time.sleep(0.3)  # чтобы не откусить начало команды

        command_audio = b""
        last_voice_time = time.time()

        while True:
            try:
                data = audio_queue.get(timeout=0.5)  # ждём кусок
                command_audio += data

                # анализируем громкость
                rms = audioop.rms(data, 2)  # 16-бит PCM
                print(rms)
                if rms > SILENCE_LEVEL:
                    last_voice_time = time.time()  # обновляем, т.к. речь есть

            except queue.Empty:
                # если данных нет — просто проверим тишину
                pass

            # если тишина дольше порога → завершаем
            if time.time() - last_voice_time > SILENCE_THRESHOLD:
                break

        print("Запись команды завершена.")
        player("voice", 5)
        send_to_flask(command_audio, player)

        keyword_detected.clear()
        print("Готов к следующей команде.\n")
        keyword_detected_s.set()
