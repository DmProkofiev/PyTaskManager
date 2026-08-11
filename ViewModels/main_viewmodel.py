import os
from datetime import date, datetime
from typing import List, Optional
from PySide6.QtCore import QObject, Signal, Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTableWidgetItem, QApplication, QSystemTrayIcon, QHeaderView, QSizePolicy
from Interfaces.IDialogService import IDialogService
from Interfaces.INoteService import INoteService
from Interfaces.ISessionService import ISessionService
from Interfaces.ITaskService import ITaskService
from Interfaces.ITrayService import ITrayService
from Models import Task, Note, TimerSession, OnceTask, DailyTask, WeeklyTask, MonthlyTask, YearlyTask
from Models.enums import TaskPriority, TaskStatus, TaskPeriodType, SessionType
from Services.task_service import TaskService
from Services.session_service import SessionService
from Services.note_service import NoteService
from Services.dialog_service import DialogService
from Services.tray_service import TrayService

class MainViewModel(QObject):
    tasks_updated = Signal()
    notes_updated = Signal()
    sessions_updated = Signal()
    timer_tick = Signal(str)
    timer_state_changed = Signal(str)
    error_occurred = Signal(str)

    def __init__(self, task_service: ITaskService, session_service: ISessionService, note_service: INoteService, tray_service: ITrayService, dialog_service: IDialogService):
        super().__init__()
        self._task_service = task_service
        self._session_service = session_service
        self._note_service = note_service
        self._tray_service = tray_service
        self._dialog = dialog_service
        self._ui = None
        self._window = None

        self._tasks: List[Task] = []
        self._sessions: List[TimerSession] = []
        self._notes: List[Note] = []

        self._current_session: Optional[TimerSession] = None
        self._timer = None
        self.load_data()

        self.tray_flag = False

    # Покдлючение кнопок
    def _connect_buttons(self) -> None:
        self._ui.btnAddTask.clicked.connect(self.add_task)
        self._ui.btnUpdateTask.clicked.connect(self.update_task)
        self._ui.btnUpdateNote.clicked.connect(self.update_note)
        self._ui.btnDelete.clicked.connect(self.delete_task)
        self._ui.btnDelete_3.clicked.connect(self.delete_note)
        self._ui.btnDelete_2.clicked.connect(self.delete_session)
        self._ui.btnCompleteTask.clicked.connect(self.complete_task)
        self._ui.btnStartWork.clicked.connect(self.start_work)
        self._ui.btnStartBreak.clicked.connect(self.start_break)
        self._ui.btnStopTimer.clicked.connect(self.stop_timer)
        self._ui.btnAddNote.clicked.connect(self.add_note)

# UI

    def set_ui(self, ui) -> None:
        self._ui = ui
        self._setup_ui()
        self._ensure_timer_running()

    def set_window(self, window) -> None:
        if self.tray_flag:
            return
        self._window = window
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_dir, "Resources", "FIBERTMico.png")
        self._tray_service.setup_tray(window, self, icon_path)
        self.tray_flag = True

    def _setup_ui(self) -> None:
        if not self._ui:
            return
        tables = [self._ui.tableRecentTasks, self._ui.tableTasks,
                  self._ui.tableSessions, self._ui.tableNotes]
        for tbl in tables:
            tbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            tbl.setWordWrap(True)
            tbl.setTextElideMode(Qt.ElideNone)
            tbl.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            header = tbl.horizontalHeader()
            for col in range(tbl.columnCount()):
                header.setSectionResizeMode(col, QHeaderView.Interactive)
        self._fill_comboboxes()
        self._connect_buttons()
        self._update_all_ui()

    def _update_all_ui(self) -> None:
        if not self._ui:
            return
        self._update_dashboard()
        self._update_tasks_table()
        self._update_notes_table()
        self._update_sessions_table()
        self._update_task_comboboxes()
        self._update_timer_stats()

    def _update_task_comboboxes(self) -> None:
        if not self._ui:
            return
        self._ui.comboBoxTimerTask.clear()
        self._ui.comboBoxNoteTask.clear()
        for task in self._tasks:
            self._ui.comboBoxTimerTask.addItem(task.title, task.id)
            self._ui.comboBoxNoteTask.addItem(task.title, task.id)

    def _update_dashboard(self) -> None:
        today = date.today()
        today_tasks = [
            t for t in self._tasks
            if t.due_date == today or t.period_type in (
                TaskPeriodType.DAILY,
                TaskPeriodType.WEEKLY,
                TaskPeriodType.MONTHLY,
                TaskPeriodType.YEARLY
            )
        ]
        completed = [t for t in self._tasks if t.status == TaskStatus.COMPLETED]
        pending = [t for t in self._tasks if t.status == TaskStatus.PENDING]
        overdue = [t for t in self._tasks if t.is_overdue()]

        self._ui.label_today_tasks_value.setText(str(len(today_tasks)))
        self._ui.label_completed_tasks_value.setText(str(len(completed)))
        self._ui.label_pending_tasks_value.setText(str(len(pending)))
        self._ui.label_overdue_tasks_value.setText(str(len(overdue)))

        self._update_table(self._ui.tableRecentTasks, self._tasks[:10], self._task_to_recent_row)

    def _update_tasks_table(self) -> None:
        self._update_table(self._ui.tableTasks, self._tasks, self._task_to_row)

    def _update_notes_table(self) -> None:
        self._update_table(self._ui.tableNotes, self._notes, self._note_to_row)

    def _update_sessions_table(self) -> None:
        self._update_table(self._ui.tableSessions, self._sessions, self._session_to_row)

    def _update_table(self, table, data, row_mapper) -> None:
        table.clearContents()
        table.setRowCount(len(data))
        for row, item in enumerate(data):
            for col, value in enumerate(row_mapper(item)):
                table.setItem(row, col, value)
        table.resizeRowsToContents()
        table.repaint()

    def _update_timer_stats(self) -> None:
        work_seconds = self._session_service.get_total_work_today()
        break_seconds = self._session_service.get_total_break_today()
        work_hours = work_seconds // 3600
        work_minutes = (work_seconds % 3600) // 60
        break_hours = break_seconds // 3600
        break_minutes = (break_seconds % 3600) // 60
        self._ui.labelTimerStatsWork.setText(f"Работа: {work_hours}ч {work_minutes}м")
        self._ui.labelTimerStatsBreak.setText(f"Отдых: {break_hours}ч {break_minutes}м")

