import builtins
import sys

from PySide6.QtCore import QThread, QObject, Signal, Qt, QUrl
from PySide6.QtGui import QTextCursor
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit
from pathlib import Path

from MGProjectRU25.Project.interface.viewmodels.ai_vm import RecognizingViewModel
from TemplateProject.interface.tools.ui_initializations.initialization_ui import loadUi, loadPyUi

from RecognizingRU24.Project.settings import SAMPLERATE, BLOCKSIZE, DTYPE, CHANNELS, AUDIO_DIR, SYSTEM_VOICE_DIR, \
    SYSTEM_VOICE, AUDIO_FILES
import threading
import sounddevice as sd
from RecognizingRU24.App.manager_audio import (
    audio_callback, keyword_listener, command_recorder, keyword_detected_s
)

from MGProjectRU25.Project.interface.views.ui_files.ai_calibration_view import Ui_QMainViewWindow

#
# class EmittingStream(QObject):
#     """Псевдо‐файл, в который можно писать через print(),
#     а он будет эмитить сигнал с текстом."""
#     textWritten = Signal(str)
#
#     def write(self, text):
#         # Qt-сигналы потокобезопасны: можно эмитить из любого потока
#         self.textWritten.emit(str(text))
#
#     def flush(self):
#         pass  # для совместимости с file‐like интерфейсом
#
#


class AudioWorker(QThread):
    """Фоновый QThread для аудио-цикла."""
    error = Signal(str)
    player = None

    def run(self):
        try:
            with sd.RawInputStream(
                samplerate=SAMPLERATE,
                blocksize=BLOCKSIZE,
                dtype=DTYPE,
                channels=CHANNELS,
                callback=audio_callback
            ):
                print("Прослушивание…")
                threading.Thread(target=keyword_listener, args=(self.player,), daemon=True).start()
                threading.Thread(target=command_recorder, args=(self.player,), daemon=True).start()
                keyword_detected_s.set()

                # Цикл удержания: поток живёт, пока слушаем
                while not self.isInterruptionRequested():
                    self.msleep(200)
        except Exception as e:
            self.error.emit(str(e))


class PrintInterceptor(QObject):
    textReady = Signal(str)

    def __init__(self):
        super().__init__()
        # Сохраним оригинал для дальнейшего вызова
        self._orig_print = builtins.print
        # Подмена print
        builtins.print = self._print

    def _print(self, *args, sep=' ', end='\n', file=None, flush=False):
        text = sep.join(str(a) for a in args)
        # Эмитим сигнал (он будет доставлен в GUI‑потоке)
        self.textReady.emit(text)
        # И дублируем в консоль
        return self._orig_print(*args, sep=sep, end=end, file=file, flush=flush)


class AICalibrationUiView(QMainWindow, Ui_QMainViewWindow):
    model = None
    viewModel = None
    buttonConnect = None
    widgetListConnect = None
    audio_worker = None

    def __init__(self, parent_view, model):
        super().__init__()
        self.setupUi(self)

        # Находим PTE
        self.log_output: QPlainTextEdit = parent_view.findChild(
            QPlainTextEdit, "PTE1121_assistentAI"
        )

        # Интерцептор print()
        self._pi = PrintInterceptor()
        # Подписываемся — слот вызовется **в GUI‑потоке**
        self._pi.textReady.connect(self._append_log)

        # Дальше остальной init
        self.InitAP()
        self.set_model(model)
        self.init_local_voice_manager()
        self.audio_worker.player = self.play_audio

    def set_model(self, model):
        self.model = model
        self.initViewModels()

    def initViewModels(self):
        self.viewModel = RecognizingViewModel(self, self.model)

    def init_local_voice_manager(self):
        self.audio_worker = AudioWorker(self)
        self.audio_worker.error.connect(self.onAudioError)
        self.audio_worker.start()

    def onAudioError(self, msg):
        print("Ошибка аудио:", msg)

    def _append_log(self, text: str):
        # print('textssss')
        self.log_output.appendPlainText(text)
        self.log_output.moveCursor(QTextCursor.End)

    def InitAP(self):
        self.AudioPlayer = AudioPlayer(self)

    def play_audio(self, audio_type, file_path_id: int):
        if audio_type == "audio":
            self.AudioPlayer.play_audio(file_path_id)
        elif audio_type == "voice":
            self.AudioPlayer.play_voice(file_path_id)


class AudioPlayer(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._player = QMediaPlayer(self)
        self._audio_output = QAudioOutput(self)
        self._player.setAudioOutput(self._audio_output)

    def play_audio(self, file_path_id: int, volume: float = 0.8):
        """
        :param filename: имя файла относительно папки resources/audio
        :param volume: громкость от 0.0 до 1.0
        """
        file_path = Path(AUDIO_DIR + AUDIO_FILES[file_path_id])
        if not file_path.exists():
            raise FileNotFoundError(f"Файл аудио не найден: {file_path}")

        # 2) создаём URL и проигрываем
        url = QUrl.fromLocalFile(str(file_path))
        self._player.setSource(url)
        self._audio_output.setVolume(volume)
        self._player.play()

    def play_voice(self, file_path_id: int, volume: float = 0.8):
        file_path = Path(SYSTEM_VOICE_DIR + SYSTEM_VOICE[file_path_id])
        if not file_path.exists():
            raise FileNotFoundError(f"Файл аудио не найден: {file_path}")

        # 2) создаём URL и проигрываем
        url = QUrl.fromLocalFile(str(file_path))
        self._player.setSource(url)
        self._audio_output.setVolume(volume)
        self._player.play()

    # def init_local_voice_manager(self):
    #     """Запускает аудиопоток и рабочие потоки в фоне."""
    #     pass
        # def audio_loop():
        #     with sd.RawInputStream(
        #         samplerate=SAMPLERATE,
        #         blocksize=BLOCKSIZE,
        #         dtype=DTYPE,
        #         channels=CHANNELS,
        #         callback=audio_callback
        #     ):
        #         print("Прослушивание... Говорите, и не забудьте ключевое слово!")
        #         # Запускаем listener и recorder
        #         threading.Thread(target=keyword_listener, daemon=True).start()
        #         threading.Thread(target=command_recorder, daemon=True).start()
        #         keyword_detected_s.set()
        #         # Ждём сигнала остановки внутри потоков,
        #         # или просто оставляем цикл открытым пока окно открыто:
        #         while True:
        #             if not self.isVisible():
        #                 break
        #
        # # Запускаем аудиопоток в демоне, чтобы не блокировать GUI
        # threading.Thread(target=audio_loop, daemon=True).start()
