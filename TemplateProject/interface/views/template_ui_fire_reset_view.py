import os

from PySide6.QtCore import QFileSystemWatcher, QTimer, QFile
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader

from TemplateProject.interface.viewmodels.template_ui_fr_viewmodel import TemplateUiFRViewModel
from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainButtonsConnection import MainButtonsConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainSpinBoxsConnection import MainSpinBoxsConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainUpdateConnection import MainUpdateConnect
from TemplateProject.interface.views.ui_settings.connections.template_main_view.MainWidgetsConnection import MainWidgetsConnect

from TemplateProject.interface.tools.ui_initializations.initialization_ui import loadUi
from TemplateProject.interface.views.ui_settings.connections.template_ui_fire_reset_view.TemplateUiFRViewButtonConnection import \
    TemplateUiFRViewButtonsConnect
from TemplateProject.interface.views.ui_settings.connections.template_ui_fire_reset_view.TemplateUiFRViewListWidgetsConnection import \
    TemplateUiFRViewWidgetListConnect


class TemplateUiFireResetView(QMainWindow):
    model = None

    def __init__(self):
        super().__init__()

        # Загружаем UI впервые
        self.ui_path = os.path.join(os.path.dirname(__file__), "ui_files", "template_ui_fire_reset_view.ui")
        self.loader = QUiLoader()
        self._load_ui()

        # Смотрим, что вернул QUiLoader.load:
        # if isinstance(self.loaded_window, QMainWindow):
            # просто показываем загруженный QMainWindow
            # self.loaded_window.show()
            # self.loaded_window.showMaximized()
            # pass
        # else:
        #     pass
            # если вернулся QWidget, оборачиваем в наше главное окно
            # self.main_win = QMainWindow()
            # self.main_win.setCentralWidget(self.loaded_window)
            # self.main_win.show()
            # self.main_win.showMaximized()

        # 4) Создаём QFileSystemWatcher, чтобы отслеживать изменения .ui
        self.file_watcher = QFileSystemWatcher([self.ui_path], parent=self)
        self.file_watcher.fileChanged.connect(self._on_ui_file_changed)

        # Таймер, чтобы сгладить “серии” сигналов при сохранении файла
        self._reload_timer = QTimer(self)
        self._reload_timer.setInterval(300)   # 300 мс задержки
        self._reload_timer.setSingleShot(True)
        self._reload_timer.timeout.connect(self._reload_ui)

    def set_template_model(self, model):
        self.model = model

    def _load_ui(self):
        """Загружает .ui через QUiLoader и устанавливает как центральный виджет."""
        # Если уже есть предыдущий центральный виджет, удалим его
        old_central = self.centralWidget()
        if old_central is not None:
            old_central.setParent(None)
            old_central.deleteLater()
        ui_file = QFile(self.ui_path)
        ui_file.open(QFile.ReadOnly)
        # loaded = self.loader.load(ui_file)
        ui_file.close()
        # self.loaded_window = loaded

        # Открываем .ui-файл
        ui_file = QFile(self.ui_path)
        if not ui_file.open(QFile.ReadOnly):
            print(f"⚠️ Не удалось открыть UI-файл: {self.ui_path}")
            return

        # Загружаем его, потом закрываем
        loaded_widget = self.loader.load(ui_file, self)
        loaded_widget.showMaximized()
        ui_file.close()

        if loaded_widget is None:
            print("⚠️ QUiLoader вернул None. Проверьте правильность .ui-файла.")
            return

        # Устанавливаем загруженный виджет как центральный
        self.setCentralWidget(loaded_widget)

        # Сохраним ссылку, чтобы дальше работать с элементами:
        # допустим, мы хотим получить, например, кнопку с objectName="myButton":
        # self.my_button = loaded_widget.findChild(QPushButton, "myButton")

        # 4) Инициализируем viewModel и подключения с уже загруженным внутренним виджетом
        self.initViewModels(loaded_widget)
        self.buttonsConnection(loaded_widget)
        self.widgetConnections(loaded_widget)
        self.spinBoxConnections(loaded_widget)
        self.updateDataConnections(loaded_widget)

        print("✅ UI загружен из", self.ui_path)

    def _on_ui_file_changed(self, path):
        """
        Когда файл .ui поменялся, запускаем таймер перезагрузки.
        Если сигнал придёт несколько раз подряд, таймер будет каждый раз перезапускаться.
        """
        if self._reload_timer.isActive():
            self._reload_timer.stop()
        self._reload_timer.start()

    def _reload_ui(self):
        """Вызывается после короткой задержки — удаляет старый виджет и заново загружает .ui."""
        print("🔄 Обнаружены изменения в UI, перезагружаю интерфейс...")
        self._load_ui()

    def initViewModels(self, loaded_widget):
        # Создаём ViewModel, передавая ему сам загруженный виджет (чтобы он мог им управлять)
        self.viewModel = TemplateUiFRViewModel(loaded_widget, self.model)

    def buttonsConnection(self, loaded_widget):
        print("== Инициализированы connections кнопок ==")
        self.buttonConnect = TemplateUiFRViewButtonsConnect(loaded_widget, self.viewModel)
        self.buttonConnect.template_stack_button_window_view()
        self.buttonConnect.template_button_apps_list()


    def widgetConnections(self, loaded_widget):
        print("== Инициализированы connections виджетов ==")
        self.widgetListConnect = TemplateUiFRViewWidgetListConnect(loaded_widget, self.viewModel)
        self.widgetListConnect.template_list_widget_project_list()