# Заполнение компобоксов

    def _fill_comboboxes(self) -> None:
        for priority in TaskPriority:
            self._ui.comboBoxPriority.addItem(priority.display_name(), priority)
        for period in TaskPeriodType:
            self._ui.comboBoxPeriodType.addItem(period.display_name(), period)

# Загрузка данных

    def load_data(self) -> None:
        try:
            self._tasks = self._task_service.get_all()
            self._sessions = self._session_service.get_all()
            self._notes = self._note_service.get_all()
            if self._ui:
                self._update_all_ui()
        except Exception as e:
            self.error_occurred.emit(str(e))

# Преобразование QTableWidgetItem

    # Отображение: Таблица задач DashBoard
    def _task_to_recent_row(self, task: Task) -> List[QTableWidgetItem]:

        status_item = QTableWidgetItem(task.status.display_name())
        priority_item = QTableWidgetItem(task.priority.display_name())

        if task.status == TaskStatus.COMPLETED:
            status_item.setBackground(QColor(200, 255, 200))  # светло-зелёный
        elif task.status == TaskStatus.PENDING:
            status_item.setBackground(QColor(255, 255, 200))  # светло-жёлтый
        elif task.status == TaskStatus.OVERDUE:
            status_item.setBackground(QColor(255, 200, 200))  # светло-красный

        if task.priority == TaskPriority.HIGH:
            priority_item.setBackground(QColor(255, 200, 200))  # красноватый
        elif task.priority == TaskPriority.MEDIUM:
            priority_item.setBackground(QColor(255, 255, 200))  # жёлтый
        elif task.priority == TaskPriority.LOW:
            priority_item.setBackground(QColor(200, 255, 200))  # зелёный

        return [
            QTableWidgetItem(task.title),
            priority_item,
            status_item,
            QTableWidgetItem(task.due_date.strftime("%d.%m.%Y") if task.due_date else ""),
        ]

    # Отображение: Таблица задач
    def _task_to_row(self, task: Task) -> List[QTableWidgetItem]:

        status_item = QTableWidgetItem(task.status.display_name())
        priority_item = QTableWidgetItem(task.priority.display_name())

        if task.status == TaskStatus.COMPLETED:
            status_item.setBackground(QColor(200, 255, 200))  # светло-зелёный
        elif task.status == TaskStatus.PENDING:
            status_item.setBackground(QColor(255, 255, 200))  # светло-жёлтый
        elif task.status == TaskStatus.OVERDUE:
            status_item.setBackground(QColor(255, 200, 200))  # светло-красный

        if task.priority == TaskPriority.HIGH:
            priority_item.setBackground(QColor(255, 200, 200))  # красноватый
        elif task.priority == TaskPriority.MEDIUM:
            priority_item.setBackground(QColor(255, 255, 200))  # жёлтый
        elif task.priority == TaskPriority.LOW:
            priority_item.setBackground(QColor(200, 255, 200))  # зелёный

        return [
            QTableWidgetItem(task.title),
            priority_item,
            QTableWidgetItem(task.period_type.display_name()),
            status_item,
            QTableWidgetItem(task.due_date.strftime("%d.%m.%Y") if task.due_date else ""),
            QTableWidgetItem(task.description),
        ]

    # Отображение: Таблица заметок
    def _note_to_row(self, note: Note) -> List[QTableWidgetItem]:
        task_title = ""
        for t in self._tasks:
            if t.id == note.task_id:
                task_title = t.title
                break
        return [
            QTableWidgetItem(task_title),
            QTableWidgetItem(note.created_at.strftime("%d.%m.%Y %H:%M")),
            QTableWidgetItem(note.title),
            QTableWidgetItem(note.content),
        ]

    # Отображение: Таблица Session
    def _session_to_row(self, session: TimerSession) -> List[QTableWidgetItem]:
        task_title = ""
        for t in self._tasks:
            if t.id == session.task_id:
                task_title = t.title
                break
        session_item = QTableWidgetItem(session.type.display_name())
        if session.type == SessionType.WORK:
            session_item.setBackground(QColor(200, 255, 200))  # светло-зелёный
        elif session.type == SessionType.BREAK:
            session_item.setBackground(QColor(255, 165, 0))  # оранжиевый

        return [
            QTableWidgetItem(task_title),
            session_item,
            QTableWidgetItem(session.start_time.strftime("%d.%m.%Y %H:%M")),
            QTableWidgetItem(session.end_time.strftime("%d.%m.%Y %H:%M") if session.end_time else "Активна"),
            QTableWidgetItem(session.get_duration_string()),
        ]

