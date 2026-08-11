from typing import Optional
from PySide6.QtWidgets import QWidget
from Models import Note, Task


class IDialogService:
    def show_error(self, parent: Optional[QWidget], message: str, title: str = "Ошибка") -> None: ...
    def show_info(self, parent: Optional[QWidget], message: str, title: str = "Информация") -> None: ...
    def show_warning(self, parent: Optional[QWidget], message: str, title: str = "Предупреждение") -> None: ...
    def show_question(self, parent: Optional[QWidget], message: str, title: str = "Подтверждение") -> bool: ...

    # редактирование

    def update_note(self, note: Note, parent: Optional[QWidget]) -> Optional[Note]:
        raise NotImplementedError

    def update_task(self, task: Task, parent: Optional[QWidget]) -> Optional[Task]:
        raise NotImplementedError