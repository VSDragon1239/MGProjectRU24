from PySide6.QtCore import QObject, QThread, Signal, Slot
from PySide6.QtGui import QImage, QIcon, QPixmap
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QImage, QColor
import random


class IconHueWorker(QObject):
    finished = Signal(object, QImage)

    @Slot(str, object)
    def process(self, icon_path, key):
        random.seed(key)

        image = QImage(icon_path).convertToFormat(QImage.Format_ARGB32)

        hue_shift = random.randint(0, 360)

        for y in range(image.height()):
            for x in range(image.width()):
                c = QColor.fromRgba(image.pixel(x, y))
                if c.alpha() == 0:
                    continue
                h, s, v, a = c.getHsv()
                if h == -1:
                    continue
                c.setHsv((h + hue_shift) % 360, s, v, a)
                image.setPixelColor(x, y, c)

        self.finished.emit(key, image)


class IconManager(QObject):
    request = Signal(str, object)  # icon_path, key
    icon_ready = Signal(object, QIcon)

    def __init__(self):
        super().__init__()

        self._cache = {}

        self.thread = QThread()
        self.worker = IconHueWorker()
        self.worker.moveToThread(self.thread)

        # 🔑 СВЯЗЬ ПОТОКОВ
        self.request.connect(self.worker.process)
        self.worker.finished.connect(self._on_finished)

        self.thread.start()

    def request_icon(self, icon_path, key):
        if key in self._cache:
            self.icon_ready.emit(key, self._cache[key])
            return

        # 🔥 ВАЖНО: emit, а не вызов
        self.request.emit(icon_path, key)

    def _on_finished(self, key, image):
        icon = QIcon(QPixmap.fromImage(image))
        self._cache[key] = icon
        self.icon_ready.emit(key, icon)
