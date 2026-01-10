# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_QMW1(object):
    def setupUi(self, QMW1):
        if not QMW1.objectName():
            QMW1.setObjectName(u"QMW1")
        QMW1.resize(1738, 979)
        font = QFont()
        font.setFamilies([u"Jura"])
        font.setBold(True)
        QMW1.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/Main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        QMW1.setWindowIcon(icon)
        QMW1.setStyleSheet(u"")
        self.action = QAction(QMW1)
        self.action.setObjectName(u"action")
        self.AOptions = QAction(QMW1)
        self.AOptions.setObjectName(u"AOptions")
        self.action_2 = QAction(QMW1)
        self.action_2.setObjectName(u"action_2")
        self.action_4 = QAction(QMW1)
        self.action_4.setObjectName(u"action_4")
        self.action_6 = QAction(QMW1)
        self.action_6.setObjectName(u"action_6")
        self.action_8 = QAction(QMW1)
        self.action_8.setObjectName(u"action_8")
        self.action_gif = QAction(QMW1)
        self.action_gif.setObjectName(u"action_gif")
        self.action_3 = QAction(QMW1)
        self.action_3.setObjectName(u"action_3")
        self.QW11 = QWidget(QMW1)
        self.QW11.setObjectName(u"QW11")
        self.QW11.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.QW11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.QLB111 = QHBoxLayout()
        self.QLB111.setObjectName(u"QLB111")
        self.StackW = QStackedWidget(self.QW11)
        self.StackW.setObjectName(u"StackW")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StackW.sizePolicy().hasHeightForWidth())
        self.StackW.setSizePolicy(sizePolicy)
        self.StackW.setMinimumSize(QSize(500, 0))
        self.StackW.setStyleSheet(u"border: 0px;")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_6 = QHBoxLayout(self.page_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.QWLayout = QWidget(self.page_5)
        self.QWLayout.setObjectName(u"QWLayout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.QWLayout.sizePolicy().hasHeightForWidth())
        self.QWLayout.setSizePolicy(sizePolicy1)
        self.QWLayout.setMinimumSize(QSize(700, 0))
        self.QWLayout.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 100);\n"
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
        self.QVBL1111 = QVBoxLayout(self.QWLayout)
        self.QVBL1111.setObjectName(u"QVBL1111")
        self.widget = QWidget(self.QWLayout)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 100);\n"
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
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.QW11111_2 = QWidget(self.widget)
        self.QW11111_2.setObjectName(u"QW11111_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.QW11111_2.sizePolicy().hasHeightForWidth())
        self.QW11111_2.setSizePolicy(sizePolicy3)
        self.QW11111_2.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.QW11111_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.QL111121_3 = QLabel(self.QW11111_2)
        self.QL111121_3.setObjectName(u"QL111121_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.QL111121_3.sizePolicy().hasHeightForWidth())
        self.QL111121_3.setSizePolicy(sizePolicy4)
        self.QL111121_3.setMinimumSize(QSize(100, 100))
        self.QL111121_3.setFont(font)
        self.QL111121_3.setStyleSheet(u"border-radius: 48px;")
        self.QL111121_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.QL111121_3)


        self.horizontalLayout_2.addWidget(self.QW11111_2)

        self.QW11111_3 = QWidget(self.widget)
        self.QW11111_3.setObjectName(u"QW11111_3")
        self.QW11111_3.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.QW11111_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.QL111121_2 = QLabel(self.QW11111_3)
        self.QL111121_2.setObjectName(u"QL111121_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.QL111121_2.sizePolicy().hasHeightForWidth())
        self.QL111121_2.setSizePolicy(sizePolicy5)
        font1 = QFont()
        font1.setFamilies([u"Jura"])
        font1.setPointSize(28)
        font1.setBold(False)
        font1.setItalic(False)
        self.QL111121_2.setFont(font1)
        self.QL111121_2.setStyleSheet(u"font: 28pt;")
        self.QL111121_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.QL111121_2)


        self.horizontalLayout_2.addWidget(self.QW11111_3)


        self.QVBL1111.addWidget(self.widget)

        self.QW11111 = QWidget(self.QWLayout)
        self.QW11111.setObjectName(u"QW11111")
        self.QW11111.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 100);\n"
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
        self.verticalLayout_5 = QVBoxLayout(self.QW11111)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.QL111111 = QLabel(self.QW11111)
        self.QL111111.setObjectName(u"QL111111")
        self.QL111111.setFont(font)
        self.QL111111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.QL111111)

        self.QHBL111111 = QHBoxLayout()
        self.QHBL111111.setObjectName(u"QHBL111111")
        self.BTN1111111 = QPushButton(self.QW11111)
        self.BTN1111111.setObjectName(u"BTN1111111")
        self.BTN1111111.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111111)

        self.BTN1111112 = QPushButton(self.QW11111)
        self.BTN1111112.setObjectName(u"BTN1111112")
        self.BTN1111112.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111112)

        self.BTN1111112_2 = QPushButton(self.QW11111)
        self.BTN1111112_2.setObjectName(u"BTN1111112_2")
        self.BTN1111112_2.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111112_2)

        self.BTN1111113 = QPushButton(self.QW11111)
        self.BTN1111113.setObjectName(u"BTN1111113")
        self.BTN1111113.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111113)

        self.BTN1111114 = QPushButton(self.QW11111)
        self.BTN1111114.setObjectName(u"BTN1111114")
        self.BTN1111114.setFont(font)

        self.QHBL111111.addWidget(self.BTN1111114)


        self.verticalLayout_5.addLayout(self.QHBL111111)


        self.QVBL1111.addWidget(self.QW11111)

        self.SW111121 = QStackedWidget(self.QWLayout)
        self.SW111121.setObjectName(u"SW111121")
        sizePolicy5.setHeightForWidth(self.SW111121.sizePolicy().hasHeightForWidth())
        self.SW111121.setSizePolicy(sizePolicy5)
        self.SW111121.setStyleSheet(u"QStackedWidget {\n"
"	border: 0;\n"
"	color: rgba(20, 30, 40, 100);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 50);\n"
"}\n"
"\n"
"QPushButton {  \n"
"    background-color: rgb(10, 80, 100); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */  \n"
"    color: rgb(100, 200, 200); /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}  \n"
"  \n"
"QPushButton:hover {  \n"
"    background-color: rgb(20, 50, 60); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */  \n"
"}  \n"
"  \n"
"QPushButton:pressed {  \n"
"    background-color: rgb(0, 60, 80); /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */  \n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SL2214 = QVBoxLayout()
        self.SL2214.setObjectName(u"SL2214")
        self.SLL22141_name = QLabel(self.page)
        self.SLL22141_name.setObjectName(u"SLL22141_name")
        sizePolicy4.setHeightForWidth(self.SLL22141_name.sizePolicy().hasHeightForWidth())
        self.SLL22141_name.setSizePolicy(sizePolicy4)
        self.SLL22141_name.setFont(font)
        self.SLL22141_name.setStyleSheet(u"margin: 10 0 10 0")
        self.SLL22141_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SL2214.addWidget(self.SLL22141_name)

        self.SB22141 = QPushButton(self.page)
        self.SB22141.setObjectName(u"SB22141")
        self.SB22141.setFont(font)
        self.SB22141.setStyleSheet(u"")

        self.SL2214.addWidget(self.SB22141)

        self.SB22142 = QPushButton(self.page)
        self.SB22142.setObjectName(u"SB22142")
        self.SB22142.setFont(font)

        self.SL2214.addWidget(self.SB22142)

        self.SB22143 = QPushButton(self.page)
        self.SB22143.setObjectName(u"SB22143")
        self.SB22143.setFont(font)

        self.SL2214.addWidget(self.SB22143)

        self.SB22144 = QPushButton(self.page)
        self.SB22144.setObjectName(u"SB22144")
        self.SB22144.setFont(font)

        self.SL2214.addWidget(self.SB22144)


        self.verticalLayout_4.addLayout(self.SL2214)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.SW111121.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 50);\n"
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
        self.horizontalLayout_3 = QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.QW1111_3 = QWidget(self.page_2)
        self.QW1111_3.setObjectName(u"QW1111_3")
        self.QW1111_3.setMinimumSize(QSize(450, 0))
        self.QW1111_3.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.QW1111_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.LL11111_GPLabel = QLabel(self.QW1111_3)
        self.LL11111_GPLabel.setObjectName(u"LL11111_GPLabel")
        self.LL11111_GPLabel.setMinimumSize(QSize(0, 50))
        self.LL11111_GPLabel.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamilies([u"Jura"])
        font2.setBold(True)
        font2.setItalic(False)
        self.LL11111_GPLabel.setFont(font2)
        self.LL11111_GPLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_11.addWidget(self.LL11111_GPLabel)

        self.lineEdit_2 = QLineEdit(self.QW1111_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)

        self.verticalLayout_11.addWidget(self.lineEdit_2)

        self.listWidget = QListWidget(self.QW1111_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 225))
        self.listWidget.setStyleSheet(u"font-size: 24px;")

        self.verticalLayout_11.addWidget(self.listWidget)

        self.BTN11112 = QPushButton(self.QW1111_3)
        self.BTN11112.setObjectName(u"BTN11112")
        self.BTN11112.setFont(font)

        self.verticalLayout_11.addWidget(self.BTN11112)


        self.horizontalLayout_3.addWidget(self.QW1111_3)

        self.SW111121.addWidget(self.page_2)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_11 = QHBoxLayout(self.page_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.QW1111_2 = QWidget(self.page_11)
        self.QW1111_2.setObjectName(u"QW1111_2")
        self.QW1111_2.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.QW1111_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.LL11111_Addons = QLabel(self.QW1111_2)
        self.LL11111_Addons.setObjectName(u"LL11111_Addons")
        sizePolicy4.setHeightForWidth(self.LL11111_Addons.sizePolicy().hasHeightForWidth())
        self.LL11111_Addons.setSizePolicy(sizePolicy4)
        self.LL11111_Addons.setMinimumSize(QSize(0, 50))
        self.LL11111_Addons.setMaximumSize(QSize(16777215, 50))
        self.LL11111_Addons.setFont(font2)
        self.LL11111_Addons.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_10.addWidget(self.LL11111_Addons, 0, Qt.AlignmentFlag.AlignVCenter)

        self.lineEdit = QLineEdit(self.QW1111_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)

        self.verticalLayout_10.addWidget(self.lineEdit)

        self.listWidget_2 = QListWidget(self.QW1111_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy5.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy5)
        self.listWidget_2.setViewMode(QListView.ViewMode.IconMode)

        self.verticalLayout_10.addWidget(self.listWidget_2)

        self.BTN11111 = QPushButton(self.QW1111_2)
        self.BTN11111.setObjectName(u"BTN11111")
        self.BTN11111.setFont(font)

        self.verticalLayout_10.addWidget(self.BTN11111)


        self.horizontalLayout_11.addWidget(self.QW1111_2)

        self.SW111121.addWidget(self.page_11)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 50);\n"
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
        self.horizontalLayout_4 = QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.SL11112131 = QVBoxLayout()
        self.SL11112131.setObjectName(u"SL11112131")
        self.SLL111121311 = QLabel(self.page_3)
        self.SLL111121311.setObjectName(u"SLL111121311")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.SLL111121311.sizePolicy().hasHeightForWidth())
        self.SLL111121311.setSizePolicy(sizePolicy6)
        self.SLL111121311.setMinimumSize(QSize(0, 50))
        self.SLL111121311.setFont(font)
        self.SLL111121311.setStyleSheet(u"margin: 10 0 10 0")
        self.SLL111121311.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SL11112131.addWidget(self.SLL111121311)

        self.SB111121311 = QPushButton(self.page_3)
        self.SB111121311.setObjectName(u"SB111121311")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.SB111121311.sizePolicy().hasHeightForWidth())
        self.SB111121311.setSizePolicy(sizePolicy7)
        self.SB111121311.setFont(font)
        self.SB111121311.setStyleSheet(u"")

        self.SL11112131.addWidget(self.SB111121311)

        self.SB111121312 = QPushButton(self.page_3)
        self.SB111121312.setObjectName(u"SB111121312")
        sizePolicy7.setHeightForWidth(self.SB111121312.sizePolicy().hasHeightForWidth())
        self.SB111121312.setSizePolicy(sizePolicy7)
        self.SB111121312.setFont(font)

        self.SL11112131.addWidget(self.SB111121312)

        self.SB111121313 = QPushButton(self.page_3)
        self.SB111121313.setObjectName(u"SB111121313")
        sizePolicy7.setHeightForWidth(self.SB111121313.sizePolicy().hasHeightForWidth())
        self.SB111121313.setSizePolicy(sizePolicy7)
        self.SB111121313.setFont(font)

        self.SL11112131.addWidget(self.SB111121313)

        self.SB111121314 = QPushButton(self.page_3)
        self.SB111121314.setObjectName(u"SB111121314")
        sizePolicy7.setHeightForWidth(self.SB111121314.sizePolicy().hasHeightForWidth())
        self.SB111121314.setSizePolicy(sizePolicy7)
        self.SB111121314.setFont(font)

        self.SL11112131.addWidget(self.SB111121314)

        self.SB111121315 = QPushButton(self.page_3)
        self.SB111121315.setObjectName(u"SB111121315")
        sizePolicy7.setHeightForWidth(self.SB111121315.sizePolicy().hasHeightForWidth())
        self.SB111121315.setSizePolicy(sizePolicy7)
        self.SB111121315.setFont(font)

        self.SL11112131.addWidget(self.SB111121315)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SL11112131.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addLayout(self.SL11112131)

        self.SW111121.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 50);\n"
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
        self.horizontalLayout_5 = QHBoxLayout(self.page_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.SL11112132 = QVBoxLayout()
        self.SL11112132.setObjectName(u"SL11112132")
        self.SLL111121321 = QLabel(self.page_4)
        self.SLL111121321.setObjectName(u"SLL111121321")
        sizePolicy4.setHeightForWidth(self.SLL111121321.sizePolicy().hasHeightForWidth())
        self.SLL111121321.setSizePolicy(sizePolicy4)
        self.SLL111121321.setFont(font)
        self.SLL111121321.setStyleSheet(u"margin: 5 0 0 0")
        self.SLL111121321.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.SL11112132.addWidget(self.SLL111121321)

        self.SB111121321 = QPushButton(self.page_4)
        self.SB111121321.setObjectName(u"SB111121321")
        sizePolicy7.setHeightForWidth(self.SB111121321.sizePolicy().hasHeightForWidth())
        self.SB111121321.setSizePolicy(sizePolicy7)
        self.SB111121321.setFont(font)
        self.SB111121321.setStyleSheet(u"")

        self.SL11112132.addWidget(self.SB111121321)

        self.SB111121322 = QPushButton(self.page_4)
        self.SB111121322.setObjectName(u"SB111121322")
        sizePolicy7.setHeightForWidth(self.SB111121322.sizePolicy().hasHeightForWidth())
        self.SB111121322.setSizePolicy(sizePolicy7)
        self.SB111121322.setFont(font)

        self.SL11112132.addWidget(self.SB111121322)

        self.SB111121323 = QPushButton(self.page_4)
        self.SB111121323.setObjectName(u"SB111121323")
        sizePolicy7.setHeightForWidth(self.SB111121323.sizePolicy().hasHeightForWidth())
        self.SB111121323.setSizePolicy(sizePolicy7)
        self.SB111121323.setFont(font)

        self.SL11112132.addWidget(self.SB111121323)

        self.SB111121324 = QPushButton(self.page_4)
        self.SB111121324.setObjectName(u"SB111121324")
        sizePolicy7.setHeightForWidth(self.SB111121324.sizePolicy().hasHeightForWidth())
        self.SB111121324.setSizePolicy(sizePolicy7)
        self.SB111121324.setFont(font)

        self.SL11112132.addWidget(self.SB111121324)

        self.SB111121325 = QPushButton(self.page_4)
        self.SB111121325.setObjectName(u"SB111121325")
        sizePolicy7.setHeightForWidth(self.SB111121325.sizePolicy().hasHeightForWidth())
        self.SB111121325.setSizePolicy(sizePolicy7)
        self.SB111121325.setFont(font)

        self.SL11112132.addWidget(self.SB111121325)

        self.vS111121321 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SL11112132.addItem(self.vS111121321)


        self.horizontalLayout_5.addLayout(self.SL11112132)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SLL111121321_2 = QLabel(self.page_4)
        self.SLL111121321_2.setObjectName(u"SLL111121321_2")
        sizePolicy4.setHeightForWidth(self.SLL111121321_2.sizePolicy().hasHeightForWidth())
        self.SLL111121321_2.setSizePolicy(sizePolicy4)
        self.SLL111121321_2.setFont(font)
        self.SLL111121321_2.setStyleSheet(u"margin: 5 0 0 0")
        self.SLL111121321_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.SLL111121321_2)

        self.BTN111111 = QPushButton(self.page_4)
        self.BTN111111.setObjectName(u"BTN111111")
        self.BTN111111.setFont(font)

        self.verticalLayout_3.addWidget(self.BTN111111)

        self.BTN111112 = QPushButton(self.page_4)
        self.BTN111112.setObjectName(u"BTN111112")
        self.BTN111112.setFont(font)

        self.verticalLayout_3.addWidget(self.BTN111112)

        self.BTN111113 = QPushButton(self.page_4)
        self.BTN111113.setObjectName(u"BTN111113")
        self.BTN111113.setFont(font)

        self.verticalLayout_3.addWidget(self.BTN111113)

        self.BTN111114 = QPushButton(self.page_4)
        self.BTN111114.setObjectName(u"BTN111114")
        self.BTN111114.setFont(font)

        self.verticalLayout_3.addWidget(self.BTN111114)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.SW111121.addWidget(self.page_4)

        self.QVBL1111.addWidget(self.SW111121)


        self.horizontalLayout_6.addWidget(self.QWLayout)

        self.stack_managers = QStackedWidget(self.page_5)
        self.stack_managers.setObjectName(u"stack_managers")
        self.stack_managers.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(10, 30, 40, 100);\n"
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
        self.page_project_manager = QWidget()
        self.page_project_manager.setObjectName(u"page_project_manager")
        self.verticalLayout_6 = QVBoxLayout(self.page_project_manager)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ProjectManagerTabs = QTabWidget(self.page_project_manager)
        self.ProjectManagerTabs.setObjectName(u"ProjectManagerTabs")
        self.ProjectManagerTabs.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid rgb(0, 100, 100);\n"