# CRUD Task

    # CREATE
    def add_task(self) -> None:
        try:
            title = self._ui.lineEditTaskTitle.text()
            if not title.strip():
                self._dialog.show_warning(self._window, "Введите название задачи")
                return
            due_date = self._ui.dateEditDueDate.date().toPython()
            priority = self._ui.comboBoxPriority.currentData()
            period_type = self._ui.comboBoxPeriodType.currentData()
            description = self._ui.textEditTaskDescription.toPlainText()

            if period_type == TaskPeriodType.ONCE:
                task = OnceTask(title=title, description=description, priority=priority, due_date=due_date)
            elif period_type == TaskPeriodType.DAILY:
                task = DailyTask(title=title, description=description, priority=priority)
            elif period_type == TaskPeriodType.WEEKLY:
                task = WeeklyTask(title=title, description=description, priority=priority, day_of_week=0)
            elif period_type == TaskPeriodType.MONTHLY:
                task = MonthlyTask(title=title, description=description, priority=priority, day_of_month=1)
            elif period_type == TaskPeriodType.YEARLY:
                task = YearlyTask(title=title, description=description, priority=priority, month=1, day=1)
            else:
                return

            task.validate()
            self._task_service.add(task)
            self.load_data()
            self._ui.lineEditTaskTitle.clear()
            self._ui.textEditTaskDescription.clear()
            self._dialog.show_info(self._window, "Задача добавлена")
        except ValueError as e:
            self.error_occurred.emit(str(e))

    # UPDATE
    def update_task(self) -> None:
        row = self._ui.tableTasks.currentRow()
        if row < 0:
            self._dialog.show_warning(self._window, "Выберите задачу")
            return
        task = self._tasks[row]
        updated = self._dialog.update_task(task, self._window)

        if updated is not None:
            try:
                self._task_service.update(updated)
                self.load_data()
            except Exception as e:
                self._dialog.show_error(self._window, str(e))

    def complete_task(self) -> None:
        row = self._ui.tableTasks.currentRow()
        if row < 0:
            self._dialog.show_warning(self._window, "Выберите задачу")
            return
        task = self._tasks[row]
        self._task_service.complete(task.id)
        self.load_data()

    # DELETE
    def delete_task(self) -> None:
        row = self._ui.tableTasks.currentRow()
        if row < 0:
            self._dialog.show_warning(self._window, "Выберите задачу")
            return
        if not self._dialog.show_question(self._window, "Удалить задачу?"):
            return
        task = self._tasks[row]
        self._task_service.delete(task.id)
        self.load_data()

