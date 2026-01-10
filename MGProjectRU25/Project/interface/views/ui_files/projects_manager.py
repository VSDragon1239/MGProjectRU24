# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projects_manager.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_QMainViewWindow(object):
    def setupUi(self, QMainViewWindow):
        if not QMainViewWindow.objectName():
            QMainViewWindow.setObjectName(u"QMainViewWindow")
        QMainViewWindow.resize(1843, 841)
        QMainViewWindow.setStyleSheet(u"QWidget {  \n"
"    border: 1px solid rgb(0, 100, 100);\n"
"    border-radius: 3px;  \n"
"    padding: 3px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 layout */  \n"
"	background-color: rgb(10, 20, 30);\n"
"	font-family: 'Jura', sans-serif;  \n"
"	font-size: 18px;\n"
"	font-weight: bold;\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}  \n"
"QListWidget {\n"
"	font-size: 12px;\n"
"}\n"
"  \n"
"QLabel {  \n"
"    border: 1px solid rgb(0, 100, 100);;; /* \u0426\u0432\u0435\u0442 \u0438 \u0442\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0430\u043c\u043a\u0438 */  \n"
"    border-radius: 3px; /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */  \n"
"    padding: 3px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 layout */  \n"
"    color: #2A9DF4; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"}\n"
"\n"
"QPushButt"
                        "on {\n"
"	border-radius: 7px; /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */  \n"
"    padding: 7px 5px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */ \n"
"    font-size: 16px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */ \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430"
                        "\u0442\u0438\u0438 */  \n"
"}\n"
"\n"
"QListWidget {\n"
"    border: 1px solid rgb(0, 100, 100);\n"
"    border-radius: 3px;\n"
"    padding: 3px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 */\n"
"    background-color: rgb(20, 30, 40);\n"
"    font-family: 'Jura', sans-serif;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    color: rgb(100, 200, 200);\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 5px 8px;              /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"    margin: 2px 0;                 /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c\u0438 */\n"
"    border-radius: 3px;            /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432"
                        " \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"	background-color: rgb(10, 80, 100);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color:  rgb(20, 100, 120);  /* \u041f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: rgb(220, 240, 240);\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(0, 60, 80); /* \u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 */\n"
