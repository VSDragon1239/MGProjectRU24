from PySide6.QtGui import QPixmap, QImage, QPainter, QPainterPath
from PySide6.QtCore import Qt, QRectF, QSize


def rounded_pixmap(source: QPixmap, size: QSize, radius: int = 20,
                   round_topleft=True, round_topright=True,
                   round_bottomleft=True, round_bottomright=True) -> QPixmap:
    scaled = source.scaled(size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    rounded = QPixmap(size)
    rounded.fill(Qt.transparent)

    path = QPainterPath()
    rect = QRectF(0, 0, size.width(), size.height())

    # Скругляем только нужные углы
    r = radius
    tl = r if round_topleft else 0
    tr = r if round_topright else 0
    br = r if round_bottomright else 0
    bl = r if round_bottomleft else 0

    path.moveTo(rect.left() + tl, rect.top())
    path.lineTo(rect.right() - tr, rect.top())
    if tr:
        path.quadTo(rect.right(), rect.top(), rect.right(), rect.top() + tr)
    path.lineTo(rect.right(), rect.bottom() - br)
    if br:
        path.quadTo(rect.right(), rect.bottom(), rect.right() - br, rect.bottom())
    path.lineTo(rect.left() + bl, rect.bottom())
    if bl:
        path.quadTo(rect.left(), rect.bottom(), rect.left(), rect.bottom() - bl)
    path.lineTo(rect.left(), rect.top() + tl)
    if tl:
        path.quadTo(rect.left(), rect.top(), rect.left() + tl, rect.top())
    path.closeSubpath()

    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setClipPath(path)
    painter.drawPixmap(0, 0, scaled)
    painter.end()

    return rounded