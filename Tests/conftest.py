import pytest
from datetime import date, timedelta
from Models import Note, OnceTask, DailyTask, WeeklyTask, MonthlyTask, YearlyTask, TimerSession
from Models.enums import TaskPriority, TaskStatus, SessionType

# даты
@pytest.fixture
def today() -> date:
    return date.today()

@pytest.fixture
def future_date() -> date:
    return date.today() + timedelta(days=7)

@pytest.fixture
def past_date() -> date:
    return date.today() - timedelta(days=1)


# Note
@pytest.fixture
def valid_note() -> Note:
    return Note(id=1, task_id=10, title="Важная заметка", content="Текст заметки")

@pytest.fixture
def empty_title_note() -> Note:
    return Note(id=2, task_id=None, title="", content="Есть контент")

@pytest.fixture
def empty_content_note() -> Note:
    return Note(id=3, task_id=None, title="Заголовок", content="")

@pytest.fixture
def fully_empty_note() -> Note:
    return Note(id=4, task_id=None, title="", content="")


# Tasks
@pytest.fixture
def sample_once_task(future_date: date) -> OnceTask:
    return OnceTask(
        id=1,
        title="Разовая задача",
        description="Описание",
        priority=TaskPriority.HIGH,
        due_date=future_date,
    )

@pytest.fixture
def overdue_once_task(past_date: date) -> OnceTask:
    return OnceTask(
        id=2,
        title="Просроченная",
        priority=TaskPriority.LOW,
        due_date=past_date,
    )

@pytest.fixture
def daily_task() -> DailyTask:
    return DailyTask(id=3, title="Ежедневная", priority=TaskPriority.MEDIUM)

@pytest.fixture
def weekly_task() -> WeeklyTask:
    return WeeklyTask(id=4, title="Недельная", day_of_week=2)

@pytest.fixture
def monthly_task() -> MonthlyTask:
    return MonthlyTask(id=5, title="Месячная", day_of_month=15)

@pytest.fixture
def yearly_task() -> YearlyTask:
    return YearlyTask(id=6, title="Годовая", month=12, day=25)

# Фабрика задач
@pytest.fixture
def task_factory():
    def _create(task_type: str, **kwargs):
        mapping = {
            "once": OnceTask,
            "daily": DailyTask,
            "weekly": WeeklyTask,
            "monthly": MonthlyTask,
            "yearly": YearlyTask,
        }
        cls = mapping.get(task_type)
        if cls is None:
            raise ValueError(f"Unknown task type: {task_type}")
        return cls(**kwargs)
    return _create


#  TimerSession
@pytest.fixture
def active_session() -> TimerSession:
    return TimerSession(id=1, task_id=10, type=SessionType.WORK)

@pytest.fixture
def stop_session() -> TimerSession:
    session = TimerSession(id=2, task_id=10, type=SessionType.BREAK)
    session.stop()
    return session