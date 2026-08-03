from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional
from Models.enums import TaskPriority, TaskStatus, TaskPeriodType, SessionType

# Модель Task

# Основной Абстрактный Класс
@dataclass
class Task(ABC):
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.PENDING
    due_date: date | None = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    period_type: TaskPeriodType = field(init=False)

    @abstractmethod
    def get_period_label(self) -> str:
        pass

    # Валидация
    def validate(self) -> None:
        if not self.title.strip():
            raise ValueError("Название не может быть пустым")
        if self.due_date and self.due_date < date.today():
            raise ValueError("Дата выполнения не может быть в прошлом")
        if not isinstance(self.priority, TaskPriority):
            raise TypeError("Неверный тип приоритета")

    # Изменение статуса ЗАВЕРШЕНО
    def complete(self) -> None:
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.now()

    # просрочка
    def is_overdue(self) -> bool:
        return (self.status != TaskStatus.COMPLETED and
                self.due_date and self.due_date < date.today())

# Наследуемый Класс: Разовая задача
@dataclass
class OnceTask(Task):
    period_type: TaskPeriodType = field(default=TaskPeriodType.ONCE, init=False)

    def get_period_label(self) -> str:
        return "Разовая"

# Наследуемый Класс: ежедневная задача
@dataclass
class DailyTask(Task):
    period_type: TaskPeriodType = field(default=TaskPeriodType.DAILY, init=False)

    def get_period_label(self) -> str:
        return "Ежедневная"

# Наследуемый Класс: еженедельная задача
@dataclass
class WeeklyTask(Task):
    day_of_week: int = 0  # 0=пн
    period_type: TaskPeriodType = field(default=TaskPeriodType.WEEKLY, init=False)

    def get_period_label(self) -> str:
        return "Еженедельная"

    def validate(self) -> None:
        super().validate()
        if not (0 <= self.day_of_week <= 6):
            raise ValueError("День недели должен быть от 0 до 6")

# Наследуемый Класс: ежемесячная задача
@dataclass
class MonthlyTask(Task):
    day_of_month: int = 1
    period_type: TaskPeriodType = field(default=TaskPeriodType.MONTHLY, init=False)

    def get_period_label(self) -> str:
        return "Ежемесячная"

    def validate(self) -> None:
        super().validate()
        if not (1 <= self.day_of_month <= 31):
            raise ValueError("День месяца должен быть от 1 до 31")

# Наследуемый Класс: ежегодная задача
@dataclass
class YearlyTask(Task):
    month: int = 1
    day: int = 1
    period_type: TaskPeriodType = field(default=TaskPeriodType.YEARLY, init=False)

    def get_period_label(self) -> str:
        return "Ежегодная"

    def validate(self) -> None:
        super().validate()
        if not (1 <= self.month <= 12):
            raise ValueError("Месяц должен быть от 1 до 12")
        if not (1 <= self.day <= 31):
            raise ValueError("День должен быть от 1 до 31")

# Модель Timer
@dataclass
class TimerSession:
    id: Optional[int]
    task_id: Optional[int]
    start_time: datetime = field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    duration_seconds: int = 0
    type: SessionType = SessionType.WORK

    def is_active(self) -> bool:
        return self.end_time is None

    def stop(self) -> None:
        self.end_time = datetime.now()
        self. duration_seconds = int((self.end_time - self.start_time).total_seconds())

    def get_duration_string(self) -> str:
        if self.is_active():
            seconds = int((datetime.now() - self.start_time).total_seconds())
        else:
            seconds = self.duration_seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

    def validate(self) -> None:
        if self.start_time > datetime.now():
            raise ValueError("Время начала не может быть в будущем")

# Модель Note
@dataclass
class Note:
    id: Optional[int]
    task_id: Optional[int]
    title: str=""
    content: str=""
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def validate(self):
        if self.title and self.content is None:
            raise ValueError("Не может быть пустым")
