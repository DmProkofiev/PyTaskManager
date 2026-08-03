from enum import Enum

# Task
class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    OVERDUE = "overdue"

class TaskPeriodType(Enum):
    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

# Timer
class SessionType(Enum):
    WORK = "Work",
    BREAK = "Break"

    def display_name(self) -> str:
        return {
            SessionType.WORK: "Активная деятельность",
            SessionType.BREAK: "Перерыв"
        }[self]