"    color: rgb(220, 240, 240);\n"
"}\n"
"\n"
"QListWidget::item:focus,\n"
"QListWidget::item:selected:focus {\n"
"    border: none;\n"
"    outline: none;    /* \u043d\u0430 \u0441\u043b\u0443\u0447\u0430\u0439, \u0435\u0441\u043b\u0438 \u0441\u0442\u0438\u043b\u044c \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442 outline */\n"
"}\n"
"\n"
"QListWidget {\n"
"    outline: 0;\n"
"}")
        self.centralwidget = QWidget(QMainViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {  \n"
"	font-size: 24px;\n"
"}  ")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.QW11111 = QWidget(self.widget)
        self.QW11111.setObjectName(u"QW11111")
        self.QW11111.setStyleSheet(u"QWidget {\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.QW11111)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.QHBL111111 = QHBoxLayout()
        self.QHBL111111.setObjectName(u"QHBL111111")
        self.BTN1111111 = QPushButton(self.QW11111)
        self.BTN1111111.setObjectName(u"BTN1111111")
        font = QFont()
        font.setFamilies([u"Jura"])
        font.setBold(True)
        self.BTN1111111.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111111)

        self.BTN1111112 = QPushButton(self.QW11111)
        self.BTN1111112.setObjectName(u"BTN1111112")
        self.BTN1111112.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111112)

        self.BTN1111113 = QPushButton(self.QW11111)
        self.BTN1111113.setObjectName(u"BTN1111113")
        self.BTN1111113.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111113)

        self.BTN1111114 = QPushButton(self.QW11111)
        self.BTN1111114.setObjectName(u"BTN1111114")
        self.BTN1111114.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111114)


        self.verticalLayout_7.addLayout(self.QHBL111111)


        self.verticalLayout_6.addWidget(self.QW11111)

        self.SW1111 = QStackedWidget(self.widget)
        self.SW1111.setObjectName(u"SW1111")
        self.SW1111.setStyleSheet(u"border: 0px;")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_3 = QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.QW111112 = QWidget(self.page_3)
        self.QW111112.setObjectName(u"QW111112")
        self.QW111112.setMinimumSize(QSize(450, 0))
        self.QW111112.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_25 = QVBoxLayout(self.QW111112)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.QL1111121 = QLabel(self.QW111112)
        self.QL1111121.setObjectName(u"QL1111121")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QL1111121.sizePolicy().hasHeightForWidth())
        self.QL1111121.setSizePolicy(sizePolicy)
        self.QL1111121.setFont(font)
        self.QL1111121.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.QL1111121)

        self.BTN1111121 = QPushButton(self.QW111112)
        self.BTN1111121.setObjectName(u"BTN1111121")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BTN1111121.sizePolicy().hasHeightForWidth())
        self.BTN1111121.setSizePolicy(sizePolicy1)
        self.BTN1111121.setFont(font)

        self.verticalLayout_25.addWidget(self.BTN1111121)

        self.BTN1111122 = QPushButton(self.QW111112)
        self.BTN1111122.setObjectName(u"BTN1111122")
        sizePolicy1.setHeightForWidth(self.BTN1111122.sizePolicy().hasHeightForWidth())
        self.BTN1111122.setSizePolicy(sizePolicy1)
        self.BTN1111122.setFont(font)
        self.BTN1111122.setIconSize(QSize(32, 32))

        self.verticalLayout_25.addWidget(self.BTN1111122)

        self.BTN1111123 = QPushButton(self.QW111112)
        self.BTN1111123.setObjectName(u"BTN1111123")
        sizePolicy1.setHeightForWidth(self.BTN1111123.sizePolicy().hasHeightForWidth())
        self.BTN1111123.setSizePolicy(sizePolicy1)
        self.BTN1111123.setFont(font)

        self.verticalLayout_25.addWidget(self.BTN1111123)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_8)

        self.BTN1111124 = QPushButton(self.QW111112)
        self.BTN1111124.setObjectName(u"BTN1111124")
        sizePolicy1.setHeightForWidth(self.BTN1111124.sizePolicy().hasHeightForWidth())
        self.BTN1111124.setSizePolicy(sizePolicy1)
        self.BTN1111124.setFont(font)

        self.verticalLayout_25.addWidget(self.BTN1111124)


        self.horizontalLayout_3.addWidget(self.QW111112)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.QW111111 = QWidget(self.page_3)
        self.QW111111.setObjectName(u"QW111111")
        self.QW111111.setMinimumSize(QSize(500, 0))
        self.QW111111.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.QW111111)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.QL1111111 = QLabel(self.QW111111)
        self.QL1111111.setObjectName(u"QL1111111")
        sizePolicy.setHeightForWidth(self.QL1111111.sizePolicy().hasHeightForWidth())
        self.QL1111111.setSizePolicy(sizePolicy)
        self.QL1111111.setFont(font)
        self.QL1111111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.QL1111111)

        self.BTN111111 = QPushButton(self.QW111111)
        self.BTN111111.setObjectName(u"BTN111111")
        sizePolicy1.setHeightForWidth(self.BTN111111.sizePolicy().hasHeightForWidth())
        self.BTN111111.setSizePolicy(sizePolicy1)
        self.BTN111111.setFont(font)

        self.verticalLayout_8.addWidget(self.BTN111111)

        self.BTN111112 = QPushButton(self.QW111111)
        self.BTN111112.setObjectName(u"BTN111112")
        sizePolicy1.setHeightForWidth(self.BTN111112.sizePolicy().hasHeightForWidth())
        self.BTN111112.setSizePolicy(sizePolicy1)
        self.BTN111112.setFont(font)
        self.BTN111112.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.BTN111112)

        self.BTN111113 = QPushButton(self.QW111111)
        self.BTN111113.setObjectName(u"BTN111113")
        sizePolicy1.setHeightForWidth(self.BTN111113.sizePolicy().hasHeightForWidth())
        self.BTN111113.setSizePolicy(sizePolicy1)
        self.BTN111113.setFont(font)

        self.verticalLayout_8.addWidget(self.BTN111113)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.BTN111114 = QPushButton(self.QW111111)
        self.BTN111114.setObjectName(u"BTN111114")
        sizePolicy1.setHeightForWidth(self.BTN111114.sizePolicy().hasHeightForWidth())
        self.BTN111114.setSizePolicy(sizePolicy1)
        self.BTN111114.setFont(font)

        self.verticalLayout_8.addWidget(self.BTN111114)


        self.horizontalLayout_3.addWidget(self.QW111111)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.QW111113 = QWidget(self.page_3)
        self.QW111113.setObjectName(u"QW111113")
        self.QW111113.setMinimumSize(QSize(450, 0))
        self.QW111113.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_26 = QVBoxLayout(self.QW111113)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.QL1111131 = QLabel(self.QW111113)
        self.QL1111131.setObjectName(u"QL1111131")
        sizePolicy.setHeightForWidth(self.QL1111131.sizePolicy().hasHeightForWidth())
        self.QL1111131.setSizePolicy(sizePolicy)
        self.QL1111131.setFont(font)
        self.QL1111131.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.QL1111131)

        self.BTN1111131 = QPushButton(self.QW111113)
        self.BTN1111131.setObjectName(u"BTN1111131")
        sizePolicy1.setHeightForWidth(self.BTN1111131.sizePolicy().hasHeightForWidth())
        self.BTN1111131.setSizePolicy(sizePolicy1)
        self.BTN1111131.setFont(font)

        self.verticalLayout_26.addWidget(self.BTN1111131)

        self.BTN1111132 = QPushButton(self.QW111113)
        self.BTN1111132.setObjectName(u"BTN1111132")
        sizePolicy1.setHeightForWidth(self.BTN1111132.sizePolicy().hasHeightForWidth())
        self.BTN1111132.setSizePolicy(sizePolicy1)
        self.BTN1111132.setFont(font)
        self.BTN1111132.setIconSize(QSize(32, 32))

        self.verticalLayout_26.addWidget(self.BTN1111132)

        self.BTN1111133 = QPushButton(self.QW111113)
        self.BTN1111133.setObjectName(u"BTN1111133")
        sizePolicy1.setHeightForWidth(self.BTN1111133.sizePolicy().hasHeightForWidth())
        self.BTN1111133.setSizePolicy(sizePolicy1)
        self.BTN1111133.setFont(font)

        self.verticalLayout_26.addWidget(self.BTN1111133)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_10)

        self.BTN1111134 = QPushButton(self.QW111113)
        self.BTN1111134.setObjectName(u"BTN1111134")
        sizePolicy1.setHeightForWidth(self.BTN1111134.sizePolicy().hasHeightForWidth())
        self.BTN1111134.setSizePolicy(sizePolicy1)
        self.BTN1111134.setFont(font)

        self.verticalLayout_26.addWidget(self.BTN1111134)


        self.horizontalLayout_3.addWidget(self.QW111113)

        self.SW1111.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_5 = QHBoxLayout(self.page_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.QW111121 = QWidget(self.page_4)
        self.QW111121.setObjectName(u"QW111121")
        self.QW111121.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.QW111121)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.QLB1111211 = QHBoxLayout()
        self.QLB1111211.setObjectName(u"QLB1111211")
        self.QW11112111 = QWidget(self.QW111121)
        self.QW11112111.setObjectName(u"QW11112111")
        self.QW11112111.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.QW11112111)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.QL111121111 = QLabel(self.QW11112111)
        self.QL111121111.setObjectName(u"QL111121111")
        self.QL111121111.setFont(font)
        self.QL111121111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.QL111121111)

        self.BTN111121111 = QPushButton(self.QW11112111)
        self.BTN111121111.setObjectName(u"BTN111121111")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BTN111121111.sizePolicy().hasHeightForWidth())
        self.BTN111121111.setSizePolicy(sizePolicy2)
        self.BTN111121111.setMinimumSize(QSize(333, 0))
        self.BTN111121111.setFont(font)
        self.BTN111121111.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.BTN111121111)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.BTN111121133 = QPushButton(self.QW11112111)
        self.BTN111121133.setObjectName(u"BTN111121133")
        sizePolicy2.setHeightForWidth(self.BTN111121133.sizePolicy().hasHeightForWidth())
        self.BTN111121133.setSizePolicy(sizePolicy2)
        self.BTN111121133.setFont(font)
        self.BTN111121133.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.BTN111121133)

        self.BTN111121134 = QPushButton(self.QW11112111)
        self.BTN111121134.setObjectName(u"BTN111121134")
        sizePolicy2.setHeightForWidth(self.BTN111121134.sizePolicy().hasHeightForWidth())
        self.BTN111121134.setSizePolicy(sizePolicy2)
        self.BTN111121134.setFont(font)
        self.BTN111121134.setIconSize(QSize(32, 32))

        self.verticalLayout_10.addWidget(self.BTN111121134)


        self.QLB1111211.addWidget(self.QW11112111)

        self.QW11112112 = QWidget(self.QW111121)
        self.QW11112112.setObjectName(u"QW11112112")
        self.QW11112112.setMinimumSize(QSize(700, 0))
        self.QW11112112.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.QW11112112)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.QL111121121 = QLabel(self.QW11112112)
        self.QL111121121.setObjectName(u"QL111121121")
        self.QL111121121.setFont(font)
        self.QL111121121.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.QL111121121)

        self.tW111121121 = QTabWidget(self.QW11112112)
        self.tW111121121.setObjectName(u"tW111121121")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_18 = QVBoxLayout(self.tab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.QW11112112111 = QWidget(self.tab)
        self.QW11112112111.setObjectName(u"QW11112112111")
        self.verticalLayout_24 = QVBoxLayout(self.QW11112112111)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.sA111121121111 = QScrollArea(self.QW11112112111)
        self.sA111121121111.setObjectName(u"sA111121121111")
        self.sA111121121111.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 36, 16))
        self.sA111121121111.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_24.addWidget(self.sA111121121111)


        self.verticalLayout_18.addWidget(self.QW11112112111)

        self.tW111121121.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tW111121121.addTab(self.tab_2, "")

        self.verticalLayout_19.addWidget(self.tW111121121)


        self.QLB1111211.addWidget(self.QW11112112)

        self.QW11112113 = QWidget(self.QW111121)
        self.QW11112113.setObjectName(u"QW11112113")
        self.QW11112113.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.QW11112113)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_7 = QLabel(self.QW11112113)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_7)

        self.comboBox_9 = QComboBox(self.QW11112113)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.verticalLayout_22.addWidget(self.comboBox_9)

        self.comboBox_10 = QComboBox(self.QW11112113)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.verticalLayout_22.addWidget(self.comboBox_10)

        self.lineEdit_5 = QLineEdit(self.QW11112113)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_22.addWidget(self.lineEdit_5)

        self.QSATOF111121131 = QScrollArea(self.QW11112113)
        self.QSATOF111121131.setObjectName(u"QSATOF111121131")
        self.QSATOF111121131.setWidgetResizable(True)
        self.SAWTOF1111211311 = QWidget()
        self.SAWTOF1111211311.setObjectName(u"SAWTOF1111211311")
        self.SAWTOF1111211311.setGeometry(QRect(0, 0, 20, 20))
        self.verticalLayout_23 = QVBoxLayout(self.SAWTOF1111211311)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.SAWTOFL11112113111 = QVBoxLayout()
        self.SAWTOFL11112113111.setObjectName(u"SAWTOFL11112113111")

        self.verticalLayout_23.addLayout(self.SAWTOFL11112113111)

        self.QSATOF111121131.setWidget(self.SAWTOF1111211311)

        self.verticalLayout_22.addWidget(self.QSATOF111121131)

        self.BTN111121112 = QPushButton(self.QW11112113)
        self.BTN111121112.setObjectName(u"BTN111121112")
        sizePolicy2.setHeightForWidth(self.BTN111121112.sizePolicy().hasHeightForWidth())
        self.BTN111121112.setSizePolicy(sizePolicy2)
        self.BTN111121112.setMinimumSize(QSize(333, 0))
        self.BTN111121112.setFont(font)

        self.verticalLayout_22.addWidget(self.BTN111121112)

        self.BTN111121113 = QPushButton(self.QW11112113)
        self.BTN111121113.setObjectName(u"BTN111121113")
        sizePolicy2.setHeightForWidth(self.BTN111121113.sizePolicy().hasHeightForWidth())
        self.BTN111121113.setSizePolicy(sizePolicy2)
        self.BTN111121113.setMinimumSize(QSize(333, 0))
        self.BTN111121113.setFont(font)

        self.verticalLayout_22.addWidget(self.BTN111121113)


        self.QLB1111211.addWidget(self.QW11112113)


        self.verticalLayout_9.addLayout(self.QLB1111211)


        self.horizontalLayout_5.addWidget(self.QW111121)

        self.SW1111.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_6 = QHBoxLayout(self.page_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.QW111131 = QWidget(self.page_5)
        self.QW111131.setObjectName(u"QW111131")
        self.QW111131.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"/* \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0441\u0442\u0438\u043b\u044c \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"QCommandLinkButton {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421"
                        "\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QCommandLinkButton:hover {\n"
"    background-color: rgb(0, 100, 100);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QCommandLinkButton:active {\n"
"    background-color: rgb(0, 100, 100);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QCommandLinkButton:visited {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QCommandLinkButton:pressed {\n"
"    background-color: rgb(0, 50, 50);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"QCommandLinkButton:disabled {\n"
"    background-color: rgb(0, 150, 120);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043a\u043d\u043e"
                        "\u043f\u043a\u0438 \u0432 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QCommandLinkButton:focus {\n"
"    background-color: rgb(0, 150, 120);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
"QCommandLinkButton QLabel {\n"
"    font-size: 16px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043f\u043e\u0434 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u043c */\n"
"QCommandLinkButton QLabel#description {\n"
"    font-size: 14px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.QW111131)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.QL1111311 = QLabel(self.QW111131)
        self.QL1111311.setObjectName(u"QL1111311")
        self.QL1111311.setFont(font)
        self.QL1111311.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.QL1111311)

        self.hLW1111311 = QHBoxLayout()
        self.hLW1111311.setObjectName(u"hLW1111311")
        self.QW11113111 = QWidget(self.QW111131)
        self.QW11113111.setObjectName(u"QW11113111")
        self.QW11113111.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.QW11113111)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.QL111131111 = QLabel(self.QW11113111)
        self.QL111131111.setObjectName(u"QL111131111")
        self.QL111131111.setFont(font)
        self.QL111131111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.QL111131111)

        self.BTN111131111 = QPushButton(self.QW11113111)
        self.BTN111131111.setObjectName(u"BTN111131111")
        sizePolicy2.setHeightForWidth(self.BTN111131111.sizePolicy().hasHeightForWidth())
        self.BTN111131111.setSizePolicy(sizePolicy2)
        self.BTN111131111.setFont(font)

        self.verticalLayout_12.addWidget(self.BTN111131111)

        self.BTN111131112 = QPushButton(self.QW11113111)
        self.BTN111131112.setObjectName(u"BTN111131112")
        sizePolicy2.setHeightForWidth(self.BTN111131112.sizePolicy().hasHeightForWidth())
        self.BTN111131112.setSizePolicy(sizePolicy2)
        self.BTN111131112.setFont(font)

        self.verticalLayout_12.addWidget(self.BTN111131112)

        self.BTN111131113 = QPushButton(self.QW11113111)
        self.BTN111131113.setObjectName(u"BTN111131113")
        sizePolicy2.setHeightForWidth(self.BTN111131113.sizePolicy().hasHeightForWidth())
        self.BTN111131113.setSizePolicy(sizePolicy2)
        self.BTN111131113.setFont(font)

        self.verticalLayout_12.addWidget(self.BTN111131113)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.BTN111131114 = QPushButton(self.QW11113111)
        self.BTN111131114.setObjectName(u"BTN111131114")
        sizePolicy2.setHeightForWidth(self.BTN111131114.sizePolicy().hasHeightForWidth())
        self.BTN111131114.setSizePolicy(sizePolicy2)
        self.BTN111131114.setFont(font)

        self.verticalLayout_12.addWidget(self.BTN111131114)

        self.BTN111131115 = QPushButton(self.QW11113111)
        self.BTN111131115.setObjectName(u"BTN111131115")
        sizePolicy2.setHeightForWidth(self.BTN111131115.sizePolicy().hasHeightForWidth())
        self.BTN111131115.setSizePolicy(sizePolicy2)
        self.BTN111131115.setFont(font)

        self.verticalLayout_12.addWidget(self.BTN111131115)


        self.hLW1111311.addWidget(self.QW11113111)

        self.QW11113112 = QWidget(self.QW111131)
        self.QW11113112.setObjectName(u"QW11113112")
        self.verticalLayout_13 = QVBoxLayout(self.QW11113112)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label = QLabel(self.QW11113112)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label)

        self.comboBox_4 = QComboBox(self.QW11113112)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_13.addWidget(self.comboBox_4)

        self.lineEdit_2 = QLineEdit(self.QW11113112)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_13.addWidget(self.lineEdit_2)

        self.QSATOF = QScrollArea(self.QW11113112)
        self.QSATOF.setObjectName(u"QSATOF")
        self.QSATOF.setWidgetResizable(True)
        self.SAWTOF = QWidget()
        self.SAWTOF.setObjectName(u"SAWTOF")
        self.SAWTOF.setGeometry(QRect(0, 0, 20, 20))
        self.verticalLayout_14 = QVBoxLayout(self.SAWTOF)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.SAWTOFLayout = QVBoxLayout()
        self.SAWTOFLayout.setObjectName(u"SAWTOFLayout")

        self.verticalLayout_14.addLayout(self.SAWTOFLayout)

        self.QSATOF.setWidget(self.SAWTOF)

        self.verticalLayout_13.addWidget(self.QSATOF)

        self.comboBox_5 = QComboBox(self.QW11113112)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_13.addWidget(self.comboBox_5)

        self.BTN111131123 = QPushButton(self.QW11113112)
        self.BTN111131123.setObjectName(u"BTN111131123")
        sizePolicy2.setHeightForWidth(self.BTN111131123.sizePolicy().hasHeightForWidth())
        self.BTN111131123.setSizePolicy(sizePolicy2)
        self.BTN111131123.setFont(font)
        self.BTN111131123.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 0, 80);\n"