"    background-color: rgba(0, 30, 40, 180);\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u043e\u0441\u0430 \u0432\u043a\u043b\u0430\u0434\u043e\u043a */\n"
"QTabBar {\n"
"    background: rgba(0, 10, 80, 100);\n"
"    border-bottom: 1px solid rgb(0, 100, 100);\n"
"}\n"
"\n"
"/* \u0421\u0430\u043c\u0438 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"QTabBar::tab {\n"
"    color: rgb(100, 200, 200);\n"
"    padding: 6px 12px;\n"
"    border: 1px solid rgb(0, 100, 100);\n"
"    border-bottom: none; /* \u0427\u0442\u043e\u0431\u044b \u0432\u044b\u0434\u0435\u043b\u044f\u043b\u0430\u0441\u044c \u0430\u043a\u0442\u0438\u0432\u043d\u0430\u044f */\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"/* \u0410\u043a\u0442\u0438\u0432\u043d\u0430\u044f \u0432\u043a\u043b\u0430\u0434\u043a\u0430 */\n"
"QTabBar::tab:selected {\n"
"    color: rgb(180, 255, 255);\n"
"}\n"
"\n"
"/* \u041d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0435 */\n"
"QTabBar::tab:hover {\n"
"    backgr"
                        "ound: rgb(0, 60, 80);\n"
"}\n"
"\n"
"/* \u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0435 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 3px; /* \u041d\u0435\u043c\u043d\u043e\u0433\u043e \u0441\u0434\u0432\u0438\u0433\u0430\u0435\u0442 \u0432\u043d\u0438\u0437 */\n"
"}\n"
"")
        self.Main = QWidget()
        self.Main.setObjectName(u"Main")
        self.horizontalLayout_10 = QHBoxLayout(self.Main)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.QW111111 = QWidget(self.Main)
        self.QW111111.setObjectName(u"QW111111")
        self.QW111111.setMinimumSize(QSize(0, 0))
        self.QW111111.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.QW111111)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.QL1111111 = QLabel(self.QW111111)
        self.QL1111111.setObjectName(u"QL1111111")
        sizePolicy2.setHeightForWidth(self.QL1111111.sizePolicy().hasHeightForWidth())
        self.QL1111111.setSizePolicy(sizePolicy2)
        self.QL1111111.setFont(font)
        self.QL1111111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.QL1111111)

        self.BTN111111_2 = QPushButton(self.QW111111)
        self.BTN111111_2.setObjectName(u"BTN111111_2")
        sizePolicy4.setHeightForWidth(self.BTN111111_2.sizePolicy().hasHeightForWidth())
        self.BTN111111_2.setSizePolicy(sizePolicy4)
        self.BTN111111_2.setFont(font)

        self.verticalLayout_32.addWidget(self.BTN111111_2)

        self.BTN111112_2 = QPushButton(self.QW111111)
        self.BTN111112_2.setObjectName(u"BTN111112_2")
        sizePolicy6.setHeightForWidth(self.BTN111112_2.sizePolicy().hasHeightForWidth())
        self.BTN111112_2.setSizePolicy(sizePolicy6)
        self.BTN111112_2.setFont(font)
        self.BTN111112_2.setIconSize(QSize(32, 32))

        self.verticalLayout_32.addWidget(self.BTN111112_2)

        self.BTN111113_2 = QPushButton(self.QW111111)
        self.BTN111113_2.setObjectName(u"BTN111113_2")
        sizePolicy4.setHeightForWidth(self.BTN111113_2.sizePolicy().hasHeightForWidth())
        self.BTN111113_2.setSizePolicy(sizePolicy4)
        self.BTN111113_2.setFont(font)

        self.verticalLayout_32.addWidget(self.BTN111113_2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_9)

        self.BTN111114_2 = QPushButton(self.QW111111)
        self.BTN111114_2.setObjectName(u"BTN111114_2")
        sizePolicy7.setHeightForWidth(self.BTN111114_2.sizePolicy().hasHeightForWidth())
        self.BTN111114_2.setSizePolicy(sizePolicy7)
        self.BTN111114_2.setFont(font)

        self.verticalLayout_32.addWidget(self.BTN111114_2)


        self.horizontalLayout_10.addWidget(self.QW111111)

        self.QW111112 = QWidget(self.Main)
        self.QW111112.setObjectName(u"QW111112")
        self.QW111112.setMinimumSize(QSize(0, 0))
        self.QW111112.setStyleSheet(u"")
        self.verticalLayout_31 = QVBoxLayout(self.QW111112)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.QL1111121 = QLabel(self.QW111112)
        self.QL1111121.setObjectName(u"QL1111121")
        sizePolicy2.setHeightForWidth(self.QL1111121.sizePolicy().hasHeightForWidth())
        self.QL1111121.setSizePolicy(sizePolicy2)
        self.QL1111121.setFont(font)
        self.QL1111121.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.QL1111121)

        self.BTN1111121 = QPushButton(self.QW111112)
        self.BTN1111121.setObjectName(u"BTN1111121")
        sizePolicy7.setHeightForWidth(self.BTN1111121.sizePolicy().hasHeightForWidth())
        self.BTN1111121.setSizePolicy(sizePolicy7)
        self.BTN1111121.setFont(font)

        self.verticalLayout_31.addWidget(self.BTN1111121)

        self.BTN1111122 = QPushButton(self.QW111112)
        self.BTN1111122.setObjectName(u"BTN1111122")
        sizePolicy7.setHeightForWidth(self.BTN1111122.sizePolicy().hasHeightForWidth())
        self.BTN1111122.setSizePolicy(sizePolicy7)
        self.BTN1111122.setFont(font)
        self.BTN1111122.setIconSize(QSize(32, 32))

        self.verticalLayout_31.addWidget(self.BTN1111122)

        self.BTN1111123 = QPushButton(self.QW111112)
        self.BTN1111123.setObjectName(u"BTN1111123")
        sizePolicy7.setHeightForWidth(self.BTN1111123.sizePolicy().hasHeightForWidth())
        self.BTN1111123.setSizePolicy(sizePolicy7)
        self.BTN1111123.setFont(font)

        self.verticalLayout_31.addWidget(self.BTN1111123)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_8)

        self.BTN1111124 = QPushButton(self.QW111112)
        self.BTN1111124.setObjectName(u"BTN1111124")
        sizePolicy7.setHeightForWidth(self.BTN1111124.sizePolicy().hasHeightForWidth())
        self.BTN1111124.setSizePolicy(sizePolicy7)
        self.BTN1111124.setFont(font)

        self.verticalLayout_31.addWidget(self.BTN1111124)


        self.horizontalLayout_10.addWidget(self.QW111112)

        self.QW111113 = QWidget(self.Main)
        self.QW111113.setObjectName(u"QW111113")
        self.QW111113.setMinimumSize(QSize(0, 0))
        self.QW111113.setStyleSheet(u"")
        self.verticalLayout_33 = QVBoxLayout(self.QW111113)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.QL1111131 = QLabel(self.QW111113)
        self.QL1111131.setObjectName(u"QL1111131")
        sizePolicy2.setHeightForWidth(self.QL1111131.sizePolicy().hasHeightForWidth())
        self.QL1111131.setSizePolicy(sizePolicy2)
        self.QL1111131.setFont(font)
        self.QL1111131.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.QL1111131)

        self.BTN1111131 = QPushButton(self.QW111113)
        self.BTN1111131.setObjectName(u"BTN1111131")
        sizePolicy7.setHeightForWidth(self.BTN1111131.sizePolicy().hasHeightForWidth())
        self.BTN1111131.setSizePolicy(sizePolicy7)
        self.BTN1111131.setFont(font)

        self.verticalLayout_33.addWidget(self.BTN1111131)

        self.BTN1111132 = QPushButton(self.QW111113)
        self.BTN1111132.setObjectName(u"BTN1111132")
        sizePolicy7.setHeightForWidth(self.BTN1111132.sizePolicy().hasHeightForWidth())
        self.BTN1111132.setSizePolicy(sizePolicy7)
        self.BTN1111132.setFont(font)
        self.BTN1111132.setIconSize(QSize(32, 32))

        self.verticalLayout_33.addWidget(self.BTN1111132)

        self.BTN1111133 = QPushButton(self.QW111113)
        self.BTN1111133.setObjectName(u"BTN1111133")
        sizePolicy7.setHeightForWidth(self.BTN1111133.sizePolicy().hasHeightForWidth())
        self.BTN1111133.setSizePolicy(sizePolicy7)
        self.BTN1111133.setFont(font)

        self.verticalLayout_33.addWidget(self.BTN1111133)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_10)

        self.BTN1111134 = QPushButton(self.QW111113)
        self.BTN1111134.setObjectName(u"BTN1111134")
        sizePolicy7.setHeightForWidth(self.BTN1111134.sizePolicy().hasHeightForWidth())
        self.BTN1111134.setSizePolicy(sizePolicy7)
        self.BTN1111134.setFont(font)

        self.verticalLayout_33.addWidget(self.BTN1111134)


        self.horizontalLayout_10.addWidget(self.QW111113)

        self.ProjectManagerTabs.addTab(self.Main, "")
        self.Docs = QWidget()
        self.Docs.setObjectName(u"Docs")
        self.horizontalLayout_9 = QHBoxLayout(self.Docs)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.QW111121 = QWidget(self.Docs)
        self.QW111121.setObjectName(u"QW111121")
        self.QW111121.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.QW111121)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.QLB1111211 = QHBoxLayout()
        self.QLB1111211.setObjectName(u"QLB1111211")
        self.QW11112111 = QWidget(self.QW111121)
        self.QW11112111.setObjectName(u"QW11112111")
        self.QW11112111.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.QW11112111)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.QL111121111 = QLabel(self.QW11112111)
        self.QL111121111.setObjectName(u"QL111121111")
        self.QL111121111.setFont(font)
        self.QL111121111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.QL111121111)

        self.BTN111121111 = QPushButton(self.QW11112111)
        self.BTN111121111.setObjectName(u"BTN111121111")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.BTN111121111.sizePolicy().hasHeightForWidth())
        self.BTN111121111.setSizePolicy(sizePolicy8)
        self.BTN111121111.setMinimumSize(QSize(0, 0))
        self.BTN111121111.setFont(font)
        self.BTN111121111.setIconSize(QSize(32, 32))

        self.verticalLayout_25.addWidget(self.BTN111121111)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_7)

        self.BTN111121133 = QPushButton(self.QW11112111)
        self.BTN111121133.setObjectName(u"BTN111121133")
        sizePolicy8.setHeightForWidth(self.BTN111121133.sizePolicy().hasHeightForWidth())
        self.BTN111121133.setSizePolicy(sizePolicy8)
        self.BTN111121133.setFont(font)
        self.BTN111121133.setStyleSheet(u"")

        self.verticalLayout_25.addWidget(self.BTN111121133)

        self.BTN111121134 = QPushButton(self.QW11112111)
        self.BTN111121134.setObjectName(u"BTN111121134")
        sizePolicy8.setHeightForWidth(self.BTN111121134.sizePolicy().hasHeightForWidth())
        self.BTN111121134.setSizePolicy(sizePolicy8)
        self.BTN111121134.setFont(font)
        self.BTN111121134.setIconSize(QSize(32, 32))

        self.verticalLayout_25.addWidget(self.BTN111121134)


        self.QLB1111211.addWidget(self.QW11112111)

        self.QW11112112 = QWidget(self.QW111121)
        self.QW11112112.setObjectName(u"QW11112112")
        self.QW11112112.setMinimumSize(QSize(0, 0))
        self.QW11112112.setStyleSheet(u"")
        self.verticalLayout_26 = QVBoxLayout(self.QW11112112)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.QL111121121 = QLabel(self.QW11112112)
        self.QL111121121.setObjectName(u"QL111121121")
        self.QL111121121.setFont(font)
        self.QL111121121.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_26.addWidget(self.QL111121121)

        self.tW111121121 = QTabWidget(self.QW11112112)
        self.tW111121121.setObjectName(u"tW111121121")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_27 = QVBoxLayout(self.tab)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.QW11112112111 = QWidget(self.tab)
        self.QW11112112111.setObjectName(u"QW11112112111")
        self.verticalLayout_28 = QVBoxLayout(self.QW11112112111)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.sA111121121111 = QScrollArea(self.QW11112112111)
        self.sA111121121111.setObjectName(u"sA111121121111")
        self.sA111121121111.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 165, 383))
        self.sA111121121111.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_28.addWidget(self.sA111121121111)


        self.verticalLayout_27.addWidget(self.QW11112112111)

        self.tW111121121.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tW111121121.addTab(self.tab_2, "")

        self.verticalLayout_26.addWidget(self.tW111121121)


        self.QLB1111211.addWidget(self.QW11112112)

        self.QW11112113 = QWidget(self.QW111121)
        self.QW11112113.setObjectName(u"QW11112113")
        self.QW11112113.setStyleSheet(u"")
        self.verticalLayout_29 = QVBoxLayout(self.QW11112113)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_7 = QLabel(self.QW11112113)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_7)

        self.comboBox_9 = QComboBox(self.QW11112113)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.verticalLayout_29.addWidget(self.comboBox_9)

        self.comboBox_10 = QComboBox(self.QW11112113)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.verticalLayout_29.addWidget(self.comboBox_10)

        self.lineEdit_6 = QLineEdit(self.QW11112113)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_29.addWidget(self.lineEdit_6)

        self.QSATOF111121131 = QScrollArea(self.QW11112113)
        self.QSATOF111121131.setObjectName(u"QSATOF111121131")
        self.QSATOF111121131.setWidgetResizable(True)
        self.SAWTOF1111211311 = QWidget()
        self.SAWTOF1111211311.setObjectName(u"SAWTOF1111211311")
        self.SAWTOF1111211311.setGeometry(QRect(0, 0, 190, 331))
        self.verticalLayout_30 = QVBoxLayout(self.SAWTOF1111211311)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.SAWTOFL11112113111 = QVBoxLayout()
        self.SAWTOFL11112113111.setObjectName(u"SAWTOFL11112113111")

        self.verticalLayout_30.addLayout(self.SAWTOFL11112113111)

        self.QSATOF111121131.setWidget(self.SAWTOF1111211311)

        self.verticalLayout_29.addWidget(self.QSATOF111121131)

        self.BTN111121112 = QPushButton(self.QW11112113)
        self.BTN111121112.setObjectName(u"BTN111121112")
        sizePolicy8.setHeightForWidth(self.BTN111121112.sizePolicy().hasHeightForWidth())
        self.BTN111121112.setSizePolicy(sizePolicy8)
        self.BTN111121112.setMinimumSize(QSize(0, 0))
        self.BTN111121112.setFont(font)

        self.verticalLayout_29.addWidget(self.BTN111121112)

        self.BTN111121113 = QPushButton(self.QW11112113)
        self.BTN111121113.setObjectName(u"BTN111121113")
        sizePolicy8.setHeightForWidth(self.BTN111121113.sizePolicy().hasHeightForWidth())
        self.BTN111121113.setSizePolicy(sizePolicy8)
        self.BTN111121113.setMinimumSize(QSize(0, 0))
        self.BTN111121113.setFont(font)

        self.verticalLayout_29.addWidget(self.BTN111121113)


        self.QLB1111211.addWidget(self.QW11112113)


        self.verticalLayout_18.addLayout(self.QLB1111211)


        self.horizontalLayout_9.addWidget(self.QW111121)

        self.ProjectManagerTabs.addTab(self.Docs, "")
        self.TOF = QWidget()
        self.TOF.setObjectName(u"TOF")
        self.verticalLayout_2 = QVBoxLayout(self.TOF)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.QW111131 = QWidget(self.TOF)
        self.QW111131.setObjectName(u"QW111131")
        self.QW111131.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.QW111131)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.QL1111311 = QLabel(self.QW111131)
        self.QL1111311.setObjectName(u"QL1111311")
        self.QL1111311.setFont(font)
        self.QL1111311.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.QL1111311)

        self.hLW1111311 = QHBoxLayout()
        self.hLW1111311.setObjectName(u"hLW1111311")
        self.QW11113111 = QWidget(self.QW111131)
        self.QW11113111.setObjectName(u"QW11113111")
        self.QW11113111.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.QW11113111)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.QL111131111 = QLabel(self.QW11113111)
        self.QL111131111.setObjectName(u"QL111131111")
        self.QL111131111.setFont(font)
        self.QL111131111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.QL111131111)

        self.BTN111131111 = QPushButton(self.QW11113111)
        self.BTN111131111.setObjectName(u"BTN111131111")
        sizePolicy8.setHeightForWidth(self.BTN111131111.sizePolicy().hasHeightForWidth())
        self.BTN111131111.setSizePolicy(sizePolicy8)
        self.BTN111131111.setFont(font)

        self.verticalLayout_13.addWidget(self.BTN111131111)

        self.BTN111131112 = QPushButton(self.QW11113111)
        self.BTN111131112.setObjectName(u"BTN111131112")
        sizePolicy8.setHeightForWidth(self.BTN111131112.sizePolicy().hasHeightForWidth())
        self.BTN111131112.setSizePolicy(sizePolicy8)
        self.BTN111131112.setFont(font)

        self.verticalLayout_13.addWidget(self.BTN111131112)

        self.BTN111131113 = QPushButton(self.QW11113111)
        self.BTN111131113.setObjectName(u"BTN111131113")
        sizePolicy8.setHeightForWidth(self.BTN111131113.sizePolicy().hasHeightForWidth())
        self.BTN111131113.setSizePolicy(sizePolicy8)
        self.BTN111131113.setFont(font)

        self.verticalLayout_13.addWidget(self.BTN111131113)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.BTN111131114 = QPushButton(self.QW11113111)
        self.BTN111131114.setObjectName(u"BTN111131114")
        sizePolicy8.setHeightForWidth(self.BTN111131114.sizePolicy().hasHeightForWidth())
        self.BTN111131114.setSizePolicy(sizePolicy8)
        self.BTN111131114.setFont(font)

        self.verticalLayout_13.addWidget(self.BTN111131114)

        self.BTN111131115 = QPushButton(self.QW11113111)
        self.BTN111131115.setObjectName(u"BTN111131115")
        sizePolicy8.setHeightForWidth(self.BTN111131115.sizePolicy().hasHeightForWidth())
        self.BTN111131115.setSizePolicy(sizePolicy8)
        self.BTN111131115.setFont(font)

        self.verticalLayout_13.addWidget(self.BTN111131115)


        self.hLW1111311.addWidget(self.QW11113111)

        self.QW11113112 = QWidget(self.QW111131)
        self.QW11113112.setObjectName(u"QW11113112")
        self.verticalLayout_14 = QVBoxLayout(self.QW11113112)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label = QLabel(self.QW11113112)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label)

        self.comboBox_4 = QComboBox(self.QW11113112)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_14.addWidget(self.comboBox_4)

        self.lineEdit_3 = QLineEdit(self.QW11113112)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_14.addWidget(self.lineEdit_3)

        self.QSATOF = QScrollArea(self.QW11113112)
        self.QSATOF.setObjectName(u"QSATOF")
        self.QSATOF.setWidgetResizable(True)
        self.SAWTOF = QWidget()
        self.SAWTOF.setObjectName(u"SAWTOF")
        self.SAWTOF.setGeometry(QRect(0, 0, 198, 308))
        self.verticalLayout_15 = QVBoxLayout(self.SAWTOF)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.SAWTOFLayout = QVBoxLayout()
        self.SAWTOFLayout.setObjectName(u"SAWTOFLayout")

        self.verticalLayout_15.addLayout(self.SAWTOFLayout)

        self.QSATOF.setWidget(self.SAWTOF)

        self.verticalLayout_14.addWidget(self.QSATOF)

        self.comboBox_5 = QComboBox(self.QW11113112)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_14.addWidget(self.comboBox_5)

        self.BTN111131123 = QPushButton(self.QW11113112)
        self.BTN111131123.setObjectName(u"BTN111131123")
        sizePolicy8.setHeightForWidth(self.BTN111131123.sizePolicy().hasHeightForWidth())
        self.BTN111131123.setSizePolicy(sizePolicy8)
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

        self.verticalLayout_14.addWidget(self.BTN111131123)

        self.BTN111131124 = QPushButton(self.QW11113112)
        self.BTN111131124.setObjectName(u"BTN111131124")
        sizePolicy8.setHeightForWidth(self.BTN111131124.sizePolicy().hasHeightForWidth())
        self.BTN111131124.setSizePolicy(sizePolicy8)
        self.BTN111131124.setFont(font)
        self.BTN111131124.setIconSize(QSize(32, 32))

        self.verticalLayout_14.addWidget(self.BTN111131124)


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

        self.lineEdit_5 = QLineEdit(self.QW11113113)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_16.addWidget(self.lineEdit_5)

        self.QSADataTOF = QScrollArea(self.QW11113113)
        self.QSADataTOF.setObjectName(u"QSADataTOF")
        self.QSADataTOF.setWidgetResizable(True)
        self.SAWTOFData = QWidget()
        self.SAWTOFData.setObjectName(u"SAWTOFData")
        self.SAWTOFData.setGeometry(QRect(0, 0, 178, 308))
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
        sizePolicy8.setHeightForWidth(self.BTN111131133.sizePolicy().hasHeightForWidth())
        self.BTN111131133.setSizePolicy(sizePolicy8)
        self.BTN111131133.setFont(font)
        self.BTN111131133.setIconSize(QSize(32, 32))

        self.verticalLayout_16.addWidget(self.BTN111131133)

        self.BTN111131134 = QPushButton(self.QW11113113)
        self.BTN111131134.setObjectName(u"BTN111131134")
        sizePolicy8.setHeightForWidth(self.BTN111131134.sizePolicy().hasHeightForWidth())
        self.BTN111131134.setSizePolicy(sizePolicy8)
        self.BTN111131134.setFont(font)
        self.BTN111131134.setIconSize(QSize(32, 32))

        self.verticalLayout_16.addWidget(self.BTN111131134)


        self.hLW1111311.addWidget(self.QW11113113)


        self.verticalLayout_12.addLayout(self.hLW1111311)


        self.verticalLayout_2.addWidget(self.QW111131)

        self.ProjectManagerTabs.addTab(self.TOF, "")
        self.Projects = QWidget()
        self.Projects.setObjectName(u"Projects")
        self.horizontalLayout_8 = QHBoxLayout(self.Projects)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.QW1111412 = QWidget(self.Projects)
        self.QW1111412.setObjectName(u"QW1111412")
        self.QW1111412.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.QW1111412)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.QL11114121 = QLabel(self.QW1111412)
        self.QL11114121.setObjectName(u"QL11114121")
        self.QL11114121.setFont(font)
        self.QL11114121.setStyleSheet(u"QWidget {  \n"
"	font-size: 36px;\n"
"}  ")
        self.QL11114121.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.QL11114121)

        self.comboBox_2 = QComboBox(self.QW1111412)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEditable(False)

        self.verticalLayout_24.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.QW1111412)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.verticalLayout_24.addWidget(self.comboBox)

        self.lineEdit_4 = QLineEdit(self.QW1111412)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_24.addWidget(self.lineEdit_4)

        self.listWidget_3 = QListWidget(self.QW1111412)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setStyleSheet(u"font-size: 20px")

        self.verticalLayout_24.addWidget(self.listWidget_3)

        self.BTN11114122 = QPushButton(self.QW1111412)
        self.BTN11114122.setObjectName(u"BTN11114122")
        sizePolicy8.setHeightForWidth(self.BTN11114122.sizePolicy().hasHeightForWidth())
        self.BTN11114122.setSizePolicy(sizePolicy8)
        self.BTN11114122.setFont(font)

        self.verticalLayout_24.addWidget(self.BTN11114122)


        self.horizontalLayout_8.addWidget(self.QW1111412)

        self.QW1111411 = QWidget(self.Projects)
        self.QW1111411.setObjectName(u"QW1111411")
        self.QW1111411.setMaximumSize(QSize(400, 16777215))
        self.QW1111411.setStyleSheet(u"")
        self.verticalLayout_23 = QVBoxLayout(self.QW1111411)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.QL11114111 = QLabel(self.QW1111411)
        self.QL11114111.setObjectName(u"QL11114111")
        self.QL11114111.setFont(font)
        self.QL11114111.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.QL11114111)

        self.QL11114112 = QLabel(self.QW1111411)
        self.QL11114112.setObjectName(u"QL11114112")
        font3 = QFont()
        font3.setFamilies([u"Jura"])
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.QL11114112.setFont(font3)
        self.QL11114112.setStyleSheet(u"QWidget {  \n"
"	font-size: 16px;\n"
"}  ")
        self.QL11114112.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.QL11114112)

        self.listWidget_4 = QListWidget(self.QW1111411)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setStyleSheet(u"font-size: 20px")

        self.verticalLayout_23.addWidget(self.listWidget_4)

        self.BTN11114123 = QPushButton(self.QW1111411)
        self.BTN11114123.setObjectName(u"BTN11114123")
        sizePolicy8.setHeightForWidth(self.BTN11114123.sizePolicy().hasHeightForWidth())
        self.BTN11114123.setSizePolicy(sizePolicy8)
        self.BTN11114123.setFont(font)

        self.verticalLayout_23.addWidget(self.BTN11114123)

        self.BTN11114116 = QPushButton(self.QW1111411)
        self.BTN11114116.setObjectName(u"BTN11114116")
        sizePolicy8.setHeightForWidth(self.BTN11114116.sizePolicy().hasHeightForWidth())
        self.BTN11114116.setSizePolicy(sizePolicy8)
        self.BTN11114116.setMinimumSize(QSize(333, 0))
        self.BTN11114116.setFont(font)
        self.BTN11114116.setIconSize(QSize(32, 32))

        self.verticalLayout_23.addWidget(self.BTN11114116)

        self.BTN11114123_2 = QPushButton(self.QW1111411)
        self.BTN11114123_2.setObjectName(u"BTN11114123_2")
        sizePolicy8.setHeightForWidth(self.BTN11114123_2.sizePolicy().hasHeightForWidth())
        self.BTN11114123_2.setSizePolicy(sizePolicy8)
        self.BTN11114123_2.setFont(font)

        self.verticalLayout_23.addWidget(self.BTN11114123_2)

        self.BTN11114116_2 = QPushButton(self.QW1111411)
        self.BTN11114116_2.setObjectName(u"BTN11114116_2")
        sizePolicy8.setHeightForWidth(self.BTN11114116_2.sizePolicy().hasHeightForWidth())
        self.BTN11114116_2.setSizePolicy(sizePolicy8)
        self.BTN11114116_2.setMinimumSize(QSize(333, 0))
        self.BTN11114116_2.setFont(font)
        self.BTN11114116_2.setIconSize(QSize(32, 32))

        self.verticalLayout_23.addWidget(self.BTN11114116_2)


        self.horizontalLayout_8.addWidget(self.QW1111411)

        self.ProjectManagerTabs.addTab(self.Projects, "")

        self.verticalLayout_6.addWidget(self.ProjectManagerTabs)

        self.stack_managers.addWidget(self.page_project_manager)
        self.zero_page = QWidget()
        self.zero_page.setObjectName(u"zero_page")
        self.stack_managers.addWidget(self.zero_page)

        self.horizontalLayout_6.addWidget(self.stack_managers)

        self.QW1111_4 = QWidget(self.page_5)
        self.QW1111_4.setObjectName(u"QW1111_4")
        self.QW1111_4.setMinimumSize(QSize(275, 0))
        self.QW1111_4.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 100);\n"
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
        self.verticalLayout_34 = QVBoxLayout(self.QW1111_4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.LL11111_Addons_2 = QLabel(self.QW1111_4)
        self.LL11111_Addons_2.setObjectName(u"LL11111_Addons_2")
        sizePolicy4.setHeightForWidth(self.LL11111_Addons_2.sizePolicy().hasHeightForWidth())
        self.LL11111_Addons_2.setSizePolicy(sizePolicy4)
        self.LL11111_Addons_2.setMinimumSize(QSize(0, 0))
        self.LL11111_Addons_2.setMaximumSize(QSize(16777215, 50))
        self.LL11111_Addons_2.setFont(font2)
        self.LL11111_Addons_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_34.addWidget(self.LL11111_Addons_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.lineEdit_7 = QLineEdit(self.QW1111_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy4.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy4)

        self.verticalLayout_34.addWidget(self.lineEdit_7)

        self.listWidget_5 = QListWidget(self.QW1111_4)
        self.listWidget_5.setObjectName(u"listWidget_5")
        sizePolicy5.setHeightForWidth(self.listWidget_5.sizePolicy().hasHeightForWidth())
        self.listWidget_5.setSizePolicy(sizePolicy5)
        self.listWidget_5.setViewMode(QListView.ViewMode.IconMode)

        self.verticalLayout_34.addWidget(self.listWidget_5)

        self.BTN11111_2 = QPushButton(self.QW1111_4)
        self.BTN11111_2.setObjectName(u"BTN11111_2")
        self.BTN11111_2.setFont(font)

        self.verticalLayout_34.addWidget(self.BTN11111_2)


        self.horizontalLayout_6.addWidget(self.QW1111_4)

        self.StackW.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_7 = QHBoxLayout(self.page_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.StackW.addWidget(self.page_6)

        self.QLB111.addWidget(self.StackW)


        self.verticalLayout.addLayout(self.QLB111)

        self.QLB112 = QVBoxLayout()
        self.QLB112.setObjectName(u"QLB112")
        self.SW1121 = QStackedWidget(self.QW11)
        self.SW1121.setObjectName(u"SW1121")
        self.SW1121.setStyleSheet(u"border: 0px;")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_20 = QVBoxLayout(self.page_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.PTE11211_console = QPlainTextEdit(self.page_7)
        self.PTE11211_console.setObjectName(u"PTE11211_console")
        font4 = QFont()
        font4.setFamilies([u"Courier"])
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.PTE11211_console.setFont(font4)
        self.PTE11211_console.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgba(20, 30, 40, 100);\n"
"    color: #fff;\n"
"    font-family: 'Courier';\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QPlainTextEdit QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.PTE11211_console.setReadOnly(False)

        self.verticalLayout_20.addWidget(self.PTE11211_console)

        self.SW1121.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_21 = QVBoxLayout(self.page_8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.PTE11211_editorRulesAndApps = QPlainTextEdit(self.page_8)
        self.PTE11211_editorRulesAndApps.setObjectName(u"PTE11211_editorRulesAndApps")
        self.PTE11211_editorRulesAndApps.setFont(font4)
        self.PTE11211_editorRulesAndApps.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgba(20, 30, 40, 100);\n"
"    color: #fff;\n"
"    font-family: 'Courier';\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QPlainTextEdit QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.PTE11211_editorRulesAndApps.setReadOnly(True)

        self.verticalLayout_21.addWidget(self.PTE11211_editorRulesAndApps)

        self.SW1121.addWidget(self.page_8)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_19 = QVBoxLayout(self.page_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.PTE1121_logs = QPlainTextEdit(self.page_10)
        self.PTE1121_logs.setObjectName(u"PTE1121_logs")
        self.PTE1121_logs.setFont(font4)
        self.PTE1121_logs.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgba(20, 30, 40, 100);\n"
"    color: #fff;\n"
"    font-family: 'Courier';\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QPlainTextEdit QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.PTE1121_logs.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.PTE1121_logs)

        self.SW1121.addWidget(self.page_10)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_22 = QVBoxLayout(self.page_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.PTE1121_assistentAI = QPlainTextEdit(self.page_9)
        self.PTE1121_assistentAI.setObjectName(u"PTE1121_assistentAI")
        self.PTE1121_assistentAI.setFont(font4)
        self.PTE1121_assistentAI.setStyleSheet(u"QWidget {\n"
"	border: 1px solid rgb(0, 100, 100);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgba(20, 30, 40, 100);\n"
"    color: #fff;\n"
"    font-family: 'Courier';\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPlainTextEdit QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"QPlainTextEdit QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.PTE1121_assistentAI.setReadOnly(True)

        self.verticalLayout_22.addWidget(self.PTE1121_assistentAI)

        self.SW1121.addWidget(self.page_9)

        self.QLB112.addWidget(self.SW1121)


        self.verticalLayout.addLayout(self.QLB112)

        self.QW113 = QWidget(self.QW11)
        self.QW113.setObjectName(u"QW113")
        self.QW113.setStyleSheet(u"QWidget {\n"
"	color: rgb(100, 200, 200);\n"
"	background-color: rgba(20, 30, 40, 100);\n"
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
        self.horizontalLayout = QHBoxLayout(self.QW113)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BTN1131 = QPushButton(self.QW113)
        self.BTN1131.setObjectName(u"BTN1131")
        self.BTN1131.setFont(font)

        self.horizontalLayout.addWidget(self.BTN1131)

        self.BTN1132 = QPushButton(self.QW113)
        self.BTN1132.setObjectName(u"BTN1132")

        self.horizontalLayout.addWidget(self.BTN1132)

        self.BTN1133 = QPushButton(self.QW113)
        self.BTN1133.setObjectName(u"BTN1133")

        self.horizontalLayout.addWidget(self.BTN1133)

        self.BTN1134 = QPushButton(self.QW113)
        self.BTN1134.setObjectName(u"BTN1134")

        self.horizontalLayout.addWidget(self.BTN1134)

        self.BTN1135 = QPushButton(self.QW113)
        self.BTN1135.setObjectName(u"BTN1135")

        self.horizontalLayout.addWidget(self.BTN1135)

        self.BTN1136 = QPushButton(self.QW113)
        self.BTN1136.setObjectName(u"BTN1136")

        self.horizontalLayout.addWidget(self.BTN1136)

        self.BTN1137 = QPushButton(self.QW113)
        self.BTN1137.setObjectName(u"BTN1137")

        self.horizontalLayout.addWidget(self.BTN1137)

        self.BTN1138 = QToolButton(self.QW113)
        self.BTN1138.setObjectName(u"BTN1138")

        self.horizontalLayout.addWidget(self.BTN1138)


        self.verticalLayout.addWidget(self.QW113)

        QMW1.setCentralWidget(self.QW11)
        self.QMBar11 = QMenuBar(QMW1)
        self.QMBar11.setObjectName(u"QMBar11")
        self.QMBar11.setGeometry(QRect(0, 0, 1738, 33))
        self.QM112 = QMenu(self.QMBar11)
        self.QM112.setObjectName(u"QM112")
        self.menu = QMenu(self.QM112)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.QM112)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.QM112)
        self.menu_3.setObjectName(u"menu_3")
        QMW1.setMenuBar(self.QMBar11)

        self.QMBar11.addAction(self.QM112.menuAction())
        self.QM112.addAction(self.menu.menuAction())
        self.QM112.addAction(self.menu_2.menuAction())
        self.QM112.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_gif)
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.action_8)

        self.retranslateUi(QMW1)

        self.StackW.setCurrentIndex(0)
        self.SW111121.setCurrentIndex(1)
        self.stack_managers.setCurrentIndex(0)
        self.ProjectManagerTabs.setCurrentIndex(3)
        self.tW111121121.setCurrentIndex(0)
        self.SW1121.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(QMW1)
    # setupUi

    def retranslateUi(self, QMW1):
        QMW1.setWindowTitle(QCoreApplication.translate("QMW1", u"VSDragon1239 - \"Base Structure\" ", None))
        self.action.setText(QCoreApplication.translate("QMW1", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435", None))
        self.AOptions.setText(QCoreApplication.translate("QMW1", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u043d\u044b", None))
        self.action_2.setText(QCoreApplication.translate("QMW1", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u043c\u0443", None))
        self.action_4.setText(QCoreApplication.translate("QMW1", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u043c\u0443", None))
        self.action_6.setText(QCoreApplication.translate("QMW1", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.action_8.setText(QCoreApplication.translate("QMW1", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c...", None))
        self.action_gif.setText(QCoreApplication.translate("QMW1", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c gif - \u0444\u043e\u043d", None))
        self.action_3.setText(QCoreApplication.translate("QMW1", u"\u0424\u043e\u043d\u043e\u0432\u0430\u044f \u043c\u0443\u0437\u044b\u043a\u0430", None))
        self.QL111121_3.setText("")
        self.QL111121_2.setText(QCoreApplication.translate("QMW1", u"\u00ab VSDragon1239 \u00bb", None))
        self.QL111111.setText(QCoreApplication.translate("QMW1", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.BTN1111111.setText(QCoreApplication.translate("QMW1", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.BTN1111112.setText(QCoreApplication.translate("QMW1", u"\u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
        self.BTN1111112_2.setText(QCoreApplication.translate("QMW1", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.BTN1111113.setText(QCoreApplication.translate("QMW1", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.BTN1111114.setText(QCoreApplication.translate("QMW1", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430", None))
        self.SLL22141_name.setText(QCoreApplication.translate("QMW1", u"\u041f\u0420\u041e\u0424\u0418\u041b\u042c", None))
        self.SB22141.setText(QCoreApplication.translate("QMW1", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.SB22142.setText(QCoreApplication.translate("QMW1", u"\u041d\u0430\u0432\u044b\u043a\u0438", None))
        self.SB22143.setText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u044f", None))
        self.SB22144.setText(QCoreApplication.translate("QMW1", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.LL11111_GPLabel.setText(QCoreApplication.translate("QMW1", u"\u0413\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u044b\u0435 \u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.BTN11112.setText(QCoreApplication.translate("QMW1", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0413\u041f", None))
        self.LL11111_Addons.setText(QCoreApplication.translate("QMW1", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.BTN11111.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044e", None))
        self.SLL111121311.setText(QCoreApplication.translate("QMW1", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.SB111121311.setText(QCoreApplication.translate("QMW1", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.SB111121312.setText(QCoreApplication.translate("QMW1", u"\u0421\u0435\u0440\u0432\u0435\u0440\u043d\u044b\u0439 \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.SB111121313.setText(QCoreApplication.translate("QMW1", u"\u041d\u043e\u0443\u0442\u0431\u0443\u043a \u0434\u043b\u044f \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.SB111121314.setText(QCoreApplication.translate("QMW1", u"3D-\u041f\u0440\u0438\u043d\u0442\u0435\u0440", None))
        self.SB111121315.setText(QCoreApplication.translate("QMW1", u"DVD-\u041f\u0440\u0438\u0432\u043e\u0434", None))
        self.SLL111121321.setText(QCoreApplication.translate("QMW1", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430", None))
        self.SB111121321.setText(QCoreApplication.translate("QMW1", u"\u041b\u043e\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u0413\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u043e\u0435 \u0425\u0440\u0430\u043d\u0438\u043b\u0438\u0449\u0435", None))
        self.SB111121322.setText(QCoreApplication.translate("QMW1", u"\u0421\u0435\u0440\u0432\u0435\u0440\u043d\u043e\u0435 \u0413\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u043e\u0435 \u0425\u0440\u0430\u043d\u0438\u043b\u0438\u0449\u0435", None))
        self.SB111121323.setText(QCoreApplication.translate("QMW1", u"\u0418\u043d\u044b\u0435 \u041e\u0431\u043b\u0430\u0447\u043d\u044b\u0435 \u0445\u0440\u0430\u043d\u0438\u043b\u0438\u0449\u0430", None))
        self.SB111121324.setText(QCoreApplication.translate("QMW1", u"\u0417\u0432\u0451\u0437\u0434\u0430\u043d\u0443\u0442\u044b\u0439 \u00abGitHooves\u00bb", None))
        self.SB111121325.setText(QCoreApplication.translate("QMW1", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0438 \u0440\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.SLL111121321_2.setText(QCoreApplication.translate("QMW1", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.BTN111111.setText(QCoreApplication.translate("QMW1", u"\u0411\u0430\u0437\u0430 \u0414\u0430\u043d\u043d\u044b\u0445", None))
        self.BTN111112.setText(QCoreApplication.translate("QMW1", u"\u0420\u0435\u0437\u0435\u0440\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.BTN111113.setText(QCoreApplication.translate("QMW1", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.BTN111114.setText(QCoreApplication.translate("QMW1", u"\u0417\u0435\u0440\u043a\u0430\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.QL1111111.setText(QCoreApplication.translate("QMW1", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.BTN111111_2.setText(QCoreApplication.translate("QMW1", u"\u0412\u0441\u0435 F-\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.BTN111112_2.setText(QCoreApplication.translate("QMW1", u"\u0427\u0442\u043e- \u0442\u043e \u043d\u0430 \u0432\u044b\u0441\u043e\u043a\u043e\u043c", None))
        self.BTN111113_2.setText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 F-\u0424\u0430\u0439\u043b\u044b", None))
        self.BTN111114_2.setText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0447\u0442\u043e \u0442\u043e", None))
        self.QL1111121.setText(QCoreApplication.translate("QMW1", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.BTN1111121.setText(QCoreApplication.translate("QMW1", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c F-\u0417\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.BTN1111122.setText(QCoreApplication.translate("QMW1", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.BTN1111123.setText(QCoreApplication.translate("QMW1", u"  \u041e\u0447\u0438\u0441\u0442\u043a\u0430 F-\u0414\u0430\u043d\u043d\u044b\u0445  ", None))
        self.BTN1111124.setText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0447\u0442\u043e \u0442\u043e", None))
        self.QL1111131.setText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0441\u0442\u0443\u043f", None))
        self.BTN1111131.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c F-\u0417\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.BTN1111132.setText(QCoreApplication.translate("QMW1", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0441\u0435\u0445 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.BTN1111133.setText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 F-\u0424\u0430\u0439\u043b\u044b", None))
        self.BTN1111134.setText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0447\u0442\u043e \u0442\u043e", None))
        self.ProjectManagerTabs.setTabText(self.ProjectManagerTabs.indexOf(self.Main), QCoreApplication.translate("QMW1", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.QL111121111.setText(QCoreApplication.translate("QMW1", u"   \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438   ", None))
        self.BTN111121111.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u043c", None))
        self.BTN111121133.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u00abMS Word\u00bb", None))
#if QT_CONFIG(tooltip)
        self.BTN111121134.setToolTip(QCoreApplication.translate("QMW1", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN111121134.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u0411\u043b\u043e\u043a\u043d\u043e\u0442\u0435", None))
        self.QL111121121.setText(QCoreApplication.translate("QMW1", u"   \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432   ", None))
        self.tW111121121.setTabText(self.tW111121121.indexOf(self.tab), QCoreApplication.translate("QMW1", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 1", None))
        self.tW111121121.setTabText(self.tW111121121.indexOf(self.tab_2), QCoreApplication.translate("QMW1", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442 2", None))
        self.label_7.setText(QCoreApplication.translate("QMW1", u"        \u0421\u043f\u0438\u0441\u043e\u043a \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432        ", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("QMW1", u"\u0410-\u042f", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("QMW1", u"\u042f-\u0410", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))

        self.comboBox_10.setItemText(0, QCoreApplication.translate("QMW1", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("QMW1", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))

        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.BTN111121112.setText(QCoreApplication.translate("QMW1", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.BTN111121113.setText(QCoreApplication.translate("QMW1", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.ProjectManagerTabs.setTabText(self.ProjectManagerTabs.indexOf(self.Docs), QCoreApplication.translate("QMW1", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f", None))
        self.QL1111311.setText(QCoreApplication.translate("QMW1", u"\u0412\u0441\u0435\u043e\u0431\u0449\u0430\u044f \u0442\u0435\u043e\u0440\u0438\u044f \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.QL111131111.setText(QCoreApplication.translate("QMW1", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.BTN111131111.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 PT-\u0414\u0430\u043d\u043d\u044b\u043c\u0438", None))
        self.BTN111131112.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 OND-\u0417\u0430\u043c\u0435\u0442\u043a\u0430\u043c\u0438", None))
        self.BTN111131113.setText(QCoreApplication.translate("QMW1", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u0432\u0441\u0435 OND-\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.BTN111131114.setText(QCoreApplication.translate("QMW1", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c PT-\u0414\u0430\u043d\u043d\u044b\u0435...", None))
        self.BTN111131115.setText(QCoreApplication.translate("QMW1", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c PT-\u0414\u0430\u043d\u043d\u044b\u0435...", None))
        self.label.setText(QCoreApplication.translate("QMW1", u"        \u0421\u043f\u0438\u0441\u043e\u043a OND-\u0417\u0430\u043c\u0435\u0442\u043e\u043a        ", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("QMW1", u"\u0410-\u042f", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("QMW1", u"\u042f-\u0410", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))

        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("QMW1", u"\u0422\u0438\u043f 1", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("QMW1", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("QMW1", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("QMW1", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("QMW1", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))

        self.BTN111131123.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u00abObsidian\u00bb", None))
#if QT_CONFIG(tooltip)
        self.BTN111131124.setToolTip(QCoreApplication.translate("QMW1", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN111131124.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 VSCode", None))
        self.QL111131131.setText(QCoreApplication.translate("QMW1", u"        \u0421\u043f\u0438\u0441\u043e\u043a PT-\u0414\u0430\u043d\u043d\u044b\u0445        ", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("QMW1", u"\u0410-\u042f", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("QMW1", u"\u042f-\u0410", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))

        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("QMW1", u"\u0422\u0438\u043f 1", None))

#if QT_CONFIG(tooltip)
        self.BTN111131133.setToolTip(QCoreApplication.translate("QMW1", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN111131133.setText(QCoreApplication.translate("QMW1", u"  \u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u041f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0435  ", None))
#if QT_CONFIG(tooltip)
        self.BTN111131134.setToolTip(QCoreApplication.translate("QMW1", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN111131134.setText(QCoreApplication.translate("QMW1", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0443\u0442\u044c", None))
        self.ProjectManagerTabs.setTabText(self.ProjectManagerTabs.indexOf(self.TOF), QCoreApplication.translate("QMW1", u"\u041e\u0431\u0449\u0430\u044f \u0442\u0435\u043e\u0440\u0438\u044f", None))
        self.QL11114121.setText(QCoreApplication.translate("QMW1", u"         \u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u043e\u0435\u043a\u0442\u043e\u0432         ", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("QMW1", u"\u0410-\u042f", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("QMW1", u"\u042f-\u0410", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("QMW1", u"\u0414\u0430\u0442\u0430 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("QMW1", u"\u0411\u0435\u0437 \u0444\u0438\u043b\u044c\u0442\u0440\u0430 \u0442\u0438\u043f\u0430", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("QMW1", u"Python", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("QMW1", u"Blender", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("QMW1", u"UnrealEngine", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("QMW1", u"Painting", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("QMW1", u"Imagers", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("QMW1", u"\u0411\u0435\u0437 \u0444\u0438\u043b\u044c\u0442\u0440\u0430 \u0442\u0438\u043f\u0430", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.BTN11114122.setText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.QL11114111.setText(QCoreApplication.translate("QMW1", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.QL11114112.setText(QCoreApplication.translate("QMW1", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430...", None))
        self.BTN11114123.setText(QCoreApplication.translate("QMW1", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435...", None))
#if QT_CONFIG(tooltip)
        self.BTN11114116.setToolTip(QCoreApplication.translate("QMW1", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN11114116.setText(QCoreApplication.translate("QMW1", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442...", None))
        self.BTN11114123_2.setText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044e...", None))
#if QT_CONFIG(tooltip)
        self.BTN11114116_2.setToolTip(QCoreApplication.translate("QMW1", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0435 \u0442\u0438\u043f\u044b: \u0417\u0430\u043c\u0435\u0442\u043a\u0438; \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f; \u0414\u0440\u0443\u0433\u0438\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.BTN11114116_2.setText(QCoreApplication.translate("QMW1", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438...", None))
        self.ProjectManagerTabs.setTabText(self.ProjectManagerTabs.indexOf(self.Projects), QCoreApplication.translate("QMW1", u"\u041f\u0440\u043e\u0435\u043a\u0442\u044b", None))
        self.LL11111_Addons_2.setText(QCoreApplication.translate("QMW1", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("QMW1", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.BTN11111_2.setText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442", None))
        self.PTE11211_console.setPlainText(QCoreApplication.translate("QMW1", u">>", None))
        self.PTE11211_editorRulesAndApps.setPlainText(QCoreApplication.translate("QMW1", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0443\u0435\u043c \u043c\u043d\u043e\u0433\u043e \u0447\u0435\u0433\u043e...", None))
        self.PTE1121_logs.setPlainText("")
        self.PTE1121_assistentAI.setPlainText(QCoreApplication.translate("QMW1", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438\u0437\u0430\u0446\u0438\u043e\u043d\u043d\u0443\u044e \u043c\u043e\u044e \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438\u0437\u0430\u0446\u0438\u044e \u043f\u043e \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u0438 \u00abO.N.D.\u00bb\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"Hello World!", None))
        self.BTN1131.setText(QCoreApplication.translate("QMW1", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c", None))
        self.BTN1132.setText(QCoreApplication.translate("QMW1", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u043f\u0440\u0430\u0432\u0438\u043b \u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0439", None))
        self.BTN1133.setText(QCoreApplication.translate("QMW1", u"\u041b\u043e\u0433\u0438", None))
        self.BTN1134.setText(QCoreApplication.translate("QMW1", u"\u0418\u0418-\u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442", None))
        self.BTN1135.setText("")
        self.BTN1136.setText("")
        self.BTN1137.setText("")
        self.BTN1138.setText(QCoreApplication.translate("QMW1", u"...", None))
        self.QM112.setTitle(QCoreApplication.translate("QMW1", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu.setTitle(QCoreApplication.translate("QMW1", u"\u041e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u0435", None))
        self.menu_2.setTitle(QCoreApplication.translate("QMW1", u"\u0421\u0435\u0440\u0432\u0435\u0440", None))
        self.menu_3.setTitle(QCoreApplication.translate("QMW1", u"\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