# CRUD NOTE
    
    # CREATE
    def add_note(self) -> None:
        title = self._ui.lineEditNoteTitle.text()
        content = self._ui.textEditTaskNote.toPlainText()
        if not title.strip() and not content.strip():
            self._dialog.show_warning(self._window, "Заполните заголовок или текст")
            return

        task_id = self._ui.comboBoxNoteTask.currentData()
        note = Note(task_id=task_id, title=title, content=content)
        try:
            note.validate()
            self._note_service.add(note)
            self.load_data()
            self._ui.lineEditNoteTitle.clear()
            self._ui.textEditNoteContent.clear()

            self._dialog.show_info(self._window, "Заметка добавлена")
        except ValueError as e:
            self.error_occurred.emit(str(e))

    # UPDATE
    def update_note(self):
        row = self._ui.tableNotes.currentRow()
        if row < 0:
            self._dialog.show_warning(self._window, "Не выбран обьект")
            return
        note = self._notes[row]
        item = self._dialog.update_note(note, self._window)

        if item is not None:
            try:
                self._note_service.update(item)
                self.load_data()
            except Exception as e:
                self._dialog.show_error(self._window, str(e))


    # DELETE
    def delete_note(self):
        row = self._ui.tableNotes.currentRow()
        if row < 0:
            self._dialog.show_warning(self._window, "Выберите запись")
            return
        if not self._dialog.show_question(self._window, "Удалить запись?"):
            return
        note = self._notes[row]
        self._note_service.delete(note.id)
        self.load_data()


# SESSION

    def _ensure_timer_running(self) -> None:
        if self._timer is not None and self._timer.isActive():
            return
        if self._timer is not None:
            self._timer.stop()
            self._timer = None
        self._timer = QTimer()
        self._timer.timeout.connect(self._on_timer_tick)
        self._timer.start(1000)

    # CREATE WORK
    def start_work(self):
        self._ensure_timer_running()
        if self._current_session and self._current_session.is_active():
            self._current_session.stop()
            self._session_service.update(self._current_session)

        task_id = self._ui.comboBoxTimerTask.currentData()
        self._current_session = TimerSession(type=SessionType.WORK, task_id=task_id)
        self._session_service.add(self._current_session)

        if self._ui:
            self._ui.labelTimerStatus.setText("Работа")
            self._ui.labelTimerTime.setStyleSheet("font-size: 48px; font-weight: bold; color: #34c759;")
        self.timer_state_changed.emit("work")
        self._update_timer_stats()

    # CREATE BREAK
    def start_break(self):
        self._ensure_timer_running()
        if self._current_session and self._current_session.is_active():
            self._current_session.stop()
            self._session_service.update(self._current_session)
        task_id = self._ui.comboBoxTimerTask.currentData()
        self._current_session = TimerSession(type=SessionType.BREAK, task_id=task_id)
        self._session_service.add(self._current_session)

        if self._ui:
            self._ui.labelTimerStatus.setText("Перерыв")
            self._ui.labelTimerTime.setStyleSheet("font-size: 48px; font-weight: bold; color: #ff9500;")
        self.timer_state_changed.emit("break")
        self._update_timer_stats()

    # UPDATE
    def stop_timer(self) -> None:
        if self._current_session and self._current_session.is_active():
            self._current_session.stop()
            self._session_service.update(self._current_session)
            self._current_session = None
        if self._ui:
            self._ui.labelTimerStatus.setText("Остановлен")
            self._ui.labelTimerTime.setStyleSheet("font-size: 48px; font-weight: bold; color: #6e6e73;")
        self.timer_tick.emit("00:00:00")
        self.timer_state_changed.emit("stopped")
        self.load_data()

    def _on_timer_tick(self) -> None:
        try:
            self._ensure_timer_running()
            if self._current_session and self._current_session.is_active():
                time_str = self._current_session.get_duration_string()
                self.timer_tick.emit(time_str)
            else:
                self.timer_tick.emit("00:00:00")
        except RuntimeError:
            pass

    # DELETE
    def delete_session(self) -> None:
        current_row = self._ui.tableSessions.currentRow()
        if current_row < 0:
            self._dialog.show_warning(self._window, "Выберите сессию для удаления")
            return
        session = self._sessions[current_row]
        session_id = session.id
        if not self._dialog.show_question(self._window, "Удалить выбранную сессию?"):
            return
        self._session_service.delete(session_id)
        self.load_data()

# TRAY

    def show_window(self) -> None:
        if self._window:
            self._window.show()
            self._window.raise_()
            self._window.activateWindow()

    def hide_window(self) -> None:
        if self._window:
            self._window.hide()

    def _on_tray_activated(self, reason) -> None:
        if reason == QSystemTrayIcon.DoubleClick:
            if self._window and self._window.isVisible():
                self._window.hide()
            else:
                self.show_window()

    def quit_application(self) -> None:
        self._tray_service.hide_tray()
        QApplication.quit()

    def handle_close_event(self, event) -> None:
        event.ignore()
        if self._window:
            self._window.hide()