"	color: rgb(120, 0, 220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(70, 0, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(20, 0, 50);\n"
"}")

        self.verticalLayout_13.addWidget(self.BTN111131123)

        self.BTN111131124 = QPushButton(self.QW11113112)
        self.BTN111131124.setObjectName(u"BTN111131124")
        sizePolicy2.setHeightForWidth(self.BTN111131124.sizePolicy().hasHeightForWidth())
        self.BTN111131124.setSizePolicy(sizePolicy2)
        self.BTN111131124.setFont(font)
        self.BTN111131124.setIconSize(QSize(32, 32))

        self.verticalLayout_13.addWidget(self.BTN111131124)


        self.hLW1111311.addWidget(self.QW11113112)

        self.QW11113113 = QWidget(self.QW111131)
        self.QW11113113.setObjectName(u"QW11113113")
        self.verticalLayout_16 = QVBoxLayout(self.QW11113113)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.QL111131131 = QLabel(self.QW11113113)
        self.QL111131131.setObjectName(u"QL111131131")
        self.QL111131131.setFont(font)
        self.QL111131131.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.QL111131131)

        self.comboBox_6 = QComboBox(self.QW11113113)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.verticalLayout_16.addWidget(self.comboBox_6)

        self.lineEdit_3 = QLineEdit(self.QW11113113)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_16.addWidget(self.lineEdit_3)

        self.QSADataTOF = QScrollArea(self.QW11113113)
        self.QSADataTOF.setObjectName(u"QSADataTOF")
        self.QSADataTOF.setWidgetResizable(True)
        self.SAWTOFData = QWidget()
        self.SAWTOFData.setObjectName(u"SAWTOFData")
        self.SAWTOFData.setGeometry(QRect(0, 0, 20, 20))
        self.verticalLayout_17 = QVBoxLayout(self.SAWTOFData)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.SAWTOFDataLayout = QVBoxLayout()
        self.SAWTOFDataLayout.setObjectName(u"SAWTOFDataLayout")

        self.verticalLayout_17.addLayout(self.SAWTOFDataLayout)

        self.QSADataTOF.setWidget(self.SAWTOFData)

        self.verticalLayout_16.addWidget(self.QSADataTOF)

        self.comboBox_7 = QComboBox(self.QW11113113)
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.verticalLayout_16.addWidget(self.comboBox_7)

        self.BTN111131133 = QPushButton(self.QW11113113)
        self.BTN111131133.setObjectName(u"BTN111131133")
        sizePolicy2.setHeightForWidth(self.BTN111131133.sizePolicy().hasHeightForWidth())
        self.BTN111131133.setSizePolicy(sizePolicy2)
        self.BTN111131133.setFont(font)
        self.BTN111131133.setIconSize(QSize(32, 32))

        self.verticalLayout_16.addWidget(self.BTN111131133)

        self.BTN111131134 = QPushButton(self.QW11113113)
        self.BTN111131134.setObjectName(u"BTN111131134")
        sizePolicy2.setHeightForWidth(self.BTN111131134.sizePolicy().hasHeightForWidth())
        self.BTN111131134.setSizePolicy(sizePolicy2)
        self.BTN111131134.setFont(font)
        self.BTN111131134.setIconSize(QSize(32, 32))

        self.verticalLayout_16.addWidget(self.BTN111131134)


        self.hLW1111311.addWidget(self.QW11113113)


        self.verticalLayout_11.addLayout(self.hLW1111311)


        self.horizontalLayout_6.addWidget(self.QW111131)

        self.SW1111.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_7 = QHBoxLayout(self.page_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.QW11114 = QWidget(self.page_6)
        self.QW11114.setObjectName(u"QW11114")
        self.QW11114.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}\n"
