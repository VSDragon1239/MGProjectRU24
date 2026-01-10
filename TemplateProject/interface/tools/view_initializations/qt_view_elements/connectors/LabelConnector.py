from PySide6.QtCore import QSize
from PySide6.QtGui import QImage, QPixmap, QMovie

from TemplateProject.interface.tools.round_image import rounded_pixmap
from TemplateProject.interface.tools.view_initializations.qt_view_elements.creates.CreateElements import \
    createBackgroundQLabel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Buttons import ViewerButtons
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Label import ViewerLabel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.ListWidget import ViewerListWidget
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.StackWidgets import \
    ViewerStackWidgets
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.TextEdit import ViewerTextEdit
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.Widgets import ViewerWidgets
from TemplateProject.interface.tools.view_initializations.qt_view_elements.viewers.SpinBoxs import ViewerSpinBox


class LabelsConnecting:
    view = None
    viewModel = None
    ViewerButtons = None
    ViewerStackWidgets = None
    ViewerTextEdit = None
    ViewerListWidget = None
    ViewerWidget = None
    ViewerSpinBox = None
    ViewerLabel = None

    def __init__(self, View, ViewModel):
        self.initViewViewModel(View, ViewModel)
        self.initViewers()

    def initViewViewModel(self, View, ViewModel):
        self.view = View
        self.viewModel = ViewModel

    def initViewers(self):
        self.ViewerButtons = ViewerButtons(self.view, self.viewModel)
        self.ViewerStackWidgets = ViewerStackWidgets(self.view, self.viewModel)
        self.ViewerTextEdit = ViewerTextEdit(self.view, self.viewModel)
        self.ViewerListWidget = ViewerListWidget(self.view, self.viewModel)
        self.ViewerSpinBox = ViewerSpinBox(self.view, self.viewModel)
        self.ViewerWidget = ViewerWidgets(self.view, self.viewModel)
        self.ViewerLabel = ViewerLabel(self.view, self.viewModel)

    def setLabelImage(self, label_index, image_dir: str, size: list = None):
        label = self.ViewerLabel.objectsArray[f'QLabel{label_index}']
        image = QImage(image_dir)
        pixmap = QPixmap.fromImage(image)
        if not pixmap.isNull():
            if size:
                rounded = rounded_pixmap(pixmap, QSize(*size), radius=64,
                                         round_topleft=True,
                                         round_topright=False,
                                         round_bottomleft=False,
                                         round_bottomright=True)
                label.setPixmap(rounded)
                label.setFixedSize(*size)
            else:
                label.setPixmap(pixmap)
        else:
            print("⚠️ Изображение не загружено!", image_dir)

    def setBackgroundImage(self, image_dir: str):
        label_index = self.createLabel(self.view, "background_label")
        label = self.ViewerLabel.objectsArray[f'QLabel{label_index}']

        image = QImage(image_dir)
        pixmap = QPixmap.fromImage(image)
        if not pixmap.isNull():
            label.setPixmap(pixmap)
            label.lower()
            label.setScaledContents(True)
            label.setFixedSize(1920, 1080)

    def setBackgroundGif(self, image_dir: str):
        label_index = self.createLabel(self.view, "background_label_gif")
        label = self.ViewerLabel.objectsArray[f'QLabel{label_index}']

        self.movie = QMovie(image_dir)
        label.setMovie(self.movie)
        label.lower()
        label.setScaledContents(True)
        label.setFixedSize(1920, 1080)
        self.movie.start()
        print("Valid:", self.movie.isValid(),
              "Frames:", self.movie.frameCount(),
              "Format:", self.movie.format())


    def createLabel(self, widget, name):
        """Возвращает индекс созданного текста"""
        cLabel = createBackgroundQLabel(widget)
        cLabel.setObjectName(name)
        return self.ViewerLabel.newLabel(cLabel)

