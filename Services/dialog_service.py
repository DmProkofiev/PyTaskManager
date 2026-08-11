from PySide6.QtWidgets import QMessageBox, QWidget, QDialog
from typing import Optional
from Interfaces.IDialogService import IDialogService
from Models import Note, Task
from Views.dialog.note_dialog import NoteDialog
from Views.dialog.task_dialog import TaskDialog

class DialogService(IDialogService):
    @staticmethod
    def show_error(parent: Optional[QWidget], message: str, title: str = "Ошибка") -> None:
        QMessageBox.critical(parent, title, message)

    @staticmethod
    def show_info(parent: Optional[QWidget], message: str, title: str = "Информация") -> None:
        QMessageBox.information(parent, title, message)

    @staticmethod
    def show_warning(parent: Optional[QWidget], message: str, title: str = "Предупреждение") -> None:
        QMessageBox.warning(parent, title, message)

    @staticmethod
    def show_question(parent: Optional[QWidget], message: str, title: str = "Подтверждение") -> bool:
        reply = QMessageBox.question(parent, title, message, QMessageBox.Yes | QMessageBox.No)
        return reply == QMessageBox.Yes

# Редактирование

    @staticmethod
    def update_note(note: Note, parent: Optional[QWidget]) -> Optional[Note]:
        dialog = NoteDialog(note, parent)
        if dialog.exec() == QDialog.Accepted:
            return dialog.update_object()
        return None

    @staticmethod
    def update_task(task: Task, parent: Optional[QWidget]) -> Optional[Task]:
        dialog = TaskDialog(task, parent)
        if dialog.exec() == QDialog.Accepted:
            return dialog.update_object()
        return None