"\n"
"\n"
"/* \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0441\u0442\u0438\u043b\u044c \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"QCommandLinkButton {\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c"
                        " \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QCommandLinkButton:hover {\n"
"    background-color: rgb(0, 100, 100);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QCommandLinkButton:active {\n"
"    background-color: rgb(0, 100, 100);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QCommandLinkButton:visited {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QCommandLinkButton:pressed {\n"
"    background-color: rgb(0, 50, 50);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"QCommandLinkButton:disabled {\n"
"    background-color: rgb(0, 150, 120);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438 \u0432"
                        " \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QCommandLinkButton:focus {\n"
"    background-color: rgb(0, 150, 120);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
"QCommandLinkButton QLabel {\n"
"    font-size: 16px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043f\u043e\u0434 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u043c */\n"
"QCommandLinkButton QLabel#description {\n"
"    font-size: 14px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.QW11114)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.hLW111141 = QHBoxLayout()
        self.hLW111141.setObjectName(u"hLW111141")
        self.QW1111411 = QWidget(self.QW11114)
        self.QW1111411.setObjectName(u"QW1111411")
        self.QW1111411.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.QW1111411)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.QL11114111 = QLabel(self.QW1111411)
        self.QL11114111.setObjectName(u"QL11114111")
        self.QL11114111.setFont(font)
        self.QL11114111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.QL11114111)

        self.QL11114112 = QLabel(self.QW1111411)
        self.QL11114112.setObjectName(u"QL11114112")
        font1 = QFont()
        font1.setFamilies([u"Jura"])
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.QL11114112.setFont(font1)
        self.QL11114112.setStyleSheet(u"QWidget {  \n"
"	font-size: 16px;\n"
"}  ")
        self.QL11114112.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.QL11114112)

        self.BTN11114111 = QPushButton(self.QW1111411)
        self.BTN11114111.setObjectName(u"BTN11114111")
        sizePolicy2.setHeightForWidth(self.BTN11114111.sizePolicy().hasHeightForWidth())
        self.BTN11114111.setSizePolicy(sizePolicy2)
        self.BTN11114111.setFont(font)

        self.verticalLayout_20.addWidget(self.BTN11114111)

        self.BTN11114112 = QPushButton(self.QW1111411)
        self.BTN11114112.setObjectName(u"BTN11114112")
        sizePolicy2.setHeightForWidth(self.BTN11114112.sizePolicy().hasHeightForWidth())
        self.BTN11114112.setSizePolicy(sizePolicy2)
        self.BTN11114112.setFont(font)

        self.verticalLayout_20.addWidget(self.BTN11114112)

        self.BTN11114113 = QPushButton(self.QW1111411)
        self.BTN11114113.setObjectName(u"BTN11114113")
        sizePolicy2.setHeightForWidth(self.BTN11114113.sizePolicy().hasHeightForWidth())
        self.BTN11114113.setSizePolicy(sizePolicy2)
        self.BTN11114113.setFont(font)

        self.verticalLayout_20.addWidget(self.BTN11114113)

        self.BTN11114114 = QPushButton(self.QW1111411)
        self.BTN11114114.setObjectName(u"BTN11114114")
        sizePolicy2.setHeightForWidth(self.BTN11114114.sizePolicy().hasHeightForWidth())
        self.BTN11114114.setSizePolicy(sizePolicy2)
        self.BTN11114114.setFont(font)

        self.verticalLayout_20.addWidget(self.BTN11114114)

        self.BTN11114115 = QPushButton(self.QW1111411)
        self.BTN11114115.setObjectName(u"BTN11114115")
        sizePolicy2.setHeightForWidth(self.BTN11114115.sizePolicy().hasHeightForWidth())
        self.BTN11114115.setSizePolicy(sizePolicy2)
        self.BTN11114115.setFont(font)

        self.verticalLayout_20.addWidget(self.BTN11114115)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_3)

        self.BTN11114123 = QPushButton(self.QW1111411)
        self.BTN11114123.setObjectName(u"BTN11114123")
        sizePolicy2.setHeightForWidth(self.BTN11114123.sizePolicy().hasHeightForWidth())
        self.BTN11114123.setSizePolicy(sizePolicy2)
        self.BTN11114123.setFont(font)

        self.verticalLayout_20.addWidget(self.BTN11114123)

        self.BTN11114116 = QPushButton(self.QW1111411)
        self.BTN11114116.setObjectName(u"BTN11114116")
        sizePolicy2.setHeightForWidth(self.BTN11114116.sizePolicy().hasHeightForWidth())
        self.BTN11114116.setSizePolicy(sizePolicy2)
        self.BTN11114116.setMinimumSize(QSize(333, 0))
        self.BTN11114116.setFont(font)
        self.BTN11114116.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.BTN11114116)

        self.BTN11114123_2 = QPushButton(self.QW1111411)
        self.BTN11114123_2.setObjectName(u"BTN11114123_2")
        sizePolicy2.setHeightForWidth(self.BTN11114123_2.sizePolicy().hasHeightForWidth())
        self.BTN11114123_2.setSizePolicy(sizePolicy2)
        self.BTN11114123_2.setFont(font)

        self.verticalLayout_20.addWidget(self.BTN11114123_2)

        self.BTN11114116_2 = QPushButton(self.QW1111411)
        self.BTN11114116_2.setObjectName(u"BTN11114116_2")
        sizePolicy2.setHeightForWidth(self.BTN11114116_2.sizePolicy().hasHeightForWidth())
        self.BTN11114116_2.setSizePolicy(sizePolicy2)
        self.BTN11114116_2.setMinimumSize(QSize(333, 0))
        self.BTN11114116_2.setFont(font)
        self.BTN11114116_2.setIconSize(QSize(32, 32))

        self.verticalLayout_20.addWidget(self.BTN11114116_2)


        self.hLW111141.addWidget(self.QW1111411)

        self.QW1111412 = QWidget(self.QW11114)
        self.QW1111412.setObjectName(u"QW1111412")
        self.verticalLayout_21 = QVBoxLayout(self.QW1111412)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.QL11114121 = QLabel(self.QW1111412)
        self.QL11114121.setObjectName(u"QL11114121")
        self.QL11114121.setFont(font)
        self.QL11114121.setStyleSheet(u"QWidget {  \n"
"	font-size: 36px;\n"
"}  ")
        self.QL11114121.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.QL11114121)

        self.comboBox_2 = QComboBox(self.QW1111412)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEditable(False)

        self.verticalLayout_21.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.QW1111412)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.verticalLayout_21.addWidget(self.comboBox)

        self.lineEdit_4 = QLineEdit(self.QW1111412)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_21.addWidget(self.lineEdit_4)

        self.listWidget = QListWidget(self.QW1111412)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_21.addWidget(self.listWidget)

        self.BTN11114122 = QPushButton(self.QW1111412)
        self.BTN11114122.setObjectName(u"BTN11114122")
        sizePolicy2.setHeightForWidth(self.BTN11114122.sizePolicy().hasHeightForWidth())
        self.BTN11114122.setSizePolicy(sizePolicy2)
        self.BTN11114122.setFont(font)

        self.verticalLayout_21.addWidget(self.BTN11114122)


        self.hLW111141.addWidget(self.QW1111412)


        self.verticalLayout_15.addLayout(self.hLW111141)


        self.horizontalLayout_7.addWidget(self.QW11114)

        self.SW1111.addWidget(self.page_6)

        self.verticalLayout_6.addWidget(self.SW1111)


        self.horizontalLayout.addWidget(self.widget)

        self.QW1113 = QWidget(self.centralwidget)
        self.QW1113.setObjectName(u"QW1113")
        self.QW1113.setMaximumSize(QSize(328, 16777215))
        self.QW1113.setStyleSheet(u"QWidget {\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgb(20, 30, 40);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.QW1113)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.QL11131 = QLabel(self.QW1113)
        self.QL11131.setObjectName(u"QL11131")
        self.QL11131.setFont(font)
        self.QL11131.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.QL11131)

        self.comboBox_3 = QComboBox(self.QW1113)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_4.addWidget(self.comboBox_3)

        self.lineEdit = QLineEdit(self.QW1113)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.scrollArea = QScrollArea(self.QW1113)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    border: 1px solid black; /* \u0426\u0432\u0435\u0442 \u0438 \u0442\u043e\u043b\u0449\u0438\u043d\u0430 \u0440\u0430\u043c\u043a\u0438 */\n"
