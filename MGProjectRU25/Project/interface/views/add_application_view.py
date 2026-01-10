from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QHBoxLayout, QPushButton, QFileDialog
)

from MGProjectRU25.Project.project_settings import APP_ICONS_DIR


class AddApplicationView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавление приложения")
        self.resize(600, 200)

        layout = QVBoxLayout(self)

        # ── Ввод пути к EXE ────────────────────────────────────
        exe_layout = QHBoxLayout()
        exe_layout.addWidget(QLabel("Путь к .exe:"))
        self.exe_edit = QLineEdit(self)
        exe_layout.addWidget(self.exe_edit, 1)
        btn_browse_exe = QPushButton("Обзор…", self)
        btn_browse_exe.clicked.connect(self._browse_exe)
        exe_layout.addWidget(btn_browse_exe)
        layout.addLayout(exe_layout)

        # ── Ввод пути к изображению ───────────────────────────
        img_layout = QHBoxLayout()
        img_layout.addWidget(QLabel("Путь к изображению:"))
        self.img_edit = QLineEdit(self)
        img_layout.addWidget(self.img_edit, 1)
        btn_browse_img = QPushButton("Обзор…", self)
        btn_browse_img.clicked.connect(self._browse_image)
        img_layout.addWidget(btn_browse_img)
        layout.addLayout(img_layout)

        # ── Кнопки OK / Cancel ─────────────────────────────────
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _browse_exe(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите .exe файл",
            "C://",
            filter="Executable Files (*.exe);;All Files (*)"
        )
        if path:
            self.exe_edit.setText(path)

    def _browse_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение",
            APP_ICONS_DIR,
            filter="Image Files (*.png *.jpg *.bmp *.svg);;All Files (*)"
        )
        if path:
            self.img_edit.setText(path)

    def get_paths(self):
        """
        Показывает диалог и возвращает кортеж:
        (path_to_exe: str or None, path_to_image: str or None)
        """
        if self.exec() == QDialog.Accepted:
            exe_path = self.exe_edit.text().strip() or None
            img_path = self.img_edit.text().strip() or None
            return exe_path, img_path
        return None, None
