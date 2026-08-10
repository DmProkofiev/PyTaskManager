import sqlite3
from datetime import date, datetime
from typing import List, Optional
from Models import Task, OnceTask, DailyTask, WeeklyTask, MonthlyTask, YearlyTask
from Models.enums import TaskPriority, TaskStatus, TaskPeriodType
from Interfaces.ITaskRepository import ITaskRepository

class SqliteTaskRepository(ITaskRepository):
    def __init__(self, connection: sqlite3.Connection):
        self._conn = connection

    # Преобразование: обьект в dict INSERT UPDATE
    def _task_to_params(self, task: Task) -> dict:
        params = {
            'title': task.title,
            'description': task.description,
            'priority': task.priority.value,
            'status': task.status.value,
            'due_date': task.due_date.isoformat() if task.due_date else None,
            'created_at': task.created_at.isoformat(),
            'updated_at': task.updated_at.isoformat(),
            'period_type': task.period_type.value,
            'day_of_week': None,
            'day_of_month': None,
            'month': None,
            'day': None,
        }
        if isinstance(task, WeeklyTask):
            params['day_of_week'] = task.day_of_week
        elif isinstance(task, MonthlyTask):
            params['day_of_month'] = task.day_of_month
        elif isinstance(task, YearlyTask):
            params['month'] = task.month
            params['day'] = task.day
        return params

    # Преобразование: строка SQL в обьект
    def _row_to_task(self, row) -> Task:
        period_type = TaskPeriodType(row['period_type'])
        kwargs = {
            'id': row['id'],
            'title': row['title'],
            'description': row['description'],
            'priority': TaskPriority(row['priority']),
            'status': TaskStatus(row['status']),
            'due_date': datetime.fromisoformat(row['due_date']).date() if row['due_date'] else None,
            'created_at': datetime.fromisoformat(row['created_at']),
            'updated_at': datetime.fromisoformat(row['updated_at']),
        }
        if period_type == TaskPeriodType.ONCE:
            return OnceTask(**kwargs)
        elif period_type == TaskPeriodType.DAILY:
            return DailyTask(**kwargs)
        elif period_type == TaskPeriodType.WEEKLY:
            return WeeklyTask(**kwargs, day_of_week=row['day_of_week'])
        elif period_type == TaskPeriodType.MONTHLY:
            return MonthlyTask(**kwargs, day_of_month=row['day_of_month'])
        elif period_type == TaskPeriodType.YEARLY:
            return YearlyTask(**kwargs, month=row['month'], day=row['day'])
        raise ValueError(f"Неизвестный period_type: {period_type}")

# CRUD
    # CREATE
    def add(self, task: Task) -> None:
        params = self._task_to_params(task)
        cursor = self._conn.execute("""
            INSERT INTO tasks (
                title, description, priority, status, due_date,
                created_at, updated_at, period_type,
                day_of_week, day_of_month, month, day
            ) VALUES (
                :title, :description, :priority, :status, :due_date,
                :created_at, :updated_at, :period_type,
                :day_of_week, :day_of_month, :month, :day
            )
        """, params)
        task.id = cursor.lastrowid

    # READ
    def get_by_id(self, task_id: int) -> Optional[Task]:
        cursor = self._conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        return self._row_to_task(row) if row else None

    def get_all(self) -> List[Task]:
        cursor = self._conn.execute("SELECT * FROM tasks ORDER BY due_date ASC")
        return [self._row_to_task(row) for row in cursor.fetchall()]

    def get_tasks_for_date(self, target_date: date) -> List[Task]:
        sqlite_weekday = (target_date.weekday() + 1) % 7
        cursor = self._conn.execute("""
            SELECT * FROM tasks
            WHERE status != 'COMPLETED'
              AND (
                  (period_type = 'ONCE' AND due_date = ?)
                  OR (period_type = 'DAILY')
                  OR (period_type = 'WEEKLY' AND day_of_week = ?)
                  OR (period_type = 'MONTHLY' AND day_of_month = ?)
                  OR (period_type = 'YEARLY' AND month = ? AND day = ?)
              )
        """, (
            target_date.isoformat(),
            sqlite_weekday,
            target_date.day,
            target_date.month,
            target_date.day,
        ))
        return [self._row_to_task(row) for row in cursor.fetchall()]

    def get_by_status(self, status: TaskStatus) -> List[Task]:
        cursor = self._conn.execute("SELECT * FROM tasks WHERE status = ?", (status.value,))
        return [self._row_to_task(row) for row in cursor.fetchall()]

    def get_by_period_type(self, period_type: TaskPeriodType) -> List[Task]:
        cursor = self._conn.execute("SELECT * FROM tasks WHERE period_type = ?", (period_type.value,))
        return [self._row_to_task(row) for row in cursor.fetchall()]

    # UPDATE
    def update(self, task: Task) -> None:
        params = self._task_to_params(task)
        params['id'] = task.id
        self._conn.execute("""
            UPDATE tasks SET
                title = :title,
                description = :description,
                priority = :priority,
                status = :status,
                due_date = :due_date,
                updated_at = :updated_at,
                period_type = :period_type,
                day_of_week = :day_of_week,
                day_of_month = :day_of_month,
                month = :month,
                day = :day
            WHERE id = :id
        """, params)

    # DELETE
    def delete(self, task_id: int) -> None:
        self._conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