"    border-radius: 3px; /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 3px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 layout */\n"
"	background-color: rgb(0, 50, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #2A9DF4; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"	padding: 3px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 layout */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color:"
                        " rgb(20, 100, 120); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 275, 643))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.VLApps = QGridLayout()
        self.VLApps.setObjectName(u"VLApps")

        self.verticalLayout_5.addLayout(self.VLApps)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.BTN11131 = QPushButton(self.QW1113)
        self.BTN11131.setObjectName(u"BTN11131")
        self.BTN11131.setFont(font)

        self.verticalLayout_4.addWidget(self.BTN11131)


        self.horizontalLayout.addWidget(self.QW1113)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QMainViewWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(QMainViewWindow)

        self.SW1111.setCurrentIndex(3)
        self.tW111121121.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(QMainViewWindow)
    # setupUi

    def retranslateUi(self, QMainViewWindow):
        QMainViewWindow.setWindowTitle(QCoreApplication.translate("QMainViewWindow", u"= = TemplateWindow = =", None))
        self.BTN1111111.setText(QCoreApplication.translate("QMainViewWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.BTN1111112.setText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f", None))
        self.BTN1111113.setText(QCoreApplication.translate("QMainViewWindow", u"\u0412\u0441\u0435\u043e\u0431\u0449\u0430\u044f \u0442\u0435\u0440\u0430\u043f\u0438\u044f", None))
        self.BTN1111114.setText(QCoreApplication.translate("QMainViewWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
        self.QL1111121.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.BTN1111121.setText(QCoreApplication.translate("QMainViewWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c F-\u0417\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.BTN1111122.setText(QCoreApplication.translate("QMainViewWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.BTN1111123.setText(QCoreApplication.translate("QMainViewWindow", u"  \u041e\u0447\u0438\u0441\u0442\u043a\u0430 F-\u0414\u0430\u043d\u043d\u044b\u0445  ", None))
        self.BTN1111124.setText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0447\u0442\u043e \u0442\u043e", None))
        self.QL1111111.setText(QCoreApplication.translate("QMainViewWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.BTN111111.setText(QCoreApplication.translate("QMainViewWindow", u"\u0412\u0441\u0435 F-\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.BTN111112.setText(QCoreApplication.translate("QMainViewWindow", u"\u0427\u0442\u043e- \u0442\u043e \u043d\u0430 \u0432\u044b\u0441\u043e\u043a\u043e\u043c", None))
        self.BTN111113.setText(QCoreApplication.translate("QMainViewWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 F-\u0424\u0430\u0439\u043b\u044b", None))
        self.BTN111114.setText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0447\u0442\u043e \u0442\u043e", None))
        self.QL1111131.setText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f", None))
        self.BTN1111131.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c F-\u0417\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.BTN1111132.setText(QCoreApplication.translate("QMainViewWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0441\u0435\u0445 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.BTN1111133.setText(QCoreApplication.translate("QMainViewWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 F-\u0424\u0430\u0439\u043b\u044b", None))
        self.BTN1111134.setText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0447\u0442\u043e \u0442\u043e", None))
        self.QL111121111.setText(QCoreApplication.translate("QMainViewWindow", u"   \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438   ", None))
        self.BTN111121111.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u043c", None))
        self.BTN111121133.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u00abMS Word\u00bb", None))
#if QT_CONFIG(tooltip)
        self.BTN111121134.setToolTip(QCoreApplication.translate("QMainViewWindow", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN111121134.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u0411\u043b\u043e\u043a\u043d\u043e\u0442\u0435", None))
        self.QL111121121.setText(QCoreApplication.translate("QMainViewWindow", u"   \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432   ", None))
        self.tW111121121.setTabText(self.tW111121121.indexOf(self.tab), QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 1", None))
        self.tW111121121.setTabText(self.tW111121121.indexOf(self.tab_2), QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 2", None))
        self.label_7.setText(QCoreApplication.translate("QMainViewWindow", u"        \u0421\u043f\u0438\u0441\u043e\u043a \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432        ", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u0410-\u042f", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("QMainViewWindow", u"\u042f-\u0410", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))

        self.comboBox_10.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))

        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("QMainViewWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.BTN111121112.setText(QCoreApplication.translate("QMainViewWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.BTN111121113.setText(QCoreApplication.translate("QMainViewWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.QL1111311.setText(QCoreApplication.translate("QMainViewWindow", u"\u0412\u0441\u0435\u043e\u0431\u0449\u0430\u044f \u0442\u0435\u043e\u0440\u0438\u044f \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.QL111131111.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.BTN111131111.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 PT-\u0414\u0430\u043d\u043d\u044b\u043c\u0438", None))
        self.BTN111131112.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 OND-\u0417\u0430\u043c\u0435\u0442\u043a\u0430\u043c\u0438", None))
        self.BTN111131113.setText(QCoreApplication.translate("QMainViewWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u0432\u0441\u0435 OND-\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.BTN111131114.setText(QCoreApplication.translate("QMainViewWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c PT-\u0414\u0430\u043d\u043d\u044b\u0435...", None))
        self.BTN111131115.setText(QCoreApplication.translate("QMainViewWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c PT-\u0414\u0430\u043d\u043d\u044b\u0435...", None))
        self.label.setText(QCoreApplication.translate("QMainViewWindow", u"        \u0421\u043f\u0438\u0441\u043e\u043a OND-\u0417\u0430\u043c\u0435\u0442\u043e\u043a        ", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u0410-\u042f", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("QMainViewWindow", u"\u042f-\u0410", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))

        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("QMainViewWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u0422\u0438\u043f 1", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("QMainViewWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("QMainViewWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("QMainViewWindow", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))

        self.BTN111131123.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u00abObsidian\u00bb", None))
#if QT_CONFIG(tooltip)
        self.BTN111131124.setToolTip(QCoreApplication.translate("QMainViewWindow", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN111131124.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 VSCode", None))
        self.QL111131131.setText(QCoreApplication.translate("QMainViewWindow", u"        \u0421\u043f\u0438\u0441\u043e\u043a PT-\u0414\u0430\u043d\u043d\u044b\u0445        ", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u0410-\u042f", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("QMainViewWindow", u"\u042f-\u0410", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))

        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("QMainViewWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u0422\u0438\u043f 1", None))

#if QT_CONFIG(tooltip)
        self.BTN111131133.setToolTip(QCoreApplication.translate("QMainViewWindow", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN111131133.setText(QCoreApplication.translate("QMainViewWindow", u"  \u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u041f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0435  ", None))
#if QT_CONFIG(tooltip)
        self.BTN111131134.setToolTip(QCoreApplication.translate("QMainViewWindow", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN111131134.setText(QCoreApplication.translate("QMainViewWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0443\u0442\u044c", None))
        self.QL11114111.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.QL11114112.setText(QCoreApplication.translate("QMainViewWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430...", None))
        self.BTN11114111.setText("")
        self.BTN11114112.setText("")
        self.BTN11114113.setText("")
        self.BTN11114114.setText("")
        self.BTN11114115.setText("")
        self.BTN11114123.setText(QCoreApplication.translate("QMainViewWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435...", None))
#if QT_CONFIG(tooltip)
        self.BTN11114116.setToolTip(QCoreApplication.translate("QMainViewWindow", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN11114116.setText(QCoreApplication.translate("QMainViewWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442...", None))
        self.BTN11114123_2.setText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044e...", None))
#if QT_CONFIG(tooltip)
        self.BTN11114116_2.setToolTip(QCoreApplication.translate("QMainViewWindow", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN11114116_2.setText(QCoreApplication.translate("QMainViewWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438...", None))
        self.QL11114121.setText(QCoreApplication.translate("QMainViewWindow", u"         \u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u043e\u0435\u043a\u0442\u043e\u0432         ", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("QMainViewWindow", u"\u0410-\u042f", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("QMainViewWindow", u"\u042f-\u0410", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u0411\u0435\u0437 \u0444\u0438\u043b\u044c\u0442\u0440\u0430 \u0442\u0438\u043f\u0430", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("QMainViewWindow", u"Python", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("QMainViewWindow", u"Blender", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("QMainViewWindow", u"UnrealEngine", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("QMainViewWindow", u"Painting", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("QMainViewWindow", u"Imagers", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("QMainViewWindow", u"\u0411\u0435\u0437 \u0444\u0438\u043b\u044c\u0442\u0440\u0430 \u0442\u0438\u043f\u0430", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("QMainViewWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.BTN11114122.setText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.QL11131.setText(QCoreApplication.translate("QMainViewWindow", u"  \u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f  ", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("QMainViewWindow", u"\u0413\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u0430\u044f \u0412\u0438\u0440\u0442\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("QMainViewWindow", u"\u0413\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u0430\u044f \u0420\u0435\u0432\u0435\u0440\u0441\u0438\u044f", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("QMainViewWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043d\u0430\u044f \u0420\u0435\u0432\u0435\u0440\u0441\u0438\u044f", None))

        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("QMainViewWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.BTN11131.setText(QCoreApplication.translate("QMainViewWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

