from typing import Protocol
from Interfaces.ITaskRepository import ITaskRepository
from Interfaces.ITimerSessionRepository import ITimerSessionRepository
from Interfaces.INoteRepository import INoteRepository


class IUnitOfWork(Protocol):
    tasks: ITaskRepository
    sessions: ITimerSessionRepository
    notes: INoteRepository

    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...