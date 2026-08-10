import sqlite3

def init_db(db_path: str = "source.db") -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                due_date TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                period_type TEXT NOT NULL,
                day_of_week INTEGER,
                day_of_month INTEGER,
                month INTEGER,
                day INTEGER
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_tasks_period_type ON tasks(period_type)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_tasks_due_date ON tasks(due_date)")

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