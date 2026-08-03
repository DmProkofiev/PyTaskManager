# Services/repositories/timer_session_repository.py
import sqlite3
from datetime import datetime, date
from typing import List, Optional
from Models import TimerSession
from Models.enums import SessionType
from Services.Interfaces.ITimerSessionRepository import ITimerSessionRepository

class SqliteTimerSessionRepository(ITimerSessionRepository):
    def __init__(self, db_path: str = "source.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS timer_sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id INTEGER,
                    type TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT,
                    duration_seconds INTEGER DEFAULT 0,
                    FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE SET NULL
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_sessions_task_id ON timer_sessions(task_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_sessions_start_time ON timer_sessions(start_time)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_sessions_end_time ON timer_sessions(end_time)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_sessions_type ON timer_sessions(type)")

# Преобразование объекта в словарь INSERT/UPDATE
    def _session_to_dict(self, session: TimerSession) -> dict:
        return {
            'task_id': session.task_id,
            'type': session.type.value,
            'start_time': session.start_time.isoformat(),
            'end_time': session.end_time.isoformat() if session.end_time else None,
            'duration_seconds': session.duration_seconds,
        }

#Преобразование строки БД в объект TimerSession
    def _row_to_session(self, row) -> TimerSession:
        return TimerSession(
            id=row['id'],
            task_id=row['task_id'],
            type=SessionType(row['type']),
            start_time=datetime.fromisoformat(row['start_time']),
            end_time=datetime.fromisoformat(row['end_time']) if row['end_time'] else None,
            duration_seconds=row['duration_seconds'] or 0,
        )

# CRUD

    # CREATE
    def add(self, session: TimerSession) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                INSERT INTO timer_sessions (task_id, type, start_time, end_time, duration_seconds)
                VALUES (:task_id, :type, :start_time, :end_time, :duration_seconds)
            """, self._session_to_dict(session))
            session.id = cursor.lastrowid

    # READ
    def get_by_id(self, session_id: int) -> Optional[TimerSession]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM timer_sessions WHERE id = ?", (session_id,))
            row = cursor.fetchone()
            return self._row_to_session(row) if row else None

    def get_all(self) -> List[TimerSession]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM timer_sessions ORDER BY start_time DESC")
            return [self._row_to_session(row) for row in cursor.fetchall()]

    # UPDATE
    def update(self, session: TimerSession) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                UPDATE timer_sessions
                SET task_id = :task_id,
                    type = :type,
                    start_time = :start_time,
                    end_time = :end_time,
                    duration_seconds = :duration_seconds
                WHERE id = :id
            """, {
                'id': session.id,
                'task_id': session.task_id,
                'type': session.type.value,
                'start_time': session.start_time.isoformat(),
                'end_time': session.end_time.isoformat() if session.end_time else None,
                'duration_seconds': session.duration_seconds,
            })

    # DELETE
    def delete(self, session_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM timer_sessions WHERE id = ?", (session_id,))

    def get_active_session(self) -> Optional[TimerSession]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM timer_sessions WHERE end_time IS NULL ORDER BY start_time DESC LIMIT 1"
            )
            row = cursor.fetchone()
            return self._row_to_session(row) if row else None

    def get_by_task_id(self, task_id: int) -> List[TimerSession]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM timer_sessions WHERE task_id = ? ORDER BY start_time DESC",
                (task_id,)
            )
            return [self._row_to_session(row) for row in cursor.fetchall()]

    def get_by_period(self, start: datetime, end: datetime) -> List[TimerSession]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM timer_sessions WHERE start_time >= ? AND start_time <= ? ORDER BY start_time ASC",
                (start.isoformat(), end.isoformat())
            )
            return [self._row_to_session(row) for row in cursor.fetchall()]

    def get_by_date(self, target_date: date) -> List[TimerSession]:
        start = datetime(target_date.year, target_date.month, target_date.day, 0, 0, 0)
        end = datetime(target_date.year, target_date.month, target_date.day, 23, 59, 59)
        return self.get_by_period(start, end)

    def get_total_duration(self, start: datetime, end: datetime, session_type: Optional[SessionType] = None) -> int:
        query = "SELECT SUM(duration_seconds) FROM timer_sessions WHERE start_time >= ? AND start_time <= ?"
        params = [start.isoformat(), end.isoformat()]
        if session_type:
            query += " AND type = ?"
            params.append(session_type.value)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(query, tuple(params))
            result = cursor.fetchone()[0]
            return result or 0