import sqlite3
from datetime import datetime
from typing import List, Optional
from Models import Note
from Interfaces.INoteRepository import INoteRepository

class SqliteNoteRepository(INoteRepository):
    def __init__(self, connection: sqlite3.Connection):
        self._conn = connection

    # Преобразование: строка SQL в обьект
    def _row_to_note(self, row) -> Note:
        return Note(
            id=row['id'],
            task_id=row['task_id'],
            title=row['title'] or "",
            content=row['content'] or "",
            created_at=datetime.fromisoformat(row['created_at']),
            updated_at=datetime.fromisoformat(row['updated_at']),
        )
# CRUD

    # CREATE
    def add(self, note: Note) -> None:
        cursor = self._conn.execute("""
            INSERT INTO notes (task_id, title, content, created_at, updated_at)
            VALUES (:task_id, :title, :content, :created_at, :updated_at)
        """, {
            'task_id': note.task_id,
            'title': note.title,
            'content': note.content,
            'created_at': note.created_at.isoformat(),
            'updated_at': note.updated_at.isoformat(),
        })
        note.id = cursor.lastrowid

    # READ
    def get_by_id(self, note_id: int) -> Optional[Note]:
        cursor = self._conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        row = cursor.fetchone()
        return self._row_to_note(row) if row else None

    def get_all(self) -> List[Note]:
        cursor = self._conn.execute("SELECT * FROM notes ORDER BY created_at DESC")
        return [self._row_to_note(row) for row in cursor.fetchall()]

    def get_by_task_id(self, task_id: int) -> List[Note]:
        cursor = self._conn.execute(
            "SELECT * FROM notes WHERE task_id = ? ORDER BY created_at DESC",
            (task_id,)
        )
        return [self._row_to_note(row) for row in cursor.fetchall()]

    # UPDATE
    def update(self, note: Note) -> None:
        note.updated_at = datetime.now()
        self._conn.execute("""
            UPDATE notes
            SET task_id = :task_id,
                title = :title,
                content = :content,
                updated_at = :updated_at
            WHERE id = :id
        """, {
            'id': note.id,
            'task_id': note.task_id,
            'title': note.title,
            'content': note.content,
            'updated_at': note.updated_at.isoformat(),
        })

    # DELETE
    def delete(self, note_id: int) -> None:
        self._conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))

