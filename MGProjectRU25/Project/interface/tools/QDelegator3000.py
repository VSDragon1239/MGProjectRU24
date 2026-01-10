from PySide6.QtWidgets import QStyledItemDelegate, QListWidget, QListWidgetItem, QStyle, QStyleOptionViewItem, \
    QApplication
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPainter, QIcon



class IconOnlyDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option, index):
        # Получаем иконку из роли DecorationRole
        # 1) Подготовим опцию и очистим текст
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)
        opt.text = ""  # убираем текст, но все остальные настройки (цвета, фоны) сохраняются

        # 2) Рисуем фон (выделение, hover и т.п.)
        widget = option.widget
        style = widget.style() if widget else QApplication.style()
        style.drawControl(QStyle.CE_ItemViewItem, opt, painter, widget)

        # 3) Достаём иконку и рисуем её по центру в области
        icon = index.data(Qt.DecorationRole)
        if isinstance(icon, QIcon):
            pix = icon.pixmap(opt.decorationSize)
            # вычисляем смещение, чтобы центрировать
            x = opt.rect.x() + (opt.rect.width() - pix.width()) // 2
            y = opt.rect.y() + (opt.rect.height() - pix.height()) // 2
            painter.drawPixmap(x, y, pix)

    def sizeHint(self, option, index):
        # задаём размер «ячейки» чуть больше иконки
        base = super().sizeHint(option, index)
        return QSize(option.decorationSize.width() + 10,
                     option.decorationSize.height() + 10)