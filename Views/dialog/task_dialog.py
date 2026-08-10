from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit, QComboBox, QPushButton, QDateEdit, QTextEdit
from PySide6.QtCore import QDate
from Models.models import Task
from Models.enums import TaskPriority, TaskPeriodType, TaskStatus


class TaskDialog(QDialog):
    def __init__(self, task: Task, parent=None):
        super().__init__(parent)
        self._original = task
        self._item = None

        self.setWindowTitle("Редактирование задачи")
        self.setModal(True)
        self.setMinimumWidth(500)

        layout = QVBoxLayout(self)

        # Название
        layout.addWidget(QLabel("Название"))
        self.title_edit = QLineEdit()
        self.title_edit.setText(str(task.title))
        layout.addWidget(self.title_edit)

        # Описание
        layout.addWidget(QLabel("Описание"))
        self.description_edit = QTextEdit()
        self.description_edit.setObjectName("textEditTaskDescription")
        self.description_edit.setText(str(task.description))
        layout.addWidget(self.description_edit)

        # Приоритет
        layout.addWidget(QLabel("Приоритет"))
        self.priority_combo = QComboBox()
        for priority in TaskPriority:
            self.priority_combo.addItem(priority.display_name(), priority)  # ← исправлено
        index = self.priority_combo.findData(task.priority)
        if index >= 0:
            self.priority_combo.setCurrentIndex(index)
        layout.addWidget(self.priority_combo)

        # Тип периода
        layout.addWidget(QLabel("Тип периода"))
        self.period_combo = QComboBox()
        for period in TaskPeriodType:
            self.period_combo.addItem(period.display_name(), period)  # ← исправлено
        index = self.period_combo.findData(task.period_type)
        if index >= 0:
            self.period_combo.setCurrentIndex(index)
        layout.addWidget(self.period_combo)

        # Статус
        layout.addWidget(QLabel("Статус"))
        self.status_combo = QComboBox()
        for status in TaskStatus:
            self.status_combo.addItem(status.display_name(), status)  # ← исправлено
        index = self.status_combo.findData(task.status)
        if index >= 0:
            self.status_combo.setCurrentIndex(index)
        layout.addWidget(self.status_combo)

        # Дата выполнения
        layout.addWidget(QLabel("Дата выполнения"))
        self.date_edit = QDateEdit()
        self.date_edit.setDisplayFormat("dd.MM.yyyy")
        self.date_edit.setCalendarPopup(True)
        if task.due_date:
            self.date_edit.setDate(QDate(task.due_date.year, task.due_date.month, task.due_date.day))
        else:
            self.date_edit.setDate(QDate.currentDate())
        layout.addWidget(self.date_edit)

        # Кнопки
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Отмена")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def update_object(self) -> Task:
        if self._item is None:
            title = self.title_edit.text()
            description = self.description_edit.toPlainText()
            priority = self.priority_combo.currentData()
            period_type = self.period_combo.currentData()
            status = self.status_combo.currentData()
            due_date = self.date_edit.date().toPython()

            if period_type == TaskPeriodType.ONCE:
                from Models import OnceTask
                self._item = OnceTask(
                    id=self._original.id,
                    title=title,
                    description=description,
                    priority=priority,
                    status=status,
                    due_date=due_date,
                    created_at=self._original.created_at,
                )
            elif period_type == TaskPeriodType.DAILY:
                from Models import DailyTask
                self._item = DailyTask(
                    id=self._original.id,
                    title=title,
                    description=description,
                    priority=priority,
                    status=status,
                    created_at=self._original.created_at,
                )
            elif period_type == TaskPeriodType.WEEKLY:
                from Models import WeeklyTask
                self._item = WeeklyTask(
                    id=self._original.id,
                    title=title,
                    description=description,
                    priority=priority,
                    status=status,
                    day_of_week=self._original.day_of_week if hasattr(self._original, 'day_of_week') else 0,
                    created_at=self._original.created_at,
                )
            elif period_type == TaskPeriodType.MONTHLY:
                from Models import MonthlyTask
                self._item = MonthlyTask(
                    id=self._original.id,
                    title=title,
                    description=description,
                    priority=priority,
                    status=status,
                    day_of_month=self._original.day_of_month if hasattr(self._original, 'day_of_month') else 1,
                    created_at=self._original.created_at,
                )
            elif period_type == TaskPeriodType.YEARLY:
                from Models import YearlyTask
                self._item = YearlyTask(
                    id=self._original.id,
                    title=title,
                    description=description,
                    priority=priority,
                    status=status,
                    month=self._original.month if hasattr(self._original, 'month') else 1,
                    day=self._original.day if hasattr(self._original, 'day') else 1,
                    created_at=self._original.created_at,
                )
            else:
                raise ValueError(f"Неизвестный тип периода: {period_type}")
        return self._item