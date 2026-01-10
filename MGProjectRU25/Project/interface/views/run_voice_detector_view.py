from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QDialogButtonBox
)


class RunVoiceDetectorDialogView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Открыть распознавание голоса?")
        self.resize(300, 100)

        layout = QVBoxLayout(self)

        # Кнопки OK / Cancel
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            parent=self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_result(self) -> bool:
        """Возвращает True, если нажали OK, иначе False."""
        return self.exec() == QDialog.Accepted
