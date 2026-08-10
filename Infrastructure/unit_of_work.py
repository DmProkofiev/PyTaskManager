import sqlite3
from Interfaces.IUnitOfWork import IUnitOfWork
from Infrastructure.Repositories.task_repository import SqliteTaskRepository
from Infrastructure.Repositories.timer_session_repository import SqliteTimerSessionRepository
from Infrastructure.Repositories.note_repository import SqliteNoteRepository

class SqliteUnitOfWork(IUnitOfWork):
    def __init__(self, db_path: str = "source.db"):
        self._db_path = db_path
        self._connection = None
        self._tasks = None
        self._sessions = None
        self._notes = None

    # Вход и соединение с БД
    def __enter__(self):
        self._connection = sqlite3.connect(self._db_path)
        self._connection.row_factory = sqlite3.Row
        self._tasks = SqliteTaskRepository(self._connection)
        self._sessions = SqliteTimerSessionRepository(self._connection)
        self._notes = SqliteNoteRepository(self._connection)
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self._connection.close()

    @property
    def tasks(self) -> SqliteTaskRepository:
        return self._tasks

    @property
    def sessions(self) -> SqliteTimerSessionRepository:
        return self._sessions

    @property
    def notes(self) -> SqliteNoteRepository:
        return self._notes

    # Изменения в БД
    def commit(self) -> None:
        if self._connection:
            self._connection.commit()

    # Откат
    def rollback(self) -> None:
        if self._connection:
            self._connection.rollback()