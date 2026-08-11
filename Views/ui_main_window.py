# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 750)
        MainWindow.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        MainWindow.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tabDashboard = QWidget()
        self.tabDashboard.setObjectName(u"tabDashboard")
        self.verticalLayout_5 = QVBoxLayout(self.tabDashboard)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frameTodayTasks = QFrame(self.tabDashboard)
        self.frameTodayTasks.setObjectName(u"frameTodayTasks")
        self.verticalLayout_2 = QVBoxLayout(self.frameTodayTasks)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_today_tasks_title = QLabel(self.frameTodayTasks)
        self.label_today_tasks_title.setObjectName(u"label_today_tasks_title")

        self.verticalLayout_2.addWidget(self.label_today_tasks_title)

        self.label_today_tasks_value = QLabel(self.frameTodayTasks)
        self.label_today_tasks_value.setObjectName(u"label_today_tasks_value")
        self.label_today_tasks_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_today_tasks_value)


        self.gridLayout.addWidget(self.frameTodayTasks, 0, 0, 1, 1)

        self.frameCompletedTasks = QFrame(self.tabDashboard)
        self.frameCompletedTasks.setObjectName(u"frameCompletedTasks")
        self.verticalLayout_3 = QVBoxLayout(self.frameCompletedTasks)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_completed_tasks_title = QLabel(self.frameCompletedTasks)
        self.label_completed_tasks_title.setObjectName(u"label_completed_tasks_title")

        self.verticalLayout_3.addWidget(self.label_completed_tasks_title)

        self.label_completed_tasks_value = QLabel(self.frameCompletedTasks)
        self.label_completed_tasks_value.setObjectName(u"label_completed_tasks_value")
        self.label_completed_tasks_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_completed_tasks_value)


        self.gridLayout.addWidget(self.frameCompletedTasks, 0, 1, 1, 1)

        self.framePendingTasks = QFrame(self.tabDashboard)
        self.framePendingTasks.setObjectName(u"framePendingTasks")
        self.verticalLayout_4 = QVBoxLayout(self.framePendingTasks)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_pending_tasks_title = QLabel(self.framePendingTasks)
        self.label_pending_tasks_title.setObjectName(u"label_pending_tasks_title")

        self.verticalLayout_4.addWidget(self.label_pending_tasks_title)

        self.label_pending_tasks_value = QLabel(self.framePendingTasks)
        self.label_pending_tasks_value.setObjectName(u"label_pending_tasks_value")
        self.label_pending_tasks_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_pending_tasks_value)


        self.gridLayout.addWidget(self.framePendingTasks, 1, 0, 1, 1)

        self.frameOverdueTasks = QFrame(self.tabDashboard)
        self.frameOverdueTasks.setObjectName(u"frameOverdueTasks")
        self.verticalLayout_6 = QVBoxLayout(self.frameOverdueTasks)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_overdue_tasks_title = QLabel(self.frameOverdueTasks)
        self.label_overdue_tasks_title.setObjectName(u"label_overdue_tasks_title")

        self.verticalLayout_6.addWidget(self.label_overdue_tasks_title)

        self.label_overdue_tasks_value = QLabel(self.frameOverdueTasks)
        self.label_overdue_tasks_value.setObjectName(u"label_overdue_tasks_value")
        self.label_overdue_tasks_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_overdue_tasks_value)


        self.gridLayout.addWidget(self.frameOverdueTasks, 1, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.labelRecentTasks = QLabel(self.tabDashboard)
        self.labelRecentTasks.setObjectName(u"labelRecentTasks")
        self.labelRecentTasks.setStyleSheet(u"font-size: 16px; font-weight: bold; color: #1c1c1e; margin-top: 10px;")

        self.verticalLayout_5.addWidget(self.labelRecentTasks)

        self.tableRecentTasks = QTableWidget(self.tabDashboard)
        if (self.tableRecentTasks.columnCount() < 4):
            self.tableRecentTasks.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableRecentTasks.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableRecentTasks.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableRecentTasks.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableRecentTasks.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableRecentTasks.setObjectName(u"tableRecentTasks")
        self.tableRecentTasks.setAlternatingRowColors(True)
        self.tableRecentTasks.horizontalHeader().setVisible(True)
        self.tableRecentTasks.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.tableRecentTasks)

        self.tabWidget.addTab(self.tabDashboard, "")
        self.tabTasks = QWidget()
        self.tabTasks.setObjectName(u"tabTasks")
        self.verticalLayout_7 = QVBoxLayout(self.tabTasks)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayoutTasks = QHBoxLayout()
        self.horizontalLayoutTasks.setObjectName(u"horizontalLayoutTasks")
        self.lineEditTaskTitle = QLineEdit(self.tabTasks)
        self.lineEditTaskTitle.setObjectName(u"lineEditTaskTitle")

        self.horizontalLayoutTasks.addWidget(self.lineEditTaskTitle)

        self.dateEditDueDate = QDateEdit(self.tabTasks)
        self.dateEditDueDate.setObjectName(u"dateEditDueDate")
        self.dateEditDueDate.setDateTime(QDateTime(QDate(2025, 12, 8), QTime(0, 0, 0)))
        self.dateEditDueDate.setCalendarPopup(True)

        self.horizontalLayoutTasks.addWidget(self.dateEditDueDate)

        self.comboBoxPriority = QComboBox(self.tabTasks)
        self.comboBoxPriority.setObjectName(u"comboBoxPriority")

        self.horizontalLayoutTasks.addWidget(self.comboBoxPriority)

        self.comboBoxPeriodType = QComboBox(self.tabTasks)
        self.comboBoxPeriodType.setObjectName(u"comboBoxPeriodType")

        self.horizontalLayoutTasks.addWidget(self.comboBoxPeriodType)

        self.btnAddTask = QPushButton(self.tabTasks)
        self.btnAddTask.setObjectName(u"btnAddTask")

        self.horizontalLayoutTasks.addWidget(self.btnAddTask)

        self.btnUpdateTask = QPushButton(self.tabTasks)
        self.btnUpdateTask.setObjectName(u"btnUpdateTask")

        self.horizontalLayoutTasks.addWidget(self.btnUpdateTask)

        self.btnDelete = QPushButton(self.tabTasks)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayoutTasks.addWidget(self.btnDelete)

        self.btnCompleteTask = QPushButton(self.tabTasks)
        self.btnCompleteTask.setObjectName(u"btnCompleteTask")

        self.horizontalLayoutTasks.addWidget(self.btnCompleteTask)


        self.verticalLayout_7.addLayout(self.horizontalLayoutTasks)

        self.textEditTaskDescription = QTextEdit(self.tabTasks)
        self.textEditTaskDescription.setObjectName(u"textEditTaskDescription")
        self.textEditTaskDescription.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditTaskDescription.sizePolicy().hasHeightForWidth())
        self.textEditTaskDescription.setSizePolicy(sizePolicy)
        self.textEditTaskDescription.setMinimumSize(QSize(0, 30))
        self.textEditTaskDescription.setMaximumSize(QSize(16777215, 16777215))
        self.textEditTaskDescription.setSizeIncrement(QSize(0, 0))
        self.textEditTaskDescription.setBaseSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.textEditTaskDescription)

        self.tableTasks = QTableWidget(self.tabTasks)
        if (self.tableTasks.columnCount() < 6):
            self.tableTasks.setColumnCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableTasks.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        self.tableTasks.setObjectName(u"tableTasks")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableTasks.sizePolicy().hasHeightForWidth())
        self.tableTasks.setSizePolicy(sizePolicy1)
        self.tableTasks.setAlternatingRowColors(True)
        self.tableTasks.setWordWrap(True)
        self.tableTasks.horizontalHeader().setVisible(True)
        self.tableTasks.horizontalHeader().setCascadingSectionResizes(True)
        self.tableTasks.horizontalHeader().setMinimumSectionSize(40)
        self.tableTasks.horizontalHeader().setStretchLastSection(True)
        self.tableTasks.verticalHeader().setCascadingSectionResizes(True)
        self.tableTasks.verticalHeader().setMinimumSectionSize(30)

        self.verticalLayout_7.addWidget(self.tableTasks)

        self.tabWidget.addTab(self.tabTasks, "")
        self.tabTimer = QWidget()
        self.tabTimer.setObjectName(u"tabTimer")
        self.verticalLayout_8 = QVBoxLayout(self.tabTimer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frameTimer = QFrame(self.tabTimer)
        self.frameTimer.setObjectName(u"frameTimer")
        self.frameTimer.setStyleSheet(u"QFrame#frameTimer {\n"
"                background-color: #f5f5f7;\n"
"                border-radius: 16px;\n"
"                padding: 10px;\n"
"                border: 2px solid #d2d2d7;\n"
"            }\n"
"            QFrame#frameTimer[state=\"work\"] {\n"
"                border-color: #34c759;\n"
"                background-color: rgba(52, 199, 89, 0.05);\n"
"            }\n"
"            QFrame#frameTimer[state=\"break\"] {\n"
"                border-color: #ff9500;\n"
"                background-color: rgba(255, 149, 0, 0.05);\n"
"            }\n"
"            QFrame#frameTimer[state=\"stopped\"] {\n"
"                border-color: #c7c7cc;\n"
"                background-color: #f5f5f7;\n"
"            }")
        self.verticalLayoutTimer = QVBoxLayout(self.frameTimer)
        self.verticalLayoutTimer.setObjectName(u"verticalLayoutTimer")
        self.labelTimerTitle = QLabel(self.frameTimer)
        self.labelTimerTitle.setObjectName(u"labelTimerTitle")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setBold(True)
        self.labelTimerTitle.setFont(font1)
        self.labelTimerTitle.setStyleSheet(u"font-size: 18px; font-weight: bold; color: #1c1c1e;")
        self.labelTimerTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayoutTimer.addWidget(self.labelTimerTitle)

        self.labelTimerStatus = QLabel(self.frameTimer)
        self.labelTimerStatus.setObjectName(u"labelTimerStatus")
        self.labelTimerStatus.setFont(font)
        self.labelTimerStatus.setStyleSheet(u"font-size: 16px; color: #6e6e73;")
        self.labelTimerStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayoutTimer.addWidget(self.labelTimerStatus)

        self.labelTimerTime = QLabel(self.frameTimer)
        self.labelTimerTime.setObjectName(u"labelTimerTime")
        self.labelTimerTime.setFont(font1)
        self.labelTimerTime.setStyleSheet(u"font-size: 48px; font-weight: bold; color: #34c759;")
        self.labelTimerTime.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayoutTimer.addWidget(self.labelTimerTime)

        self.horizontalLayoutTimer = QHBoxLayout()
        self.horizontalLayoutTimer.setObjectName(u"horizontalLayoutTimer")
        self.spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutTimer.addItem(self.spacerItem)

        self.btnStartWork = QPushButton(self.frameTimer)
        self.btnStartWork.setObjectName(u"btnStartWork")
        self.btnStartWork.setFont(font)
        self.btnStartWork.setStyleSheet(u"background-color: #34c759;")

        self.horizontalLayoutTimer.addWidget(self.btnStartWork)

        self.btnStartBreak = QPushButton(self.frameTimer)
        self.btnStartBreak.setObjectName(u"btnStartBreak")
        self.btnStartBreak.setFont(font)
        self.btnStartBreak.setStyleSheet(u"background-color: #ff9500;")

        self.horizontalLayoutTimer.addWidget(self.btnStartBreak)

        self.btnStopTimer = QPushButton(self.frameTimer)
        self.btnStopTimer.setObjectName(u"btnStopTimer")
        self.btnStopTimer.setFont(font)
        self.btnStopTimer.setStyleSheet(u"background-color: #ff3b30;")

        self.horizontalLayoutTimer.addWidget(self.btnStopTimer)

        self.spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutTimer.addItem(self.spacerItem1)


        self.verticalLayoutTimer.addLayout(self.horizontalLayoutTimer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBoxTimerTask = QComboBox(self.frameTimer)
        self.comboBoxTimerTask.setObjectName(u"comboBoxTimerTask")
        self.comboBoxTimerTask.setMinimumSize(QSize(120, 0))
        self.comboBoxTimerTask.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxTimerTask)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnDelete_2 = QPushButton(self.frameTimer)
        self.btnDelete_2.setObjectName(u"btnDelete_2")
        self.btnDelete_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnDelete_2.sizePolicy().hasHeightForWidth())
        self.btnDelete_2.setSizePolicy(sizePolicy2)
        self.btnDelete_2.setFont(font)

        self.horizontalLayout.addWidget(self.btnDelete_2)


        self.verticalLayoutTimer.addLayout(self.horizontalLayout)

        self.horizontalLayoutStats = QHBoxLayout()
        self.horizontalLayoutStats.setObjectName(u"horizontalLayoutStats")
        self.labelTimerStatsWork = QLabel(self.frameTimer)
        self.labelTimerStatsWork.setObjectName(u"labelTimerStatsWork")
        self.labelTimerStatsWork.setFont(font1)
        self.labelTimerStatsWork.setStyleSheet(u"font-size: 14px; color: #34c759; font-weight: bold;")
        self.labelTimerStatsWork.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayoutStats.addWidget(self.labelTimerStatsWork)

        self.labelTimerStatsBreak = QLabel(self.frameTimer)
        self.labelTimerStatsBreak.setObjectName(u"labelTimerStatsBreak")
        self.labelTimerStatsBreak.setFont(font1)
        self.labelTimerStatsBreak.setStyleSheet(u"font-size: 14px; color: #ff9500; font-weight: bold;")
        self.labelTimerStatsBreak.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayoutStats.addWidget(self.labelTimerStatsBreak)


        self.verticalLayoutTimer.addLayout(self.horizontalLayoutStats)


        self.verticalLayout_8.addWidget(self.frameTimer)

        self.labelSessionsHistory = QLabel(self.tabTimer)
        self.labelSessionsHistory.setObjectName(u"labelSessionsHistory")
        self.labelSessionsHistory.setStyleSheet(u"font-size: 14px; font-weight: bold; color: #1c1c1e; margin-top: 10px;")

        self.verticalLayout_8.addWidget(self.labelSessionsHistory)

        self.tableSessions = QTableWidget(self.tabTimer)
        if (self.tableSessions.columnCount() < 5):
            self.tableSessions.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableSessions.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableSessions.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableSessions.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableSessions.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableSessions.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tableSessions.setObjectName(u"tableSessions")
        self.tableSessions.setAlternatingRowColors(True)
        self.tableSessions.horizontalHeader().setVisible(True)
        self.tableSessions.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_8.addWidget(self.tableSessions)

        self.tabWidget.addTab(self.tabTimer, "")
        self.tabNotes = QWidget()
        self.tabNotes.setObjectName(u"tabNotes")
        self.verticalLayout_9 = QVBoxLayout(self.tabNotes)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayoutNotes = QHBoxLayout()
        self.horizontalLayoutNotes.setObjectName(u"horizontalLayoutNotes")
        self.lineEditNoteTitle = QLineEdit(self.tabNotes)
        self.lineEditNoteTitle.setObjectName(u"lineEditNoteTitle")
        self.lineEditNoteTitle.setMinimumSize(QSize(0, 25))
        self.lineEditNoteTitle.setFont(font)

        self.horizontalLayoutNotes.addWidget(self.lineEditNoteTitle)

        self.comboBoxNoteTask = QComboBox(self.tabNotes)
        self.comboBoxNoteTask.setObjectName(u"comboBoxNoteTask")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBoxNoteTask.sizePolicy().hasHeightForWidth())
        self.comboBoxNoteTask.setSizePolicy(sizePolicy3)
        self.comboBoxNoteTask.setMinimumSize(QSize(160, 0))
        self.comboBoxNoteTask.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayoutNotes.addWidget(self.comboBoxNoteTask)

        self.btnAddNote = QPushButton(self.tabNotes)
        self.btnAddNote.setObjectName(u"btnAddNote")

        self.horizontalLayoutNotes.addWidget(self.btnAddNote)

        self.btnUpdateNote = QPushButton(self.tabNotes)
        self.btnUpdateNote.setObjectName(u"btnUpdateNote")

        self.horizontalLayoutNotes.addWidget(self.btnUpdateNote)

        self.btnDelete_3 = QPushButton(self.tabNotes)
        self.btnDelete_3.setObjectName(u"btnDelete_3")

        self.horizontalLayoutNotes.addWidget(self.btnDelete_3)


        self.verticalLayout_9.addLayout(self.horizontalLayoutNotes)

        self.textEditTaskNote = QTextEdit(self.tabNotes)
        self.textEditTaskNote.setObjectName(u"textEditTaskNote")
        sizePolicy.setHeightForWidth(self.textEditTaskNote.sizePolicy().hasHeightForWidth())
        self.textEditTaskNote.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.textEditTaskNote)

        self.tableNotes = QTableWidget(self.tabNotes)
        if (self.tableNotes.columnCount() < 4):
            self.tableNotes.setColumnCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableNotes.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableNotes.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableNotes.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableNotes.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        self.tableNotes.setObjectName(u"tableNotes")
        self.tableNotes.setAlternatingRowColors(True)
        self.tableNotes.horizontalHeader().setVisible(True)
        self.tableNotes.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_9.addWidget(self.tableNotes)

        self.tabWidget.addTab(self.tabNotes, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FIBER Task Manager", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.frameTodayTasks.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_today_tasks_title.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438 \u043d\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.label_today_tasks_title.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card-title", None))
        self.label_today_tasks_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.frameCompletedTasks.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_completed_tasks_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.label_completed_tasks_title.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card-title", None))
        self.label_completed_tasks_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.framePendingTasks.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_pending_tasks_title.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043e\u0436\u0438\u0434\u0430\u043d\u0438\u0438", None))
        self.label_pending_tasks_title.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card-title", None))
        self.label_pending_tasks_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.frameOverdueTasks.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card", None))
        self.label_overdue_tasks_title.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043e", None))
        self.label_overdue_tasks_title.setProperty(u"class", QCoreApplication.translate("MainWindow", u"card-title", None))
        self.label_overdue_tasks_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelRecentTasks.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        ___qtablewidgetitem = self.tableRecentTasks.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430", None))
        ___qtablewidgetitem1 = self.tableRecentTasks.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        ___qtablewidgetitem2 = self.tableRecentTasks.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        ___qtablewidgetitem3 = self.tableRecentTasks.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDashboard), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u041f\u0430\u043d\u0435\u043b\u044c", None))
        self.lineEditTaskTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.dateEditDueDate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.btnAddTask.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnUpdateTask.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnCompleteTask.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem4 = self.tableTasks.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem5 = self.tableTasks.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        ___qtablewidgetitem6 = self.tableTasks.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        ___qtablewidgetitem7 = self.tableTasks.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        ___qtablewidgetitem8 = self.tableTasks.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None))
        ___qtablewidgetitem9 = self.tableTasks.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTasks), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.labelTimerTitle.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438", None))
        self.labelTimerStatus.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d", None))
        self.labelTimerTime.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.btnStartWork.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.btnStartBreak.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0440\u044b\u0432", None))
        self.btnStopTimer.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btnDelete_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.labelTimerStatsWork.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430: 0\u0447 0\u043c", None))
        self.labelTimerStatsBreak.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u044b\u0445: 0\u0447 0\u043c", None))
        self.labelSessionsHistory.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0441\u0435\u0441\u0441\u0438\u0439", None))
        ___qtablewidgetitem10 = self.tableSessions.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430", None))
        ___qtablewidgetitem11 = self.tableSessions.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        ___qtablewidgetitem12 = self.tableSessions.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e", None))
        ___qtablewidgetitem13 = self.tableSessions.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem14 = self.tableSessions.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTimer), QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440", None))
        self.lineEditNoteTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.btnAddNote.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnUpdateNote.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.btnDelete_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem15 = self.tableNotes.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430", None))
        ___qtablewidgetitem16 = self.tableNotes.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        ___qtablewidgetitem17 = self.tableNotes.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        ___qtablewidgetitem18 = self.tableNotes.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNotes), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
    # retranslateUi

