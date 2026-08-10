from typing import List, Optional
from datetime import date
from Models import Task
from Interfaces.IUnitOfWork import IUnitOfWork
from Interfaces.ITaskService import ITaskService

class TaskService(ITaskService):
    def __init__(self, uow: IUnitOfWork):
        self._uow = uow
# CRUD

    # CREATE
    def add(self, task: Task) -> None:
        with self._uow:
            self._uow.tasks.add(task)

    # READ
    def get_all(self) -> List[Task]:
        with self._uow:
            return self._uow.tasks.get_all()

    def get_by_id(self, task_id: int) -> Optional[Task]:
        with self._uow:
            return self._uow.tasks.get_by_id(task_id)

    def get_for_today(self) -> List[Task]:
        with self._uow:
            return self._uow.tasks.get_tasks_for_date(date.today())

    # UPDATE
    def update(self, task: Task) -> None:
        with self._uow:
            self._uow.tasks.update(task)

    def complete(self, task_id: int) -> None:
        with self._uow:
            task = self._uow.tasks.get_by_id(task_id)
            if task:
                task.complete()
                self._uow.tasks.update(task)

    # DELETE
    def delete(self, task_id: int) -> None:
        with self._uow:
            sessions = self._uow.sessions.get_by_task_id(task_id)
            for session in sessions:
                self._uow.sessions.delete(session.id)
            notes = self._uow.notes.get_by_task_id(task_id)
            for note in notes:
                self._uow.notes.delete(note.id)
            self._uow.tasks.delete(task_id)