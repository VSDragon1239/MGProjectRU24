from PySide6.QtWidgets import QPushButton, QSpacerItem, QSizePolicy, QWidget, QLabel


def createQPushButton(widget, context, isGrid=False, row=0, col=0):
    if not isGrid:
        button = QPushButton(context)
        # button.objectName(name)
        widget.layout().addWidget(button)
        return button
    else:
        button = QPushButton(context)
        widget.addWidget(button, row, col)
        return button


def setImage(id_image):
    print('Установлена иконка', id_image)


def setGrid(col, row, size):
    col += 1
    if col >= size:
        col = 0
        row += 1
        return col, row
    return col, row


def createQSpacer(widget):
    spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    widget.layout().addItem(spacer)


def createQWidget(widget):
    cWidget = QWidget()
    widget.addWidget(cWidget)


def createBackgroundQLabel(widget):
    label = QLabel(widget)
    return label
