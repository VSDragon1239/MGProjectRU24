from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QPushButton, QFrame
)
from PySide6.QtCore import Qt


class GlobalProjectItemWidget(QWidget):
    def __init__(self, project, viewModel, parent=None):
        super().__init__(parent)

        self.project = project
        self.viewModel = viewModel

        self.frame = QFrame(self)
        self.frame.setObjectName("gpItemFrame")

        frame_layout = QHBoxLayout(self.frame)
        frame_layout.setContentsMargins(14, 10, 14, 10)
        frame_layout.setSpacing(12)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 4, 0, 4)
        main_layout.addWidget(self.frame)

        self.label = QLabel(project["GlobalProjectRuName"])
        self.label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label.setStyleSheet("""
            QLabel {
                color: #7ffcff;
                font-size: 26px;
                font-weight: 500;
                padding: 5px;
            }
        """)

        self.btn_up = QPushButton("▲")
        self.btn_down = QPushButton("▼")
        for btn in (self.btn_up, self.btn_down):
            btn.setFixedSize(32, 48)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setObjectName("gpArrow")
            # color: #7ffcff;
            btn.setStyleSheet("""
                        QPushButton {
                            font-size: 16px;
                        }
                    """)


        self.btn_up.clicked.connect(self.move_up)
        self.btn_down.clicked.connect(self.move_down)

        main_layout.addWidget(self.label)
        # main_layout.addStretch()
        main_layout.addWidget(self.btn_up)
        main_layout.addWidget(self.btn_down)

    def move_up(self):
        self.viewModel.move_global_project_up(self.project["GlobalProjectRuName"])

    def move_down(self):
        self.viewModel.move_global_project_down(self.project["GlobalProjectRuName"])
