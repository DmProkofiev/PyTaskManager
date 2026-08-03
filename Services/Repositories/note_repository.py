# Services/repositories/note_repository.py
import sqlite3
from datetime import datetime
from typing import List, Optional
from Models import Note
from Services.Interfaces.INoteRepository import INoteRepository

class SqliteNoteRepository(INoteRepository):
    def __init__(self, db_path: str = "source.db"):
        self.db_path = db_path
        self._init_db()

    #Инициализация таблицы и индексов
    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id INTEGER,
                    title TEXT,
                    content TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE SET NULL
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_notes_task_id ON notes(task_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_notes_created ON notes(created_at)")

# Преобразование объекта в словарь INSERT/UPDATE
    def _note_to_dict(self, note: Note) -> dict:
        return {
            'task_id': note.task_id,
            'title': note.title,
            'content': note.content,
            'created_at': note.created_at.isoformat(),
            'updated_at': note.updated_at.isoformat(),
        }

# Преобразование строки БД в объект Note
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
    def add(self, note: Note) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                INSERT INTO notes (task_id, title, content, created_at, updated_at)
                VALUES (:task_id, :title, :content, :created_at, :updated_at)
            """, self._note_to_dict(note))
            note.id = cursor.lastrowid

    def get_by_id(self, note_id: int) -> Optional[Note]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
            row = cursor.fetchone()
            return self._row_to_note(row) if row else None

    def get_all(self) -> List[Note]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM notes ORDER BY created_at DESC")
            return [self._row_to_note(row) for row in cursor.fetchall()]

    def update(self, note: Note) -> None:
        note.updated_at = datetime.now()
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
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

    def delete(self, note_id: int) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))

    # ---- Дополнительная фильтрация ----
    def get_by_task_id(self, task_id: int) -> List[Note]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(
                "SELECT * FROM notes WHERE task_id = ? ORDER BY created_at DESC",
                (task_id,)
            )
            return [self._row_to_note(row) for row in cursor.fetchall()]