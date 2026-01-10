from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox
)


class ProjectDialogView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Новый проект")
        self.resize(300, 100)

        layout = QVBoxLayout(self)

        # Метка и поле ввода
        layout.addWidget(QLabel("Введите название проекта:"))
        self.name_edit = QLineEdit(self)
        layout.addWidget(self.name_edit)

        # Кнопки OK / Cancel
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            parent=self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_name(self):
        """Возвращает введённое имя (или None)."""
        if self.exec() == QDialog.Accepted:
            text = self.name_edit.text().strip()
            return text or None
        return None
