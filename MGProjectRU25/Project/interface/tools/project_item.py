from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QPushButton, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt


class ProjectItemWidget(QWidget):
    def __init__(self, project, viewModel, parent=None):
        super().__init__(parent)

        self.project = project
        self.viewModel = viewModel

        # self.frame = QFrame(self)
        # self.frame.setObjectName("projectItemFrame")

        # frame_layout = QHBoxLayout(self.frame)
        frame_layout = QHBoxLayout()
        frame_layout.setContentsMargins(10, 10, 10, 10)
        frame_layout.setSpacing(10)
        # self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(8, 3, 8, 3)



        def search_end_index_prefix():
            data = project["ProjectRuName"]
            prefix_data = 0
            for i, ch in enumerate(data):
                if ch == "-":
                    prefix_data = i - 2
                    break
            if prefix_data == 0:
                return "", data
            data_prefix = data[:prefix_data + 1]
            data_name = data[prefix_data + 3:]
            return data_prefix, data_name


        prefix_name, main_name = search_end_index_prefix()

        self.label = QLabel(prefix_name)
        self.label1 = QLabel(main_name)
        self.label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label.setWordWrap(True)
        self.label1.setWordWrap(True)
        self.label.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setMinimumWidth(0)
        self.label1.setMinimumWidth(0)
        # color:  # 7ffcff;
        self.label.setStyleSheet("""
                                QLabel {
                                    font-size: 18px;
                                    background-color: rgba(0, 0, 0, 0);
                                    padding: 0px;
                                }
                            """)
        self.label1.setStyleSheet("""
                                QLabel {
                                    font-size: 18px;
                                    background-color: rgba(0, 0, 0, 0);
                                    padding: 0px;
                                }
                            """)

        self.btn_up = QPushButton("▲")
        self.btn_down = QPushButton("▼")
        for btn in (self.btn_up, self.btn_down):
            btn.setCursor(Qt.PointingHandCursor)
            btn.setObjectName("gpArrow")
            btn.setStyleSheet("""
                        QPushButton {
                            font-size: 16px;
                            color: #7ffcff;
                            background-color: rgba(0, 0, 0, 0);
                            padding: 10px 0;
                        }
                    """)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.setFixedWidth(28)

        self.btn_up.clicked.connect(self.move_up)
        self.btn_down.clicked.connect(self.move_down)

        if self.label.text() != "":
            main_layout.addWidget(self.label)
        if self.label1.text() != "":
            main_layout.addWidget(self.label1)
        # main_layout.addWidget(self.frame)
        # main_layout.addStretch()
        main_layout.addWidget(self.btn_up)
        main_layout.addWidget(self.btn_down)

    def move_up(self):
        self.viewModel.move_project_up(self.project["ProjectRuName"])

    def move_down(self):
        self.viewModel.move_project_down(self.project["ProjectRuName"])
