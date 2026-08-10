from typing import List
from Models import Note
from Interfaces.IUnitOfWork import IUnitOfWork
from Interfaces.INoteService import INoteService

class NoteService(INoteService):
    def __init__(self, uow: IUnitOfWork):
        self._uow = uow

    def add(self, note: Note) -> None:
        with self._uow:
            self._uow.notes.add(note)

    def update(self, note: Note) -> None:
        with self._uow:
            self._uow.notes.update(note)

    def delete(self, note_id: int) -> None:
        with self._uow:
            self._uow.notes.delete(note_id)

    def get_all(self) -> List[Note]:
        with self._uow:
            return self._uow.notes.get_all()

    def get_by_task(self, task_id: int) -> List[Note]:
        with self._uow:
            return self._uow.notes.get_by_task_id(task_id)