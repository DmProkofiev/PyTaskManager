from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QDateEdit, \
    QTextEdit
from Models.models import Note
from datetime import datetime

class NoteDialog(QDialog):
    def __init__(self, note: Note, parent = None):
        super().__init__(parent)
        self._original = note
        self._item = None

        self.setWindowTitle("Редактирование Заметки")
        self.setModal(True)
        self.setMinimumWidth(400)

        layout = QVBoxLayout(self)

        # Заголовок
        layout.addWidget(QLabel("Заголовок"))
        self.title_edit = QLineEdit()
        self.title_edit.setText(str(note.title))
        layout.addWidget(self.title_edit)

        # Содержание
        layout.addWidget(QLabel("Содержание"))
        self.content_edit = QTextEdit()
        self.content_edit.setObjectName("content_edit")
        self.content_edit.setText(str(note.content))
        layout.addWidget(self.content_edit)

        #buttons
        btn_layout = QHBoxLayout()
        ok_btn = QPushButton("Ok")
        ok_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("Отмена")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(ok_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def update_object(self) -> Note:
        if self._item is None:
            title = self.title_edit.text()
            content = self.content_edit.text()
            self._item = Note(id = self._original.id,title = title,content = content)
        return self._item