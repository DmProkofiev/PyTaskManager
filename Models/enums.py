from enum import Enum

# Task
class TaskPriority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

    def display_name(self) -> str:
        return {TaskPriority.LOW: "Низкий",TaskPriority.MEDIUM: "Средний",TaskPriority.HIGH: "Высокий"}[self]

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    OVERDUE = "overdue"

    def display_name(self) -> str:
        return {TaskStatus.PENDING: "В процессе", TaskStatus.COMPLETED: "Завершено", TaskStatus.OVERDUE: "Просрочено"}[self]

class TaskPeriodType(Enum):
    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    def display_name(self) -> str:
        return {TaskPeriodType.ONCE: "Единоразовая", TaskPeriodType.DAILY: "Ежедневная", TaskPeriodType.WEEKLY: "Еженедельная", TaskPeriodType.MONTHLY: "Ежемесячная", TaskPeriodType.YEARLY: "Ежегодная"}[self]

# Timer
class SessionType(Enum):
    WORK = "Work"
    BREAK = "Break"

    def display_name(self) -> str:
        return {SessionType.WORK: "Активная деятельность", SessionType.BREAK: "Перерыв"}[self]
