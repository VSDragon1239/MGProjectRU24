import random
from PySide6.QtGui import QIcon, QPixmap, QImage, QColor

_icon_cache = {}


def icon_with_random_hue(icon_path: str, hue_range=360) -> QIcon:
    pixmap = QPixmap(icon_path)
    image = pixmap.toImage().convertToFormat(QImage.Format_ARGB32)

    hue_shift = random.randint(0, hue_range)

    for y in range(image.height()):
        for x in range(image.width()):
            color = QColor.fromRgba(image.pixel(x, y))
            if color.alpha() == 0:
                continue

            h, s, v, a = color.getHsv()
            if h == -1:
                continue

            color.setHsv((h + hue_shift) % 360, s, v, a)
            image.setPixelColor(x, y, color)

    return QIcon(QPixmap.fromImage(image))


def cached_random_icon(path: str, key, hue_range=360) -> QIcon:
    if key not in _icon_cache:
        random.seed(key)  # 🔐 стабильный цвет для ключа
        _icon_cache[key] = icon_with_random_hue(path, hue_range)
    return _icon_cache[key]
