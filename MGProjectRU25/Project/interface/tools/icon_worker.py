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
