from typing import List, Optional
from datetime import date, datetime
from Models import TimerSession
from Models.enums import SessionType
from Interfaces.IUnitOfWork import IUnitOfWork
from Interfaces.ISessionService import ISessionService

class SessionService(ISessionService):
    def __init__(self, uow: IUnitOfWork):
        self._uow = uow

    def add(self, session: TimerSession) -> None:
        with self._uow:
            self._uow.sessions.add(session)

    def update(self, session: TimerSession) -> None:
        with self._uow:
            self._uow.sessions.update(session)

    def get_active(self) -> Optional[TimerSession]:
        with self._uow:
            return self._uow.sessions.get_active_session()

    def get_by_task(self, task_id: int) -> List[TimerSession]:
        with self._uow:
            return self._uow.sessions.get_by_task_id(task_id)

    def get_all(self) -> List[TimerSession]:
        with self._uow:
            return self._uow.sessions.get_all()

    def get_total_work_today(self) -> int:
        today = date.today()
        start = datetime(today.year, today.month, today.day, 0, 0, 0)
        end = datetime(today.year, today.month, today.day, 23, 59, 59)
        with self._uow:
            return self._uow.sessions.get_total_duration(start, end, SessionType.WORK)

    def get_total_break_today(self) -> int:
        today = date.today()
        start = datetime(today.year, today.month, today.day, 0, 0, 0)
        end = datetime(today.year, today.month, today.day, 23, 59, 59)
        with self._uow:
            return self._uow.sessions.get_total_duration(start, end, SessionType.BREAK)

    def delete(self, session_id: int) -> None:
        with self._uow:
            self._uow.sessions.delete(session_id)