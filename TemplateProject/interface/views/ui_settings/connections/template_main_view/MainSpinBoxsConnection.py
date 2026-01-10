from PySide6.QtWidgets import QLineEdit, QComboBox, QHBoxLayout, QWidget

from TemplateProject.interface.viewmodels.template_viewmodel import TemplateViewModel
from TemplateProject.interface.tools.view_initializations.qt_view_elements.connectors.SpinBoxConnector import SpinBoxConnecting


class MainSpinBoxsConnect(SpinBoxConnecting):
    def __init__(self, View, ViewModel: TemplateViewModel):
        super().__init__(View, ViewModel)
        self.viewModel = ViewModel
        self.PlainTextEdit = self.ViewerPlainTextEdit.getObjectByIndex(2)
        self.widgetMap = {}

    def mainSpinBoxConnect(self):
        """Связь виджетов и viewModel"""
        widget = self.ViewerWidget.getObjectByIndex(44)
        conn_func = self.onSpinBoxValueChanged

        self.setSpinBoxChange(index=1, widget=widget, conn_func=conn_func, typeFunc="1")

    def onSpinBoxValueChanged(self, value):
        """Обработчик изменения значения QSpinBox."""
        aggregateWidget = self.ViewerWidget.getObjectByIndex(44)
        current_count = aggregateWidget.layout().count()

        # Добавляем недостающие виджеты
        if value > current_count:
            for i in range(value - current_count):
                line_edit = QLineEdit()
                index = self.ViewerLineEdit.newObject(line_edit)
                line_edit.setObjectName("QLineEdit_" + str(index))
                combo_box = QComboBox()
                indexCB = self.ViewerComboBox.newObject(combo_box)
                combo_box.setObjectName("QComboBox_" + str(indexCB))

                combo_box.setMinimumSize(100, 25)  # Минимальный размер
                combo_box.addItems(self.viewModel.getCIDRArray())  # Пример значений для CIDR

                # Привязка сигнала textChanged к методу ViewModel
                line_edit.textChanged.connect(
                    lambda text, name=line_edit.objectName(): self.createLineEditUpdateCallback('line_edit', text, name)
                )
                combo_box.currentTextChanged.connect(
                    lambda text, name=combo_box.objectName(): self.createLineEditUpdateCallback('combo_box', text, name)
                )

                print('kkk', str(index))
                self.widgetMap[str(index)] = {'line_edit': line_edit, 'combo_box': combo_box}

                horizontal_layout = QHBoxLayout()
                horizontal_layout.addWidget(line_edit)
                horizontal_layout.addWidget(combo_box)

                container = QWidget()
                container.setLayout(horizontal_layout)
                aggregateWidget.layout().addWidget(container)

        # Убираем лишние виджеты
        elif value < current_count:
            for i in range(current_count - value):
                self.deleteLastWidget(aggregateWidget)

    def createLineEditUpdateCallback(self, type_widget, text, name):
        """Создает callback для обновления ViewModel и QPlainTextEdit."""
        print(f"value: {text}, name: {name}")

        # Обновляем данные в ViewModel
        self.viewModel.updateLineEditData(self.widgetMap, type_widget, name, text)

    def deleteLastWidget(self, aggregateWidget):
        """Удаляет последний виджет из указанного контейнера."""
        layout = aggregateWidget.layout()
        if layout.count() > 0:
            child = layout.takeAt(layout.count() - 1)
            if child.widget():
                widget_to_remove = child.widget()
                # Если это контейнер с QLineEdit, удаляем его из ViewModel
                for line_edit in widget_to_remove.findChildren(QLineEdit):
                    self.deleteLineEditByName(line_edit.objectName())
                widget_to_remove.deleteLater()
                # Найти и удалить из widgetMap
                for index, widgets in list(self.widgetMap.items()):
                    if widgets['line_edit'] in widget_to_remove.findChildren(QLineEdit):
                        del self.widgetMap[index]
                        break

                widget_to_remove.deleteLater()

    def deleteLineEditByName(self, name):
        """Удаляет данные QLineEdit из ViewModel и объектов."""
        if name in self.viewModel.lineEditData:
            del self.viewModel.lineEditData[name]
            print(f"Удалено значение: {name}")

        # Удаляем из ViewerLineEdit
        key_to_remove = None
        for key, value in self.ViewerLineEdit.objectsArray.items():
            if value.objectName() == name:
                key_to_remove = key
                break

        if key_to_remove:
            del self.ViewerLineEdit.objectsArray[key_to_remove]
            print(f"Удален объект: {name}, индекс: {key_to_remove}")
