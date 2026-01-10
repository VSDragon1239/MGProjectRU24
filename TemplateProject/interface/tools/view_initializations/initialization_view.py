

def initMainView(targetView, model, is_maximize):
    """Главный виджет"""
    return initFirstView(targetView(model), is_maximize)


def initFirstView(targetView, is_maximize):
    """Используется для отображения виджета и его на весь экран"""
    targetView.show()
    if is_maximize:
        targetView.showMaximized()
    return targetView
