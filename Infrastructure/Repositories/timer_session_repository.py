import sqlite3
from datetime import datetime
from typing import List, Optional
from Models import TimerSession
from Models.enums import SessionType
from Interfaces.ITimerSessionRepository import ITimerSessionRepository


class SqliteTimerSessionRepository(ITimerSessionRepository):
    def __init__(self, connection: sqlite3.Connection):
        self._conn = connection

    def _row_to_session(self, row) -> TimerSession:
        return TimerSession(
            id=row['id'],
            task_id=row['task_id'],
            type=SessionType(row['type']),
            start_time=datetime.fromisoformat(row['start_time']),
            end_time=datetime.fromisoformat(row['end_time']) if row['end_time'] else None,
            duration_seconds=row['duration_seconds'] or 0,
        )

    def add(self, session: TimerSession) -> None:
        cursor = self._conn.execute("""
            INSERT INTO timer_sessions (task_id, type, start_time, end_time, duration_seconds)
            VALUES (:task_id, :type, :start_time, :end_time, :duration_seconds)
        """, {
            'task_id': session.task_id,
            'type': session.type.value,
            'start_time': session.start_time.isoformat(),
            'end_time': session.end_time.isoformat() if session.end_time else None,
            'duration_seconds': session.duration_seconds,
        })
        session.id = cursor.lastrowid

    def get_by_id(self, session_id: int) -> Optional[TimerSession]:
        cursor = self._conn.execute("SELECT * FROM timer_sessions WHERE id = ?", (session_id,))
        row = cursor.fetchone()
        return self._row_to_session(row) if row else None

    def get_all(self) -> List[TimerSession]:
        cursor = self._conn.execute("SELECT * FROM timer_sessions ORDER BY start_time DESC")
        return [self._row_to_session(row) for row in cursor.fetchall()]

    def get_active_session(self) -> Optional[TimerSession]:
        cursor = self._conn.execute(
            "SELECT * FROM timer_sessions WHERE end_time IS NULL ORDER BY start_time DESC LIMIT 1"
        )
        row = cursor.fetchone()
        return self._row_to_session(row) if row else None

    def get_by_task_id(self, task_id: int) -> List[TimerSession]:
        cursor = self._conn.execute(
            "SELECT * FROM timer_sessions WHERE task_id = ? ORDER BY start_time DESC",
            (task_id,)
        )
        return [self._row_to_session(row) for row in cursor.fetchall()]

    def get_total_duration(self, start: datetime, end: datetime, session_type: Optional[SessionType] = None) -> int:
        query = "SELECT COALESCE(SUM(duration_seconds), 0) FROM timer_sessions WHERE start_time >= ? AND start_time <= ?"
        params = [start.isoformat(), end.isoformat()]
        if session_type:
            query += " AND type = ?"
            params.append(session_type.value)
        cursor = self._conn.execute(query, tuple(params))
        return cursor.fetchone()[0]

    def update(self, session: TimerSession) -> None:
        self._conn.execute("""
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

    def delete(self, session_id: int) -> None:
        self._conn.execute("DELETE FROM timer_sessions WHERE id = ?", (session_id,))